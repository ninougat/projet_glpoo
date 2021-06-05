from view_classes import *
from controller.club_class import *
from controller.member_class import *
from controller.licence_class import *


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


def generateClubPage(club):
    page = Page("club " + club.nom)

    type_membre = 3

    if type_membre < 2:
        page.addText(Text(content="Adresse : " + club.adresse, textSize=[320, 50], textPos=[0, 30]))
        page.addText(Text(content=club.description, textSize=[320, 50], textPos=[0, 90]))

    if type_membre > 1:
        page.addZoneText(ZoneText(title="Adresse", text=club.adresse, textSize=[320, 50], textPos=[0, 30]))
        page.addZoneText(ZoneText(title="", text=club.description, textSize=[320, 50], textPos=[0, 90]))

    if type_membre == 0:
        page.addButton(Button([320, 50], [0, 150], text="S'inscrire"))

    if type_membre > 0:
        page.addButton(Button([320, 50], [0, 150], text="Se desinscrire"))
        page.addButton(Button([320, 50], [0, 210], text="Voir licence"))

    if type_membre > 1:
        page.addButton(Button([320, 50], [0, 270], text="Afficher tous les membres"))
        page.addButton(Button([320, 50], [0, 330], text="Ajouter licence"))

    if type_membre == 3:
        page.addButton(Button([320, 50], [0, 390], text="Afficher le bureau"))
        page.addButton(Button([320, 50], [0, 450], text="Supprimer le club"))

    return page


def generatelicencePage(licence):
    page = Page("licence " + licence.nom)

    type_membre = 3

    if type_membre < 2:
        page.addText(Text(content="Prix : "+licence.prix, textSize=[320, 50], textPos=[0, 30]))
        page.addText(Text(content="nb_seances : "+licence.nb_seances, textSize=[320, 50], textPos=[0, 90]))
        page.addText(Text(content="Avantages : "+licence.avantage, textSize=[320, 50], textPos=[0, 150]))
    if type_membre > 1:
        page.addZoneText(ZoneText(title="Prix", text=licence.prix, textSize=[320, 50], textPos=[0, 30]))
        page.addZoneText(ZoneText(title="nb_seances", text=licence.nb_seances, textSize=[320, 50], textPos=[0, 90]))
        page.addZoneText(ZoneText(title="Avantages", text=licence.avantage, textSize=[320, 50], textPos=[0, 150]))

    if type_membre > 0:
        page.addButton(Button([320, 50], [0, 210], text="Changer licence"))

    if type_membre > 1:
        page.addButton(Button([320, 50], [0, 270], text="Ajouter licence"))
        page.addButton(Button([320, 50], [0, 330], text="Supprimer licence"))
        page.addButton(Button([320, 50], [0, 390], text="Modifier licence"))

    return page

def generateNouveauClub():
    page = Page("Ajouter un Club")
    page.addZoneText(ZoneText(title="Nom", text="", textPos=[0, 30]))
    page.addZoneText(ZoneText(title="Adresse", text="", textPos=[0, 90]))
    page.addZoneText(ZoneText(title="Description", text="", textPos=[0, 150]))
    page.addButton(Button([320, 50], [0, 210], text="Ajouter licence"))
    return page

def generateAjouterlicence(id):
    page = Page("Ajouter licence")
    page.addZoneText(ZoneText(title="ID", text=str(id),  textPos=[0, 30]))
    page.addZoneText(ZoneText(title="Nom", text="", textPos=[0, 90]))
    page.addZoneText(ZoneText(title="Prix", text="", textPos=[0, 150]))
    page.addZoneText(ZoneText(title="Nombre de seances", text="", textPos=[0, 210]))
    page.addZoneText(ZoneText(title="Description", text="", textPos=[0, 270]))
    page.addButton(Button([320, 50], [0, 330], text="Valider"))
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


def generateMemberList():
    member = Page("Membres")

    return member


def generateBureauList():
    bureau = Page("Bureau")

    return bureau
