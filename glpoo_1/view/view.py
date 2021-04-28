from view_classes import *
from utils import *
from model.club_class import *
from model.member_class import *
from model.licence_class import *

def vue():
    pg.init()
    size = width, height = 320, 240
    screen = pg.display.set_mode(size)
    pg.display.set_caption("Oui.")
    font = pg.font.SysFont(None, 20)
    screen.fill([255, 255, 255])

    util = User (0, "Quentin", "PAJON", "Quentin", "12345", [])


    clubs = []
    c = Club (0, "Club Chef", "Adresse Chef", "Ceci est un club dont vous etes le chef", util.id)
    clubs.append([c, 1])
    # util.ajoutLicence(0, 3)

    c = Club (1, "Club Bureau", "Adresse Bureau", "Ceci est un club dont vous etes membre du bureau", 1)
    clubs.append([c, 1])
    # util.ajoutLicence(0, 2)

    c = Club (2, "Club Membre", "Adresse Membre", "Ceci est un club dont vous etes un membre", 1)
    clubs.append([c, 1])
    # util.ajoutLicence(0, 1)

    for i in range(10):
        c = Club (3 + i, "Club %d" % i, "Adresse club n°%d" % i, "Ceci est le club n°%d" % i, 1)
        clubs.append ([c, 0])


    Accueil = Page ()
    Accueil.addButton(Button([320, 50], [0, 20], text="Votre profil"))
    Accueil.addButton(Button([320, 50], [0, 80], text="Liste de vos Clubs"))
    Accueil.addButton(Button([320, 50], [0, 140], text="Rechercher des Clubs"))

    page = Accueil
    current = "Accueil"

    run = 1
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = 0
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    if current == "Accueil":
                        run = 0
                    else:
                        if current == "Profil":
                            util.name = page.GetZone("Prénom")
                            util.fullname = page.GetZone ("Nom")
                            util.user = page.GetZone ("Pseudo")
                        current = "Accueil"
                        page = Accueil
                for text in page.zoneTexts:
                    if text.isIn:
                        text.handleKeyDown (event)
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for button in page.buttons:
                        button.mouseInButton(True)
                    for zone in page.zoneTexts:
                        zone.clickIn ()
                if current == "Mes clubs" or current == "Clubs":
                    if event.button == 4:
                        page.ScrollUp()
                    if event.button == 5:
                        page.ScrollDown()
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    for idx, button in enumerate (page.buttons):
                        wasPressed = button.mouseInButton(False)
                        if wasPressed:
                            if current == "Accueil":
                                if button.content == "Votre profil":
                                    current = "Profil"
                                    page = GenerateProfile(util)
                                elif button.content == "Liste de vos Clubs":
                                    current = "Mes clubs"
                                    page = GenerateMesClubs(clubs)
                                elif button.content == "Rechercher des Clubs":
                                    current = "Clubs"
                                    page = GenerateClubs(clubs)
                            elif current == "Profil":
                                pass
                            elif current == "Mes clubs":
                                current = str (page.links[str (idx)].id)
                                page = GenerateClubPage(page.links[str (idx)])
                            elif current == "Clubs":
                                current = str (page.links[str (idx)].id)
                                page = GenerateClubPage(page.links[str (idx)])
                            else:
                                pass

        page.afficher(screen, font)
        pg.display.flip()

    pg.quit()


if __name__ == "__main__":
    vue()
