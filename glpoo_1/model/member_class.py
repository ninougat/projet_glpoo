from model import *
class User():

    def __init__(self,id,name,fullname,user,password,clubs):
        self.id=id
        self.name=name
        self.fullname=fullname
        self.user=user
        self.password=password
        self.clubs=clubs

    def Modifier_Profil(self,name=None,fullname=None,user=None,password=None):
        if name:
            self.name = name
        if fullname:
            self.fullname = fullname
        if user:
            self.user = user
        if password:
            self.password = password
        modify_name(self.id,name=name,fullname=fullname,user=user,password=password)


    def Inscription(self,club):
        pass
    def Desinscription(self,club):
        pass
    def Consulter(self,club):
        pass
    def supprimer(self):
        del_member(id)

    def creer_club(self,name):
        pass


class Membre(User):
    def __init__(self,member,type,licence):
        self.id=member.id
        self.name=member.name
        self.fullname=member.fullname
        self.user=member.user
        self.password=member.password
        self.type=type
        self.licence=licence

    def Changer_license(self):
        pass

    def Modifier_Club(self):
        pass

    def Modifier_license(self):
        pass

    def Lister_Membres(self):
        pass

    def Desinscrire_Membre(self,membre):
        pass

    def Promouvoir(self,membre):
        pass

    def Desinscrire_Membre(self,membre):
        pass

    def supprimer_Club(self):
        pass


class Admin(User):

    def Supprimer_Club(self,club):
        pass

    def Supprimer_Utilisateur(self,user):
        session.delete(session.query(Member).filter_by(user=user).one())
        session.commit()