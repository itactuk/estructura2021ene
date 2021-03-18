
class monticulo:
    def __init__(self, arr):
        self.tamano = len(arr)
        self.arr = [None] + arr  # tener un arreglo que empiece en indice 1
        # asignar correctamente el tamano de la heap. completar arr para que sea un arbol completo
        # llamar build_heap

    def heap_maximum(self):
        return self.arr[1]

    def heap_extract_max(self):
        if len(self.arr) < 1:
            raise Exception("No hay mas elementos en la heap")
        maximo = self.heap_maximum()
        self.arr[1] = self.arr[self.tamano]
        self.tamano -= 1
        self.heapify(1)
        return maximo

    def heap_increase_key(self, i, key):
        if key < self.arr[i]:
            raise Exception("No se puede asignarle a un key un valor menor")
        self.arr[i] = key
        while i > 1 and self.arr[self.padre(i)] < self.arr[i]:
            self.arr[i], self.arr[self.padre(i)] = self.arr[self.padre(i)], self.arr[i]
            i = self.padre(i)

    def padre(self, i):
        return -1

    def heapify(self, i):
        pass


class Estudiante:
    def get_key(self):
        pass