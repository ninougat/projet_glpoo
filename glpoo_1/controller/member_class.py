from model.model import *


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
        del_member(self.id)# on supprime le membbre via son ID

    def creer_club(self, nom,adresse,description):
        clu=Club(nom,adresse,description,self.id)#on créé une classe club
        add_club(club);#on l'ajoute à la BDD

class Membre(User):
    def __init__(self, name, fullname, user, password, type, licence):
        User.__init__(self, name=name, fullname=fullname, user=user, password=password)
        self.type = type
        self.licence = licence

    def changer_license(self,n_licence):
        self.licence=n_licence# on remplace l'ancienen licence par la nouvelle

    def modifier_club(self,club,nom=None, adresse=None, chef=None, description=None):
        modify_club(club.id,nom=nom,adresse=adresse,chef=chef,description=description)#On modifie le club en fonction des infos founi par les parametres

    def modifier_license(self,licence,name=None, prix=None, nb_seances=None, avantage=None):
        modify_licence(ida=licence.id,name=name,prix=prix,nb_seances=nb_seances,avantage=avantage)

    def lister_membres(self):
        pass

    def desinscrire_membre(self, membre):
        pass

    def promouvoir(self, membre):
        modify_membre_licence(id_licence=membre.licence, statut=1,id_member=membre.id)

    def supprimer_Club(self,club):
        del_club(club.id)


class Admin(User):

    def supprimer_club(self, club):
        del_club(club.id)

    def supprimer_utilisateur(self, user):
        del_Member(user.id)
        session.delete(session.query(Member_bdd).filter_by(user=user).one())
        session.commit()
