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
generation = 300
g  = 9.81
p  = 7850
E  = 210

print("Random : start")
population = sco_functions.randomScorpions(taille_population,g,p,E)
print("Random : done")

for i in range(0,generation):
	print("Eval : start")
	population = sco_functions.eval(population)
	print("Eval : done")

	print("-------------------------- Génération %i --------------------------" % i)
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
		

	print("Bestpop : start")
	bestPop = sco_functions.bestPop(population, taille_population)
	print("Bestpop : done")

	population = []

	i = 0
	print("Selection : start")
	while i < taille_population:
		parent1 = sco_functions.selectOne(bestPop)
		popTemp = list(bestPop)
		popTemp.remove(parent1)
		parent2 = sco_functions.selectOne(popTemp)

		newIndiv = sco_functions.childPop(parent1,parent2,g,p,E)
		newIndiv2 = sco_functions.childPop(parent2,parent1,g,p,E)

		if newIndiv not in population and newIndiv2 not in population:
			population.append(newIndiv)
			population.append(newIndiv2)
			i+=2
	print("Selection : done")


plt.plot(xgeneration, ybetter,'r',xgeneration,yaverage,'b',xgeneration,yless,'g')
plt.ylabel('scores')
plt.xlabel('génération')
plt.show()








"""print("(a) Angle : %f " % (population[1]["a"]))
print("(Lb) Longueur du bras : %f " % (population[1]["Lb"]))
print("(b) Base de la section du bras : %f " % (population[1]["b"]))
print("(h) Hauteur de la section du bras : %f " % (population[1]["h"]))
print("(Lc) Longueur corde : %f " % (population[1]["Lc"]))
print("(Lf) Longueur flèche : %f " % (population[1]["Lf"]))
print("(v) Coefficient de Poisson : %f " % (population[1]["v"]))
print("(K) Ressort : %f " % (population[1]["K"]))
print("(Lv) Longueur à vide : %f " % (population[1]["Lv"]))
print("(Ld) Longueur déplacement : %f " % (population[1]["Ld"]))
print("(Df) Diamètre projectile : %f " % (population[1]["Df"]))
print("(mp) Masse projectile : %f " % (population[1]["mp"]))
print("(V) Velocité : %f " % (population[1]["V"]))
print("(d) Portée : %f " % (population[1]["d"]))
print("(Ec) Energie Impacte : %f " % (population[1]["Ec"]))
print("(Et) Energie TNT : %f " % (population[1]["Et"]))
print("(I) Moment Quadratique : %f " % (population[1]["I"]))
print("(F) Force de traction : %f " % (population[1]["F"]))
print("(f) Flèche Bras : %f " % (population[1]["f"]))
print("Score : %f " % (population[1]["score"]))"""

# for indiv in bestPop:
	# if indiv["score"] > 0:
		# print("(Ld) Longueur déplacement : %f " % (indiv["Ld"]))
		# print("(f) Flèche Bras : %f " % (indiv["f"]))
		# print("(Lv) Longueur à vide : %f " % (indiv["Lv"]))
		# print("(Lf) Longueur flèche : %f " % (indiv["Lf"]))
		# print("(Lc) Longueur corde : %f " % (indiv["Lc"]))
		# print("(Lb) Longueur du bras : %f " % (indiv["Lb"]))
		# print("(d) Portée : %f " % (indiv["d"]))
		# print("(Et) Energie TNT : %f " % (indiv["Et"]))
		# print("Score : %f " % (indiv["score"]))