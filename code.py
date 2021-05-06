import random
def est_vide(tab):
    return len(tab)==0

def colorie_tout(tab_colori,tab_testage_colori,nb_coul):
    for i in range(0,len(tab_testage_colori)):
        tab_colori[tab_testage_colori[i]] = random.randint(1,nb_coul)
    return tab_colori

def test_tout(tab):
    tab_res = []
    for i in range(0,len(tab)-1):
        if tab[i] == tab[i+1]:
            tab_res += [i+1]
    return tab_res

def lemme_locaz():
	return ...
def init(nb_case_init,nb_coul_init):
    tab = [0]*nb_case_init
    for i in range(0,len(tab)):
        tab[i] = random.randint(1,nb_coul_init)
    return tab

def simulation():
    nb_case = 10
    nb_coul = 2
    tab = init(nb_case,nb_coul)
    print(tab)
    fin = False
    while fin == False:
        print(tab)
        tab_testage = test_tout(tab)
        print(tab_testage)
        if est_vide(tab_testage):
            fin = True
        else:
            tab = colorie_tout(tab,tab_testage,nb_coul)
    return tab

def affiche_sim():
	return ...

#tab = init(10,3)    
#print(tab)
#print(colorie_tout(tab,[0,3,4,5,6,7,8,9],3))
#print(test_tout(tab))
print(simulation())
