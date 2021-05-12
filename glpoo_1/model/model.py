from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class Member_bdd(Base):
    __tablename__ = 'members'
    id = Column(Integer, primary_key=True)
    status = Column(String)  # user ou admin
    name = Column(String)
    fullname = Column(String)
    user = Column(String)  # nom d'utilisateur
    password = Column(String)

    # jointure avec une table pour trouver les clubs

    def __repr__(self):
        return "(ID='%s', name='%s', fullname='%s', user='%s',password='%s',status='%s')" % (
            self.id, self.name, self.fullname, self.user, self.password, self.status)


class Member_licence(Base):  # association entre member et licence
    __tablename__ = 'members_licence'
    id = Column(Integer, primary_key=True)
    id_licence = Column(Integer, ForeignKey('licences.id'))
    licence = relationship("Licence_bdd")
    id_member = Column(Integer, ForeignKey('members.id'))
    member = relationship("Member")  # creer relation entre cette table et la table membre
    statut = Column(Integer)  # membre(0), bureau(1),chef(2)

    # jointure avec une table pour trouver les clubs

    def __repr__(self):
        return "(ID='%s', id_licence='%s', id_member='%s', id_statut='%s')" % (
            self.id, self.id_licence, self.id_member, self.statut)


class Licence_bdd(Base):
    __tablename__ = 'licences'
    id = Column(Integer, primary_key=True)
    id_club = Column(Integer)

    name = Column(String)
    prix = Column(Integer)
    nb_seances = Column(Integer)
    avantage = Column(String)

    def __repr__(self):
        return "(ID='%s',ID_club='%s', name='%s', prix='%s', nb_seance='%s', avantage='%s')" % (
            self.id, self.id_club, self.name, self.prix, self.nb_seances, self.avantage)


class Club_bdd(Base):
    __tablename__ = 'clubs'
    id = Column(Integer, primary_key=True)
    nom = Column(String)
    adresse = Column(String)
    description = Column(String)
    chef = Column(Integer)

    def __repr__(self):
        return "(ID='%s',nom='%s', adresse='%s', ID_Chef='%s', description='%s')" % (
            self.id, self.nom, self.adresse, self.chef, self.description)

class Evenement_bdd(Base):
    __tablename__ = 'evenement'
    id = Column(Integer, primary_key=True)
    nom = Column(String)
    lieu = Column(String)
    date = Column(String)
    horaire = Column(String)
    id_club = Column(Integer)

    def __repr__(self):
        return "(ID='%s',nom='%s', lieu='%s', date='%s', horaire='%s')" % (
            self.id, self.nom, self.lieu, self.date, self.horaire)


Base.metadata.create_all(engine)


def add_member(membre):
    add_user = Member_bdd(name=membre.name, fullname=membre.fullname, user=membre.user, password=membre.password, status=membre.status)
    session.add(add_user)
    session.commit()
    # on récupère l'id de l'évènement dans la base de données
    membre.id = session.query(Evenement_bdd).order_by(Evenement_bdd.id.desc()).first()


def list_members():
    for member in session.query(Member_bdd):
        print(member)


def del_member(ida):
    member_to_delete=session.query(Member_bdd).filter_by(id=ida).one()# on récupère le membre à supprimer
    try:
        licenses=session.query(Member_licence).filter_by(id_members=ida)# on récupère les licences auquels il était lié
        for licence in licenses :# pour chacune de ces licences
            session.delete(licence)# on supprime son abonnement
        session.delete(member_to_delete)#on supprime le membre
        session.commit()
    except:
        print("le membre n'existe pas")


def modify_member(ida, name=None, fullname=None, user=None, password=None):
    try:
        mod = session.query(Member_bdd).filter_by(id=ida).one()
        if name:
            mod.name = name
        if fullname:
            mod.fullname = fullname
        if user:
            mod.user = user
        if password:
            mod.password = password
    except:
        print("L'id " + ida + " de la table members n'existe pas")

def add_member_licence(id_member,id_licence,statut):
    member=session.query(Member_bdd).filter_by(id=id_member).one()
    licence=session.query(Licence_bdd).filter_by(id=id_licence).one()
    if member==None or licence==None:
        print("le membre ou la licence est incorrect")
    elif statut<0 or statut>2  :
        print("Le statut du membre est incorrect")
    else:

        add_ml=Member_licence(id_member=id_member,id_licence=id_licence,statut=statut)
        session.add(add_ml)
        session.commit()

