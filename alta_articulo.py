class productos:
	def __init__ (self,ID,nombre,precio,existencia):
		self.ID = ID
		self.nombre = nombre
		self.precio = precio
		self.existencia = existencia
	def mostrar(self):
		print("\n *********************************")
		print(" ID:          "+ self.ID)
		print(" Nombre:      "+ self.nombre)
		print(" Precio:      ", self.precio)
		print(" Existencias:  ", self.existencia)
		print("")
    
	def getID(self):
		return self.ID
	def setnombre(self,nombre):
		self.nombre = nombre
	def setprecio(self,precio):
		self.precio = precio
	def setexistencia(self,existencia):
		self.existencia = existencia



def submenuregistro():
	op = int(input(" hacer otro registro?  0 = SI,  1 = NO:      "))
	return op

LISTA = []
def agregar():
	seg = 0
	while(seg == 0):
		print("\n")
		ID =       		 input(" Ingrese el ID:        ")
		nombre = 	     input(" Ingrese el nombre:    ")
		precio   = float(input(" Ingrese el precio:    "))
		existencia = -1
		while existencia < 0:
			existencia = int(input(" Existencias:        "))

		LISTA.append( productos(ID,nombre,precio,existencia))
		seg = submenuregistro()	
	return LISTA
