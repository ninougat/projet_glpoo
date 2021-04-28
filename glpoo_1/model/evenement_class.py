class Evenement:
    def __init__(self, id, nom, lieu, date, horaire,id_club):
        self.id = id
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.horaire = horaire
        self.id_club=id_club

    def afficher_evenement(self):
        print(f"{self.nom} aura lieu à {self.lieu} le {self.date} à {self.horaire}")