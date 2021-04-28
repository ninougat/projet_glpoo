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


class Member(Base):
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
    add_user = Member(name=membre.name, fullname=membre.fullname, user=membre.user, password=membre.password, status=membre.status)
    session.add(add_user)
    session.commit()
    # on récupère l'id de l'évènement dans la base de données
    membre.id = session.query(Evenement_bdd).order_by(Evenement_bdd.id.desc()).first()


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
            mod.name = name
        if fullname:
            mod.fullname = fullname
        if user:
            mod.user = user
        if password:
            mod.password = password
    except:
        print("L'id " + ida + " de la table members n'existe pas")


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
    try:
        session.delete(session.query(Licence_bdd).filter_by(id=ida).one())
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
        session.query(Member).filter_by(id=club.chef).one()  # on vérifie que l'ID passé en paramètre existe
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
            session.query(Member).filter_by(id=chef).one()  # on vérifie que l'ID passé en paramètre existe
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
        session.delete(session.query(Club_bdd).filter_by(id=ida).one())
        session.commit()
    except:
        print("le club n'existe pas")
