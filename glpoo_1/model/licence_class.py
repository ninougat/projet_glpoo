from model import *


class Licence:

    def __init__(self, id, id_club, name, prix, nb_sceance, avantage):
        self.id = id
        self.id_club = id_club
        self.name = name
        self.prix = prix
        self.nb_sceance = nb_sceance
        self.avantage = avantage

    def modifier_licence(self, name=None, prix=None, nb_sceance=None, avantage=None):
        if name:
            self.name = name
        if prix:
            self.prix = prix
        if nb_sceance:
            self.nb_sceance = nb_sceance
        if avantage:
            self.avantage = avantage
        modify_licence(self.id, name=name, prix=prix, nb_sceance=nb_sceance, avantage=avantage)

    def afficher_licence(self):
        print(" "+self.id+"\n")
        print(" " + self.name + "\n")
        print(" " + self.prix + "\n")
        print(" " + self.nb_sceance + "\n")
        print(" " + self.avantage + "\n")

    def supprimer_license(self):
        del_licence(id)


def creer_License(id_club, name, prix, nb_sceance, avantage):
    new_licence = Licence()
    new_licence.init(id_club, name, prix, nb_sceance, avantage)
    add_licence(id_club, name, prix, nb_sceance, avantage)
