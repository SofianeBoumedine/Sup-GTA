######################################################
############ Sup'GTA. Fichier principal. ############
# Celui ci contient tout le gameplay, le menu etc...#
#####################################################

from pygame.locals import *
import pygame, sys

pygame.init()

# Variable contenant les codes couleurs
color = (205, 205, 180)
color_1 = (47, 79, 79)
WHITE = (255, 255, 255)
rouge = (255, 0, 0)
vert = (0, 255, 0)
BLACK = (0, 0, 0)

# Variable contenant les coordonnées des différents éléments du jeu
Xperso = 1
Yperso = 275
Xcar = 70
Ycar = 275
Xcar2 = 250
Ycar2 = 275
Xcar3 = 750
Ycar3 = 550
Xcar4 = 180
Ycar4 = 550
XpointA = 70
YpointA = 275
XpointB = 750
YpointB = 560
# Vitesse de déplacement(de 5px en 5px)
vitesse = 5

# Chargement du son
pygame.mixer.music.load("sound/son1.wav")
son = pygame.mixer.Sound("sound/son1.wav")
pygame.mixer.fadeout(300)
son.play()

# Chargement des images de notre menu
menu_principal = pygame.image.load("img/Menu1.png")
menu_Jouer = pygame.image.load("img/Menu1-2.png")
menu_Commande = pygame.image.load("img/Menu2.png")
commande = pygame.image.load("img/MenuCommande.png")
menu_Quitter = pygame.image.load("img/menu3.png")
menu_credit = pygame.image.load("img/Menu5.png")
credit = pygame.image.load("img/MenuCredit.png")
menu_Option = pygame.image.load("img/Menu4.png")
option = pygame.image.load("img/MenuOption.png")
topbar = pygame.image.load("img/bardejeux.png")

# Bloc qui contient notre police, notre fenetre ainsi que le titre de notre fenêtre
# De plus on a configuré le temps de répétition de l'action lors d'un appui sur une touche
font = pygame.font.Font(None, 30)
ecran = pygame.display.set_mode((1024, 768), FULLSCREEN)
pygame.display.set_caption('Sup\'GTA')
pygame.key.set_repeat(1, 80)

# Chargement des images de notre jeu
pb1 = pygame.image.load("imgperso/pb1.png")
pb2 = pygame.image.load("imgperso/pb2.png")
pb3 = pygame.image.load("imgperso/pb3.png")
ph1 = pygame.image.load("imgperso/ph1.png")
pg1 = pygame.image.load("imgperso/pg1.png")
pd1 = pygame.image.load("imgperso/pd1.png")
pg2 = pygame.image.load("imgperso/pb2.png")
ph2 = pygame.image.load("imgperso/ph2.png")
pd2 = pygame.image.load("imgperso/pd2.png")
pg2 = pygame.image.load("imgperso/pg2.png")
pd3 = pygame.image.load("imgperso/pd3.png")
pg3 = pygame.image.load("imgperso/pg3.png")
ph3 = pygame.image.load("imgperso/ph3.png")

pdc1 = pygame.image.load("imgperso/pdc1.png")
pgc1 = pygame.image.load("imgperso/pgc1.png")
phc1 = pygame.image.load("imgperso/phc1.png")
pbc1 = pygame.image.load("imgperso/pbc1.png")
pda1 = pygame.image.load("imgperso/pda1.png")
pga1 = pygame.image.load("imgperso/pga1.png")
pha1 = pygame.image.load("imgperso/pha1.png")
pba1 = pygame.image.load("imgperso/pba1.png")

# Sprite des voitures
carh1 = pygame.image.load("imgcar/carh1.png")
carb1 = pygame.image.load("imgcar/carb1.png")
card1 = pygame.image.load("imgcar/card1.png")
carg1 = pygame.image.load("imgcar/carg1.png")
carh2 = pygame.image.load("imgcar/carh2.png")
carb2 = pygame.image.load("imgcar/carb2.png")
card2 = pygame.image.load("imgcar/card2.png")
carg2 = pygame.image.load("imgcar/carg2.png")
carh3 = pygame.image.load("imgcar/carh3.png")
carb3 = pygame.image.load("imgcar/carb3.png")
card3 = pygame.image.load("imgcar/card3.png")
carg3 = pygame.image.load("imgcar/carg3.png")
carh4 = pygame.image.load("imgcar/carh4.png")
carb4 = pygame.image.load("imgcar/carb4.png")
card4 = pygame.image.load("imgcar/card4.png")
carg4 = pygame.image.load("imgcar/carg4.png")

# Sprite des pointsA et pointsB
pointA = pygame.image.load("imgperso/pointA.png")
pointB = pygame.image.load("imgperso/pointB.png")

