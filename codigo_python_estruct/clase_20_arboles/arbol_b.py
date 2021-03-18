import json
import os
import uuid
from typing import List, Union


class ArbolB:

    def __init__(self, t=3):  # Crear el arbol
        self.t = t
        self.root = Nodo(self.t)  # Allocate Nodo

    def insert(self, k, data):
        """k es el id del elemento que quiero insertar"""
        with open(obtener_ruta_data(k), 'w') as f:
            json.dump(data, f)

        r = self.root
        if r.n == 2 * self.t - 1:  # se alcanzó la cantida maxima de llaves
            s = Nodo(self.t)
            self.root = s
            s.leaf = False
            s.n = 0
            s.children[1] = r
            self._split_children(s, 1)
            self._insert_non_full(s, k)
        else:
            self._insert_non_full(r, k)

    def _split_children(self, x, i):
        z = Nodo(self.t)
        y = x.children[i]
        z.leaf = y.leaf
        z.n = self.t - 1  # t-1
        for j in range(1, self.t - 2):
            z.keys[j] = y.keys[j + self.t]  # pasamos t-1 de y a z
        if not y.leaf:
            for j in range(1, self.t - 2):
                z.children[j] = y.children[j + self.t]
        y.n = self.t - 1
        for j in range(x.n + 1, i+2, -1):
            x.children[j+1] = x.children[j]
        x.children[i+1] = z
        for j in range(x.n, i+1, -1):
            x.keys[j+1] = x.keys[j]
        x.keys[i] = y.keys[self.t]
        x.n += 1
        disk_write(x)
        disk_write(y)
        disk_write(z)

    def _insert_non_full(self, x, k):
        i = x.n
        if x.leaf:
            while i >= 1 and x.keys[i] is not None and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i+1] = k
            x.n += 1
            disk_write(x)
        else:
            while i >= 1 and k < x.keys[i]:
                i -= 1
            i += 1
            ci = disk_read(x.children[i])
            if ci.n == 2*self.t - 1:
                self._split_children(x, i)
                if k > x.keys[i]:
                    i += 1
            self._insert_non_full(ci, k)

    def search(self, k):
        """k es el id del elemento que quiero buscar."""
        pass

    def _search(self, x, k):
        pass


class Nodo:
    def __init__(self, t=3, guardar=True):
        self.leaf = True
        self.n = 0
        self.id = str(uuid.uuid4())
        self.children: List[Nodo] = [None] * (2 * t + 1)
        self.keys = [None] * (2*t)
        if guardar:
            # escribimos en el disco
            disk_write(self)

    def count_children(self):
        return len([c for c in self.children if c is not None])

    def count_keys(self):
        return len([c for c in self.keys if c is not None])

    def serializar(self):
        datos = [self.leaf, self.n, self.id]
        if len(self.keys) > 0:
            llaves = []
            for k in self.keys:
                llaves.append(k)
            if len(llaves) > 0:
                datos.append(self.keys)
        if len(self.children) > 0:
            hijos_str = []
            for c in self.children:
                if isinstance(c, Nodo):
                    hijos_str.append(c.id)
                else:
                    hijos_str.append(c)
            if len(hijos_str) > 0:
                datos.append(hijos_str)
        return datos

    def __str__(self):
        return self.id


ruta_base_archivo = 'data_arbol'  # indicando ruta relativa


def disk_write(x: Nodo):
    with open(obtener_ruta_nodo(x.id), 'w') as f:
        json.dump(x.serializar(), f)


def disk_read(id_nodo: Union[str, Nodo]) -> Nodo:
    if isinstance(id_nodo, Nodo):
        id_nodo = id_nodo.id
    with open(obtener_ruta_nodo(id_nodo), 'r') as f:
        obj_json = json.load(f)
    nodo = Nodo(guardar=False)
    nodo.leaf = obj_json[0]
    nodo.n = obj_json[1]
    nodo.id = obj_json[2]
    nodo.children = obj_json[3]
    nodo.keys = obj_json[4]
    return nodo


def obtener_ruta_nodo(nodo_uuid: str):
    return os.path.join(ruta_base_archivo, nodo_uuid) + '.json'


def obtener_ruta_data(key):
    return os.path.join(ruta_base_archivo, str(key)) + '_key.json'