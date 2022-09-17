import os
from alta_articulo import *
from consultar_existencias import*
from eliminar_articulo import *
from inventario_total import *
from modificar_articulo import*
def menu():
	os.system ("cls")  
	print("\n  ***** Menu principal del inventario *******")
	print("\t 1  Dar de alta un artículo")
	print("\t 2  Modificar un articulo")
	print("\t 3  Eliminar un articulo")
	print("\t 4  Consultar existencias")
	print("\t 5  Inventario total")
	print("\t 6  Salir del programa")
	respuesta = 10
	while(respuesta < 1 or respuesta > 6):
		respuesta  = int(input("\t ingrese su opción: "))
	return respuesta

LISTA = []
opcion = 1
while opcion != 6:
	opcion = menu()
	os.system ("cls")  
	if (opcion == 1):
		LISTA = agregar()
	elif(opcion == 2):
		LISTA = modificar(LISTA)
	elif(opcion == 3):
		LISTA = eliminar(LISTA)
	elif opcion == 4:
		existencias(LISTA)
	elif opcion == 5:
		inventario(LISTA)
	else:
		print("\n\n\t <<<<< HASTA PRONTO >>>> \n\n")
	a = input("\n\n presione una tecla para continuar.....")

