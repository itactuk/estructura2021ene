
class Nodo:
    def __init__(self, valor, siguente=None) -> None:
        super().__init__()
        self.siguiente = siguente
        self.valor = valor


class SencillamenteEnlazadaLista:
    def __init__(self) -> None:
        super().__init__()
        self.nodo_inicial = None

    def agregar(self, valor) -> None:
        nodo = Nodo(valor)
        if self.nodo_inicial is None:
            self.nodo_inicial = nodo
        else:
            ultimo_nodo = self.ultimo_nodo()
            ultimo_nodo.siguiente = nodo

    
    def ultimo_nodo(self) -> Nodo:
        nodo = self.nodo_inicial
        while nodo is not None:
            if nodo.siguiente is None:
                return nodo
            nodo = nodo.siguiente
        return nodo

    def __iter__(self):
        self.curr = self.nodo_inicial
        return self

    def __next__(self):
        if self.curr is not None:
            v = self.curr.valor
            self.curr = self.curr.siguiente
            return v
        else:
            raise StopIteration



lista = SencillamenteEnlazadaLista()
lista.agregar(1)
lista.agregar(2)

# lista.insertar(1, 4)  # al comienzo?  O(1)
# lista.insertar(1, 4)  # en el medio?  O(n)
# lista.insertar(1, 4)  # y al final?  O(n) 

for l in lista:
    print(l)