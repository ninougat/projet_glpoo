from model import *


class User:

    def __init__(self, id, name, fullname, user, password, clubs=None):
        self.id = id
        self.name = name
        self.fullname = fullname
        self.user = user
        self.password = password
        if clubs is not None:
            self.clubs = clubs
        else:
            self.clubs = []

    def modifier_profil(self, name=None, fullname=None, user=None, password=None):
        if name:
            self.name = name
        if fullname:
            self.fullname = fullname
        if user:
            self.user = user
        if password:
            self.password = password
        modify_member(self.id, name=name, fullname=fullname, user=user, password=password)

    def inscription(self, club):
        self.clubs.append(club)
        club.ajouter_membre(self.id)

    def desinscription(self, club):
        if club in self.clubs:
            self.clubs.remove(club)
            club.supprimer_membre(self.id)

    def consulter(self, club):
        pass

    def supprimer(self):
        del_member(self.id)

    def creer_club(self, name):
        pass


class Membre(User):
    def __init__(self, id, name, fullname, user, password, type, licence):
        User.__init__(id, name, fullname, user, password)
        self.type = type
        self.licence = licence

    def changer_license(self):
        pass

    def modifier_club(self):
        pass

    def modifier_license(self):
        pass

    def lister_membres(self):
        pass

    def desinscrire_membre(self, membre):
        pass

    def promouvoir(self, membre):
        pass

    def supprimer_Club(self):
        pass


class Admin(User):

    def supprimer_club(self, club):
        pass

    def supprimer_utilisateur(self, user):
        session.delete(session.query(Member).filter_by(user=user).one())
        session.commit()
