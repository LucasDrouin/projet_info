import sys
from utils.dessin import selection_joueurs
from utils.fltk import *
from utils.classe import ratelier

cree_fenetre(1050, 800)

def jeu():
    from utils.plateau import initialiser_plateau, verifier, dessine_tout, capturer, retour_menu, plateau
    from utils.fin_de_partie import partie_finie


    import utils.fin_de_partie
    utils.fin_de_partie.partie_finie = False

    plateau_jeu = initialiser_plateau()
    verifier(plateau_jeu)

    tour = 0
    mode = selection_joueurs()

    if mode == -1:
        ferme_fenetre()
        sys.exit(0)

    ratelier_joueur = ratelier(tour, mode)
    efface_tout()
    dessine_tout(ratelier_joueur, mode)

    while True:
        ev = donne_ev()
        tev = type_ev(ev)

        if tev == "ClicGauche":
            if retour_menu(ev):
                return "menu"


            if not partie_finie:
                capturer(ev, ratelier_joueur, mode)

        if tev == "Quitte":
            ferme_fenetre()
            return "quitte"

        from utils.fin_de_partie import verif_fini
        verif_fini(ratelier_joueur, tour, mode)

        mise_a_jour()

jeux = True
while jeux:
    action = jeu()

    if action == "quitte":
        jeux = False
    elif action == "menu":
        continue

ferme_fenetre()
