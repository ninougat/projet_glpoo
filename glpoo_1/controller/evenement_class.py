
class Evenement:
    def __init__(self, id_club, nom=None, lieu=None, date=None, horaire=None, id=None):
        self.id = id
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.horaire = horaire
        self.id_club = id_club

    def afficher_evenement(self):
        print(f"{self.nom} aura lieu à {self.lieu} le {self.date} à {self.horaire}")