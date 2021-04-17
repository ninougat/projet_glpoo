from view_classes import *
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
    c = Club ()
    c.id = 0
    c.nom = "Club Chef"
    c.description = "Ceci est un club dont vous etes le chef"
    clubs.append(c)
    # util.ajoutLicence(0, 3)

    c = Club ()
    c.id = 1
    c.nom = "Club Bureau"
    c.description = "Ceci est un club dont vous etes le membre du bureau"
    clubs.append(c)
    # util.ajoutLicence(0, 2)

    c = Club()
    c.id = 1
    c.nom = "Club Membre"
    c.description = "Ceci est un club dont vous etes un membre"
    clubs.append(c)
    # util.ajoutLicence(0, 1)

    current = 0

    Pages = [[], [], [], []]

    Pages[0].append(Button([320, 50], [0, 20], background=[128, 128, 255], backgroundWhenPressed=[255, 128, 0], text="Votre profil"))
    Pages[0].append(Button([320, 50], [0, 80], background=[128, 128, 255], backgroundWhenPressed=[255, 128, 0], text="Liste de vos Clubs"))
    Pages[0].append(Button([320, 50], [0, 140], background=[128, 128, 255], backgroundWhenPressed=[255, 128, 0], text="Rechercher des Clubs"))

    Pages[1].append(ZoneText (title="Prénom", text=util.name, textSize=[320, 50], textPos=[0, 20]))
    Pages[1].append(ZoneText (title="Nom", text=util.fullname, textSize=[320, 50], textPos=[0, 80]))
    Pages[1].append(ZoneText (title="Pseudo", text=util.user, textSize=[320, 50], textPos=[0, 140]))

    for (idx, club) in enumerate(clubs):
        Pages[2].append(
            Button([320, 50], [0, 20 + 60 * idx], background=[128, 128, 255], backgroundWhenPressed=[255, 128, 0], text=club.nom))

    for i in range(10):
        Pages[3].append(
            Button([320, 50], [0, 20 + i * 60], background=[128, 128, 255], backgroundWhenPressed=[223, 109, 20], text="Club %d" % i))

    end = 0
    while not end:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                end = 1
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    if current == 0:
                        end = 1
                    else:
                        current = 0
                for element in Pages[current]:
                    if type (element) is ZoneText and element.isIn:
                        element.handleKeyDown (event)
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for button in Pages[current]:
                        if type (button) is Button:
                            button.mouseInButton(True)
                        elif type (button) is ZoneText:
                            button.clickIn ()
                if current == 2 or current == 3:
                    if event.button == 4:
                        for button in Pages[current]:
                            button.pos[1] += 10
                    if event.button == 5:
                        for button in Pages[current]:
                            button.pos[1] -= 10
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    for nb, button in enumerate(Pages[current]):
                        if type (button) is Button:
                            wasPressed = button.mouseInButton(False)
                            if wasPressed:
                                if current == 0:
                                    if nb == 0:
                                        current = 1
                                    elif nb == 1:
                                        current = 2
                                    elif nb == 2:
                                        current = 3

        screen.fill([255, 255, 255])
        for button in Pages[current]:
            button.afficher(screen, font)
        pg.display.flip()

    pg.quit()


if __name__ == "__main__":
    vue()
