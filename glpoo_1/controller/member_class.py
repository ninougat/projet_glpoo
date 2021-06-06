from model.model import *


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
        modify_member(self.id, name=name, firstname=firstname, user=user, password=password)

    def inscription(self, club,id_licence):
        self.clubs.append(club)
        club.ajouter_membre(self.id,id_licence)

    def desinscription(self, club):
        if club.id in self.clubs:
            self.clubs.remove(club.id)
            club.supprimer_membre(self.id)

    def supprimer(self):
        del_member(self.id)# on supprime le membre via son ID


class Membre(User):
    def __init__(self, name,  firstname, user, password, type, licence):
        User.__init__(self, name=name,  firstname=firstname, user=user, password=password)
        self.type = type
        self.id_licence = licence

    def changer_license(self,n_licence):
        id_club = get_club_by_licence(self.id_licence).id # on récupère l'id du club
        licence, statut = get_licence_by_club_and_member(self.id, id_club) # on récupère l'id de la ligne qui associe le membre à sa licence
        self.id_licence=n_licence# on remplace l'ancienne licence par la nouvelle
        modify_membre_licence(ida=licence.id, id_licence=n_licence) # on change la licence dans la BDD

    def modifier_club(self,club,nom=None, adresse=None, chef=None, description=None):
        modify_club(club.id,nom=nom,adresse=adresse,chef=chef,description=description)#On modifie le club en fonction des infos founi par les parametres

    def modifier_licence(self,licence,name=None, prix=None, nb_seances=None, avantage=None):
        if self.type>0:
            modify_licence(ida=licence.id,name=name,prix=prix,nb_seances=nb_seances,avantage=avantage)

    def lister_membres(self):
        club = get_club_by_licence(self.id_licence)
        return list_members_by_club(club.id)

    def desinscrire_membre(self, membre, club):
        licence, statut = get_licence_by_club_and_member(membre.id, club.id)
        if self.type > statut:
            del_member_licence(id_member=membre.id, id_licence=licence.id)

    def promouvoir(self, membre, club):
        licence, statut = get_licence_by_club_and_member(membre.id, club.id)
        if statut == 0 and self.type > 0:
            modify_membre_licence(id_licence=licence.id, statut=1, id_member=membre.id)
        elif statut == 1 and self.type == 2:
            modify_membre_licence(id_licence=licence.id, statut=2, id_member=membre.id)
            modify_membre_licence(id_licence=self.id_licence, statut=1, id_member=self.id)
            modify_club(club.id, chef=membre.id)
            self.type = 1
        else :
            print(" la promotion n'a pas eu lieu , un des parametres est incorrect")

    def retrograder(self, membre, club):
        licence, statut = get_licence_by_club_and_member(membre.id, club.id)
        if statut == 1 and self.type == 2:
            modify_membre_licence(id_licence=licence.id, statut=0, id_member=membre.id)
        elif statut!=1 :
            print(" la retrogradation n'a pas eu lieu,"+membre.name+" la cible  n'est pas membre du bureau ou est le chef")
        elif self.type!=2 :
            print(" la retrogradation n'a pas eu lieu, vous n'etes pas chef")

    def supprimer_Club(self):
        if self.type == 2:
            club = get_club_by_licence(self.id_licence)
            if club:
                del_club(club.id)