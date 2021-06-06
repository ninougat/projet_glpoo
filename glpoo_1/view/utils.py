from view.view_classes import *


def generateProfile(user):
    profil = Page("Profil")

    profil.addZoneText(ZoneText(title="Prénom", text=user.name, textSize=[320, 50], textPos=[0, 25]))
    profil.addZoneText(ZoneText(title="Nom", text=user.firstname, textSize=[320, 50], textPos=[0, 80]))
    profil.addZoneText(ZoneText(title="Pseudo", text=user.user, textSize=[320, 50], textPos=[0, 135]))
    profil.addZoneText(ZoneText(title="Mot de passe", text=user.password, textSize=[320, 50], textPos=[0, 190]))
    return profil


def generateMesClubs(clubs):
    mesClubs = Page("Mes clubs")

    idx = 0
    for club in clubs:
        mesClubs.addButton(Button([320, 50], [0, 30 + 60 * idx], text=club.nom))
        mesClubs.links[str(idx)] = club
        idx += 1

    return mesClubs



def generateClubs(clubs):
    liste = Page("Clubs")

    idx = 0
    for club in clubs:
        liste.addButton(Button([320, 50], [0, 30 + 60 * idx], text=club.nom))
        liste.links[str(idx)] = club
        idx += 1

    return liste


def generateClubPage(club, type_membre):
    page = Page("club " + club.nom)

    if type_membre < 2:
        page.addText(Text(content="Adresse : " + club.adresse, textSize=[320, 50], textPos=[0, 30]))
        page.addText(Text(content=club.description, textSize=[320, 50], textPos=[0, 90]))

    if type_membre > 1:
        page.addZoneText(ZoneText(title="Adresse", text=club.adresse, textSize=[320, 50], textPos=[0, 30]))
        page.addZoneText(ZoneText(title="", text=club.description, textSize=[320, 50], textPos=[0, 90]))

    if type_membre == 0:
        page.addButton(Button([320, 50], [0, 150], text="S'inscrire"))

    if 0 < type_membre < 3:
        page.addButton(Button([320, 50], [0, 150], text="Se desinscrire"))

    if type_membre > 0:
        page.addButton(Button([320, 50], [0, 210], text="Voir licence"))

    if type_membre > 1:
        page.addButton(Button([320, 50], [0, 270], text="Afficher tous les membres"))
        page.addButton(Button([320, 50], [0, 330], text="Ajouter licence"))

    if type_membre == 3:
        page.addButton(Button([320, 50], [0, 150], text="Afficher le bureau"))
        page.addButton(Button([320, 50], [0, 390], text="Supprimer le club"))

    return page


def generateNouveauClub():
    page = Page("Ajouter un Club")
    page.addZoneText(ZoneText(title="Nom", text="", textPos=[0, 30]))
    page.addZoneText(ZoneText(title="Adresse", text="", textPos=[0, 90]))
    page.addZoneText(ZoneText(title="Description", text="", textPos=[0, 150]))
    page.addButton(Button([320, 50], [0, 210], text="Ajouter licence"))
    return page


def generateMesLicences(licences):
    mesLicences = Page("Mes licences")

    idx = 0
    for licence in licences:
        mesLicences.addButton(Button([320, 50], [0, 30 + 60 * idx], text=licence.name))
        mesLicences.links[str(idx)] = licence
        idx += 1

    return mesLicences


def generatelicencePage(licence, type_membre):
    page = Page("licence " + licence.name)
    if type_membre < 2:
        page.addText(Text(content="Prix : "+str(licence.prix), textSize=[320, 50], textPos=[0, 30]))
        page.addText(Text(content="nb_seances : "+str(licence.nb_seances), textSize=[320, 50], textPos=[0, 90]))
        page.addText(Text(content="Avantages : "+licence.avantage, textSize=[320, 50], textPos=[0, 150]))
    if type_membre > 1:
        page.addZoneText(ZoneText(title="Prix", text=str(licence.prix), textSize=[320, 50], textPos=[0, 30]))
        page.addZoneText(ZoneText(title="nb_seances", text=str(licence.nb_seances), textSize=[320, 50], textPos=[0, 90]))
        page.addZoneText(ZoneText(title="Avantages", text=licence.avantage, textSize=[320, 50], textPos=[0, 150]))

    if type_membre > 0:
        page.addButton(Button([320, 50], [0, 210], text="Changer licence"))

    if type_membre > 1:
        page.addButton(Button([320, 50], [0, 270], text="Ajouter licence"))
        page.addButton(Button([320, 50], [0, 330], text="Supprimer licence"))
        page.addButton(Button([320, 50], [0, 390], text="Modifier licence"))

    return page



def generateAjouterlicence(id):
    page = Page("Ajouter licence")
    page.addZoneText(ZoneText(title="Nom", text="", textPos=[0, 30]))
    page.addZoneText(ZoneText(title="Prix", text="", textPos=[0, 90]))
    page.addZoneText(ZoneText(title="Nombre de seances", text="", textPos=[0, 150]))
    page.addZoneText(ZoneText(title="Description", text="", textPos=[0, 210]))
    page.addButton(Button([320, 50], [0, 270], text="Valider"))
    return page


