from evenement_class import Evenement

class Club:
    def __init__(self):
        self.id = 0
        self.nom = ""
        self.adresse = ""
        self.logo = ""
        self.description = ""
        self.chef = 0
        self.membres_bureau = []
        self.membres = []
        self.calendrier_evenements = []

    def changer_nom(self, nom):
        self.nom = nom

    def afficher_adresse(self):
        print(self.adresse)

    def changer_adresse(self, adresse):
        self.adresse = adresse

    def afficher_description(self):
        print(self.description)

    def changer_description(self):
        self.description = input("Entrez la nouvelle description")

    def afficher_logo(self):
        #TODO
        pass

    def modifier_logo(self, logo):
        self.logo = logo

    def rechercher_membre(self):
        pass
        #TODO requète bdd sur nom prenom

    def afficher_membres(self):
        #TODO requète BDD
        pass

    def ajouter_membre(self, membre):
        self.membres.append(membre)

    def supprimer_membre(self, membre):
        for i in range(len(self.membres)):
            if self.membres[i] == membre:
                self.membres.pop(i)

    def afficher_evenements(self):
        for evenement in self.calendrier_evenements:
            evenement.afficher_evenement()

    def ajouter_evenement(self):
        evenement = Evenement()
        print("Entrez la description de l'événement :")
        evenement.nom = input("Nom :")
        evenement.lieu = input("Lieu :")
        evenement.date = input("Date (jj/mm/aaaa) :")
        evenement.horraire = input("Horraire (HHhMM) :")
        self.calendrier_evenements.append(evenement)
        #TODO ajout BDD
        print(f"L'énévement {evenement.nom} a bien été ajouté au calendrier.")