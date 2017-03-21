from math import *
import random 
import sco_functions
import matplotlib.pyplot as plt
import numpy as np

# α  = Angle de Hausse  			 				(degrès) 	[0:90]
# Lb = Longueur du bras 			 				(mètre)		[0,1:5]
# b  = Base de la section du bras b  				(mètre)		[0,1:5]
# h  = Hauteur de la section du bras 				(mètre)		[0,1:5]
# Lc = Longueur de la corde 		 				(mètre)		[0,1:5]
# Lf = Longueur de la flèche		 				(mètre)		[0,1:5]
# ρ  = Masse volumique de la flèche  				(kg/m^3) 	7850
# E  = Module de Young du matériaux d l'arc			(GPa)		210
# ν  = Coefficient de Poisson du matériaux de l'arc				[0,24:0,30]
# g  = 9,81

# Pour des soucis d'encodage "α"" a été changé en "a", "ρ" en "p" et "ν" en "v"

population = []
ybetter = []
yaverage = []
yless = []
xgeneration = []
taille_population = 10000
generation = 100
g  = 9.81
p  = 7850
E  = 210

# Génération de la population
population = sco_functions.randomScorpions(taille_population,g,p,E)

# Pour chaque génération : 
for i in range(0,generation):
# l'évaluer
	population = sco_functions.eval(population)

	print("-------------------------- Génération %i --------------------------" % i)
# Gestion des listes pour l'affichage des courbes
	best_score = 1
	less_score = 10
	listaverage = []
	xgeneration.append(i)
	for indiv in population:
		listaverage.append(indiv["score"])
		if indiv["score"] > best_score:
			best_score = indiv["score"]
		if indiv["score"] < less_score:
			less_score = indiv["score"]

	avg_score = np.average(listaverage)

	yaverage.append(avg_score)
	ybetter.append(best_score)
	yless.append(less_score)
		
# Génération de la population enfant
	population = sco_functions.bestPop(population, taille_population,g,p,E)

# Affichage des courbes (Meilleur, moins bon et moyenne de la population pour chaque génération)
plt.plot(xgeneration, ybetter,'r',xgeneration,yaverage,'b',xgeneration,yless,'g')
plt.ylabel('scores')
plt.xlabel('génération')
plt.show()