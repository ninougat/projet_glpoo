from model.model import *
from controller.club_class import *


class User:

    def __init__(self, name, firstname, user, password, id=None):
        self.id = id
        self.name = name
        self.firstname = firstname
        self.user = user
        self.password = password
        self.clubs = []

    def modifier_profil(self, name=None, firstname=None, user=None, password=None):
        if name:
            self.name = name
        if firstname:
            self.firstname = firstname
        if user:
            self.user = user
        if password:
            self.password = password
        modify_member(self.id, name=name, fullname=firstname, user=user, password=password)

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
        club=Club(nom,adresse,description,self.id)#on créé une classe club
        add_club(club)#on l'ajoute à la BDD

class Membre(User):
    def __init__(self, name,  firstname, user, password, type, licence):
        User.__init__(self, name=name,  firstname=firstname, user=user, password=password)
        self.type = type
        self.licence = licence

    def changer_license(self,n_licence):
        self.licence=n_licence# on remplace l'ancienen licence par la nouvelle

    def modifier_club(self,club,nom=None, adresse=None, chef=None, description=None):

        modify_club(club.id,nom=nom,adresse=adresse,chef=chef,description=description)#On modifie le club en fonction des infos founi par les parametres

    def modifier_licence(self,licence,name=None, prix=None, nb_seances=None, avantage=None):
        if self.type>0:
            modify_licence(ida=licence.id,name=name,prix=prix,nb_seances=nb_seances,avantage=avantage)

    def lister_membres(self):
        club= get_club_by_licence(self.licence)
        return list_members_by_club(club.id)


    def desinscrire_membre(self, membre):
        if self.type > membre.type:

            del_member_licence(id_member=membre.id,id_licence=membre.licence)

    def promouvoir(self, membre,club):
        if membre.type==0 and self.type>0 :
            modify_membre_licence(id_licence=membre.licence, statut=1,id_member=membre.id)
        elif membre.type==1 and self.type==2:
            modify_membre_licence(id_licence=membre.licence, statut=2, id_member=membre.id)
            modify_membre_licence(id_licence=self.licence, statut=1, id_member=self.id)
            modify_club(club.id,chef=membre.id)
            self.type=1

    def supprimer_Club(self,club):
        if self.type==2:
            club=get_club_by_licence(self.licence)
            if club:
                del_club(club.id)


class Admin(User):

    def supprimer_club(self, club):
        del_club(club.id)

    def supprimer_utilisateur(self, user):
        del_member(user.id)


def connexion(pseudo, password):
    utilisateur = search_member(pseudo)
    compte = None
    print(pseudo)
    print(password)
    print(utilisateur)
    if utilisateur and utilisateur[0] == password:
        print("1")
        if utilisateur[1] == "user":
            compte = User(utilisateur[2], utilisateur[3], utilisateur[4], utilisateur[5])
            compte.clubs = list_clubs_by_member(compte.id)
        else:
            compte = Admin(utilisateur[2], utilisateur[3], utilisateur[4], utilisateur[5])
    print(compte.user)
    return compte


