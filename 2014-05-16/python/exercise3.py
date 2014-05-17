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


def loopmne(ritorno,tomerge,toremove,vett):
	split = assemblyDiagramInit([len(vett[0]),len(vett[1]),len(vett[2])])([vett[0],vett[1],vett[2]])
	ritorno = diagram2cell(split,ritorno,tomerge)
	hpc = SKEL_1(STRUCT(MKPOLS(ritorno)))
	hpc = cellNumbering (ritorno,hpc)(range(len(ritorno[1])),CYAN,1)
	ritorno= ritorno[0],[cell for k, cell in enumerate (ritorno[1]) if not (k in toremove)]
	return ritorno

def visualMaster(master):
	hpc = SKEL_1(STRUCT(MKPOLS(master)))
	hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,1)
	VIEW(hpc)

def merge(vett,master,tomerge):
	split = assemblyDiagramInit([len(vett[0]),len(vett[1]),len(vett[2])])([vett[0],vett[1],vett[2]])
	master = diagram2cell(split,master,tomerge)
	return master

def remove(master,toremove):
	master= master[0],[cell for k, cell in enumerate (master[1]) if not (k in toremove)]
	return master