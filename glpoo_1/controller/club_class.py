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

        licenses = session.query(Licence_bdd).filter_by(id=self.id)  # on récupère toute les licences du clubs
        for i in licenses:  # pour chaque licence du club
            mem_lic = session.query(Member_licence).filter_by(
                id_licence=i.id)  # on récupère la table intermédiaire entre membre et licence
            for j in mem_lic:  # pour chaque ligne de la table
                mem = None
                mem = session.query(Member_bdd).filter_by(id=j.id, name=name, fullname=fullname)  # on récupère le membre
                if mem:
                    return Membre(mem.name, mem.fullname, mem.user, mem.password, j.statut, j.id)
        return None

    def afficher_membres(self):
        liste_membres = []
        licenses = session.query(Licence_bdd).filter_by(id=self.id)  # on récupère toutes les licences du club
        for i in licenses:  # pour chaque licence du club
            mem_lic = session.query(Member_licence).filter_by(id_licence=i.id)  # on récupère la table intermédiaire entre membre et licence
            for j in mem_lic:  # pour chaque ligne de la table
                mem = session.query(Member_bdd).filter_by(id=j.id)  # on récupère le membre
                liste_membres.append((mem.name, mem.fullname, j.statut))
                print(mem.name, mem.fullname, j.statut)  # et on l'affiche
        return liste_membres

    def ajouter_membre(self, membre):
        self.membres.append(membre.id)
        membre.clubs.append(self.id)

    def supprimer_membre(self, membre):
        for i in range(len(self.membres)):
            if self.membres[i] == membre:
                self.membres.pop(i)
        session.delete(session.query(Member_licence).filter_by(user=self.id).one()) # on supprime la liaison entre l'utilisateur et la license dans la base de données
        session.commit()

    def afficher_informations(self):
        print(f"nom : ${self.nom}")
        print(f"adresse : ${self.adresse}")
        print(f"description : ${self.description}")
        return self.nom, self.adresse, self.description

def creer_club(licence,club):
    create_club(club,licence)
