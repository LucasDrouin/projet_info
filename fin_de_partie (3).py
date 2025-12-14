
from utils.fltk import texte, rectangle, efface, rectangle, attend_clic_gauche, mise_a_jour

partie_finie = False

def bonus(ratelier_joueur):
    rectangle(475, 440, 700, 525, couleur='green', epaisseur=5)
    ratelier_joueur.score_j1 += 20
    texte(485, 460, "Bravo! bonus +20", couleur="green", taille=18, tag="message")
    from . import dessin
    dessin.dessine_plateau(ratelier_joueur)
    efface("turn_info")

def perdu(ratelier_joueur, tour, mode):
    global partie_finie
    partie_finie = True
    from . import dessin
    rectangle(475, 440, 700, 525, couleur='red', epaisseur=5)
    texte(485, 460, "Fin de la partie", couleur="red", taille=18, tag="message")
    
    if mode == 1:
        texte(485, 485, "Vous avez perdu!", couleur="red", taille=18, tag="message2")
        ratelier_joueur.score_j1 = 0
    elif mode == 2:
        if tour % 2 == 0:
            texte(485, 485, "Joueur 1 a perdu!", couleur="red", taille=18, tag="message2")
            ratelier_joueur.score_j1 = 0
        else:
            texte(485, 485, "Joueur 2 a perdu!", couleur="red", taille=18, tag="message2")
            ratelier_joueur.score_j2 = 0
    
    dessin.dessine_plateau(ratelier_joueur)
    efface("turn_info")
    
   
    

def gagne(ratelier_joueur, tour, mode):
    global partie_finie
    partie_finie = True
    from . import dessin
    from .plateau import dessine_tout
    dessine_tout(ratelier_joueur, mode)
    
    if mode == 1:
        bonus(ratelier_joueur)
    else:
        scores = []
        if mode >= 1:
            scores.append(("Joueur 1", ratelier_joueur.score_j1))
        if mode >= 2:
            scores.append(("Joueur 2", ratelier_joueur.score_j2))
        if mode >= 3:
            scores.append(("Joueur 3", ratelier_joueur.score_j3))
        if mode == 4:
            scores.append(("Joueur 4", ratelier_joueur.score_j4))
        
        scores.sort(key=lambda x: x[1], reverse=True)
        
        if len(scores) > 1 and scores[0][1] == scores[1][1]:
            rectangle(475, 440, 700, 525, couleur='black', epaisseur=5)
            texte(485, 460, "Egalité!", couleur="black", taille=18, tag="message")
        else:
            rectangle(475, 440, 700, 525, couleur='green', epaisseur=5)
            texte(485, 460, f"{scores[0][0]} gagne!", couleur="green", taille=18, tag="message")
    
    efface("turn_info")
    
    

def verif_fini(ratelier_joueur, tour, mode):
    from .plateau import plateau
    global partie_finie

    if partie_finie:
        return

    compteur = 0
    for i in range(len(plateau)):
        for j in range(len(plateau[0])):
            if plateau[i][j].etat != "noir" and plateau[i][j].etat != "vide":
                compteur += 1

    if compteur == 0:
        gagne(ratelier_joueur, tour, mode)

def fini(ratelier_joueur, tour, mode):
    global partie_finie
    perdu(ratelier_joueur, tour, mode)
    
    

    