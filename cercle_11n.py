import random

nb_couleur = 500
nb_point = 11

def creerCercle(nb_couleur,nb_point):
    """"creation du cercle
    out : tab avec le numero de la couleur de chaque point
    ex : [1,0,2,4,0,...,1,0,0] pour n couleur = 5"""
    cpt_couleur = [0]*nb_couleur
    tab = []
    while len(tab) != (nb_couleur*nb_point):
        couleur = random.randint(0,nb_couleur-1)
        if cpt_couleur[couleur] != nb_point :
            tab += [couleur]
            cpt_couleur[couleur] += 1
    return tab

def get_pos_couleur(cercle,nb_couleur,nb_point):
    """renvoi un tableau de la possition des point ranger par couleur
    ex : [[5,7,9,22,30,...],[1,2,3,...]] index de la list = numero couleur
    valeur = position dans le cercle"""
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
    """renvoi un tableau avec la position des points tire au hasard
    ex [12,3,6,7] pour n couleur 4 avec index = numero couleur et valeur = position dans le cercle"""
    tab_res = []
    tab_pos_couleur = get_pos_couleur(cercle,nb_couleur,nb_point)
    for i in range(0,len(tab_pos_couleur)):
        tab_res += [tab_pos_couleur[i][random.randint(0,10)]]
    return tab_res

def trouve_element_mauvais(element_tire,nb_couleur,nb_point):
    """renvoi un tableau avec la position des éléments mauvais dans le tableau des élements tire"""
    tab_res = []
    for i in range(0,len(element_tire)):
        if element_tire[i] == 0:
            if ((element_tire[i] + 1) in element_tire) or ((nb_couleur*nb_point)-1 in element_tire):
                tab_res += [i]
        elif element_tire[i] == (nb_couleur*nb_point)-1:
            if ((element_tire[i] - 1) in element_tire) or (0 in element_tire):
                tab_res += [i]
        if ((element_tire[i] + 1) in element_tire) or ((element_tire[i] - 1) in element_tire):
            tab_res += [i]
    return tab_res

def retire_mauvais_element(element_mauvais,tab_pos_couleur,element_tire,nb_couleur):
    """retire les élements mauvais stocker dans le tableau element_mauvais"""
    for i in range(0,len(element_mauvais)-1):
        element_tire[element_mauvais[i]] = tab_pos_couleur[element_mauvais[i]][random.randint(0,10)]
    return element_tire

def algo_lemme(element_tire,tab_pos_couleur,nb_couleur,nb_point):
    """algo de resolution du lemme
    retire les mauvais evenement jusqu'a tomber que sur des bons evements"""
    element_mauvais = trouve_element_mauvais(element_tire,nb_couleur,nb_point)
    while element_mauvais != []:
        element_tire = retire_mauvais_element(element_mauvais,tab_pos_couleur,element_tire,nb_couleur)
        element_mauvais = trouve_element_mauvais(element_tire,nb_couleur,nb_point)
    return element_tire

def main(nb_couleur,nb_point):
    cercle = creerCercle(nb_couleur,nb_point)
    print(cercle)
    tab_pos_couleur = get_pos_couleur(cercle,nb_couleur,nb_point)
    tire_element = tire_E(cercle,nb_couleur,nb_point)
    res = algo_lemme(tire_element,tab_pos_couleur,nb_couleur,nb_point)
    print(res)

"""cercle = creerCercle(nb_couleur,nb_point)
print(cercle)
tab_pos_couleur = get_pos_couleur(cercle,nb_couleur,nb_point)
print(tab_pos_couleur)
tire_element = tire_E(cercle,nb_couleur,nb_point)

tire_element += [tire_element[0]+1]
print(tire_element)
element_mauvais = trouve_element_mauvais(tire_element,nb_couleur,nb_point)
print(element_mauvais)
tire_element = retire_mauvais_element(element_mauvais,tab_pos_couleur,tire_element,nb_couleur)
print(tire_element)"""

main(nb_couleur,nb_point)




