from archivo.MiArchivo import MiArchivo
from busqueda.MiBusqueda import Busqueda

m = MiArchivo() #Se crea un objeto MiArchivo


lista = []
lista2 = []
lista = m.obtener_informacion() #lista toma la información del archivo mediante el metodo 
lista = [l.split(",") for l in lista] #Para separar mediante ,

#procedimiento para separar las cadenas y convertir a enteros
for l in lista:
	
	for x in l:
		m = int(x)
		lista2.append(m)


lista_ordenada = sorted(lista2) #se ordena la lista
print("La lista ordenada es:")
print(lista_ordenada)

#se define el numero a buscar en la variable numero
numero = 3

#se envia la lista ordenada a Busqueda
b = Busqueda(lista_ordenada)

#Se imprime el valor que retorna b.BusquedaBinaria
print("\nLa posicion en la que se encuentra el elemento %d es:" % (numero))
print(b.BusquedaBinaria(numero))

