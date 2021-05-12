from glpoo_1.model.model import *


class User:

    def __init__(self, name, fullname, user, password, clubs=None, id=None):
        self.id = id
        self.name = name
        self.fullname = fullname
        self.user = user
        self.password = password
        if clubs:
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
        self.clubs.append(club.id)
        club.ajouter_membre(self.id)

    def desinscription(self, club):
        if club.id in self.clubs:
            self.clubs.remove(club.id)
            club.supprimer_membre(self.id)

    def consulter(self, club):
        club.afficher_informations()

    def supprimer(self):
        del_member(self.id)

    def creer_club(self, name):
        pass


class Membre(User):
    def __init__(self, name, fullname, user, password, type, licence):
        User.__init__(self, name=name, fullname=fullname, user=user, password=password)
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
        session.delete(session.query(Member_bdd).filter_by(user=user).one())
        session.commit()
