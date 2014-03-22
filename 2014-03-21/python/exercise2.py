from pyplasm import *

def circle(r):
	def circle0(p):
		alpha = p[0]
		return [0, r*SIN(alpha)]
	return circle0

culomnbase = T([1,2])([4,4])(MAP(circle(1))(INTERVALS(2*PI)(20)))

culomnpic=T([1,2,3])([4,4,10])(MAP(circle(0.7))(INTERVALS(2*PI)(20)))
culomngra=T([1,2,3])([4,4,10.5])(MAP(circle(1))(INTERVALS(2*PI)(360)))
c1=JOIN([culomnpic,culomnbase])
c2=JOIN([culomnpic,culomngra])
x_cubo=PROD([Q(0),Q(2)])
cubo=T([1,2,3])([3,3,10.5])(PROD([x_cubo,Q(0.4)]))

colonna=STRUCT([c1,c2,cubo])

trasl = [T([1,2])([5,0]),culomnbase]
colonnato = STRUCT(NN(5)(trasl))

trasl2 = [T([1,2])([0,5]),culomnbase]
colonnato2 = STRUCT(NN(12)(trasl2))

culomnbase2=T([1,2])([25,0])(culomnbase)
trasl3 = [T([1,2])([0,5]),culomnbase2]
colonnato3 = STRUCT(NN(12)(trasl3))

culomnbase3=T([1,2])([0,60])(culomnbase)	

trasl =[T([1,2])([5,0]), colonna]
colonnato = STRUCT(NN(5)(trasl))

trasl2 = [T([1,2])([0,5]),colonna]
colonnato2 = STRUCT(NN(12)(trasl2))

colonna2=T([1,2])([25,0])(colonna)
trasl3 = [T([1,2])([0,5]),colonna2]
colonnato3 = STRUCT(NN(12)(trasl3))

colonna3=T([1,2])([0,60])(colonna)

north=colonnato3
south=colonnato2


def circle(r):
	def circle0(p):
		alpha = p[0]
		return [r*COS(alpha), 0]
	return circle0

culomnbase = T([1,2])([4,4])(MAP(circle(1))(INTERVALS(2*PI)(20)))

culomnpic=T([1,2,3])([4,4,10])(MAP(circle(0.7))(INTERVALS(2*PI)(20)))
culomngra=T([1,2,3])([4,4,10.5])(MAP(circle(1))(INTERVALS(2*PI)(360)))
c1=JOIN([culomnpic,culomnbase])
c2=JOIN([culomnpic,culomngra])
x_cubo=PROD([Q(0),Q(2)])
cubo=T([1,2,3])([3,3,10.5])(PROD([x_cubo,Q(0.4)]))

colonna=STRUCT([c1,c2,cubo])

trasl = [T([1,2])([5,0]),culomnbase]
colonnato = STRUCT(NN(5)(trasl))

trasl2 = [T([1,2])([0,5]),culomnbase]
colonnato2 = STRUCT(NN(12)(trasl2))

culomnbase2=T([1,2])([25,0])(culomnbase)
trasl3 = [T([1,2])([0,5]),culomnbase2]
colonnato3 = STRUCT(NN(12)(trasl3))

culomnbase3=T([1,2])([0,60])(culomnbase)
trasl4 = [T([1,2])([5,0]),culomnbase3]
colonnato4 = STRUCT(NN(5)(trasl4))

trasl =[T([1,2])([5,0]), colonna]
colonnato = STRUCT(NN(5)(trasl))

trasl2 = [T([1,2])([0,5]),colonna]
colonnato2 = STRUCT(NN(12)(trasl2))

colonna2=T([1,2])([25,0])(colonna)
trasl3 = [T([1,2])([0,5]),colonna2]
colonnato3 = STRUCT(NN(12)(trasl3))

colonna3=T([1,2])([0,60])(colonna)
trasl4 = [T([1,2])([5,0]),colonna3]
colonnato4 = STRUCT(NN(5)(trasl4))

east=colonnato4
west=colonnato
two_and_half_model=STRUCT([north,south,east,west])
VIEW(two_and_half_model)
