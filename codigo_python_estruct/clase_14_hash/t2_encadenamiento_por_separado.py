from collections import deque


class DiccEncSep:
    """
    Implementa un Diccionario usando Encadenamiento (Chaining) para resolver colisiones
    """

    def __init__(self, tamano=100):
        if tamano <= 0:
            raise Exception("Tamaño inicial debe de ser mayor que 0")
        self.tamano = tamano
        self.n = 0
        self.tabla = [None] * self.tamano

    def insert(self, llave: int, valor):
        h = self.obtener_hash(llave)
        if self.tabla[h] is None:
            self.tabla[h] = deque()
        self.tabla[h].insert(0, (llave, valor,))
        self.n += 1

    def borrar(self, llave: int):
        h = self.obtener_hash(llave)
        if self.tabla[h] is None:
            return False
        for i, v in enumerate(self.tabla[h]):  # una mejor manera seria que en vez de usar deque creemos una lista enlazada propia que nos permita manejar los nodos
            if v[0] == llave:
                self.tabla[h].remove(v)  # O(n), mejora: usar lista enlaz propia para conv en O(1)
                self.n -= 1
                return True
        return False

    def obtener_valor(self, llave: int):
        """
        El libro lo llama search
        """
        h = self.obtener_hash(llave)
        if self.tabla[h] is None:
            return None
        for i, v in enumerate(self.tabla[h]):  # una mejor manera seria que en vez de usar deque creemos una lista enlazada propia que nos permita manejar los nodos
            if v[0] == llave:
                return v[1]
        return None

    def obtener_hash(self, llave):
        """usa método de división"""
        return llave % self.tamano

    def factor_carga(self):
        return self.n / self.tamano


d = DiccEncSep()  # d = {}
d.insert(1, 6)  # d[1] = 6
d.insert(101, 7)  # d[101] = 7
d.insert(201, 8)  # d[201] = 8

d.borrar(101)  # del d[101]

print(d.obtener_valor(1))  # print(d[1])
print(d.obtener_valor(201))
print(d.obtener_valor(101))
