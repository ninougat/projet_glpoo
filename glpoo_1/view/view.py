from view_classes import *
from utils import *
from controller.club_class import *
from controller.member_class import *
from controller.licence_class import *


def connexion_user(pseudo,password):
    user=connexion(pseudo,password)
    if isinstance(user, User) :
        recup_club(user)

def vue():
    pg.init()
    size = width, height = 320, 240
    screen = pg.display.set_mode(size)
    pg.display.set_caption("Oui.")
    font = pg.font.SysFont(None, 20)
    screen.fill([255, 255, 255])
    Quentin = User("Quentin", "PAJON", "Quentin1", "12345", 2)
    Quentin2 = User("Quentin", "PAJON", "Quentin2", "12345", 1)
    add_member(Quentin, "user")
    add_member(User("", "", "", "", 1), "admin")
    util = User("a", "a", "a", "a", 1)
    user = None

    add_member(util, "user")
    c = Club("Club Test", "Adresse", "description", 2)
    lic = Licence(c.id, "Licence test", 100, 1, "100 balles et un mars")
    creer_club(lic, c)
    Quentin.inscription(c, lic.id)
    Quentin2.inscription(c, lic.id)

    c = Club("Club 2", "Adresse 2", "description 2", 2)
    lic = Licence(c.id, "Licence 2", 200, 2, "200 balles et 2 mars")
    creer_club(lic, c)


    Initiale = Page("Initiale")
    Initiale.addButton(Button([320, 50], [0, 30], text="Connexion"))
    Initiale.addButton(Button([320, 50], [0, 90], text="Nouveau Membre"))
    Accueil = Page("Accueil")
    Accueil.addButton(Button([320, 50], [0, 30], text="Votre profil"))
    Accueil.addButton(Button([320, 50], [0, 90], text="Liste de vos Clubs"))
    Accueil.addButton(Button([320, 50], [0, 150], text="Rechercher des Clubs"))
    Accueil.addButton(Button([320, 50], [0, 210], text="Ajouter un Club"))
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
                    elif current == "Accueil":
                        current = "Initiale"
                        page = Initiale
                    elif current == "Connexion":
                        current = "Initiale"
                        page = Initiale
                    elif current == "Nouveau Membre":
                        current = "Initiale"
                        page = Initiale
                    else:
                        if current == "Profil":
                            util.modifier_profil(page.GetZone("Prénom"),page.GetZone("Nom"), page.GetZone("Pseudo"), page.GetZone("Mot de passe"))
                        if page.title[:5] == "club ":
                            club = None
                            user = None
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
                                    recup_club(util)
                                    page = generateMesClubs(util.clubs)
                                elif button.content == "Rechercher des Clubs":
                                    current = "Clubs"
                                    page = generateClubs(lister_clubs())  ############################# club non inscrit
                                elif button.content == "Ajouter un Club":
                                    current = "Ajouter un Club"
                                    page = generateNouveauClub()
                            elif current == "Connexion":
                                if button.content == "Valider":
                                    if connexion(page.GetZone("Identifiant"), page.GetZone("mot de passe")):
                                        util = connexion(page.GetZone("Identifiant"), page.GetZone("mot de passe"))
                                        recup_club(util)
                                        current = "Accueil"
                                        page = Accueil
                                    else:
                                        current = "Initiale"
                                        page = Initiale
                            elif current == "Nouveau Membre":
                                if button.content == "Valider":
                                    util = nouveau_membre(page.GetZone("Nom"), page.GetZone("Prenom"), page.GetZone("Pseudo"), page.GetZone("Mot de passe"))
                                    current = "Accueil"
                                    page = Accueil
                            elif current == "Profil":
                                pass
                            elif current == "Mes clubs":
                                current = str(page.links[str(idx)].id)
                                club = page.links[str(idx)]
                                user = connexion_club(util, club)
                                if user:
                                    recup_club(user)
                                    page = generateClubPage(page.links[str(idx)], 1 + user.type)
                                else:
                                    page = generateClubPage(page.links[str(idx)], 0)
                            elif current == "Clubs":
                                current = str(page.links[str(idx)].id)
                                club = page.links[str(idx)]
                                user = connexion_club(util, club)
                                if user:
                                    recup_club(user)
                                    page = generateClubPage(page.links[str(idx)], 1 + user.type)
                                else:
                                    page = generateClubPage(page.links[str(idx)], 0)
                            elif page.title[:5] == "club ":
                                if button.content == "S'inscrire":
                                    util.inscription(club, 0)#####
                                    current = "Accueil"
                                    page = Accueil
                                if button.content == "Se desinscrire" and user:
                                    user.desinscription(club)
                                    current = "Accueil"
                                    page = Accueil
                                if button.content == "Supprimer le club" and user:

                                    current = "Accueil"
                                    page = Accueil
                                elif button.content == "Voir licence":
                                    current = "Mes licences"
                                    page = generateMesLicences(lister_licences_club(club.id))
                                elif button.content == "Afficher tous les membres":
                                    current = "Membres"
                                    page = generateMemberList(club.afficher_membres())
                                elif button.content == "Ajouter licence":
                                    current = "Ajouter licence"
                                    page = generateAjouterlicence(club.id)
                            elif current == "Mes licences":
                                lic = page.links[str(idx)]
                                current = str(page.links[str(idx)].id)
                                print(page.links[str(idx)].avantage)
                                page = generatelicencePage(page.links[str(idx)])
                            elif current == "Membres":
                                current = str(page.links[str(idx)])
                                page = generateMembrePage(page.links[str(idx)])
                            elif page.title[:8] == "licence ":
                                if button.content == "Changer licence":
                                    current = "change licence"
                                    page = generateMesLicences(lister_licences_club(club.id))
                                elif button.content == "Ajouter licence":
                                    current = "Ajouter licence"
                                    page = generateAjouterlicence(club.id)
                                elif button.content == "Supprimer licence":
                                    lic.supprimer_licence()
                                    current = "Accueil"
                                    page = Accueil
                                elif button.content == "Modifier licence":
                                    lic.modifier_licence(prix=page.GetZone("Prix"),nb_seances=page.GetZone("nb_seances"),avantage=page.GetZone("Avantages"))
                            elif page.title[:7] == "Membre ":
                                if button.content == "Désinscrire":
                                    club.supprimer_membre(page.links[str(idx)])
                                    current = "Accueil"
                                    page = Accueil
                                elif button.content == "Retrograder":
                                    current = "Ajouter licence"
                                    page = generateAjouterlicence(club.id)
                                elif button.content == "Supprimer licence":
                                    lic.supprimer_licence()
                                    current = "Accueil"
                                    page = Accueil
                            elif current == "Ajouter un Club":
                                if button.content == "Ajouter licence":
                                    club = cre_club(page.GetZone("Nom"), page.GetZone("Adresse"), page.GetZone("Description"), util.id)
                                    current = "Ajouter licence"
                                    page = generateAjouterlicence(club.id)
                            elif current == "change licences":
                                lic = page.links[str(idx)]
                                current = str(page.links[str(idx)].id)
                                page = generatelicencePage(page.links[str(idx)])
                                user.changer_license(lic)
                            elif current == "Ajouter licence":
                                if button.content == "Valider":
                                    licence = creer_Licence(club.id, page.GetZone("Nom"), int(page.GetZone("Prix")), int(page.GetZone("Nombre de seances")), page.GetZone("Description"), util, club)
                                    print(licence.avantage)
                                    current = "Accueil"
                                    page = Accueil

                            else:
                                pass

        page.afficher(screen, font)
        pg.display.flip()

    pg.quit()


if __name__ == "__main__":
    vue()