def modify_membre_licence(ida,id_licence=None,statut=None):
     try:
         mod= session.query(Member_licence)
         if id_licence :
             mod.id_licence=id_licence
         if statut :
             mod.statut=statut
     except :
         print("")

def add_licence(licence):
    try:
        session.query(Club_bdd).filter_by(id=licence.id_club).one()
        add_licenc = Licence_bdd(id_club=licence.id_club, name=licence.name, prix=licence.prix, nb_seances=licence.nb_sceances,
                                 avantage=licence.avantage)

        session.add(add_licenc)
        session.commit()
        # on récupère l'id de la licence dans la base de données
        licence.id = session.query(Evenement_bdd).order_by(Evenement_bdd.id.desc()).first()

    except:
        print("Le club n'existe pas")


def list_licences():
    for licence in session.query(Licence_bdd):
        print(licence)


def del_licence(ida):
    licence_to_delete=session.query(Licence_bdd).filter_by(id=ida).one()
    try:

        members_to_delete=session.query(Member_licence).filter_by(id_licence=ida) # on récupère les membres lié à la license
        try :
            for member in members_to_delete : #pour chaque membre
                session.delete(member)#on le supprime de la table intermédiaire
        except :
            pass

        session.delete(licence_to_delete)
        session.commit()
    except:
        print("la licence n'existe pas")


def modify_licence(ida, name=None, prix=None, nb_seances=None, avantage=None):
    try:
        mod = session.query(Licence_bdd).filter_by(id=ida).one()
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


def add_club(club):
    try:
        session.query(Member_bdd).filter_by(id=club.chef).one()  # on vérifie que l'ID passé en paramètre existe
        add_user = Club_bdd(nom=club.nom, adresse=club.adresse, description=club.description, chef=club.chef)

        session.add(add_user)
        session.commit()
        # on récupère l'id du club dans la base de données
        club.id = session.query(Evenement_bdd).order_by(Evenement_bdd.id.desc()).first()
    except:
        print("Le chef n'existe pas")


def list_clubs():
    for club in session.query(Club_bdd):
        print(club)


def modify_club(ida, nom=None, adresse=None, chef=None, description=None):
    erreur = f"L'id ${ida} de la table clubs n'existe pas"
    try:
        mod = session.query(Club_bdd).filter_by(id=ida).one()
        if chef:
            erreur = "Le chef n'existe pas"
            session.query(Member_bdd).filter_by(id=chef).one()  # on vérifie que l'ID passé en paramètre existe
            mod.chef = chef
        if nom:
            mod.nom = nom
        if adresse:
            mod.adresse = adresse
        if description:
            mod.description = description

    except:
        print(erreur)


def add_event(evenement):
    try:
        session.query(Club_bdd).filtre_by(id=evenement.id_club).one()

    except:
        print("Le club n'existe pas")
        return

    new_event = Evenement_bdd(nom=evenement.nom, lieu=evenement.lieu, date=evenement.date, horaire=evenement.horaire, id_club=evenement.id_club)
    session.add(new_event)
    session.commit()
    # on récupère l'id de l'évènement dans la base de données
    evenement.id = session.query(Evenement_bdd).order_by(Evenement_bdd.id.desc()).first()

def del_club(ida):
    try:
        club_to_delete=session.query(Club_bdd).filter_by(id=ida).one()#on récupère le club à supprimer
        licences_to_delete=session.query(Licence_bdd).filter_by(id_club=ida)# on récupère les licenses lié au club
        events_to_delete=session.query(Evenement_bdd).filter_by(id_club=ida)# on récupère les evenements lié au club
        try :
            for licence in licences_to_delete: #pour chaque licence
                del_licence(licence.id)
        except :
            pass
        try :
            for event in events_to_delete :# pour chaque evenement
                session.delete(event) # on le supprime

        except :
            pass
        session.delete(club_to_delete)#on supprime le club
        session.commit()
    except:
        print("le club n'existe pas")


    #TODO supprimer les licences associées au club, evenements, membres