class Evenement:
    def __init__(self):
        self.nom = ""
        self.lieu = ""
        self.date = ""
        self.horraire = ""

    def afficher_evenement(self):
        print(f"{self.nom} aura lieu à {self.lieu} le {self.date} à {self.horraire}")