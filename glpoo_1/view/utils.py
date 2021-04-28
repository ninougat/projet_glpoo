from view_classes import *
from model.club_class import *
from model.member_class import *
from model.licence_class import *

def GenerateProfile (user):
    profil = Page ()

    profil.addZoneText(ZoneText (title="Prénom", text=user.name, textSize=[320, 50], textPos=[0, 20]))
    profil.addZoneText(ZoneText (title="Nom", text=user.fullname, textSize=[320, 50], textPos=[0, 80]))
    profil.addZoneText(ZoneText (title="Pseudo", text=user.user, textSize=[320, 50], textPos=[0, 140]))

    return profil


def GenerateMesClubs (clubs):
    mesClubs = Page ()

    idx = 0
    for club, isInscrit in clubs:
        if isInscrit:
            mesClubs.addButton(Button([320, 50], [0, 20 + 60 * idx], text=club.nom))
            mesClubs.links[str (idx)] = club
            idx += 1

    return mesClubs

def GenerateClubs (clubs):
    liste = Page ()

    idx = 0
    for club, isInscrit in clubs:
        if not isInscrit:
            liste.addButton(Button([320, 50], [0, 20 + 60 * idx], text=club.nom))
            liste.links[str (idx)] = club
            idx += 1

    return liste

def GenerateClubPage (club):
    page = Page ()

    page.addButton(Button ([320, 50], [0, 20], text=club.description))

    return page

