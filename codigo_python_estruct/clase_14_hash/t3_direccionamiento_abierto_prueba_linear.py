from collections import deque


class DiccDirAbiertoPruebaLineal:
    """
    Implementa un Diccionario usando Encadenamiento (Chaining) para resolver colisiones
    """
    DEL = (None, None)

    def __init__(self, tamano=100):
        if tamano <= 0:
            raise Exception("Tamaño inicial debe de ser mayor que 0")
        self.tamano = tamano
        self.tabla = [None] * self.tamano
        self.n = 0

    def insert(self, llave: int, valor):
        """
        Cuando nuestro factor de carga sea mayor a 75, haremos un rehash
        :param llave:
        :param valor:
        :return:
        """
        if self.factor_carga() > 0.75:  # se esta llenando mucho, nuestra tabla
            self._rehash()
        i = 0
        h = self.obtener_hash(llave, i)
        while self.tabla[h] is not None:  # hay colision
            if self.tabla[h] == self.DEL:  # si un elemento ha sido borrado, usar esta posición
                self.n -= 1  # esto es para que n se mantenga igual
                break
            i += 1
            h = self.obtener_hash(llave, i)
        self.tabla[h] = (llave, valor)
        self.n += 1

    def borrar(self, llave: int):
        i = 0
        h = self.obtener_hash(llave, i)
        while self.tabla[h] is not None:
            if self.tabla[h][0] == llave:
                self.tabla[h] = self.DEL
        return False

    def obtener_valor(self, llave: int):
        """
        El libro lo llama search
        """
        i = 0
        h = self.obtener_hash(llave, i)
        while self.tabla[h] is not None:
            if self.tabla[h][0] == llave:
                return self.tabla[h][1]
        return None

    def obtener_hash_primo(self, llave):
        """usa método de división. Este es h'(k) """
        return llave % self.tamano

    def obtener_hash(self, llave, i):
        """usa método de prueba lineal"""
        return (self.obtener_hash_primo(llave) + i) % self.tamano

    def factor_carga(self):
        return self.n / self.tamano

    def _rehash(self):
        # guardar tabla. Hacer copia
        tabla_original = self.tabla.copy()  # O(n)
        # duplicamos el tamano
        self.tamano *= 2
        self.n = 0
        self.tabla = [None] * self.tamano
        # reinsertamos con nuestro tamanao cambiado
        for k, v in tabla_original:
            self.insert(k, v)
