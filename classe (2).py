import random
from utils.fltk import *
from utils.fin_de_partie import fini
from utils import dessin
from . import fin_de_partie





class ratelier:
    def __init__(self, tour, mode):
        self.tour = tour
        self.mode = mode
        self.joueur_actif = 1  
        self.pion_ratelier = [None] * 5
        self.score_j1 = 0
        self.score_j2 = 0
        if mode >= 3:
            self.score_j3 = 0
        else :
            None
        if mode == 4 :
            self.score_j4 = 0
        else :
            None

    def dessiner_ratelier(self):
        from utils.dessin import pion_ratelier, case_vide_ratelier
        rectangle(475, 25, 525, 275, couleur='black', epaisseur=1)
        for i in range(5):
            rectangle(475, 25 + i * 50, 525, 75 + i * 50, couleur='black', epaisseur=1)
        for i, pion in enumerate(self.pion_ratelier):
            if pion is not None:
                pion_ratelier(i, pion)
            else:
                case_vide_ratelier(i)

    def ajouter_pion(self, couleur):
        for i in range(len(self.pion_ratelier)):
            if self.pion_ratelier[i] is None:
                self.pion_ratelier[i] = couleur
                break

    def verification(self):
        compte = {'red': 0, 'green': 0, 'blue': 0, 'yellow': 0}
        for couleur in self.pion_ratelier:
            if couleur is not None:
                compte[couleur] += 1

        for couleur, nb in compte.items():
            if nb >= 3:
                bonus = 2 if self.pion_ratelier.count(None) == 0 else 1

                if self.mode == 1:
                    self.score_j1 += bonus
                elif self.mode >= 2:
                    if self.joueur_actif == 1:
                        self.score_j1 += bonus
                    elif self.joueur_actif == 2:
                        self.score_j2 += bonus
                    elif self.mode >= 3 and self.joueur_actif == 3:
                        self.score_j3 += bonus
                    elif self.mode == 4 and self.joueur_actif == 4:
                        self.score_j4 += bonus

                for i in range(len(self.pion_ratelier)):
                    if self.pion_ratelier[i] == couleur:
                        self.pion_ratelier[i] = None
    
        if None not in self.pion_ratelier and len(self.pion_ratelier) == 5:
            return "perdu"


class Case():
    def __init__(self,i,k,etat,couleur=None):
        self.i=i
        self.k=k
        self.couleur=couleur
        self.etat=etat
        if self.etat!="noir" and self.couleur is None:
            self.couleur=random.choice(['red','green','blue','yellow'])
    
    def dessiner_case(self):
        from utils.dessin import case_noire, cercle_non_capturable, cercle_capturable, case_vide

        if self.etat=="noir":
            case_noire(self.i,self.k)
        elif self.etat=="non_capturable":
            cercle_non_capturable(self.i,self.k,self.couleur)
        elif self.etat=="capturable":
            cercle_capturable(self.i,self.k,self.couleur)
        elif self.etat=="vide":
            case_vide(self.i,self.k)

    def click(self, plateau, ratelier_joueur, lignes, colonnes):
        if fin_de_partie.partie_finie:
            return False
        if self.etat == "capturable":
            self.etat = "vide"
            ratelier_joueur.ajouter_pion(self.couleur)
            resultat = ratelier_joueur.verification()
            if resultat == "perdu":
                fin_de_partie.fini(ratelier_joueur, ratelier_joueur.tour, ratelier_joueur.mode)
        
         
            if ratelier_joueur.mode > 1:
                ratelier_joueur.joueur_actif += 1
                if ratelier_joueur.joueur_actif > ratelier_joueur.mode:
                    ratelier_joueur.joueur_actif = 1

            if resultat == "perdu":
                return "perdu"
        
         
            if self.i > 0:
                case_au_dessus = plateau[self.i - 1][self.k]
                if case_au_dessus.etat == "non_capturable":
                    case_au_dessus.etat = "capturable"

            if self.i < lignes - 1:
                case_en_dessous = plateau[self.i + 1][self.k]
                if case_en_dessous.etat == "non_capturable":
                    case_en_dessous.etat = "capturable"

            if self.k > 0:
                case_gauche = plateau[self.i][self.k - 1]
                if case_gauche.etat == "non_capturable":
                    case_gauche.etat = "capturable"

            if self.k < colonnes - 1:
                case_droite = plateau[self.i][self.k + 1]
                if case_droite.etat == "non_capturable":
                    case_droite.etat = "capturable"
        
            return True

        return False