# Sprite des figurants
bolossvoiture = pygame.image.load("sprite/pd1.png")
passant1 = pygame.image.load("imgperso/p24.png")
passant2 = pygame.image.load("imgperso/p23.png")
passant3 = pygame.image.load("imgperso/p1.png")
passant4 = pygame.image.load("imgperso/p13.png")

# Sprite du sang, de la dague, et d'une image vide pour faire disparaitre une image prise par le personnage
blood = pygame.image.load("imgperso/blood.png")
dague = pygame.image.load("imgperso/dague.png")
vide = pygame.image.load("imgperso/vide.png")

# Chargement dans des variables des mapss
map = pygame.image.load("map.png")
map2 = pygame.image.load("map2.png")
map3 = pygame.image.load("map3.png")
map4 = pygame.image.load("map4.png")

# Variable contenant les textes utilisés lors de différents événements
textewelcome = font.render("Bienvenue dans Sup GTA !", 1, (255, 255, 255))
texte = font.render("***Future Mission...***", 1, (255, 255, 255))
textevoiturecasser = font.render("***Vous avez cassé la voiture.***", 1, (255, 255, 255))
textevoituredamage = font.render("***Vous avez abîmé la voiture, la vitesse est donc diminuée.***", 1, (255, 255, 255))
textemissionvoiture = font.render("***Déplacez vous du point A au Point B en voiture.***", 1, (255, 255, 255))
textemissionarme = font.render("***Trouvez une dague et ramassez la...***", 1, (255, 255, 255))
textemissiontuer = font.render("***Tuez l'un des piétons.***", 1, (255, 255, 255))
textemissionreussie = font.render("***Vous avez réussi la mission !!! ***", 1, (255, 255, 255))
textemissioncomplete0 = font.render("***Missions effectuées 0/3", 1, (255, 255, 255))
textemissioncomplete1 = font.render("***Missions effectuées 1/3", 1, (255, 255, 255))
textemissioncomplete2 = font.render("***Missions effectuées 2/3", 1, (255, 255, 255))
textemissioncomplete3 = font.render("***Missions effectuées 3/3", 1, (255, 255, 255))


# Ensemble de variable qu'on va utiliser pour stocker des éléments variables
totalmissioncompleted = textemissioncomplete0

# Variable contenant l'image actuelle des personnages
lepassant1 = passant1
lepassant2 = passant2
lepassant3 = passant3
lepassant4 = passant4
personnage = pd1
# Sprite de la dague
dagueobjet = dague

# Sprite contenant l'image actuel des images
car = card1
car2 = card2
car3 = card3
car4 = card4
i = 0
j = 0
# La variable vaut 0 si le joueur est à pied et 1 si il est en voiture
lvl = 0
# Map afficher
mapnow = 1
# Ecran Afficher
vue = 1
# Texte afficher à l'écran
contenu = texte
# degat actuel de la voiture
degat = 0
# Nombre de kill
kill = 0
# Variable dans laquelle on stoque la direction à l'instant T du joueur
pos = 0
arme = 0
# Degâts actuel des passants
degatpassant1 = 0
degatpassant2 = 0
degatpassant3 = 0
degatpassant4 = 0
# Variable permettant de savoir si une mission est faite ou pas
missiontuer = 0
missionarme = 0
missionvoiture = 0
# Liste essentielle à l'effet de mouvement de notre personnage
liste1 = [ph1, ph2, ph3]
liste2 = [pb1, pb2, pb3]
liste3 = [pg1, pg2, pg3]
liste4 = [pd1, pd2, pd3]

