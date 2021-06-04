
from controller.member_class import *
from controller.club_class import *
from controller.licence_class import *
from model.model import *

if __name__ == '__main__':
    add_member(User('Gégé', 'Accordéon', "essai@test.com", "azerty"),0)
    """add_member(User('Albert', 'helicopter', "essai@test.com", "azerty"),0)
    add_member(User('Robert', 'essai', "essai@test.com", "azerty"),0)
    add_member(User('Gilbert', 'Commissaire', "essai@test.com", "azerty"),0)
    add_member(User('Jean', 'sansnom', "essai@test.com", "azerty"),0)
    list_members()
    modify_member(3, name="Jean-Robert", firstname="lampadaire", user="apothicaire")
    list_members()"""

    add_club(Club('club de pétanque du Roussilon',"Languedoc-Roussillon","Pétanque et Languedoc que du bon",1))
    add_club(Club('club de volleyball du Roussilon', "Languedoc-Roussillon", "volley et Languedoc que du bon", 1))
    add_club(Club('club de basket du Roussilon', "Languedoc-Roussillon", "basket et Languedoc que du bon", 1))
    add_club(Club('club de foot du Roussilon', "Languedoc-Roussillon", "foot et Languedoc que du bon", 1))
    add_club(Club('club de tennis du Roussilon', "Languedoc-Roussillon", "tennis et Languedoc que du bon", 1))
    list_clubs()
    del_club(4)
    modify_club(1,"Club des buveurs de vins","Languedoc de Monbazillac",1,"Vive le vin du Languedoc")
    list_clubs()
    add_licence(Licence(1, "licence du pétanqueur débutant", 1, 1, "un verre par séance"))
    add_licence(Licence(2, "licence du pétanqueur intermédiaire", 15, 3, "deux verres par séance"))
    add_licence(Licence(3, "licence du pétanqueur alcoolique", 50, 7, "une bouteille hips par séance. Et viens boire un ptit coup à la maison"))
    list_licences()
    del_licence(1)
    modify_licence(2, name="licence du pétanqueur ultime", prix=100, nb_seances=0, avantage="plus de séance que du vin")
    list_licences()



