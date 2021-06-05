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

    def rechercher_membre(self, name, firstname):

        membre=search_member(name=name, firstname=firstname)
        return membre


    def afficher_membres(self):
        membres=list_members_by_club(self.id)
        return membres

    def ajouter_membre(self, id_membre,id_licence):
        self.membres.append(id_membre)
        add_member_licence(id_membre,id_licence,0)

    def supprimer_membre(self, membre):
        del_member_licence_by_club(membre,self.id)

    def afficher_informations(self):
        print(f"nom : ${self.nom}")
        print(f"adresse : ${self.adresse}")
        print(f"description : ${self.description}")
        return self.nom, self.adresse, self.description


def creer_club(licence,club):
    create_club(club,licence)

def cre_club(nom, adresse, description, id_chef):
    club = Club(nom, adresse, description, id_chef)  # on créé une classe club
    add_club(club)  # on l'ajoute à la BDD
    return club

def lister_clubs():
    clubs = []
    clubs_bdd = list_clubs()
    for club_bdd in clubs_bdd:
        clubs.append(Club(club_bdd.nom, club_bdd.adresse, club_bdd.description, club_bdd.chef, id))
    return clubs


def recup_club(util):
    if util.id:
        clubs=list_clubs_by_member(util.id)
        if clubs  and not util.clubs:
            for club in clubs:
               util.clubs.append(Club(club.nom,club.adresse,club.description,club.chef))


def lister_licences_club(id_club):
    licences = []
    licences_bdd = list_licences_by_club(id_club)
    for licence_bdd in licences_bdd:
        licences.append(Licence(id_club, licence_bdd.name, licence_bdd.prix, licence_bdd.avantage, licence_bdd.id))
    return licences