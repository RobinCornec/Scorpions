from math import *
import random 

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

population = {}
taille_population = 30
g  = 9.81

# regarder pour les random avec virgule ","

def randomScorpions(taillepop, pop):
	for num in range(0,taille_population):
		a  = random.randrange(0.1,5,0.01)
		Lb = random.randrange(0.1,5,0.01)
		b  = random.randrange(0.1,5,0.01)
		h  = random.randrange(0.1,5,0.01)
		Lc = random.randrange(0.1,5,0.01)
		Lf = random.randrange(0.1,5,0.01)
		p  = 7850
		E  = 210
		v  = random.randrange(0.24,0.30,0.01)
		pop.update({"a":a,"Lb":Lb,"b":b,"h":h,"Lc":Lc,"Lf":Lf,"p":p,"E":E,"v":v})

population = randomScorpions(taille_population, population)
print(population)


# Ressort K (en N/m)
def RessortK(E,v):
	K = (1/3)*(E/(1-2*v))
	return K

# Longueur à vide (en m)
def LongeurAVide(Lb,Lc):
	Lv = sqrt(pow(Lb,2)-(1/4)*pow(Lc,2))
	return Lv

# Longueur du déplacement (en m)
def LongueurDeplacement(Lf,Lv):
	Ld = Lf - Lv
	return Ld

# Masse du projectile (en kg)
def MasseProjectile(p,b,h,Lf):
	mp = p*b*h*Lf
	return mp

# Vélocité V (en m/s
def VelociteV(K,Ld,mp):
	V = sqrt((K*pow(Ld,2))/mp)
	return V

# Portée P (en m)
def PorteeP(V,g,a):
	d = pow(V,2)/g*sin(2*a)
	return d

# Energie d'impact (en joules), assimilée à la force cinétique transformée à l'impact
def EnergieImpact(mp,V):
	Ec = 1/2*mp*pow(V,2)
	return Ec

# Equivalence Joule et gramme de TNT
def JouleToTNT(Ec):
	Et = Ec/4184
	return Et

# Moment quadratique du bras I (en m4)
def MomentQuadratique(b,h):
	I = (b*pow(h,3))/12
	return I

# Force de traction F (en N)
def ForceDeTraction(K,Lf):
	F = K*Lf
	return F

# Flèche du bras f max
def FlecheBras(F,Lb,E,I):
	f = (F*pow(Lb,3))/48*E*I