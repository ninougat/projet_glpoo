from controller.member_class import *


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

    def affiher_nom(self):
        print(self.nom)
        return self.nom

    def afficher_adresse(self):
        print(self.adresse)
        return self.adresse

    def changer_adresse(self, adresse):
        self.adresse = adresse
        modify_club(self.id, adresse=adresse)

    def afficher_description(self):
        print(self.description)
        return self.description

    def changer_description(self):
        self.description = input("Entrez la nouvelle description")
        modify_club(self.id, description=self.description)

    def rechercher_membre(self, name, fullname):

        membre=search_member(name=name,fullname=fullname)
        return membre


    def afficher_membres(self):
        membres=list_members_by_club(self.id)
        return membres

    def ajouter_membre(self, membre):
        self.membres.append(membre.id)
        membre.clubs.append(self.id)

    def supprimer_membre(self, membre):
        del_member_licence_by_club(membre,self.id)


    def afficher_informations(self):
        print(f"nom : ${self.nom}")
        print(f"adresse : ${self.adresse}")
        print(f"description : ${self.description}")
        return self.nom, self.adresse, self.description

def creer_club(licence,club):
    create_club(club,licence)
