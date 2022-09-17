
def buscaID(LISTA,ID):
	for index in range(len(LISTA)):
		if LISTA[index].getID() == ID:
			return index
	return -1

def submenu():
	print("\n -------- cual desea modificar? ------")
	print(" 1   Nombre")
	print(" 2   Precio")
	print(" 3   Existencia")
	respuesta = 0
	while(respuesta < 1 or respuesta > 3):
		respuesta = int(input(" Escoja una opcion:  "))
	return respuesta


def modificar(LISTA):
	if(len(LISTA) == 0):
		print("\n    <<< LISTA VACIA >>>")
		return LISTA
	ID = input(" ingrese ID:  ")
	index = buscaID(LISTA,ID) 
	if( index != -1):
		LISTA[index].mostrar()
		opcion = submenu()
		if(opcion == 1):
			nombre = input(" Ingrese nombre:       ")
			LISTA[index].setnombre(nombre)
		elif(opcion == 2):
			precio = float(input("Ingrese precio:       "))
			LISTA[index].setprecio(precio)
		else:
			existencia = -1
			while(existencia < 0):
				existencia = int(input("Ingrese existencia:  "))
			LISTA[index].setexistencia(existencia)	
	else:
		print("\n <<<  ESE PRODUCTO NO EXISTE >>> \n")
	return LISTA

