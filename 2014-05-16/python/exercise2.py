from pyplasm import *
import sys
sys.path.insert(0, 'C:/Users/661119/lar-cc/lib/py')
from simplexn import *
from larcc import *
from lar2psm import *
from largrid import *
from morph import *
from mapper import *
from splines import *
from scipy import *
from architectural import *
from myfont import *
from sysml import *
from exercise1 import master_block

DRAW = COMP([VIEW,STRUCT,MKPOLS])

#modifichiamo il piano terra
piano_terra=master_block
V,CV = piano_terra
hpc = SKEL_1(STRUCT(MKPOLS(piano_terra)))
hpc = cellNumbering (piano_terra,hpc)(range(len(piano_terra[1])),CYAN,2)
#VIEW(hpc)

#serve per creare la porta d'ingresso al piano terra
toMerge = 16
split = assemblyDiagramInit([3,1,2])([[0.1,1,3.9],[0.2],[2,.7]])
piano_terra = diagram2cell(split,piano_terra,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(piano_terra)))
hpc = cellNumbering (piano_terra,hpc)(range(len(piano_terra[1])),CYAN,1)
#VIEW(hpc)

toRemove=[101,97,98]
piano_terra= piano_terra[0],[cell for k, cell in enumerate (piano_terra[1]) if not (k in toRemove)]
#VIEW(hpc)

#chiudo il buco della porta del piano terra
portachiusa = assemblyDiagramInit([1,1,1])([[0.3],[0.75],[2.7]])
pchiusa=STRUCT(MKPOLS(portachiusa))

piano_t= STRUCT(MKPOLS(piano_terra))
piano_t=STRUCT([piano_t,T([1,2])([5.85,0.65])(pchiusa)])

#metto il pavimento in fondo al primo piano
pavchiuso = assemblyDiagramInit([1,1,1])([[5.2],[2.6],[0.3]])
pvchiuso=STRUCT(MKPOLS(pavchiuso))

#aggiungo camera da letto di nonna
camnonna=assemblyDiagramInit([1,1,1])([[6.8],[5],[3.3]])
camnonna= larApply(t(0,13.4,0))(camnonna)
hpc = SKEL_1(STRUCT(MKPOLS(camnonna)))
hpc = cellNumbering (camnonna,hpc)(range(len(camnonna[1])),CYAN,1)
#VIEW(hpc)

toMerge = 0
split = assemblyDiagramInit([3,3,2])([[0.4,6,0.4],[0.4,4.2,0.4],[0.3,3]])
camnonna = diagram2cell(split,camnonna,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(camnonna)))
hpc = cellNumbering (camnonna,hpc)(range(len(camnonna[1])),CYAN,1)
#VIEW(hpc)

#facciamo la finestra della camera di nonna
toMerge = 15
split = assemblyDiagramInit([1,5,3])([[0.4],[1.2,0.8,0.2,0.8,1.2],[1,1,1]])
camnonna = diagram2cell(split,camnonna,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(camnonna)))
hpc = cellNumbering (camnonna,hpc)(range(len(camnonna[1])),CYAN,1)
#VIEW(hpc)

toRemove=[7,9,21,27]
camnonna= camnonna[0],[cell for k, cell in enumerate (camnonna[1]) if not (k in toRemove)]

#ora uniamo la camera di nonna al piano terra
camnonna=STRUCT(MKPOLS(camnonna))
piano_t=STRUCT([piano_t,camnonna])
#VIEW(piano_t)
#fine piano terra

#modifichiamo il primo e il secondo piano nello stesso modo: aggiungiamo i balconi 
#creiamo il balcone della cameretta e della camera di mamma
balconecm = assemblyDiagramInit([1,1,1])([[2],[8.6],[1.5]])
balconecm= larApply(t(11.5,4.8,0))(balconecm)
hpc = SKEL_1(STRUCT(MKPOLS(balconecm)))
hpc = cellNumbering (balconecm,hpc)(range(len(balconecm[1])),CYAN,1)
#VIEW(hpc)

toMerge = 0
split = assemblyDiagramInit([3,3,2])([[0.4,1.2,0.4],[0.4,7.8,0.4],[0.3,1.2]])
balconecm = diagram2cell(split,balconecm,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(balconecm)))
hpc = cellNumbering (balconecm,hpc)(range(len(balconecm[1])),CYAN,1)
#VIEW(hpc)

toRemove=[3,9]
balconecm= balconecm[0],[cell for k, cell in enumerate (balconecm[1]) if not (k in toRemove)]
#DRAW(balconecm)
#fine del primo balcone

#creiamo il balcone della camera mia
balconemio = assemblyDiagramInit([1,1,1])([[6.8],[5],[1.5]])
balconemio= larApply(t(0,13.4,0))(balconemio)
hpc = SKEL_1(STRUCT(MKPOLS(balconemio)))
hpc = cellNumbering (balconemio,hpc)(range(len(balconemio[1])),CYAN,1)
#VIEW(hpc)

