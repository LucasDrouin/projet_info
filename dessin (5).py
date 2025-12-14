
from utils.fltk import *
s2=0
s=0
mode=0
def pion_ratelier(i, couleur):
    x=500
    y = 25 + i*50 + 25
    cercle(x, y, 20, couleur=couleur, remplissage=couleur, epaisseur=1)


def case_vide_ratelier(i):
    x=475
    y = 25 + i*50
    rectangle(x, y, x+50, y+50, couleur='black')

def dessine_plateau(ratelier_joueur):
    global mode
    
    efface("score_text")
    efface("score_value")
    efface("score_text_1")
    efface("score_value_1")
    efface("score_text_2")
    efface("score_value_2")
    efface("score_text_3")
    efface("score_value_3")
    efface("score_text_4")
    efface("score_value_4")
    efface("turn_info")
    efface("player_labels")
    
    rectangle(25, 25, 425, 525, couleur='black', epaisseur=1)
    for i in range(10):
        for l in range(8):
            rectangle(25 + l * 50, 25 + i * 50, 75 + l * 50, 75 + i * 50, couleur='black', epaisseur=1)
    
    rectangle(800, 700, 950, 750, couleur='black', epaisseur=2, tag="menu_button")
    texte(875, 725, "Menu", ancrage="center", couleur='black', taille=20, tag="menu_text")
    
    if mode > 1:
        texte(485, 300, 
              f"Au tour du joueur {ratelier_joueur.joueur_actif}",
              couleur="black", taille=20, tag="turn_info")
    
    if mode == 1:
        texte(485, 300, "Votre score:", couleur="black", taille=20, tag="turn_info")
        
        rectangle(475, 340, 650, 420, couleur='blue', epaisseur=3)
        texte(485, 360, "Score:", couleur="blue", taille=20, tag="score_text")
        texte(560, 385, str(ratelier_joueur.score_j1), couleur="blue", taille=30, tag="score_value")
    
    elif mode == 2:
        rectangle(475, 340, 600, 420, couleur='blue', epaisseur=3)
        texte(485, 360, "Joueur 1:", couleur="blue", taille=16, tag="player_labels")
        texte(540, 385, str(ratelier_joueur.score_j1), couleur="blue", taille=25, tag="score_value_1")
        
        rectangle(625, 340, 750, 420, couleur='purple', epaisseur=3)
        texte(635, 360, "Joueur 2:", couleur="purple", taille=16, tag="player_labels")
        texte(690, 385, str(ratelier_joueur.score_j2), couleur="purple", taille=25, tag="score_value_2")
    
    elif mode == 3:
        rectangle(475, 340, 585, 420, couleur='blue', epaisseur=3)
        texte(485, 360, "Joueur 1:", couleur="blue", taille=16, tag="player_labels")
        texte(525, 385, str(ratelier_joueur.score_j1), couleur="blue", taille=25, tag="score_value_1")
        
        rectangle(600, 340, 710, 420, couleur='green', epaisseur=3)
        texte(610, 360, "Joueur 2:", couleur="green", taille=16, tag="player_labels")
        texte(650, 385, str(ratelier_joueur.score_j2), couleur="green", taille=25, tag="score_value_2")
        
        rectangle(725, 340, 835, 420, couleur='purple', epaisseur=3)
        texte(735, 360, "Joueur 3:", couleur="purple", taille=16, tag="player_labels")
        texte(775, 385, str(ratelier_joueur.score_j3), couleur="purple", taille=25, tag="score_value_3")
    
    elif mode == 4:
        rectangle(475, 340, 585, 420, couleur='blue', epaisseur=3)
        texte(485, 360, "Joueur 1:", couleur="blue", taille=16, tag="player_labels")
        texte(525, 385, str(ratelier_joueur.score_j1), couleur="blue", taille=25, tag="score_value_1")
        
        rectangle(600, 340, 710, 420, couleur='green', epaisseur=3)
        texte(610, 360, "Joueur 2:", couleur="green", taille=16, tag="player_labels")
        texte(650, 385, str(ratelier_joueur.score_j2), couleur="green", taille=25, tag="score_value_2")
        
        rectangle(475, 440, 585, 520, couleur='orange', epaisseur=3)
        texte(485, 460, "Joueur 3:", couleur="orange", taille=16, tag="player_labels")
        texte(525, 485, str(ratelier_joueur.score_j3), couleur="orange", taille=25, tag="score_value_3")
        
        rectangle(600, 440, 710, 520, couleur='purple', epaisseur=3)
        texte(610, 460, "Joueur 4:", couleur="purple", taille=16, tag="player_labels")
        texte(650, 485, str(ratelier_joueur.score_j4), couleur="purple", taille=25, tag="score_value_4")
            

def case_noire(i,k):
    rectangle(25+k*50,25+i*50,75+k*50,75+i*50,couleur='black', remplissage='black', epaisseur=1, tag='')


def case_vide(i, k):
    x = 25 + k*50 + 25
    y = 25 + i*50 + 25
    x1 = 25 + k*50
    y1 = 25 + i*50
    x2 = x1 + 50
    y2 = y1 + 50
    rectangle(x1, y1, x2, y2, couleur='black')
    cercle(x, y, 20, couleur='black', epaisseur=1)

