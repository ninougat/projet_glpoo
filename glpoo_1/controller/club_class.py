from controller.member_class import *
from controller.licence_class import *


class Club:
    def __init__(self, nom, adresse, description, id_chef, id=None):
        self.id = id
        self.nom = nom
        self.adresse = adresse
        self.description = description
        self.chef = id_chef
        self.membres_bureau = []
        self.membres = []

    def changer_nom(self, nom):
        self.nom = nom
        modify_club(self.id, nom=nom)


    def changer_adresse(self, adresse):
        self.adresse = adresse
        modify_club(self.id, adresse=adresse)


    def changer_description(self):
        self.description = input("Entrez la nouvelle description")
        modify_club(self.id, description=self.description)

    def rechercher_membre(self, name, firstname):
        membre=search_member(name=name, firstname=firstname)
        return User(membre.name, membre.firstname, membre.user, membre.password, membre.id)

    def afficher_membres(self, type):
        membres = []
        membres_bdd=list_members_by_club(self.id)
        for membre_bdd in membres_bdd:
            if membre_bdd.statut >= type :
                membre = search_member(id=membre_bdd.id_member)
                licence = search_licence(membre_bdd.id_licence)
                membres.append({"membre": User(membre.name, membre.firstname, membre.user, membre.password, membre.id), "licence": licence[0], "statut": membre_bdd.statut})
        return membres

    def ajouter_membre(self, id_membre,id_licence):
        self.membres.append(id_membre)
        add_member_licence(id_membre,id_licence,0)

    def supprimer_membre(self, id_membre):
        del_member_licence_by_club(id_membre,self.id)



