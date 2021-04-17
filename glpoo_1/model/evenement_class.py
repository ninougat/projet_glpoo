class Evenement:
    def __init__(self, nom, lieu, date, horraire):
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.horraire = horraire

    def afficher_evenement(self):
        print(f"{self.nom} aura lieu à {self.lieu} le {self.date} à {self.horraire}")