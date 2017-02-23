from math import *
import random 

# Ressort K (en N/m)
def RessortK(E,v):
	K = (1/3)*(E/(1-2*v))
	return K

# Longueur à vide (en m)
def LongeurAVide(Lb,Lc):
	cLb=pow(Lb,2)
	cLc=(1/4)*pow(Lc,2)
	cT = (pow(Lb,2)) - ((1/4)*pow(Lc,2))
	if cT > 0:
		Lv = sqrt(cT)
	else:
		Lv = 0
	return Lv

# Longueur du déplacement (en m)
def LongueurDeplacement(Lf,Lv):
	Ld = Lf - Lv
	return Ld

# Masse du projectile (en kg)
def MasseProjectile(p,Df,Lf):
	mp = p*pi*pow((Df/2),2)*Lf
	return mp

# Vélocité V (en m/s)
def VelociteV(K,Ld,mp):
	V = sqrt((K*pow(Ld,2))/mp)
	return V

# Portée P (en m)
def PorteeP(V,g,a):
	d = ((pow(V,2))/g)*(sin(2*a))
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
def ForceDeTraction(K,Ld):
	F = K*Ld
	return F

# Flèche du bras f max
def FlecheBras(F,Lb,E,I):
	f = (F*pow(Lb,3))/48*E*I
	return f

# Evaluation des individus
def eval(pop):
	for indiv in pop:
		if indiv["Ld"] > indiv["f"] or indiv["Lv"] > indiv["Lf"] or indiv["Lc"] > indiv["Lb"]:
			indiv["score"] = 0
		else:
			indiv["score"] = 3

		if indiv["d"] >= 100 and indiv["d"] < 200:
			indiv["score"] += 1
		elif indiv["d"] >= 200 and indiv["d"] < 280 :
			indiv["score"] += 2
		elif indiv["d"] >= 280 and indiv["d"] <= 320:
			indiv["score"] += 3
		elif indiv["d"] > 320 and indiv["d"] <= 400:
			indiv["score"] += 2
		elif indiv["d"] > 400 and indiv["d"] <= 500:
			indiv["score"] += 1

		if indiv["Et"] >= 1 and indiv["Et"] < 2:
			indiv["score"] += 1
		elif indiv["Et"] >= 2 and indiv["Et"] < 3:
			indiv["score"] += 2
		elif indiv["Et"] >= 3:
			indiv["score"] += 3
	return pop
	
# Génération des scorpions aléatoire
def randomScorpions(taillepop,g,p,E):
	pop = []
	for num in range(0,taillepop):
		indiv = {}
		a  = radians(random.randrange(0,90))
		Lb = random.randrange(1,15)
		b  = random.randrange(1,15)
		h  = random.randrange(1,15)
		Lc = random.randrange(1,15)
		Lf = random.uniform(1,2)
		v  = random.uniform(0.24,0.30)
		Df = random.uniform(0.01,0.05)
		K  = RessortK(E,v)
		Lv = LongeurAVide(Lb,Lc)
		Ld = LongueurDeplacement(Lf,Lv)
		mp = MasseProjectile(p,Df,Lf)
		V  = VelociteV(K,Ld,mp)
		d  = PorteeP(V,g,a)
		Ec = EnergieImpact(mp,V)
		Et = JouleToTNT(Ec)
		I = MomentQuadratique(b,h)
		F = ForceDeTraction(K,Ld)
		f = FlecheBras(F,Lb,E,I)
		indiv.update({"a":a,"Lb":Lb,"b":b,"h":h,"Lc":Lc,"Lf":Lf,"v":v,"K":K,"Lv":Lv,"Ld":Ld,"Df":Df,"mp":mp,"V":V,"d":d,"Ec":Ec,"Et":Et,"I":I,"F":F,"f":f})
		pop.append(indiv)
	return pop

# Selection de la meilleur population
def BestPop(population, taille_population):
	for indiv in population:


# Selection
def selectOne(population):
    max     = sum([c.score for c in population])
    pick    = random.uniform(0, max)
    current = 0
    for chromosome in population:
        current += chromosome.score
        if current > pick:
            return chromosome