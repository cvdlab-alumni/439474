from pyplasm import *

def circle(r):
	def circle0(p):
		alpha = p[0]
		return [r*COS(alpha), r*SIN(alpha)]
	return circle0

x_firststep=QUOTE([33])
Y_firststep=QUOTE([68])
firststep=PROD([x_firststep,Y_firststep])

x_secondstep=QUOTE([-1.5,30])
Y_secondstep=QUOTE([-1.5,65])
secondstep=PROD([x_secondstep,Y_secondstep])

x_thirdstep=QUOTE([-3,27])
Y_thirdstep=QUOTE([-3,62])
thirdstep=PROD([x_thirdstep,Y_thirdstep])

step=STRUCT([firststep,secondstep,thirdstep])

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

tetto=STRUCT([xy2,xy3,xy4,xy])

firststep=PROD([firststep,Q(1)])
secondstep=PROD([secondstep,Q(2)])
thirdstep=PROD([thirdstep,Q(3)])
step=STRUCT([firststep,secondstep,thirdstep])


tetto=PROD([tetto,Q(10.9)])

p1 = MAP(circle(1.175))(INTERVALS(PI)(32))
p1=PROD([Q(1),p1])
p1=T(2)(1.175)(p1)
c=CUBOID([1,1.175,0])
s=JOIN([c,p1])
s=T(3)(4.275)(s)
c1=CUBOID([1,2.35,4.275])
ss=T([1,2])([10,17.5])(STRUCT([s,c1]))
ss=T(3)(3)(STRUCT(NN(6)([T(2)(4),ss])))
ss2=T(1)(12)(ss)

tetto=DIFF([tetto,ss,ss2])

primocubo=CUBOID([13,1,1.8])
secondocubo=T([1,3])([1.2,1.8])(CUBOID([10.6,1,1.6]))
terzocubo=T([1,3])([2.05,3.4])(CUBOID([8.9,1,0.7]))
quartocubo=T([1,3])([4.8,4.1])(CUBOID([3.4,1,1.2]))
buco=T([1,3])([5.9,1.8])(CUBOID([1.2,1,1.6]))
secondocubo=DIFF([secondocubo,buco])

x=PROD([Q(2),Q(2)])
cc=T([1,2,3])([9.5,10.5,10.5])(PROD([x,Q(0.4)]))
cc2=T(1)(12)(cc)
cc3=T(2)(45)(cc)
cc4=T(2)(45)(cc2)
cap=STRUCT([cc,cc2,cc3,cc4])
cubi=STRUCT([primocubo,secondocubo,terzocubo,quartocubo])
cubi=T([1,2,3])([10,11,10.9])(cubi)
cubi2=T(2)(45)(cubi)

VIEW(STRUCT([step,tetto,cubi,cubi2]))