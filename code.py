import random
def  colirie_case():
	return ...
def colorie_tout():
	return ...
def test_tout():
	return ...
def lemme_locaz():
	return ...
def init(nb_case_init,nb_coul_init):
    tab = [0]*nb_case_init
    for i in range(0,len(tab)):
        tab[i] = random.randint(1,nb_coul_init)
    return tab

def simlation():
	nb_case = 10
	nb_coul = 3
	tab = init(nb_case,nb_coul)
	fin = False
	while fin == False:
		tab_testage = test_tout(tab)
		if est_vide(tab_testage) :
			fin = True
		else
			tab = colorie_tout(tab,tab_testage)
	return tab 

def affiche_sim():
	return ...

print(init(10,3))



