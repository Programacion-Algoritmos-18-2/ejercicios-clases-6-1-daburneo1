class Busqueda (object):

	def __init__(self, datos):
		self.data = datos #
		

	def BusquedaBinaria(self, elem):
		#Se crean las variables necesarias, y se da valor a elemB con el valor de elem obtenido de la clase principal
		elemB = elem
		inferior = 0
		superior = len(self.data)-1  #Se obtiene el tamaño del arreglo y se le resta 1
		medio = int(((inferior + superior +1)/2)) #Se convierte a int 
		ubicacion = -1 

		while((inferior <= superior) and (ubicacion == -1)): #condicion para que realice el ciclo
			if elemB == self.data[medio]: #si el elemento a buscar es igual al valor de data en la posicion medio
				ubicacion = medio #ubicacion toma el valor de medio
			elif elemB < self.data[medio]: #Si el elemeento a buscar es menor
				superior = medio - 1 #superior toma el valor de medio - 1
			else:
				inferior = medio + 1 #inferior toma el valor de medio + 1
			medio = int(((inferior + superior + 1)/2)) #Despues de las condiciones, medio toma un nuevo valor

		return ubicacion #Retorna la ubicacion, si no es encontrado el numero retorna -1

	def __str__(self): #Equivalente al to string para que imprima 

		return "Posicion %s" % (self.ubicacion)