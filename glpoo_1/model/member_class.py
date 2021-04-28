from model import *


class User():

    def __init__(self,id,name,fullname,user,password,clubs=None):
        self.id=id
        self.name=name
        self.fullname=fullname
        self.user=user
        self.password=password
        if clubs is not None:
            self.clubs=clubs
        else:
            self.clubs = []

    def modifier_Profil(self,name=None,fullname=None,user=None,password=None):
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
        club.ajouter_membre(id)

    def desinscription(self, club):
        if club in self.clubs:
            self.clubs.remove(club)
            club.supprimer_membre(id)

    def consulter(self,club):
        pass

    def supprimer(self):
        del_member(id)

    def creer_club(self,name):
        pass


class Membre(User):
    def __init__(self,id,name,fullname,user,password,type,licence):
        User.__init__(id,name,fullname,user,password)
        self.type=type
        self.licence=licence

    def changer_license(self):
        pass

    def modifier_Club(self):
        pass

    def modifier_license(self):
        pass

    def lister_Membres(self):
        pass

    def desinscrire_Membre(self,membre):
        pass

    def promouvoir(self,membre):
        pass

    def desinscrire_Membre(self,membre):
        pass

    def supprimer_Club(self):
        pass


class Admin(User):

    def supprimer_Club(self, club):
        pass

    def supprimer_Utilisateur(self, user):
        session.delete(session.query(Member).filter_by(user=user).one())
        session.commit()