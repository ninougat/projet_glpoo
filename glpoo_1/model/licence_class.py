from model import *


class Licence:

    def __init__(self, id, id_club, name, prix, nb_seances, avantage):
        self.id = id
        self.id_club = id_club
        self.name = name
        self.prix = prix
        self.nb_seances = nb_seances
        self.avantage = avantage

    def modifier_licence(self, name=None, prix=None, nb_seances=None, avantage=None):
        if name:
            self.name = name
        if prix:
            self.prix = prix
        if nb_seances:
            self.nb_seances = nb_seances
        if avantage:
            self.avantage = avantage
        modify_licence(self.id, name=name, prix=prix, nb_seances=nb_seances, avantage=avantage)

    def afficher_licence(self):
        print(" "+self.id+"\n")
        print(" " + self.name + "\n")
        print(" " + self.prix + "\n")
        print(" " + self.nb_seances + "\n")
        print(" " + self.avantage + "\n")

    def supprimer_licence(self):
        del_licence(id)


def creer_License(id_club, name, prix, nb_seance, avantage):
    add_licence(id_club, name, prix, nb_seance, avantage)
