from model.evenement_class import Evenement
from model.member_class import *
class Club:
    def __init__(self, id, nom, adresse, description, id_chef):
        self.id = id
        self.nom = nom
        self.adresse = adresse
        self.description = description
        self.chef = id_chef
        self.membres_bureau = []
        self.membres = []
        self.calendrier_evenements = []

    def changer_nom(self, nom):
        self.nom = nom
        modify_club(id, nom=nom)

    def afficher_adresse(self):
        print(self.adresse)

    def changer_adresse(self, adresse):
        self.adresse = adresse
        modify_club(id, adresse=adresse)

    def afficher_description(self):
        print(self.description)

    def changer_description(self):
        self.description = input("Entrez la nouvelle description")
        modify_club(id, description=self.description)

    def modifier_logo(self, logo):
        self.logo = logo

    def rechercher_membre(self,name,fullname):

        licenses = session.query(Licence_bdd).filter_by(id=self.id)  # on récupère toute les licences du clubs
        for i in licenses:  # pour chaque licence du club
            mem_lic = session.query(Member_licence).filter_by(
                id_licence=i.id)  # on récupère la table intermédiaire entre membre et licence
            for j in mem_lic:  # pour chaque ligne de la table
                mem=None
                mem = session.query(Member).filter_by(id=j.id,name=name,fullname=fullname)  # on récupère le membre
                if mem :
                    return Membre(mem.id,mem.name,mem.fullname,mem.user,mem.password,j.statut,j.id)
        return None


    def afficher_membres(self):
        licenses=session.query(Licence_bdd).filter_by(id=self.id)#on récupère toute les licences du club
        for i in licenses : #pour chaque licence du club
            mem_lic=session.query(Member_licence).filter_by(id_licence=i.id)#on récupère la table intermédiaire entre membre et licence
            for j in mem_lic :#pour chaque ligne de la table
                mem=session.query(Member).filter_by(id=j.id)#on récupère le membre
                print(mem.name,mem.fullname,j.statut)#et on l'affiche


    def ajouter_membre(self, membre):
        self.membres.append(membre)


    def supprimer_membre(self, membre):
        for i in range(len(self.membres)):
            if self.membres[i] == membre:
                self.membres.pop(i)
        session.delete(session.query(Member_licence).filter_by(user=id).one()) # on supprime la liaison entre l'utilisateur et la license dans la base de données
        session.commit()

    def afficher_evenements(self):
        for evenement in self.calendrier_evenements:
            evenement.afficher_evenement()

    def ajouter_evenement(self, nom, lieu, date, horaire):
        evenement = Evenement(nom, lieu, date, horaire)
        print("Entrez la description de l'événement :")
        evenement.nom = input("Nom :")
        evenement.lieu = input("Lieu :")
        evenement.date = input("Date (jj/mm/aaaa) :")
        evenement.horraire = input("Horraire (HHhMM) :")
        self.calendrier_evenements.append(evenement)
        # on ajoute l'évènement dans la base de données
        add_event(id, evenement)
        print(f"L'énévement {evenement.nom} a bien été ajouté au calendrier.")