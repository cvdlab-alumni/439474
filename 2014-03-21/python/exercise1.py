from pyplasm import *

#definisco un po di colori
celeste=[0/100,191/100,255/100]
arancione=[255/100,165/100,79/100]
verde=[0/100,255/100,127/100]
rosa=[255/100,182/100,193/100]
giallo=[255/100,215/100,0/100]
rosso=[178/100,34/100,34/100]

#this is the first step of the temple
x_firststep=QUOTE([33])
Y_firststep=QUOTE([68])
firststep=PROD([x_firststep,Y_firststep])
firststep=SKELETON(1)(firststep)
firststep=COLOR(celeste)(firststep)

#this is the second step of the temple
x_secondstep=QUOTE([-1.5,30])
Y_secondstep=QUOTE([-1.5,65])
secondstep=PROD([x_secondstep,Y_secondstep])
secondstep=SKELETON(1)(secondstep)
secondstep=COLOR(arancione)(secondstep)

#this is the third step of the temple
x_thirdstep=QUOTE([-3,27])
Y_thirdstep=QUOTE([-3,62])
thirdstep=PROD([x_thirdstep,Y_thirdstep])
thirdstep=SKELETON(1)(thirdstep)
thirdstep=COLOR(verde)(thirdstep)

#step is the union of the three step
step=STRUCT([firststep,secondstep,thirdstep])
 
#this is the function to create a circle in wich r is the radius
def circle(r):
	def circle0(p):
		alpha = p[0]
		return [r*COS(alpha), r*SIN(alpha)]
	return circle0

#this is the base of the first column
columnbase = T([1,2])([4,4])(MAP(circle(1))(INTERVALS(2*PI)(20)))

#this is the all base of the column of the temple for all side 
trasl = [T([1,2])([5,0]),columnbase]
colonnato = STRUCT(NN(5)(trasl))

trasl2 = [T([1,2])([0,5]),columnbase]
colonnato2 = STRUCT(NN(12)(trasl2))

columnbase2=T([1,2])([25,0])(columnbase)
trasl3 = [T([1,2])([0,5]),columnbase2]
colonnato3 = STRUCT(NN(12)(trasl3))

columnbase3=T([1,2])([0,60])(columnbase)
trasl4 = [T([1,2])([5,0]),columnbase3]
colonnato4 = STRUCT(NN(5)(trasl4))
col5=T([1,2])([10,7.5])(columnbase)
col6=T([1,2])([15,7.5])(columnbase)
col7=T([1,2])([10,52.5])(columnbase)
col8=T([1,2])([15,52.5])(columnbase)

#colcentr is the struct of the four column inside the temple
colcentr=STRUCT([col5,col6,col7,col8])
colcentr=SKELETON(1)(colcentr)
colcentr=COLOR(rosa)(colcentr)

#this is for the column near the temple
collat=STRUCT([colonnato,colonnato2,colonnato3,colonnato4,columnbase])
collat=SKELETON(1)(collat)
collat=COLOR(giallo)(collat)

#this is for create the wall inside the temple
y_r1=QUOTE([-10.5,47])
x_r1=QUOTE([-10,1])
xy=PROD([x_r1,y_r1])
xy2=T(1)(12)(xy)

y_r2=QUOTE([-18.5,1])
x_r2=QUOTE([-11,11])
xy3=PROD([x_r2,y_r2])

y_r3=QUOTE([-47,4])
x_r3=QUOTE([-11,4,-3,4])
xy4=PROD([x_r3,y_r3])

wall=STRUCT([xy2,xy3,xy4,xy])
wall=SKELETON(1)(wall)
wall=COLOR(rosso)(wall)

#this is the first floor
floor0=STRUCT([step,wall,colcentr,collat])
building=floor0
VIEW(building)