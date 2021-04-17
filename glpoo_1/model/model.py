from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


engine = create_engine('sqlite:///:memory:', echo=True)
Base=declarative_base()


Session = sessionmaker(bind=engine)
session = Session()

class Member(Base):
    __tablename__ = 'members'
    id = Column(Integer, primary_key=True)
    right= Column(String)#user ou admin
    name = Column(String)
    fullname = Column(String)
    user= Column(String)#nom d'utilisateur
    password = Column(String)
    #jointure avec une table pour trouver les clubs


    def __repr__(self):
        return "(ID='%s', name='%s', fullname='%s', user='%s',password='%s',right='%s')" % (
            self.id, self.name, self.fullname, self.user,self.password,self.right)


class Member_licence(Base):#association entre member et licence
    __tablename__ = 'members_licence'
    id = Column(Integer, primary_key=True)
    id_licence=Column(Integer,ForeignKey('licences.id'))
    licence = relationship("Licence_bdd")
    id_member=Column(Integer,ForeignKey('members.id'))
    member=relationship("Member")#creer relation entre cette table et la table membre
    statut= Column(Integer)#membre(0), bureau(1),chef(2)
    #jointure avec une table pour trouver les clubs


    def __repr__(self):
        return "(ID='%s', id_licence='%s', id_member='%s', id_statut='%s')" % (
            self.id, self.id_licence, self.id_member,self.statut)


class Licence_bdd(Base):
    __tablename__='licences'
    id = Column(Integer,primary_key=True)
    id_club = Column(Integer)

    name = Column(String)
    prix = Column(Integer)
    nb_seances = Column(Integer)
    avantage = Column(String)

    def __repr__(self):
        return "(ID='%s',ID_club='%s', name='%s', prix='%s', nb_seance='%s', avantage='%s')" % (
            self.id,self.id_club,self.name, self.prix, self.nb_seances,self.avantage)

class Club_bdd(Base):
    __tablename__='clubs'
    id = Column(Integer,primary_key=True)
    nom = Column(String)
    adresse = Column(String)
    description = Column(String)
    chef = Column(Integer)

    def __repr__(self):
        return "(ID='%s',nom='%s', adresse='%s', ID_Chef='%s', description='%s')" % (
            self.id,self.nom,self.adresse,self.chef,self.description)

def add_club(add_nom, add_adresse, add_description,add_chef):
    add_user = Member(nom=add_nom, adresse=add_adresse,description=add_description,chef=add_chef)

    session.add(add_user)
    session.commit()

class Evenement_bdd(Base):
    __tablename__ = 'evenement'
    id = Column(Integer, primary_key=True)
    nom = Column(String)
    lieu = Column(String)
    date = Column(String)
    horaire = Column(String)

    def __repr__(self):
        return "(ID='%s',nom='%s', lieu='%s', date='%s', horaire='%s')" % (
            self.id, self.nom, self.lieu, self.date, self.horaire)


Base.metadata.create_all(engine)


def add_member(add_name, add_fullname, add_user,add_password,add_right):
    add_user = Member(name=add_name, fullname=add_fullname,user=add_user,password=add_password,right=add_right)

    session.add(add_user)
    session.commit()


def list_members():
    for member in session.query(Member):
        print(member)


def del_member(ida):
    try:
        session.delete(session.query(Member).filter_by(id=ida).one())
        session.commit()
    except:
        print("le membre n'existe pas")


def modify_member(ida, name=None, fullname=None, user=None, password=None):

    try:
        mod = session.query(Member).filter_by(id=ida).one()
        if name:
            mod.name=name
        if fullname:
            mod.fullname=fullname
        if user:
            mod.user=user
        if password:
            mod.password=password
    except:
        print("L'id " + ida + " de la table members n'existe pas")


def add_licence(add_id_club, add_name, add_prix, add_nb_sceances,add_avantage):
    try:
        session.query(Club_bdd).filter_by(id=add_id_club).one()
        add_licenc = Licence_bdd(id_club=add_id_club, name=add_name, prix=add_prix, nb_seances=add_nb_sceances,avantage=add_avantage)

        session.add(add_licenc)
        session.commit()
    except:
        print("Le club n'existe pas")


def list_licences():
    for licence in session.query(Licence_bdd):
        print(licence)


def del_licence(ida):
    try:
        session.delete(session.query(Licence_bdd).filter_by(id=ida).one())
        session.commit()
    except:
        print("la licence n'existe pas")


def modify_licence(ida, name=None, prix=None, nb_seances=None, avantage=None):
    try:
        mod=session.query(Licence_bdd).filter_by(id=ida).one()
        if name:
            mod.name = name
        if prix:
            mod.prix = prix
        if nb_seances:
            mod.nb_seances = nb_seances
        if avantage:
            mod.avantage = avantage
    except:
        print("L'id " + str(ida) + " de la table licences n'existe pas")






def add_club(add_nom, add_adresse, add_description,add_chef):
    try:
        session.query(Member).filter_by(id=add_chef).one()  # on vérifie que l'ID passé en paramètre existe
        add_user = Club_bdd(nom=add_nom, adresse=add_adresse,description=add_description,chef=add_chef)

        session.add(add_user)
        session.commit()
    except:
        print("Le chef n'existe pas")


def list_clubs():
    for club in session.query(Club_bdd):
        print(club)


def modify_clubs(ida, nom=None, adresse=None, chef=None, description=None):

    erreur=f"L'id ${ida} de la table clubs n'existe pas"
    try:
        mod = session.query(Club_bdd).filter_by(id=ida).one()
        if chef:
            erreur = "Le chef n'existe pas"
            session.query(Member).filter_by(id=chef).one()#on vérifie que l'ID passé en paramètre existe
            mod.chef = chef
        if nom:
            mod.nom = nom
        if adresse:
            mod.adresse = adresse
        if description:
            mod.description = description

    except:
        print(erreur)


def del_Club(ida):
    try:
        session.delete(session.query(Club_bdd).filter_by(id=ida).one())
        session.commit()
    except:
        print("le club n'existe pas")