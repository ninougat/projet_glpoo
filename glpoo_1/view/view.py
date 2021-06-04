from view_classes import *
from utils import *
from controller.club_class import *
from controller.member_class import *
from controller.licence_class import *


def vue():
    pg.init()
    size = width, height = 320, 240
    screen = pg.display.set_mode(size)
    pg.display.set_caption("Oui.")
    font = pg.font.SysFont(None, 20)
    screen.fill([255, 255, 255])

    util = User("Quentin", "PAJON", "Quentin", "12345", [], 1)

    clubs = []
    c = Club("Club Chef", "Adresse Chef", "Ceci est un club dont vous etes le chef", util.id, id=0)
    clubs.append([c, 1])
    # util.ajoutLicence(0, 3)

    c = Club("Club Bureau", "Adresse Bureau", "Ceci est un club dont vous etes membre du bureau", 1, id=1)
    clubs.append([c, 1])
    # util.ajoutLicence(0, 2)

    c = Club("Club Membre", "Adresse Membre", "Ceci est un club dont vous etes un membre", 1, id=2)
    clubs.append([c, 1])
    # util.ajoutLicence(0, 1)

    for i in range(10):
        c = Club("Club %d" % i, "Adresse club n°%d" % i, "Ceci est le club n°%d" % i, 1, id=3 + i)
        clubs.append([c, 0])

    Initiale = Page("Initiale")
    Initiale.addButton(Button([320, 50], [0, 30], text="Connexion"))
    Initiale.addButton(Button([320, 50], [0, 90], text="Nouveau Membre"))
    Accueil = Page("Accueil")
    Accueil.addButton(Button([320, 50], [0, 30], text="Votre profil"))
    Accueil.addButton(Button([320, 50], [0, 90], text="Liste de vos Clubs"))
    Accueil.addButton(Button([320, 50], [0, 150], text="Rechercher des Clubs"))
    current = "Initiale"
    page = Initiale

    run = 1
    while run:
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                run = 0
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    if current == "Initiale":
                        run = 0
                    elif current =="Accueil":
                        current = "Initiale"
                        page = Initiale
                    else:
                        if current == "Profil":
                            util.name = page.GetZone("Prénom")
                            util.fullname = page.GetZone("Nom")
                            util.user = page.GetZone("Pseudo")
                        current = "Accueil"
                        page = Accueil
                for text in page.zoneTexts:
                    if text.isIn:
                        text.handleKeyDown(event)
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for button in page.buttons:
                        button.mouseInButton(True)
                    for zone in page.zoneTexts:
                        zone.clickIn()
                if current == "Mes clubs" or current == "Clubs":
                    if event.button == 4:
                        page.ScrollUp()
                    if event.button == 5:
                        page.ScrollDown(screen.get_height())
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    for idx, button in enumerate(page.buttons):
                        wasPressed = button.mouseInButton(False)
                        if wasPressed:
                            if current == "Initiale":
                                if button.content == "Connexion":
                                    current = "Connexion"
                                    page = generateConnexion()
                                elif button.content == "Nouveau Membre":
                                    current = "Nouveau Membre"
                                    page = generateNouveauMembre()
                            elif current == "Accueil":
                                if button.content == "Votre profil":
                                    current = "Profil"
                                    page = generateProfile(util)
                                elif button.content == "Liste de vos Clubs":
                                    current = "Mes clubs"
                                    page = generateMesClubs(clubs)
                                elif button.content == "Rechercher des Clubs":
                                    current = "Clubs"
                                    page = generateClubs(clubs)
                            elif current == "Connexion":
                                if button.content == "Valider":

                                    current = "Accueil"
                                    page = Accueil
                            elif current == "Nouveau Membre":
                                if button.content == "Valider":
                                    user = User(page.GetZone("Nom"), page.GetZone("Prenom"), page.GetZone("Pseudo"), page.GetZone("Mot de passe"))
                                    current = "Accueil"
                                    page = Accueil
                            elif current == "Profil":
                                pass
                            elif current == "Mes clubs":
                                current = str(page.links[str(idx)].id)
                                page = generateClubPage(page.links[str(idx)])
                            elif current == "Clubs":
                                current = str(page.links[str(idx)].id)
                                page = generateClubPage(page.links[str(idx)])
                            else:
                                pass

        page.afficher(screen, font)
        pg.display.flip()

    pg.quit()


if __name__ == "__main__":
    vue()
