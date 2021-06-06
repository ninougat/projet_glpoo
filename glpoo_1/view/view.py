
from utils import *

from controller.controller import *


def connexion_user(pseudo,password):
    user=connexion(pseudo,password)
    if isinstance(user, User) :
        return recup_club(user)

def vue():
    pg.init()
    size = width, height = 320, 240
    screen = pg.display.set_mode(size)
    pg.display.set_caption("Oui.")
    font = pg.font.SysFont(None, 20)
    screen.fill([255, 255, 255])
    user = None
    list_clubs = []

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
                                    list_clubs = recup_club(util)
                                    page = generateMesClubs(list_clubs)
                                elif button.content == "Rechercher des Clubs":
                                    current = "Clubs"
                                    page = generateClubs(lister_clubs())
                                elif button.content == "Ajouter un Club":
                                    current = "Ajouter un Club"
                                    page = generateNouveauClub()
                            elif current == "Connexion":
                                if button.content == "Valider":
                                    if connexion(page.GetZone("Identifiant"), page.GetZone("mot de passe")):
                                        util = connexion(page.GetZone("Identifiant"), page.GetZone("mot de passe"))
                                        list_clubs = recup_club(util)
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
                                    list_clubs = recup_club(user)
                                    page = generateClubPage(page.links[str(idx)], 1 + user.type)
                                else:
                                    page = generateClubPage(page.links[str(idx)], 0)
                            elif current == "Clubs":
                                current = str(page.links[str(idx)].id)
                                club = page.links[str(idx)]
                                user = connexion_club(util, club)
                                if user:
                                    list_clubs = recup_club(user)
                                    page = generateClubPage(page.links[str(idx)], 1 + user.type)
                                else:
                                    page = generateClubPage(page.links[str(idx)], 0)
                            elif page.title[:5] == "club ":
                                if button.content == "S'inscrire":
                                    current = "Choix licence"
                                    page = generateMesLicences(lister_licences_club(club.id))
                                elif button.content == "Se desinscrire" and user:
                                    user.desinscription(club)
                                    current = "Accueil"
                                    page = Accueil
                                elif button.content == "Supprimer le club" and user:
                                    user.supprimer_Club()
                                    current = "Accueil"
                                    page = Accueil
                                elif button.content == "Voir licence":
                                    current = "Mes licences"
                                    page = generateMesLicences(lister_licences_club(club.id))
                                elif button.content == "Afficher tous les membres":
                                    current = "Membres"
                                    page = generateMemberList(club.afficher_membres(0))
                                elif button.content == "Ajouter licence":
                                    current = "Ajouter licence"
                                    page = generateAjouterlicence(club.id)
                                elif button.content == "Afficher le bureau":
                                    current = "Bureau"
                                    page = generateBureauList(club.afficher_membres(1))
                            elif current == "Mes licences":
                                lic = page.links[str(idx)]
                                current = str(page.links[str(idx)].id)
                                print(page.links[str(idx)].avantage)
                                if user:
                                    page = generatelicencePage(page.links[str(idx)], 1 + user.type)
                                else:
                                    page = generatelicencePage(page.links[str(idx)], 0)
                            elif current == "Membres" or current == "Bureau":
                                current = str(page.links[str(idx)])
                                user_next = page.links[str(idx)]
                                page = generateMembrePage(user,page.links[str(idx)])
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
                                    lic.modifier_licence(prix=page.GetZone("Prix"), nb_seances=page.GetZone("nb_seances"), avantage=page.GetZone("Avantages"))
                            elif page.title[:7] == "Membre ":
                                if button.content == "Désinscrire":
                                    user.desinscrire_membre(user_next["membre"], club)
                                elif button.content == "Retrograder":
                                    user.retrograder(user_next["membre"], club)
                                elif button.content == "Promouvoir":
                                    user.promouvoir(user_next["membre"], club)
                                current = "Accueil"
                                page = Accueil
                            elif current == "Ajouter un Club":
                                if button.content == "Ajouter licence":
                                    club = cre_club(page.GetZone("Nom"), page.GetZone("Adresse"), page.GetZone("Description"), util.id)
                                    current = "Ajouter licence"
                                    page = generateAjouterlicence(club.id)
                            elif current == "change licence":
                                lic = page.links[str(idx)].id
                                user.changer_license(lic)
                                current = "Mes clubs"
                                list_clubs = recup_club(util)
                                page = generateMesClubs(list_clubs)
                            elif current == "Choix licence":
                                print("OK")
                                print(page.links[str(idx)])
                                print("KO")
                                lic = page.links[str(idx)].id
                                util.inscription(club, lic)
                                current = "Accueil"
                                page = Accueil
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