toMerge = 0
split = assemblyDiagramInit([3,3,2])([[0.4,6,0.4],[0.4,4.2,0.4],[0.3,1.2]])
balconemio = diagram2cell(split,balconemio,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(balconemio)))
hpc = cellNumbering (balconemio,hpc)(range(len(balconemio[1])),CYAN,1)
#VIEW(hpc)

toRemove=[7,9]
balconemio= balconemio[0],[cell for k, cell in enumerate (balconemio[1]) if not (k in toRemove)]
#DRAW(balconemio)
#fine del secondo balcone

#ora aggrego la casa e i balconi
secondopiano=evalStruct(Struct([master_block,balconecm,balconemio]))
secondopiano=STRUCT(CAT(AA(MKPOLS)(secondopiano)))

#ora facciamo le scale
#pianerottolo
pian = assemblyDiagramInit([1,1,1])([[1],[2.5],[0.135]])
app=STRUCT(MKPOLS(pian))

V=[[0,0,0],[0,1.1,0],[0.4,1.1,0.135],[0.4,0,0.135],[0,0,0.27],[0,1.1,0.27],[0.4,1.1,0.27],[0.4,0,0.27]]
FV=[[0,1,2,3,4,5,6,7]]
dwelling = V,FV
gradino=STRUCT(MKPOLS((V,FV)))
gradino=T(1)(0.6)(gradino)
app2=STRUCT(NN(9)([T([1,3])([0.4,0.135]),gradino]))

#secondo pianerottolo
pian2=T([1,3])([4.2,1.35])(app)

#seconda rampa
rampa2=R([1,2])(PI)(app2)
rampa2=T([1,2,3])([5.2,2.5,1.35])(rampa2)
gradino2=T([1,2,3])([5.2,2.5,1.35])(R([1,2])(PI)(gradino))

#colonna
column = larApply(t(11.3,0.2,0))(larRod(0.2,3)())
column=STRUCT(MKPOLS(column))

scala=STRUCT([app2,app,gradino,pian2,rampa2,gradino2])
scala=STRUCT([scala,T(3)(2.7)(scala),T(3)(5.4)(app)])
scala=T([1,2])([6.1,1.9])(scala)
#VIEW(scala)

casa=STRUCT([piano_t,T(3)(2.7)(secondopiano),T(3)(5.4)(secondopiano),scala,column])

#balcone curvo con bezier
c1=larBezierCurve([[0.84, 0.27], [0.46, 0.18], [0.24, 0.29], [0.22, 0.75]])
dom = larDomain([32])
obj = larMap(c1)(dom)
x1=STRUCT(MKPOLS(obj))
app=PROD([x1,Q(1.2)])
app2=R([1,2])(PI/2)(app)
balcone=STRUCT([T([1,2,3])([11.8,-0.3,3])(app2),T([1,2,3])([11.8,-0.3,5.7])(app2)])
#casa senza tetto
casa=STRUCT([casa,balcone])
#VIEW(casa)

#tetto
#tutto il tetto e' da rifare con V e CV 
#parte del tetto che sta sopra a sala cucina parte del corridoio  e cameretta
part1 = assemblyDiagramInit([1,1,1])([[11.9],[9],[0.3]]) 
p1=STRUCT(MKPOLS(part1))
p1=R([2,3])(PI/12)(p1)

#parte del tetto che sta sopra la camera mia il bagno e camera di mamma
p2 = assemblyDiagramInit([1,1,1])([[11.9],[5],[0.3]]) 
p2=STRUCT(MKPOLS(p2))
p2=R([2,3])(PI-PI/7)(p2)
p2=T(2)(12.5)(p2)
tetto=T(3)(17.3)(STRUCT([p1,p2]))
#VIEW(tetto)
tetto=S(3)(0.5)(tetto)

part2 = assemblyDiagramInit([1,1,1])([[11.5],[13.4],[0.1]])
p3=STRUCT(MKPOLS(part2))
p3=T(3)(8.6)(p3)
tetto=JOIN([tetto,p3])




#proviamo a fare una parete con gli archi........
def circle(r):
	def circle0(p):
		alpha = p[0]
		return [r*COS(alpha), r*SIN(alpha)]
	return circle0

parete=assemblyDiagramInit([1,1,1])([[0.4],[8.6],[3.3]])
parete=STRUCT(MKPOLS(parete))
# tutto il balcone e' 8.6 metto tre colonne ciascuna da 0.4 quindi ottengo un raggio che e' di 1.85
arco = MAP(circle(1.85))(INTERVALS(PI)(32))
arco=PROD([Q(0.4),arco])
arco=T(2)(1.85)(arco)
c=CUBOID([0.4,1.85,0])
s=JOIN([c,arco])

