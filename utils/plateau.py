import random
from utils.dessin import dessine_plateau
from utils.classe import Case
from utils.fltk import *
from utils.fin_de_partie import partie_finie,fini,perdu
from utils.dessin import s

import random

lignes = 10
colonnes = 8

plateau = [[None for _ in range(colonnes)] for _ in range(lignes)]


def initialiser_plateau():
    global plateau
    for i in range(lignes):
        for j in range(colonnes):
            plateau[i][j] = Case(i, j, "non_capturable")

    noirs_pos = set()
    while len(noirs_pos) < 23:
        a = random.randint(0, lignes - 1)
        b = random.randint(0, colonnes - 1)
        if (a,b) not in noirs_pos:
            plateau[a][b] = Case(a, b, "noir")
            noirs_pos.add((a,b))

    return plateau 

def initaliser_couleurs(plateau):
    while True:
        for i in range(8):
            if plateau[0][i].etat != "noir":
                couleur = random.choice(['red','green','blue','yellow'])
                plateau[0][i] = Case(0, i, "capturable", couleur)

        for i in range(1, 10):
            for j in range(8):
                if plateau[i][j].etat != "noir":
                    couleur = random.choice(['red','green','blue','yellow'])
                    plateau[i][j] = Case(i, j, "non_capturable", couleur)

        rouge = bleu = jaune = vert = 0
        for i in range(10):
            for y in range(8):
                c = plateau[i][y].couleur
                if c == "red":
                    rouge += 1
                elif c == "blue":
                    bleu += 1
                elif c == "yellow":
                    jaune += 1
                elif c == "green":
                    vert += 1


        if rouge % 3 == 0 and bleu % 3 == 0 and jaune % 3 == 0 and vert % 3 == 0:
            break


def compter_cases_accessibles(plateau):
    visite = set()
    
    # 1) trouver une première case non-noire
    start = None
    for i in range(lignes):
        for j in range(colonnes):
            if plateau[i][j].etat != "noir":
                start = (i, j)
                break
        if start:
            break

    if not start:
        return 0  # impossible mais sécurite

    # 2) DFS depuis cette case
    stack = [start]
    visite.add(start)

    while stack:
        x, y = stack.pop()
        for a, b in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            if 0 <= a < lignes and 0 <= b < colonnes:
                if plateau[a][b].etat != "noir" and (a, b) not in visite:
                    visite.add((a, b))
                    stack.append((a, b))

    return len(visite)


def verifier(plateau):

    total_non_noir = sum(
        1 for i in range(lignes) for j in range(colonnes)
        if plateau[i][j].etat != "noir"
    )

    total_accessibles = compter_cases_accessibles(plateau)

    while total_accessibles != total_non_noir:
        initialiser_plateau()
        total_non_noir = sum(
            1 for i in range(lignes) for j in range(colonnes)
            if plateau[i][j].etat != "noir"
        )
        total_accessibles = compter_cases_accessibles(plateau)

    initaliser_couleurs(plateau)


def dessine_tout(ratelier_joueur, mode):
    efface_tout()  
    dessine_plateau(ratelier_joueur) 
    ratelier_joueur.dessiner_ratelier()
    for ligne in plateau:
        for case in ligne:
            case.dessiner_case()
    
    if partie_finie:
        perdu()
    mise_a_jour()
    

def capturer(ev, ratelier_joueur, mode):
    from .fin_de_partie import partie_finie
    
    
    if partie_finie:
        return

    tev = type_ev(ev)
    if tev == "ClicGauche":
        x = abscisse(ev)
        y = ordonnee(ev)
        if 25 <= x <= 425 and 25 <= y <= 525:
            k = (x - 25) // 50
            i = (y - 25) // 50
            case = plateau[i][k]
            resultat = case.click(plateau, ratelier_joueur, lignes, colonnes)
            dessine_tout(ratelier_joueur, mode)

            if resultat == "perdu":
                fini(ratelier_joueur, ratelier_joueur.tour, ratelier_joueur.mode)

def retour_menu(ev):
    x = abscisse(ev)
    y = ordonnee(ev)
    if 800 <= x <= 950 and 700 <= y <= 750:
        return True
    return False

