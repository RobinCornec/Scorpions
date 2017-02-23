from math import *
import random 
import sco_functions

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
taille_population = 30
generation = 50
g  = 9.81
p  = 7850
E  = 210

population = sco_functions.randomScorpions(taille_population,g,p,E)
population = sco_functions.eval(population)

for i in range(0,generation):
	bestPop = sco_functions.BestPop(population, taille_population)
	# sco_functions.selectOne(taille_population,bestPop)

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

"""for indiv in population:
	# print("(Et) Energie TNT : %f " % (indiv["Et"]))
	# print("(d) Portée : %f " % (indiv["d"]))
	print("Score : %f " % (indiv["score"]))"""