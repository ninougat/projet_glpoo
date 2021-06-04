from view_classes import *
from controller.club_class import *
from controller.member_class import *
from controller.licence_class import *


def generateProfile(user):
    profil = Page("Profil")

    profil.addZoneText(ZoneText(title="Prénom", text=user.name, textSize=[320, 50], textPos=[0, 25]))
    profil.addZoneText(ZoneText(title="Nom", text=user.fullname, textSize=[320, 50], textPos=[0, 80]))
    profil.addZoneText(ZoneText(title="Pseudo", text=user.user, textSize=[320, 50], textPos=[0, 135]))
    profil.addZoneText(ZoneText(title="Mot de passe", text=user.password, textSize=[320, 50], textPos=[0, 190]))
    return profil


def generateMesClubs(clubs):
    mesClubs = Page("Mes clubs")

    idx = 0
    for club, isInscrit in clubs:
        if isInscrit:
            mesClubs.addButton(Button([320, 50], [0, 30 + 60 * idx], text=club.nom))
            mesClubs.links[str(idx)] = club
            idx += 1

    return mesClubs


def generateClubs(clubs):
    liste = Page("Clubs")

    idx = 0
    for club, isInscrit in clubs:
        if not isInscrit:
            liste.addButton(Button([320, 50], [0, 30 + 60 * idx], text=club.nom))
            liste.links[str(idx)] = club
            idx += 1

    return liste


def generateClubPage(club):
    page = Page(club.nom)

    page.addButton(Button([320, 50], [0, 30], text=club.description))

    return page


def generateConnexion():
    Connection = Page("Connexion")
    Connection.addZoneText(ZoneText(title="Identifiant", text="", textPos=[0, 30]))
    Connection.addZoneText(ZoneText(title="mots de passe", text="", textPos=[0, 90]))
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