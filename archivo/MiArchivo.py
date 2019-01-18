import codecs
import sys

class MiArchivo:

	def __init__(self):

		#Se abre el archivo en esa direccion
		self.archivo = codecs.open("data/datos.txt", "r")

	def obtener_informacion(self):
		return self.archivo.readlines()

	def cerrar_archivo(self):
		self.archivo.close()