def cercle_non_capturable(i, k, couleur):
    x = 25 + k*50 + 25  # centre en x de la case
    y = 25 + i*50 + 25  # centre en y de la case
    cercle(x, y, 20, couleur='black',remplissage="white",epaisseur=1)
    cercle(x, y, 10, couleur='black', remplissage=couleur, epaisseur=1)

def cercle_capturable(i, k, couleur):
    x = 25 + k*50 + 25  # centre en x de la case
    y = 25 + i*50 + 25  # centre en y de la case
    cercle(x, y, 20, couleur=couleur, remplissage=couleur, epaisseur=1)  # seul cercle de couleur


def selection_joueurs():
    global mode
    efface_tout()
    rectangle(50, 150, 250, 250, couleur="black", remplissage="white", epaisseur= 4)
    texte(125, 200, "1 joueur", ancrage="center", taille=24)

    rectangle(50, 300, 250, 400, couleur="black", remplissage="white", epaisseur= 4)
    texte(150, 350, "Multijoueurs", ancrage="center", taille=24)
    
    rectangle(50, 450, 250, 550, couleur="red", remplissage="white", epaisseur= 4)
    texte(125, 500, "QUITTER", ancrage="center",couleur='red', taille=24)
    
    rectangle(500, 600, 700, 550, couleur="green", remplissage="white", epaisseur= 4)
    texte(600, 575, "HISTORIQUE", ancrage="center",couleur='green', taille=22)
    
    rectangle(800, 500, 1000, 200, couleur="BLACK", remplissage="white", epaisseur= 4)
    rectangle(800, 250, 1000, 200, couleur="BLACK", remplissage="white", epaisseur= 4)
    rectangle(800, 335, 1000, 420, couleur="BLACK", remplissage="white", epaisseur= 4)
    texte(900, 225, "HALL OF FAME", ancrage="center",couleur='#d79a10', taille=18)
    texte(900, 275, "pseudo", ancrage="center",couleur='#d79a10', taille=18)
    texte(900, 305, "70", ancrage="center",couleur='#d79a10', taille=18)
    texte(900, 360, "pseudo", ancrage="center",couleur='#d79a10', taille=18)
    texte(900, 390, "66", ancrage="center",couleur='#d79a10', taille=18)
    texte(900, 440, "pseudo", ancrage="center",couleur='#d79a10', taille=18)
    texte(900, 470, "63", ancrage="center",couleur='#d79a10', taille=18)
    
    texte(525, 75, "PICKTOK", ancrage="center",couleur='black', taille=40)
    rectangle(450, 200, 600, 350, couleur="black", remplissage="white", epaisseur= 4)
    rectangle(600, 200, 750, 350, couleur="black", remplissage="white", epaisseur= 4)
    rectangle(450, 350, 600, 500, couleur="black", remplissage="black", epaisseur= 4)
    rectangle(600, 350, 750, 500, couleur="black", remplissage="white", epaisseur= 4)
    cercle(675, 425, 65, couleur='black', remplissage='blue', epaisseur=4)
    cercle(525, 275, 65, couleur='black', remplissage='white', epaisseur=4)
    cercle(675, 275, 65, couleur='black', remplissage='white', epaisseur=4)
    cercle(675, 275, 35, couleur='black', remplissage='red', epaisseur=4)

    mise_a_jour()
    
    while True:
        x, y = attend_clic_gauche()
        
        if 50 <= x <= 250:
            if 150 <= y <= 250:
                mode = 1
                efface_tout()
                mise_a_jour()
                return 1  
            elif 300 <= y <= 400:
                efface_tout()
                mise_a_jour()
                nb_joueurs = selection_nombre_joueurs()
                if nb_joueurs in [2, 3, 4]:
                    return nb_joueurs
                elif nb_joueurs == "retour":
                    continue
            elif 450 <= y <= 550:
                efface_tout()
                mise_a_jour()
                return -1

def selection_nombre_joueurs():
    global mode
    efface_tout()
    texte(525, 75, "Nombre de joueurs", ancrage="center", couleur='black', taille=40)
    
    rectangle(200, 200, 500, 300, couleur="blue", remplissage="white", epaisseur=4)
    texte(350, 250, "2 joueurs", ancrage="center", taille=24)
    
    rectangle(600, 200, 900, 300, couleur="green", remplissage="white", epaisseur=4)
    texte(750, 250, "3 joueurs", ancrage="center", taille=24)
    
    rectangle(400, 350, 700, 450, couleur="purple", remplissage="white", epaisseur=4)
    texte(550, 400, "4 joueurs", ancrage="center", taille=24)
    
    rectangle(50, 500, 200, 600, couleur="gray", remplissage="white", epaisseur=4)
    texte(125, 550, "Retour", ancrage="center", taille=24)
    
    mise_a_jour()
    
    while True:
        x, y = attend_clic_gauche()
        
        if 200 <= x <= 500 and 200 <= y <= 300:  
            mode = 2
            efface_tout()
            mise_a_jour()
            return 2  
        elif 600 <= x <= 900 and 200 <= y <= 300: 
            mode = 3
            efface_tout()
            mise_a_jour()
            return 3 
        elif 400 <= x <= 700 and 350 <= y <= 450:  
            mode = 4
            efface_tout()
            mise_a_jour()
            return 4 
        elif 50 <= x <= 200 and 500 <= y <= 600: 
            return "retour"
