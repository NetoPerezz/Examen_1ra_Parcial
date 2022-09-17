
def inventario(LISTA):
	if(len(LISTA) == 0):
		print("\n    <<< LISTA VACIA >>>")
	else:
		print("\n >>>>>>>>>>>> INFORMACIÓN TOTAL DEL INVENTARIO <<<<<<<<<<<<< ")
		for actual in LISTA:
			actual.mostrar()