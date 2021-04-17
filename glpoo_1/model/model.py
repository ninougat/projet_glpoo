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
    __tablename__ = 'members_license'
    id = Column(Integer, primary_key=True)
    id_licence=Column(Integer,ForeignKey('licences.id'))
    license = relationship("licences",back_populates="id_licence")
    id_member=Column(Integer,ForeignKey('members.id'))
    member=relationship("members",back_populates="id_member")#creer relation entre cette table et la table membre
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
    nb_seance = Column(Integer)
    avantage = Column(String)

    def __repr__(self):
        return "(ID='%s',ID_club='%s', name='%s', prix='%s', nb_seance='%s', avantage='%s')" % (
            self.id,self.id_club,self.name, self.prix, self.nb_seance,self.avantage)

class Club_bdd(Base):
    __tablename__='club'
    id = Column(Integer,primary_key=True)
    nom = Column(String)
    adresse = Column(String)
    description = Column(String)
    chef = Column(Integer)

    def __repr__(self):
        return "(ID='%s',nom='%s', adresse='%s', ID_Chef='%s', description='%s')" % (
            self.id,self.nom,self.adresse,self.adresse,self.description)

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


def list_member():
    for member in session.query(Member):
        print(member)


def del_member(ida):
    session.delete(session.query(Member).filter_by(id=ida).one())
    session.commit()


def modify_name(ida,name=None,fullname=None,user=None,password=None):
    mod=session.query(Member).filter_by(id=ida).one()
    if name:
        mod.name=name
    if fullname:
        mod.fullname=fullname
    if user:
        mod.user=user
    if password:
        mod.password=password


def add_licence(add_id_club, add_name, add_prix, add_nb_sceance,add_avantage):
    add_licenc = Licence_bdd(id_club=add_id_club, name=add_name, prix=add_prix, nb_seance=add_nb_sceance,avantage=add_avantage)

    session.add(add_licenc)
    session.commit()


def list_licence():
    for licence in session.query(Licence_bdd):
        print(licence)


def del_licence(ida):
    session.delete(session.query(Licence_bdd).filter_by(id=ida).one())
    session.commit()


def modify_licence(ida, name=None, prix=None, nb_licence=None, avantage=None):
    mod=session.query(Licence_bdd).filter_by(id=ida).one()
    if name:
        mod.name = name
    if prix:
        mod.prix = prix
    if nb_licence:
        mod.nb_licence = nb_licence
    if avantage:
        mod.avantage = avantage