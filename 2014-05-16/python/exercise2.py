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
#casa senza tetto
VIEW(STRUCT([casa,balcone]))


#casa con tetto

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

VIEW(casa)