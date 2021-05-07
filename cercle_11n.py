import random

nb_couleur = 2
nb_point = 11

def creerCercle(nb_couleur,nb_point):
    cpt_couleur = [0]*nb_couleur
    tab = []
    while len(tab) != (nb_couleur*nb_point):
        couleur = random.randint(0,nb_couleur-1)
        if cpt_couleur[couleur] != nb_point :
            tab += [couleur]
            cpt_couleur[couleur] += 1
    return tab

def get_pos_couleur(cercle,nb_couleur,nb_point):
    tab_res = [-1]*nb_couleur
    tab_res_int = []
    for i in range(0,nb_couleur):
        for j in range(0,len(cercle)):
            if cercle[j] == i:
                tab_res_int += [j]
   
        tab_res[i] = tab_res_int
        tab_res_int = []
    return tab_res

def tire_E(cercle,nb_couleur,nb_point):
    tab_pos_couleur = get_pos_couleur(cercle,nb_couleur,nb_point)
    return ...

cercle = creerCercle(nb_couleur,nb_point)
print(cercle)
tab_pos_couleur = get_pos_couleur(cercle,nb_couleur,nb_point)
print(tab_pos_couleur)