# BOUCLE PRINCIPALE qui actualise notre fenetre
inProgress = True
while inProgress:
    for event in pygame.event.get():
        pygame.display.update()

        if event.type == MOUSEBUTTONDOWN:
            x, y = event.pos
        if vue == 0:
            ############################################################################
            ############################################################################
            ##### ALGORITHME DU GAMEPLAY (MOUVEMENT, COLISIONS, ACHIEVMENT, ETC...######
            ############################################################################
            ############################################################################
            ecran.fill(WHITE)
            # Affichage des éléments des images
            ecran.blit(topbar, (0, 0))
            ecran.blit(contenu, (20, 10))
            nombredekill = font.render("***Kills :" + str(kill), 1, (255, 255, 255))
            ecran.blit(nombredekill, (600, 40))
            ecran.blit(totalmissioncompleted, (600, 10))
            # Si la map 1 est affichée les conditions dans la boucle sont appliquées
            if mapnow == 1:
                if missiontuer == 0:
                    contenu = textemissiontuer
                lvl = 0

                j = 0
                ecran.blit(map, (0, 75))
                Xpassant1 = 250
                Ypassant1 = 309
                Xpassant2 = 775
                Ypassant2 = 375
                Xpassant3 = 638
                Ypassant3 = 620
                Xpassant4 = 208
                Ypassant4 = 745
                ecran.blit(lepassant1, (Xpassant1, Ypassant1))
                ecran.blit(lepassant2, (Xpassant2, Ypassant2))
                ecran.blit(lepassant3, (Xpassant3, Ypassant3))
                ecran.blit(lepassant4, (Xpassant4, Ypassant4))
            if mapnow == 2:
                lvl = 0
                j = 0
                ecran.blit(map2, (0, 75))
                Xpassant1 = 345
                Ypassant1 = 200
                Xpassant2 = 450
                Ypassant2 = 680
                Xpassant3 = 178
                Ypassant3 = 700
                Xpassant4 = 208
                Ypassant4 = 745
                ecran.blit(lepassant1, (Xpassant1, Ypassant1))
                ecran.blit(lepassant2, (Xpassant2, Ypassant2))
                ecran.blit(lepassant3, (Xpassant3, Ypassant3))
                ecran.blit(lepassant4, (Xpassant4, Ypassant4))
                ecran.blit(dagueobjet, (700, 237))
            if mapnow == 3:
                ecran.blit(map3, (0, 75))
                ecran.blit(car, (Xcar, Ycar))
                ecran.blit(car2, (Xcar2, Ycar2))
                ecran.blit(car3, (Xcar3, Ycar3))
                ecran.blit(car4, (Xcar4, Ycar4))
                Xpassant1 = 345
                Ypassant1 = 200
                Xpassant2 = 450
                Ypassant2 = 680
                Xpassant3 = 178
                Ypassant3 = 700
                Xpassant4 = 208
                Ypassant4 = 745
                ecran.blit(lepassant1, (Xpassant1, Ypassant1))
                ecran.blit(lepassant2, (Xpassant2, Ypassant2))
                ecran.blit(lepassant3, (Xpassant3, Ypassant3))
                ecran.blit(lepassant4, (Xpassant4, Ypassant4))
            if mapnow == 4:
                ecran.blit(map4, (0, 75))
                ecran.blit(car, (Xcar, Ycar))
                ecran.blit(car2, (Xcar2, Ycar2))
                ecran.blit(car3, (Xcar3, Ycar3))
                ecran.blit(car4, (Xcar4, Ycar4))
                Xpassant1 = 345
                Ypassant1 = 200
                Xpassant2 = 450
                Ypassant2 = 680
                Xpassant3 = 178
                Ypassant3 = 700
                Xpassant4 = 208
                Ypassant4 = 745
                ecran.blit(lepassant1, (Xpassant1, Ypassant1))
                ecran.blit(lepassant2, (Xpassant2, Ypassant2))
                ecran.blit(lepassant3, (Xpassant3, Ypassant3))
                ecran.blit(lepassant4, (Xpassant4, Ypassant4))
            ecran.blit(personnage, (Xperso, Yperso))
            if lvl == 1 and missionvoiture == 0:
                ecran.blit(pointA, (XpointA, YpointA))
                ecran.blit(pointB, (XpointB, YpointB))
            if lvl == 1 and (YpointB + 23 >= Yperso >= YpointB - 23.) and (XpointB + 13 >= Xperso >= XpointB-13) and missionvoiture == 0:
                print("okok")
                missionvoiture = 1
                contenu = textemissionreussie
            if degat >= 5:
                vitesse = 6
                contenu = textevoituredamage
            if degat >= 10:
                j = 0
                vitesse = 5
                lvl = 0
                personnage = pb1
                car = card1
                contenu = textevoiturecasser
                degat = 0
            if lvl == 0 and (mapnow == 3 or mapnow == 4):
                contenu = texte
            if degatpassant1 == 4:
                degatpassant1 = 0
                kill += 1
                print("ONE KILL")
                if missiontuer == 0:
                    contenu = textemissionreussie
                missiontuer = 1
                lepassant1 = blood
            if degatpassant2 == 4:
                degatpassant2 = 0
                kill += 1
                print("ONE KILL")
                if missiontuer == 0:
                    contenu = textemissionreussie
                missiontuer = 1
                lepassant2 = blood
            if degatpassant3 == 4:
                degatpassant3 = 0
                kill += 1
                print("ONE KILL")
                if missiontuer == 0:
                    contenu = textemissionreussie
                missiontuer = 1
                lepassant3 = blood
            if degatpassant4 == 4:
                degatpassant4 = 0
                kill += 1
                print("ONE KILL")
                if missiontuer == 0:
                    contenu = textemissionreussie
                missiontuer = 1
                lepassant4 = blood
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                #Variable qui contient la direction actuel de notre personnage
                pos = 0
                i += 1
                Xperso += vitesse
                personnage = liste4[i % 3]
                # Si la map est la map 3 ou la map 4 les conditions suivantes seront appliquer :
                if mapnow == 3 or mapnow == 4:
                    # Colision des voitures
                    if (Ycar + 23 >= Yperso and Ycar - 23 <= Yperso) and (Xcar + 13 >= Xperso and Xcar - 13 <= Xperso):
                        degat = 0
                        if missionvoiture == 0:
                            contenu = textemissionvoiture
                        lvl = 1
                        j = 1
                        personnage = card1
                    if (Ycar2 + 23 >= Yperso and Ycar2 - 23 <= Yperso) and (
                                        Xcar2 + 13 >= Xperso and Xcar2 - 13 <= Xperso) and j == 0:
                        degat = 0
                        lvl = 2
                        j = 1
                        personnage = card2
                    if (Ycar3 + 23 >= Yperso and Ycar3 - 23 <= Yperso) and (
                                        Xcar3 + 13 >= Xperso and Xcar3 - 13 <= Xperso) and j == 0:
                        degat = 0
                        lvl = 3
                        j = 1
                        personnage = card3
                    if (Ycar4 + 23 >= Yperso and Ycar4 - 23 <= Yperso) and (
                                        Xcar4 + 13 >= Xperso and Xcar4 - 13 <= Xperso) and j == 0:
                        degat = 0
                        lvl = 4
                        j = 1
                        personnage = card3
                # Cette boucle permet de faire apparaitre un passager lorsque notre joueur prend une voiture
                if lvl == 1:
                    personnage = card1
                    car = bolossvoiture
                    vitesse = 10
                if lvl == 2:
                    personnage = card2
                    car2 = bolossvoiture
                    vitesse = 10
                if lvl == 3:
                    personnage = card3
                    car3 = bolossvoiture
                    vitesse = 10
                if lvl == 4:
                    personnage = card4
                    car4 = bolossvoiture
                    vitesse = 10
                if Xperso > 980:
                    Xperso -= vitesse
                if mapnow == 1:
                    if Xperso > 811 and Xperso < 820 and Yperso > 380 and Yperso < 690:
                        Xperso -= vitesse
                    if Xperso > 970 and Yperso > 300 and Yperso < 380:
                        # Changement de map donc rénitialisation de nos variable de bases permettant la bonne mise en place de la map
                        mapnow = 2
                        Xperso = 1
                        Yperso = 273
                        contenu = textemissionarme
                        lepassant1 = passant1
                        lepassant2 = passant2
                        lepassant3 = passant3
                        lepassant4 = passant4
                        degatpassant1 = 0
                        degatpassant2 = 0
                        degatpassant3 = 0
                        degatpassant4 = 0
                if mapnow == 2:
                    if Xperso > 70 and Yperso > 225 and Yperso < 300:
                        Xperso -= vitesse
                    if Xperso > 160 and Yperso > 230 and Yperso < 515:
                        Xperso -= vitesse
                    if Xperso > 430 and Xperso < 535 and Yperso > 600:
                        Xperso -= vitesse
                    if Xperso >= 700 and (Yperso <= 237 or Yperso >= 237) and missionarme == 0:
                        missionarme = 1
                        arme = 1
                        contenu = textemissionreussie
                        dagueobjet = vide
                    if Xperso > 960 and (Yperso <= 237 or Yperso >= 237):
                        mapnow = 3
                        Xperso = 1
                        Yperso = 273
                        lepassant1 = passant1
                        lepassant2 = passant2
                        lepassant3 = passant3
                        lepassant4 = passant4
                        degatpassant1 = 0
                        degatpassant2 = 0
                        degatpassant3 = 0
                        degatpassant4 = 0
                if mapnow == 3:
                    if Xperso > 220 and Xperso < 290 and Yperso > 295 and Yperso < 726:
                        Xperso -= vitesse
                        if j == 1:
                            degat += 1
                    if Xperso > 220 and Xperso < 780 and Yperso > 70 and Yperso < 160:
                        Xperso -= vitesse
                        if j == 1:
                            degat += 1
                    if Xperso > 490 and Xperso < 770 and Yperso > 290 and Yperso < 523:
                        Xperso -= vitesse
                        if j == 1:
                            degat += 1
                    if Xperso > 490 and Xperso < 770 and Yperso > 650 and Yperso < 728:
                        Xperso -= vitesse
                        if j == 1:
                            degat += 1
                    if Xperso > 840 and Xperso < 1000 and Yperso > 290 and Yperso < 528:
                        Xperso -= vitesse
                        if j == 1:
                            degat += 1
                    if Xperso > 840 and Xperso < 1000 and Yperso > 640 and Yperso < 728:
                        Xperso -= vitesse
                        if j == 1:
                            degat += 1
                    if Xperso > 840 and Xperso < 1000 and Yperso > 70 and Yperso < 160:
                        Xperso -= vitesse
                        if j == 1:
                            degat += 1
                if mapnow == 4:
                    if Xperso > 170 and Yperso < 190:
                        Xperso -= vitesse
                        if j == 1:
                            degat += 1
                    if Xperso > 170 and Yperso > 299 and Yperso < 538:
                        Xperso -= vitesse
                        if j == 1:
                            degat += 1
                    if Xperso > 170 and Yperso > 654:
                        Xperso -= vitesse
                        if j == 1:
                            degat += 1
            if event.key == K_LEFT:
                pos = 1
                i += 1
                Xperso = Xperso - vitesse
                if lvl == 1:
                    personnage = carg1
                elif lvl == 2:
                    personnage = carg2
                elif lvl == 3:
                    personnage = carg3
                elif lvl == 4:
                    personnage = carg4
                else:
                    personnage = liste3[i % 3]
                if Xperso < 0:
                    Xperso += vitesse
                if mapnow == 1:
                    if Xperso < 170 and Yperso > 280 and Yperso < 1024:
                        Xperso += vitesse
                        print("1")
                    if Xperso < 600 and Yperso < 695 and Yperso > 380:
                        Xperso += vitesse
                    if Xperso > 900 and Xperso < 930 and Yperso > 380 and Yperso < 670:
                        Xperso += vitesse
                if mapnow == 2:
                    if Xperso < 20:
                        Xperso = 900
                        Yperso = 275
                        mapnow = 1
                        lepassant1 = passant1
                        lepassant2 = passant2
                        lepassant3 = passant3
                        lepassant4 = passant4
                        degatpassant1 = 0
                        degatpassant2 = 0
                        degatpassant3 = 0
                        degatpassant4 = 0
                    if Xperso < 100 and Yperso > 350 and Yperso < 604:
                        Xperso = Xperso + vitesse
                    if Xperso > 430 and Xperso < 535 and Yperso > 600:
                        Xperso = Xperso + vitesse
                if mapnow == 3:
                    if Xperso < 20:
                        lepassant1 = passant1
                        lepassant2 = passant2
                        lepassant3 = passant3
                        lepassant4 = passant4
                        degatpassant1 = 0
                        degatpassant2 = 0
                        degatpassant3 = 0
                        degatpassant4 = 0
                        Xperso = 960
                        Yperso = 225
                        mapnow = 2
                    if Xperso < 140 and Yperso > 295 and Yperso < 726:
                        Xperso += vitesse
                        print("1")
                        if j == 1:
                            degat += 1
                    if Xperso < 140 and Yperso > 70 and Yperso < 160:
                        Xperso += vitesse
                        print("2")
                        if j == 1:
                            degat += 1
                    if Xperso < 770 and Yperso > 296 and Yperso < 510:
                        Xperso += vitesse
                        print("4")
                        if j == 1:
                            degat += 1
                    if Xperso < 770 and Yperso > 70 and Yperso < 160:
                        Xperso += vitesse
                        print("6")
                        if j == 1:
                            degat += 1
                if mapnow == 4:
                    if Xperso < 20:
                        lepassant1 = passant1
                        lepassant2 = passant2
                        lepassant3 = passant3
                        lepassant4 = passant4
                        degatpassant1 = 0
                        degatpassant2 = 0
                        degatpassant3 = 0
                        degatpassant4 = 0
                        Xperso = 900
                        Yperso = 275
                        mapnow = 2
                    if Xperso < 110 and Yperso < 188:
                        Xperso += vitesse
                        if j == 1:
                            degat += 1
                    if Xperso < 110 and Yperso > 300:
                        Xperso += vitesse
                        if j == 1:
                            degat += 1
                    if Xperso < 900 and Yperso < 189:
                        Xperso += vitesse
                        if j == 1:
                            degat += 1
                    if Xperso < 900 and Yperso > 300 and Yperso < 540:
                        Xperso += vitesse
                        if j == 1:
                            degat += 1
                    if Xperso < 900 and Yperso > 650:
                        Xperso += vitesse
                        if j == 1:
                            degat += 1
            if event.key == K_UP:
                pos = 2
                i += 1
                Yperso -= vitesse
                if lvl == 1:
                    personnage = carh1
                elif lvl == 2:
                    personnage = carh2
                elif lvl == 3:
                    personnage = carh3
                elif lvl == 4:
                    personnage = carh4
                else:
                    personnage = liste1[i % 3]
                if Yperso < 75:
                    Yperso += vitesse
                if mapnow == 1:
                    if Yperso < 210:
                        Yperso += vitesse
                    if Yperso < 650 and Yperso > 270 and 239 < Xperso < 590:
                        Yperso += vitesse
                    if Xperso > 820 and Xperso < 920 and Yperso < 687:
                        Yperso += vitesse
                if mapnow == 2:
                    if Yperso < 200:
                        Yperso += vitesse
                    if Xperso > 180 and Xperso < 435 and Yperso > 515 and Yperso < 606:
                        Yperso += vitesse
                    if Xperso > 530 and Xperso < 1000 and Yperso > 515 and Yperso < 606:
                        Yperso += vitesse
                if mapnow == 3:
                    if Xperso > 0 and Xperso < 160 and Yperso < 178:
                        Yperso += vitesse
                        if j == 1:
                            degat += 1
                    if Xperso > 260 and Xperso < 785 and Yperso < 178:
                        Yperso += vitesse
                        if j == 1:
                            degat += 1
                    if Xperso > 880 and Xperso < 1000 and Yperso < 178:
                        Yperso += vitesse
                        if j == 1:
                            degat += 1
                    if Xperso > 525 and Xperso < 780 and Yperso < 530 and Yperso > 400:
                        Yperso += vitesse
                        if j == 1:
                            degat += 1
                    if Xperso > 880 and Xperso < 1000 and Yperso < 530 and Yperso > 400:
                        Yperso += vitesse
                        if j == 1:
                            degat += 1
                if mapnow == 4:
                    if Xperso < 110 and Yperso < 189:
                        Yperso += vitesse
                        if j == 1:
                            degat += 1
                    if Xperso > 210 and Xperso < 910 and Yperso < 189:
                        Yperso += vitesse
                        if j == 1:
                            degat += 1
                    if Xperso > 210 and Xperso < 910 and Yperso > 303 and Yperso < 540:
                        Yperso += vitesse
                        if j == 1:
                            degat += 1
            if event.key == K_DOWN:
                pos = 3
                i += 1
                Yperso += vitesse
                if lvl == 1:
                    personnage = carb1
                elif lvl == 2:
                    personnage = carb2
                elif lvl == 3:
                    personnage = carb3
                elif lvl == 4:
                    personnage = carb4
                else:
                    personnage = liste2[i % 3]
                if Yperso > 725:
                    Yperso -= vitesse
                if mapnow == 1:
                    if Yperso > 319 and 0 < Xperso < 170:
                        Yperso -= vitesse
                    if Yperso > 665 and 240 < Xperso < 640:
                        Yperso -= vitesse
                    if Xperso > 340 and Xperso < 625 and Yperso > 235 and Yperso < 240:
                        Yperso -= vitesse
                    if Xperso > 630 and Xperso < 766 and Yperso > 275 and Yperso < 280:
                        Yperso -= vitesse
                    if Xperso > 760 and Xperso < 900 and Yperso > 345 and Yperso < 350:
                        Yperso -= vitesse
                if mapnow == 2:
                    if Xperso > 70 and Xperso < 980 and Yperso > 200 and Yperso < 235:
                        Yperso -= vitesse
                    if Xperso > 0 and Xperso < 110 and Yperso > 310 and Yperso < 340:
                        Yperso -= vitesse
                    if Xperso > 104 and Xperso < 432 and Yperso > 520 and Yperso < 580:
                        Yperso -= vitesse
                    if Xperso > 534 and Xperso < 885 and Yperso > 520 and Yperso < 580:
                        Yperso -= vitesse
                    if Xperso > 885 and Yperso > 560 and Yperso < 610:
                        Yperso -= vitesse
                    if Yperso > 705:
                        lepassant1 = passant1
                        lepassant2 = passant2
                        lepassant3 = passant3
                        lepassant4 = passant4
                        mapnow = 4
                        Xperso = 1
                        Yperso = 273
                        degatpassant1 = 0
                        degatpassant2 = 0
                        degatpassant3 = 0
                        degatpassant4 = 0
                if mapnow == 3:
                    if Xperso > 0 and Xperso < 160 and Yperso > 260:
                        Yperso -= vitesse
                        if j == 1:
                            degat += 1
                    if Xperso > 260 and Xperso < 415 and Yperso > 260:
                        Yperso -= vitesse
                        if j == 1:
                            degat += 1
                    if Xperso > 530 and Xperso < 780 and Yperso > 260 and Yperso < 520:
                        Yperso -= vitesse
                        if j == 1:
                            degat += 1
                    if Xperso > 530 and Xperso < 780 and Yperso > 640:
                        Yperso -= vitesse
                        if j == 1:
                            degat += 1
                    if Xperso > 880 and Xperso < 1000 and Yperso > 260 and Yperso < 520:
                        Yperso -= vitesse
                        if j == 1:
                            degat += 1
                    if Xperso > 880 and Xperso < 1000 and Yperso > 640:
                        Yperso -= vitesse
                        if j == 1:
                            degat += 1
                if mapnow == 4:
                    if Xperso > 0 and Xperso < 110 and Yperso > 270:
                        Yperso -= vitesse
                        if j == 1:
                            degat += 1
                    if Xperso > 210 and Xperso < 910 and Yperso > 270:
                        Yperso -= vitesse
                        if j == 1:
                            degat += 1
                    if Xperso > 210 and Xperso < 910 and Yperso > 650:
                        Yperso -= vitesse
                        if j == 1:
                            degat += 1

            if event.key == K_s:
                j = 0
                if lvl == 1:
                    vitesse = 3
                    lvl = 0
                    personnage = pb1
                    car = card1
                    Xcar = Xperso
                    Ycar = Yperso
                if lvl == 2:
                    vitesse = 3
                    lvl = 0
                    personnage = pb1
                    car2 = card2
                    Xcar2 = Xperso
                    Ycar2 = Yperso
                if lvl == 3:
                    vitesse = 3
                    lvl = 0
                    personnage = pb1
                    car3 = card3
                    Xcar3 = Xperso
                    Ycar3 = Yperso
                if lvl == 4:
                    vitesse = 3
                    lvl = 0
                    personnage = pb1
                    car4 = card4
                    Xcar4 = Xperso
                    Ycar4 = Yperso

        if event.type == KEYDOWN:
            if event.key == K_d:
                if (Ypassant1 + 23 >= Yperso and Ypassant1 - 23 <= Yperso) and (
                                    Xpassant1 + 13 >= Xperso and Xpassant1 - 13 <= Xperso):
                    degatpassant1 += 1
                    print(degatpassant1)
                if (Ypassant2 + 23 >= Yperso and Ypassant2 - 23 <= Yperso) and (
                                    Xpassant2 + 13 >= Xperso and Xpassant2 - 13 <= Xperso):
                    degatpassant2 += 1
                    print(degatpassant2)
                if (Ypassant3 + 23 >= Yperso and Ypassant3 - 23 <= Yperso) and (
                                    Xpassant3 + 13 >= Xperso and Xpassant3 - 13 <= Xperso):
                    degatpassant3 += 1
                    print(degatpassant3)
                if (Ypassant4 + 23 >= Yperso and Ypassant4 - 23 <= Yperso) and (
                                    Xpassant4 + 13 >= Xperso and Xpassant4 - 13 <= Xperso):
                    degatpassant4 += 1
                    print(degatpassant4)
                if pos == 0:
                    if arme == 1:
                        personnage = pda1
                    else:
                        personnage = pdc1
                if pos == 1:
                    if arme == 1:
                        personnage = pga1
                    else:
                        personnage = pgc1
                if pos == 2:
                    if arme == 1:
                        personnage = pha1
                    else:
                        personnage = phc1
                if pos == 3:
                    if arme == 1:
                        personnage = pba1
                    else:
                        personnage = pbc1
        if event.type == KEYUP:
            if event.key == K_d:
                if pos == 0:
                    personnage = pd1
                if pos == 1:
                    personnage = pg1
                if pos == 2:
                    personnage = ph1
                if pos == 3:
                    personnage = pb1
                pygame.display.update()


                ############################################################################
                ############################################################################
                ######################AFFICHAGE DES MISSIONS################################
                ############################################################################
                ############################################################################
            if event.key == K_ESCAPE:
                vue=1
            if event.key == K_SPACE:
                texture = pygame.font.Font('freesansbold.ttf', 16)  # style et taille de police d ecriture
                pygame.draw.rect(ecran, color, (362, 50, 350, 670))  # tracer un rectangle

                if missiontuer == 1:
                    mission1 = pygame.draw.rect(ecran, vert, (412, 125, 250, 150))
                    texteSurface1 = texture.render('*Tuer un passant*', True, BLACK, vert)  # ce qui est ecrit dans le premier petit rectangle
                    texte1 = texteSurface1.get_rect()  # construire un rectangle pour pygame et le placement
                    texte1.topleft = (412, 185)  # afficher a partir de ces coordonée
                    ecran.blit(texteSurface1, texte1)  # affichage
                else :
                    mission1 = pygame.draw.rect(ecran, rouge, (412, 125, 250, 150))
                    texteSurface1 = texture.render('*Tuer un passant*', True, BLACK, rouge)  # ce qui est ecrit dans le premier petit rectangle
                    texte1 = texteSurface1.get_rect()  # construire un rectangle pour pygame et le placement
                    texte1.topleft = (412, 185)  # afficher a partir de ces coordonée
                    ecran.blit(texteSurface1, texte1)  # affichage

                if missionarme == 1:
                    mission2 = pygame.draw.rect(ecran, vert, (412, 325, 250, 150))
                    texteSurface2 = texture.render('*Rammaser une dague*', True, BLACK, vert)
                    texte2 = texteSurface2.get_rect()
                    texte2.topleft = (412, 385)
                    ecran.blit(texteSurface2, texte2)
                else:
                    mission2 = pygame.draw.rect(ecran, rouge, (412, 325, 250, 150))
                    texteSurface2 = texture.render('*Rammaser une dague*', True, BLACK, rouge)
                    texte2 = texteSurface2.get_rect()
                    texte2.topleft = (412, 385)
                    ecran.blit(texteSurface2, texte2)

                if missionvoiture == 1:
                    mission3 = pygame.draw.rect(ecran, vert, (412, 525, 250, 150))
                    texteSurface3 = texture.render('*Amener le vehicule au point B*', True, BLACK, vert)
                    texte3 = texteSurface3.get_rect()
                    texte3.topleft = (412, 585)
                    ecran.blit(texteSurface3, texte3)
                else :
                    mission3 = pygame.draw.rect(ecran, rouge, (412, 525, 250, 150))
                    texteSurface3 = texture.render('*Amener le vehicule au point B*', True, BLACK, rouge)
                    texte3 = texteSurface3.get_rect()
                    texte3.topleft = (412, 585)
                    ecran.blit(texteSurface3, texte3)

                    ############################################################################
                    ############################################################################
                    #########ALGOROITHME PERMETTANT DE SAVOIR QUELLES MISSIONS EST FINI ########
                    ############################################################################
                    ############################################################################

            if missionarme == 1 and missionvoiture == 0 and missiontuer == 0:
                totalmissioncompleted = textemissioncomplete1
            if missionarme == 0 and missionvoiture == 1 and missiontuer == 0:
                totalmissioncompleted = textemissioncomplete1
            if missionarme == 0 and missionvoiture == 0 and missiontuer == 1:
                totalmissioncompleted = textemissioncomplete1
            if missionarme == 1 and missionvoiture == 1 and missiontuer == 0:
                totalmissioncompleted = textemissioncomplete2
            if missionarme == 1 and missionvoiture == 0 and missiontuer == 1:
                totalmissioncompleted = textemissioncomplete2
            if missionarme == 0 and missionvoiture == 1 and missiontuer == 1:
                totalmissioncompleted = textemissioncomplete2
            if missionarme == 1 and missionvoiture == 1 and missiontuer == 1:
                totalmissioncompleted = textemissioncomplete3

                ############################################################################
                ############################################################################
                ####ALGOROITHME PERMETTANT LA NAVIGATION ET LES INTERACTION DANS LE MENU.###
                ############################################################################
                ############################################################################
        if vue == 1 or vue == 11 or vue == 12 or vue == 13 or vue == 14 or vue == 15:
            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                if 740 < x < 990 and 246 < y < 312:
                    vue = 2
                if 34 < x < 290 and 314 < y < 380:
                    vue = 3
                if 740 < x < 990 and 385 < y < 452:
                    vue = 4
                if 34 < x < 290 and 437 < y < 505:
                    pygame.quit()
                if 34 < x < 290 and 190 < y < 260:
                    vue = 0

        if vue == 1 or vue == 11 or vue == 12 or vue == 13 or vue == 14 or vue == 15:
            if event.type == MOUSEMOTION:
                x, y = event.pos
                if 40 < x < 290 and 190 < y < 260:
                    vue = 11
                if 40 < x < 290 and 316 < y < 385:
                    vue = 12
                if 40 < x < 290 and 435 < y < 503:
                    vue = 13
                if 740 < x < 990 and 385 < y < 451:
                    vue = 14
                if 740 < x < 990 and 245 < y < 311:
                    vue = 15

        if vue == 1:
            ecran.blit(menu_principal, (0, 0))
        if vue == 11:
            ecran.blit(menu_Jouer, (0, 0))
        if vue == 12:
            ecran.blit(menu_Commande, (0, 0))
        if vue == 13:
            ecran.blit(menu_Quitter, (0, 0))
        if vue == 14:
            ecran.blit(menu_credit, (0, 0))
        if vue == 15:
            ecran.blit(menu_Option, (0, 0))
        if vue == 2:
            ecran.blit(option, (0, 0))
        if vue == 3:
            ecran.blit(commande, (0, 0))
        if vue == 4:
            ecran.blit(credit, (0, 0))

        if vue == 2 or vue == 3 or vue == 4:
            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                if 0 < x < 250 and 0 < y < 70:
                    vue = 1
        if vue == 2:
            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                if 247 < x < 475 and 306 < y < 521:
                    son.set_volume(9.9)
                if 606 < x < 829 and 306 < y < 521:
                    son.set_volume(0.0)

        if event.type == QUIT:
            inProgress = False

    pygame.display.update()
pygame.quit()
