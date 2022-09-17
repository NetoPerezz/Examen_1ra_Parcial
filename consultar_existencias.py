
from modificar_articulo import buscaID
def existencias(LISTA):
	if(len(LISTA) == 0):
		print("\n    <<< LISTA VACIA >>>")
	else: 
		ID = input(" ingrese ID:  ")
		index = buscaID(LISTA,ID) 
		if( index != -1):
			print("\n >>>>>>>>>>>> INFORMACIÓN DEL PRODUCTO <<<<<<<<<<<<< ")
			LISTA[index].mostrar()
		else:
			print("\n <<<  ESE PRODUCTO NO EXISTE >>> \n")

