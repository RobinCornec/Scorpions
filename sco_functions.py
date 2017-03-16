from math import *
import random 

# Ressort K (en N/m)
def RessortK(E,v):
	K = (1/3)*(E/(1-2*v))
	return K

# Longueur à vide (en m)
def LongeurAVide(Lb,Lc):
	cT = (pow(Lb,2)) - (pow(Lc,2))
	if cT > 0:
		Lv = (1/2)*sqrt(cT)
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
	f = (F*pow(Lb,3))/(48*E*I)
	return f

# Evaluation des individus
def eval(pop):
	for indiv in pop:
		indiv["score"] = 10
		if indiv["Ld"] <= indiv["f"]:
			indiv["score"] -= 3
		if indiv["Lv"] <= indiv["Lf"]:
			indiv["score"] -= 3
		if indiv["Lc"] <= indiv["Lb"]:
			indiv["score"] -= 3


		if indiv["d"] >= 200 and indiv["d"] < 270 :
			indiv["score"] -= 1
		elif indiv["d"] > 330 and indiv["d"] <= 400:
			indiv["score"] -= 1
		elif indiv["d"] < 200 or indiv["d"] > 400:
			indiv["score"] -= 2

		if indiv["Et"] >= 0.1 and indiv["Et"] < 0.3:
			indiv["score"] -= 1
		elif indiv["Et"] <= 0.1:
			indiv["score"] -= 2

		if indiv["score"] <= 0:
			indiv["score"] = 1
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
def bestPop(population, taille_population):
	best_pop = []
	taille_selec = taille_population/2
	i=0
	for i in range(0,int(taille_selec)):
		best_indiv = 0
		worst_indiv = 0
		indivs = random.sample(range(0,taille_population-1),2)
		indiv1 = population[indivs[0]]
		indiv2 = population[indivs[1]]

		if indiv1["score"] > indiv2["score"]:
			best_indiv = indiv1
			worst_indiv = indiv2
		elif indiv2["score"] > indiv1["score"]:
			best_indiv = indiv2
			worst_indiv = indiv1

		percent = random.randrange(1,100)

		if best_indiv != 0 and worst_indiv != 0:
			percentscore = (worst_indiv["score"]/best_indiv["score"])*50
			if percent > percentscore:
				best_pop.append(best_indiv)
				choicepop = best_indiv
			elif percent <= percentscore:
				best_pop.append(worst_indiv)
				choicepop = worst_indiv
		else:
			if percent > 50:
				best_pop.append(indiv1)
				choicepop = indiv1
			elif percent <= 50:
				best_pop.append(indiv2)
				choicepop = indiv2

		population.remove(choicepop)
		taille_population -= 1
	return best_pop

		

# Selection
def selectOne(population):
    max     = sum([c["score"] for c in population])
    pick    = random.uniform(0, max)
    current = 0
    for chromosome in population:
        current += chromosome["score"]
        if current > pick:
            return chromosome

def childPop(parent1,parent2,g,p,E):
	indiv = {}
	a  = parent1["a"]
	Lb = parent1["Lb"]
	b  = parent1["b"]
	h  = parent1["h"]

	Lc = parent2["Lc"]
	Lf = parent2["Lf"]
	v  = parent2["v"]
	Df = parent2["Df"]


	toChange = random.randrange(1,100)
	if toChange == 1:
		valueToChange = random.randrange(1,8)
		if valueToChange == 1:
			a  = radians(random.randrange(0,90))
		elif valueToChange == 2:
			Lb = random.randrange(1,15)
		elif valueToChange == 3:
			b  = random.randrange(1,15)
		elif valueToChange == 4:
			h  = random.randrange(1,15)
		elif valueToChange == 5:
			Lc = random.randrange(1,15)
		elif valueToChange == 6:
			Lf = random.uniform(1,2)
		elif valueToChange == 7:
			v  = random.uniform(0.24,0.30)
		elif valueToChange == 8:
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

	return indiv