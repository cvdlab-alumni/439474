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

#unico blocco iniziale 
master_block = assemblyDiagramInit([3,3,3])([[0.4,10.7,0.4],[0.4,12.6,0.4],[0.3,2.7,0.3]])
DRAW = COMP([VIEW,STRUCT,MKPOLS])
V,CV = master_block
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(CV)),CYAN,2)
#VIEW(hpc)

#divisione tra sala corridoio cucina camera mia e balcone scale, cameretta, camera mamma 
toMerge = 13
split = assemblyDiagramInit([3,1,1])([[5.5,0.3,5],[12.6],[2.7]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,2)
#VIEW(hpc)

#divisione tra sala camera mia ed uno spazio comprensivo di corridoio bagno e cucina 
toMerge = 26
split = assemblyDiagramInit([1,5,1])([[5.5],[4,0.2,4.7,0.2,3.5],[2.7]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,2)
#VIEW(hpc)

#divisione tra balcone buco delle scale cameretta e camera di mamma
toMerge = 27
split = assemblyDiagramInit([1,7,1])([[5],[1.3,0.2,2.5,0.2,3.4,0.2,4.8],[2.7]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,2)
#VIEW(hpc)

#divisione tra corridoio e lo spazio con bagno e cucina
toMerge = 29
split = assemblyDiagramInit([3,1,1])([[3.5,0.2,1.3],[4.7],[2.7]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,2)
#VIEW(hpc)

#divisione tra bagno e cucina
toMerge = 38
split = assemblyDiagramInit([1,3,1])([[3.5],[2.5,0.2,2],[2.7]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,2)
#VIEW(hpc)

#per rimuovere il dentro delle camere e il piano superiore 
toRemove=[27,40,42,30,39,31,33,35,37,13]
master_block= master_block[0],[cell for k, cell in enumerate (master_block[1]) if not (k in toRemove)]
#DRAW(master_block)

#ora facciamo le porte da 2 metri per 80 cm
#porta finestra sul balcone, porta della sala,porta della cameretta e porta della camera di mamma
toMerge = 25
split = assemblyDiagramInit([1,9,2])([[0.2],[0.3,0.7,1,1.8,0.9,0.8,2.8,0.8,4],[2,0.7]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,2)
#VIEW(hpc)

#porta della cucina e arco dell'ingresso tra sala cucina e corridoio 
toMerge = 25
split = assemblyDiagramInit([5,1,2])([[1.5,0.8,1.85,0.8,0.35],[0.2],[2,0.7]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,2)
#VIEW(hpc)

#porta camera mia
toMerge = 25
split = assemblyDiagramInit([3,1,2])([[4.15,0.8,0.35],[0.2],[2,0.7]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,2)
#VIEW(hpc)

#porta del bagno
toMerge = 28
split = assemblyDiagramInit([1,3,2])([[0.2],[3.3,0.8,0.6],[2,0.7]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,1)
#VIEW(hpc)

#tolgo il balcone
#divido il lato in due: la parte della sala e del balcone
toMerge = 10
split = assemblyDiagramInit([2,1,1])([[5.8,5],[0.4],[2.7]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,1)
#VIEW(hpc)

#divido il cornicione superiore in due: la parte della sala e del balcone
toMerge = 10
split = assemblyDiagramInit([2,1,1])([[5.8,5],[0.4],[2.7]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,1)
#VIEW(hpc)

#divido il lato in due: la parte delle camerette e del balcone
toMerge = 18
split = assemblyDiagramInit([1,2,1])([[0.4],[1.3,11.3],[2.7]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,1)
#VIEW(hpc)

#divido il cornicione superiore in due: la parte delle camerette e del balcone
toMerge = 18
split = assemblyDiagramInit([1,2,1])([[0.4],[1.3,11.3],[2.7]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,1)
#VIEW(hpc)

#ora facciamo le finestre
#finestra della cucina e finestra del bagno 
toMerge = 4
split = assemblyDiagramInit([1,5,3])([[0.4],[4.9,1.1,1.5,0.8,4.4],[1,1,0.7]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,1)
#VIEW(hpc)

#porta finestra della cameretta e della camera di mamma
toMerge = 69
split = assemblyDiagramInit([1,5,2])([[0.4],[4.1,1,4.4,1,0.8],[2,0.7]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,1)
#VIEW(hpc)

#portafinestra camera mia
toMerge = 11
split = assemblyDiagramInit([3,1,2])([[4.2,1,5.6],[0.4],[2,0.7]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,1)
#VIEW(hpc)

#finestra sala
toMerge = 63
split = assemblyDiagramInit([5,1,3])([[1.9,0.8,0.2,0.8,1.9],[0.4],[1,1,0.7]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,1)
#VIEW(hpc)

#la cella 9 rappresenta tutto il pavimento e vine suddivisa per ottenere la parte del pavimento del balcone
toMerge = 9
split = assemblyDiagramInit([2,3,1])([[5.7,5],[1.5,2.5,8.6],[0.3]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,1)
#VIEW(hpc)

#divide il piano del balcone, lato sala, in modo da farlo piu basso
toMerge = 62
split = assemblyDiagramInit([1,1,2])([[5],[0.4],[1.2,1.5]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,1)
#VIEW(hpc)

#divide il piano del balcone, lato cameretta, in modo da farlo piu basso
toMerge = 64
split = assemblyDiagramInit([1,1,2])([[0.4],[1.3],[1.2,1.5]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,1)
#VIEW(hpc)

#divide il pilastro del balcone ovvero l'angolo con i fiori, in modo da farlo piu basso
toMerge = 12
split = assemblyDiagramInit([1,1,2])([[0.4],[0.4],[1.2,1.5]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,1)
#VIEW(hpc)

toRemove=[23,27,31,35,41,51,57,63,12,75,69,45,86,106,100,62,122,118,121,120,82,115,92]
master_block= master_block[0],[cell for k, cell in enumerate (master_block[1]) if not (k in toRemove)]
DRAW(master_block)