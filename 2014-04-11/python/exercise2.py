from pyplasm import *

def circle(r):
	def circle0(p):
		alpha = p[0]
		return [r*COS(alpha), r*SIN(alpha)]
	return circle0

culomnbase = T([1,2])([4,4])(MAP(circle(1))(INTERVALS(2*PI)(20)))

#queste righe successive servono per fare una colonna
culomnpic=T([1,2,3])([4,4,10])(MAP(circle(0.7))(INTERVALS(2*PI)(20)))
culomngra=T([1,2,3])([4,4,10.5])(MAP(circle(1))(INTERVALS(2*PI)(360)))
c1=JOIN([culomnpic,culomnbase])
c2=JOIN([culomnpic,culomngra])
x_cubo=PROD([Q(2),Q(2)])
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
col5=T([1,2])([10,7.5])(culomnbase)
col6=T([1,2])([15,7.5])(culomnbase)
col7=T([1,2])([10,52.5])(culomnbase)
col8=T([1,2])([15,52.5])(culomnbase)

colcentr=STRUCT([col5,col6,col7,col8])

ctot1=STRUCT([colcentr])
	
ctot=STRUCT([colonnato,colonnato2,culomnbase,colonnato3,colonnato4,colcentr])	

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
col5=T([1,2])([10,7.5])(colonna)
col6=T([1,2])([15,7.5])(colonna)
col7=T([1,2])([10,52.5])(colonna)
col8=T([1,2])([15,52.5])(colonna)
colonnati=STRUCT([colonnato,colonnato2,colonna,colonnato3,colonnato4,col5,col6,col7,col8])

#cornicione
x_matt1=QUOTE([26.5])
y_matt1=QUOTE([1.5])
matt1=PROD([x_matt1,y_matt1])
matt1=PROD([matt1,Q(1.2)])
x_matt2=QUOTE([1.5])
y_matt2=QUOTE([61.5])
matt2=PROD([x_matt2,y_matt2])
matt2=PROD([matt2,Q(1.2)])
cornice=STRUCT([matt1,matt1])
matt3=T([1,2])([0,60])(matt1)
matt4=T([1,2])([25,0])(matt2)
cornicione=STRUCT([matt1,matt2,matt3,matt4])
cornicione=T([1,2,3])([3.25,3.25,10.9])(cornicione)

x_bord1=QUOTE([26.75])
y_bord1=QUOTE([1.75])
bord1=PROD([x_bord1,y_bord1])
bord1=PROD([bord1,Q(0.3)])
x_bord2=QUOTE([1.75])
y_bord2=QUOTE([61.75])
bord2=PROD([x_bord2,y_bord2])
bord2=PROD([bord2,Q(0.3)])
bordino=STRUCT([bord1,bord1])
bord3=T([1,2])([0,60])(bord1)
bord4=T([1,2])([25,0])(bord2)
bordoncino=STRUCT([bord1,bord2,bord3,bord4])
bordoncino=T([1,2,3])([3.125,3.125,12.2])(bordoncino)

x_cfront1=QUOTE([26.5])
y_cfront1=QUOTE([1.5])
cfront1=PROD([x_cfront1,y_cfront1])
cfront1=PROD([cfront1,Q(1.5)])
cfront1=T([1,2,3])([3.25,3.25,12.5])(cfront1)
cfront2=T(2)(60)(cfront1)
front=STRUCT([cfront1,cfront2])

x_bord3=QUOTE([26.75])
y_bord3=QUOTE([1.75])
bord3=PROD([x_bord3,y_bord3])
bord3=PROD([bord3,Q(0.3)])
bordoncino2=T([1,2,3])([3.125,3.125,13.7])(bord3)
bordoncino3=T(2)(60)(bordoncino2)

#triangolo

base=CUBOID([27,2.5,0.5])
l1=CUBOID([13.5/COS(PI/9),2.5,0.5])
l2=R([1,3])(7*PI/18+PI/2)(l1)
l1=R([1,3])(PI/9)(l1)
l1=T(1)(0.5*COS(7*PI/18))(l1)
l2=T([1,3])([27,0.5])(l2)
triangolo=JOIN([base,l1,l2])
triangolo=T([1,2,3])([3.125,2.75,14])(triangolo)

t2=S([1,2,3])([0.9,0.4,0.9])(triangolo)
t2=T([1,2,3])([1.6,1.6,1.6])(t2)

t=DIFF([triangolo,t2])
t2=T(2)(62)(t2)
triangolo2=T(2)(60)(triangolo)
triangolo2=DIFF([triangolo2,t2])


VIEW(STRUCT([colonnati,cornicione,bordoncino,front,bordoncino2,bordoncino3,t,triangolo2]))
