from model.model import *

if __name__ == '__main__':
    add_member('Gégé', 'Accordéon', "essai@test.com", "azerty", "0")
    add_member('Albert', 'helicopter', "essai@test.com", "azerty", "0")
    add_member('Robert', 'essai', "essai@test.com", "azerty", "0")
    add_member('Gilbert', 'Commissaire', "essai@test.com", "azerty", "0")
    add_member('Jean', '', "essai@test.com", "azerty", "1")
    list_members()
    modify_member(3, name="Jean-Robert", fullname="lampadaire", user="apothicaire")
    list_members()

    add_club('club de pétanque du Roussilon',"Languedoc-Roussillon","Pétanque et Languedoc que du bon",1)
    add_club('club de volleyball du Roussilon', "Languedoc-Roussillon", "volley et Languedoc que du bon", 2)
    add_club('club de basket du Roussilon', "Languedoc-Roussillon", "basket et Languedoc que du bon", 2)
    add_club('club de foot du Roussilon', "Languedoc-Roussillon", "foot et Languedoc que du bon", 2)
    add_club('club de tennis du Roussilon', "Languedoc-Roussillon", "tennis et Languedoc que du bon", 2)
    list_clubs()
    del_club("")
    modify_club(1,"Club des buveurs de vins","Languedoc de Monbazillac",1,"Vive le vin du Languedoc")
    list_clubs()
    add_licence(1,"licence du pétanqueur débutant",1,1,"un verre par séance")
    add_licence(1, "licence du pétanqueur intermédiaire", 15, 3, "deux verres par séance")
    add_licence(1, "licence du pétanqueur alcoolique", 50, 7, "une bouteille hips par séance. Et viens boire un ptit coup à la maison")
    list_licences()
    del_licence(1)
    modify_licence(2,name="licence du pétanqueur ultime",prix=100,nb_seances=0, avantage="plus de séance que du vin")
    list_licences()




