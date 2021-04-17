class Evenement:
    def __init__(self, nom, lieu, date, horaire):
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.horaire = horaire

    def afficher_evenement(self):
        print(f"{self.nom} aura lieu à {self.lieu} le {self.date} à {self.horaire}")