s=T(3)(1)(s)
c1=CUBOID([0.4,3.7,1])
ss=T(2)(0.4)(STRUCT([s,c1]))
ss2=T(2)(3.7+0.4)(ss)
parete=DIFF([parete,ss,ss2])
parete=T([1,2])([13.1,4.8])(parete)
#VIEW(parete)
casa=STRUCT([casa,parete])
#casa=STRUCT([casa,tetto,parete])
VIEW(casa)














"""#casa con tetto

DRAW = COMP([VIEW,STRUCT,MKPOLS])
block= STRUCT(MKPOLS(master_block))

#modifichiamo il piano terra
piano_terra=master_block
V,CV = piano_terra
hpc = SKEL_1(STRUCT(MKPOLS(piano_terra)))
hpc = cellNumbering (piano_terra,hpc)(range(len(piano_terra[1])),CYAN,2)
#VIEW(hpc)

toMerge = 17
split = assemblyDiagramInit([3,1,2])([[0.1,1,3.9],[0.2],[2,.7]])
piano_terra = diagram2cell(split,piano_terra,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(piano_terra)))
hpc = cellNumbering (piano_terra,hpc)(range(len(piano_terra[1])),CYAN,1)
#VIEW(hpc)

toRemove=[104,103,102,106]
piano_terra= piano_terra[0],[cell for k, cell in enumerate (piano_terra[1]) if not (k in toRemove)]
#VIEW(hpc)

#provo a chiudere il buco della porta del piano terra
portachiusa = assemblyDiagramInit([1,1,1])([[0.3],[0.75],[2.7]])
pchiusa=STRUCT(MKPOLS(portachiusa))

piano_t= STRUCT(MKPOLS(piano_terra))
piano_t=STRUCT([piano_t,T([1,2])([5.85,0.65])(pchiusa)])

#provo a mettere il pavimento in fondo al primo piano
pavchiuso = assemblyDiagramInit([1,1,1])([[5.2],[2.6],[0.3]])
pvchiuso=STRUCT(MKPOLS(pavchiuso))

piano_t=STRUCT([piano_t,T([1,2])([6,1.8])(pvchiuso)])
#VIEW(piano_t)

#ora facciamo le scale
#pianerottolo
pian = assemblyDiagramInit([1,1,1])([[1],[2.5],[0.135]])
app=STRUCT(MKPOLS(pian))

V=[[0,0,0],[0,1.1,0],[0.4,1.1,0.135],[0.4,0,0.135],[0,0,0.27],[0,1.1,0.27],[0.4,1.1,0.27],[0.4,0,0.27]]
FV=[[0,1,2,3,4,5,6,7]]
dwelling = V,FV
gradino=STRUCT(MKPOLS((V,FV)))
gradino=T(1)(0.6)(gradino)
app2=STRUCT(NN(9)([T([1,3])([0.4,0.135]),gradino]))

#secondo pianerottolo
pian2=T([1,3])([4.2,1.35])(app)

#seconda rampa
rampa2=R([1,2])(PI)(app2)
rampa2=T([1,2,3])([5.2,2.5,1.35])(rampa2)
gradino2=T([1,2,3])([5.2,2.5,1.35])(R([1,2])(PI)(gradino))

#colonna
column = larApply(t(11.3,0.2,0))(larRod(0.2,3)())
column=STRUCT(CAT(AA(MKPOLS)(evalStruct(Struct([column])))))

scala=STRUCT([app2,app,gradino,pian2,rampa2,gradino2])
scala=STRUCT([scala,T(3)(2.7)(scala),T(3)(5.4)(app)])
scala=T([1,2])([6.1,1.9])(scala)
casa=STRUCT([piano_t,T(3)(2.7)(block),T(3)(5.4)(block),scala,column])

#balcone curvo con bezier
c1=larBezierCurve([[0.84, 0.27], [0.46, 0.18], [0.24, 0.29], [0.22, 0.75]])
dom = larDomain([32])
obj = larMap(c1)(dom)
x1=STRUCT(MKPOLS(obj))
app=PROD([x1,Q(1.2)])
app2=R([1,2])(PI/2)(app)
balcone=STRUCT([T([1,2,3])([11.8,-0.3,3])(app2),T([1,2,3])([11.8,-0.3,5.7])(app2)])

#tetto
part1 = assemblyDiagramInit([1,1,1])([[6.7],[13.4],[0.2]])
p1=STRUCT(MKPOLS(part1))
p1=R([1,3])(PI/6)(p1)
p2=R([1,3])(PI*2/3)(p1)
p2=T([1,3])([11.6,0.3])(p2)
tetto=T(3)(17.3)(STRUCT([p1,p2]))
tetto=S(3)(0.5)(tetto)

part2 = assemblyDiagramInit([1,1,1])([[11.5],[13.4],[0.1]])
p3=STRUCT(MKPOLS(part2))
p3=T(3)(8.6)(p3)
tetto=JOIN([tetto,p3])

casa=STRUCT([casa,balcone,tetto])

#VIEW(casa)"""