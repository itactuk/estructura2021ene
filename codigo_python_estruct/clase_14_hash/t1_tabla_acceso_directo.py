

class TablaAccesoDirecto:
	"""
	Tabla de acceso directo para contar las letras del alfabeto inglés.
	Solo incluye mayúsculas
	"""
	def __init__(self):
		self.tabla = [0] * 26

	def convertir_a_indice(self, letra):
		return ord(letra.upper()) - 65

	def obtener_valor(self, letra):
		i = self.convertir_a_indice(letra)
		return self.tabla[i]

	def insertar(self, letra, cant_elementos):
		i = self.convertir_a_indice(letra)
		self.tabla[i] = cant_elementos
		return cant_elementos

	def borrar(self, letra):
		i = self.convertir_a_indice(letra)
		self.tabla[i] = 0


if __name__ == '__main__':
	tabla = TablaAccesoDirecto()
	texto = "ABCDDA"
	for c in texto:
		cant = tabla.obtener_valor(c)
		tabla.insertar(c, cant + 1)
	print(tabla.tabla)