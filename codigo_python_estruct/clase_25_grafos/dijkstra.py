from heapdict import heapdict
from collections import deque

import sys

class Vertice:
	def __init__(self, valor):
		self.d = sys.maxsize
		self.p = None
		self.valor = valor

	def __str__(self):
		return f"{self.valor}, {self.d}, {self.p}"

class Grafo:
	def __init__(self):
		self._lista_vertices = []
		self._dict_aristas = {}

	def agregar_vertice(self, vertice: Vertice):
		if vertice not in self._lista_vertices :
			self._lista_vertices.append(vertice)

	def iterador_vertices(self):
		return self._lista_vertices.__iter__()

	def iterador_aristas(self, vertice):
		if vertice not in self._dict_aristas:
			return []
		return self._dict_aristas[vertice].__iter__()

	def agregar_arista(self, v_src: Vertice, v_dst: Vertice, peso):
		# Ya que Dikjstra no permite pesos negativos, lanzar excepcion
		if peso <= 0:
			raise Exception("El valor del peso debe de ser mayor a 0")
		self.agregar_vertice(v_src)
		self.agregar_vertice(v_dst)
		if v_src not in self._dict_aristas:
			self._dict_aristas[v_src] = []
		self._dict_aristas[v_src].append((v_dst, peso))

	def __str__(self):
		res = ""
		for v, aristas in self._dict_aristas.items():
			res += str(v) + "\n"
			for v, p in aristas:
				res += " " + str(v) + " - peso=" + str(p) + "\n"
		return res

def inicializar(grafo: Grafo, source: Vertice):
	for v in grafo.iterador_vertices():
		v.d = sys.maxsize
		v.p = None
	source.d = 0


def dijkstra(grafo: Grafo, source: Vertice):
	inicializar(grafo, source)
	pq = heapdict()
	for v in grafo.iterador_vertices():
		pq[v] = v.d
	while len(pq)>0:
		u, d = pq.popitem()
		for v, p in grafo.iterador_aristas(u):
			if v.d > u.d + p:
				v.d = u.d + p
				pq[v] = v.d
				v.p = u


def ruta_mas_corto(grafo: Grafo, vertice_1: Vertice, vertice_2: Vertice):
	if vertice_1.d != 0:  # asumo que Dikjstra NO se ha corrido
		dijkstra(grafo, vertice_1)
	print(grafo)
	stack = deque()
	v = vertice_2
	while v is not None:
		stack.append(v)
		v = v.p
	ruta = ""
	while len(stack)>0:
		ruta += str(stack.pop().valor) + "->"

	if len(ruta) > 0:
		ruta = ruta[:-2]

	return ruta

if __name__ == '__main__':
	g = Grafo()
	v_a = Vertice("A")
	v_b = Vertice("B")
	v_c = Vertice("C")
	v_d = Vertice("D")
	v_e = Vertice("E")
	g.agregar_arista(v_a, v_b, 5)
	g.agregar_arista(v_a, v_c, 10)
	g.agregar_arista(v_a, v_d, 20)
	g.agregar_arista(v_a, v_e, 30)
	g.agregar_arista(v_b, v_c, 1)
	g.agregar_arista(v_b, v_d, 1)

	print(ruta_mas_corto(g, v_a, v_c))