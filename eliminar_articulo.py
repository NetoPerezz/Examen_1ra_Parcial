
from modificar_articulo import buscaID

def eliminar(LISTA):
	if(len(LISTA) == 0):
		print("\n    <<< LISTA VACIA >>>")
		return LISTA
	ID = input(" ingrese ID:  ")
	index = buscaID(LISTA,ID) 
	if( index != -1):
		LISTA[index].mostrar()
		del(LISTA[index])
		print("\n >>>>>>>>>>>> ELIMINADO EXITOSAMENTE <<<<<<<<<<<<< ")
	else:
		print("\n <<<  ESE PRODUCTO NO EXISTE >>> \n")
	return LISTA
