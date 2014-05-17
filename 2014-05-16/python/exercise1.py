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

master_block = assemblyDiagramInit([3,3,3])([[0.4,10.7,0.4],[0.4,12.6,0.4],[0.3,2.7,0.3]])
DRAW = COMP([VIEW,STRUCT,MKPOLS])
V,CV = master_block
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(CV)),CYAN,2)
VIEW(hpc)

toMerge = 13
split = assemblyDiagramInit([3,1,1])([[5.5,0.3,5],[12.6],[2.7]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,2)
VIEW(hpc)

toMerge = 26
split = assemblyDiagramInit([1,5,1])([[5.5],[4,0.2,4.7,0.2,3.5],[2.7]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,2)
VIEW(hpc)

toMerge = 27
split = assemblyDiagramInit([1,7,1])([[5],[1.3,0.2,2.5,0.2,3.4,0.2,4.8],[2.7]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,2)
VIEW(hpc)

toMerge = 29
split = assemblyDiagramInit([3,1,1])([[3.5,0.2,1.3],[4.7],[2.7]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,2)
VIEW(hpc)

toMerge = 38
split = assemblyDiagramInit([1,3,1])([[3.5],[2.5,0.2,2],[2.7]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,2)
VIEW(hpc)

toRemove=[27,40,42,30,39,31,33,35,37,13]
master_block= master_block[0],[cell for k, cell in enumerate (master_block[1]) if not (k in toRemove)]
DRAW(master_block)

#ora facciamo le porte da 2 metri per 80 cm
toMerge = 25
split = assemblyDiagramInit([1,9,2])([[0.2],[0.3,0.7,1,1.8,0.9,0.8,2.8,0.8,4],[2,0.7]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,2)
VIEW(hpc)

toMerge = 25
split = assemblyDiagramInit([5,1,2])([[1.5,0.8,1.85,0.8,0.35],[0.2],[2,0.7]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,2)
VIEW(hpc)

toMerge = 25
split = assemblyDiagramInit([3,1,2])([[4.15,0.8,0.35],[0.2],[2,0.7]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,2)
VIEW(hpc)

toMerge = 28
split = assemblyDiagramInit([1,3,2])([[0.2],[3.3,0.8,0.6],[2,0.7]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,1)
VIEW(hpc)

#tolgo il balcone
toMerge = 10
split = assemblyDiagramInit([2,1,1])([[5.8,5],[0.4],[2.7]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,1)
VIEW(hpc)

toMerge = 10
split = assemblyDiagramInit([2,1,1])([[5.8,5],[0.4],[2.7]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,1)
VIEW(hpc)

toMerge = 18
split = assemblyDiagramInit([1,2,1])([[0.4],[1.3,11.3],[2.7]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,1)
VIEW(hpc)

toMerge = 18
split = assemblyDiagramInit([1,2,1])([[0.4],[1.3,11.3],[2.7]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,1)
VIEW(hpc)

#ora facciamo le finestre
toMerge = 4
split = assemblyDiagramInit([1,9,3])([[0.4],[1.2,1.6,2.1,1.1,1.5,0.8,1.8,1.5,1],[1,1,0.7]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,1)
VIEW(hpc)

toMerge = 69
split = assemblyDiagramInit([1,7,3])([[0.4],[0.9,1.1,1.9,1.4,2.6,2,1.4],[1,1,0.7]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,1)
VIEW(hpc)

toMerge = 9
split = assemblyDiagramInit([2,3,1])([[5.7,5],[1.5,2.5,8.6],[0.3]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,1)
VIEW(hpc)

toMerge = 64
split = assemblyDiagramInit([1,1,2])([[5],[0.4],[1.2,1.5]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,1)
VIEW(hpc)

toMerge = 66
split = assemblyDiagramInit([1,1,2])([[0.4],[1.3],[1.2,1.5]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,1)
VIEW(hpc)

toMerge = 13
split = assemblyDiagramInit([1,1,2])([[0.4],[0.4],[1.2,1.5]])
master_block = diagram2cell(split,master_block,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master_block)))
hpc = cellNumbering (master_block,hpc)(range(len(master_block[1])),CYAN,1)
VIEW(hpc)

toRemove=[24,28,32,36,42,52,58,124,65,13,71,77,83,89,104,110,46,122,119,126,64,125]
master_block= master_block[0],[cell for k, cell in enumerate (master_block[1]) if not (k in toRemove)]
DRAW(master_block)