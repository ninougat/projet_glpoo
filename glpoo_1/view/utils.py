from view_classes import *
from model.club_class import *
from model.member_class import *
from model.licence_class import *


def generateProfile(user):
    profil = Page("Profil")

    profil.addZoneText(ZoneText(title="Prénom", text=user.name, textSize=[320, 50], textPos=[0, 30]))
    profil.addZoneText(ZoneText(title="Nom", text=user.fullname, textSize=[320, 50], textPos=[0, 90]))
    profil.addZoneText(ZoneText(title="Pseudo", text=user.user, textSize=[320, 50], textPos=[0, 150]))

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