def generateConnexion():
    Connection = Page("Connexion")
    Connection.addZoneText(ZoneText(title="Identifiant", text="", textPos=[0, 30]))
    Connection.addZoneText(ZoneText(title="mot de passe", text="", textPos=[0, 90]))
    Connection.addButton(Button([320, 50], [0, 150], text="Valider"))
    return Connection


def generateNouveauMembre():
    Nouveau = Page("Nouveau Membre")
    Nouveau.addZoneText(ZoneText(title="Nom", text="", textSize=[320, 40], textPos=[0, 22]))
    Nouveau.addZoneText(ZoneText(title="Prenom", text="", textSize=[320, 40], textPos=[0, 64]))
    Nouveau.addZoneText(ZoneText(title="Pseudo", text="", textSize=[320, 40], textPos=[0, 106]))
    Nouveau.addZoneText(ZoneText(title="Mot de passe", text="", textSize=[320, 40], textPos=[0, 148]))
    Nouveau.addButton(Button([320, 40], [0, 190], text="Valider"))
    return Nouveau


def generateMemberList(membres):
    liste = Page("Membres")
    idx = 0
    print(membres)
    for membre in membres:
        print(membre)
        print(membre["membre"].name)
        liste.addButton(Button([320, 50], [0, 30 + 60 * idx], text=membre["membre"].name))
        liste.links[str(idx)] = membre
        idx += 1
    return liste


def generateMembrePage(membre1, membre):
    Nouveau = Page("Membre "+membre["membre"].name +" "+str(membre["statut"]))
    if membre["statut"] == 0 and membre1.type > 0:
        Nouveau.addText(Text(content="Nom : " + membre["membre"].name, textSize=[320, 40], textPos=[0, 22]))
        Nouveau.addText(Text(content="Prenom : " + membre["membre"].firstname, textSize=[320, 40], textPos=[0, 64]))
        Nouveau.addText(Text(content="Pseudo : " + membre["membre"].user, textSize=[320, 40], textPos=[0, 106]))
        Nouveau.addText(Text(content="licence : " + membre["licence"], textSize=[320, 40], textPos=[0, 148]))
        Nouveau.addButton(Button([160, 40], [0, 190], text="Désinscrire"))
        Nouveau.addButton(Button([160, 40], [160, 190], text="Promouvoir"))
    elif membre["statut"] == 1 and membre1.type > 1:
        Nouveau.addText(Text(content="Nom : " + membre["membre"].name, textSize=[320, 40], textPos=[0, 22]))
        Nouveau.addText(Text(content="Prenom : " + membre["membre"].firstname, textSize=[320, 40], textPos=[0, 64]))
        Nouveau.addText(Text(content="Pseudo : " + membre["membre"].user, textSize=[320, 40], textPos=[0, 106]))
        Nouveau.addText(Text(content="licence : "+membre["licence"], textSize=[320, 40], textPos=[0, 148]))
        Nouveau.addButton(Button([100, 40], [0, 190], text="Désinscrire"))
        Nouveau.addButton(Button([100, 40], [105, 190], text="Retrograder"))
        Nouveau.addButton(Button([100, 40], [210, 190], text="Promouvoir"))
    elif membre["statut"] == 2 and membre1.type == 2:
        Nouveau.addText(Text(content="Nom : " + membre["membre"].name, textSize=[320, 40], textPos=[0, 22]))
        Nouveau.addText(Text(content="Prenom : " + membre["membre"].firstname, textSize=[320, 40], textPos=[0, 64]))
        Nouveau.addText(Text(content="Pseudo : " + membre["membre"].user, textSize=[320, 40], textPos=[0, 106]))
        Nouveau.addText(Text(content="licence : " + membre["licence"], textSize=[320, 40], textPos=[0, 148]))
        Nouveau.addButton(Button([160, 40], [0, 190], text="Désinscrire"))
        Nouveau.addButton(Button([160, 40], [160, 190], text="Retrograder"))
    else:
        Nouveau.addText(Text(content="Nom : " + membre["membre"].name, textSize=[320, 40], textPos=[0, 22]))
        Nouveau.addText(Text(content="Prenom : " + membre["membre"].firstname, textSize=[320, 40], textPos=[0, 64]))
        Nouveau.addText(Text(content="Pseudo : " + membre["membre"].user, textSize=[320, 40], textPos=[0, 106]))
    return Nouveau

def generateBureauList(membres_bureau):
    bureau = Page("Bureau")

    idx = 0
    for membre in membres_bureau:
        bureau.addButton(Button([320, 50], [0, 30 + 60 * idx], text=membre["membre"].name))
        bureau.links[str(idx)] = membre
        idx += 1

    return bureau
