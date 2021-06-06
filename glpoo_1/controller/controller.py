from controller.club_class import *
from controller.member_class import *
from controller.licence_class import *


def creer_club(licence,club):
    create_club(club,licence)


def cre_club(nom, adresse, description, id_chef):
    club = Club(nom, adresse, description, id_chef)  # on créé une classe club
    add_club(club)  # on l'ajoute à la BDD
    return club


def lister_clubs():
    clubs = []
    clubs_bdd = list_clubs()
    for club_bdd in clubs_bdd:
        clubs.append(Club(club_bdd.nom, club_bdd.adresse, club_bdd.description, club_bdd.chef, club_bdd.id))
    return clubs


def recup_club(util):
    club_ret = []
    if util.id:
        clubs=list_clubs_by_member(util.id)
        util.clubs=[]

        if clubs:
            for club in clubs:
                club_ret.append(Club(club.nom,club.adresse,club.description,club.chef,id=club.id))
                util.clubs.append(club.id)
    return club_ret


def connexion_club(user, club):
    licence_bdd, statut = get_licence_by_club_and_member(user.id, club.id)
    if licence_bdd is None or statut is None:
        return None
    membre = Membre(user.name, user.firstname, user.user, user.password, statut, licence_bdd.id)
    membre.clubs = user.clubs.copy()
    membre.id = user.id
    return membre


def creer_Licence(id_club, name, prix, nb_seance, avantage, util, club):
    licence = Licence(id_club, name, prix, nb_seance, avantage)
    add_licence(licence)
    if id_club not in util.clubs:             # si on vient de créer le club (si il n'est pas dans notre liste de clubs)
        util.inscription(club, licence.id)    # on s'y inscrit
        modify_membre_licence(id_licence=licence.id, id_member=util.id, statut=2)   # on se nomme chef
    return licence


def lister_licences_club(id_club):
    licences = []
    licences_bdd = list_licences_by_club(id_club)
    for licence_bdd in licences_bdd:
        licences.append(Licence(id_club, licence_bdd.name, licence_bdd.prix,licence_bdd.nb_seances, licence_bdd.avantage, id=licence_bdd.id))
    return licences


def connexion(pseudo, password):
    utilisateur = search_member(pseudo)
    compte = None
    if utilisateur and utilisateur.password == password:
        compte = User(utilisateur.name, utilisateur.firstname, utilisateur.user, utilisateur.password, utilisateur.id)
        compte.clubs = list_clubs_by_member(compte.id)
    return compte


def nouveau_membre(nom, prenom, pseudo, mot_de_passe):
    membre = User(nom, prenom, pseudo, mot_de_passe)
    add_member(membre, "user")
    return membre


def connexion_user(pseudo, password):
    user = connexion(pseudo, password)
    if isinstance(user, User):
        return recup_club(user)


