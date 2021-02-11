
def ordena(arr):
    _ordena(arr, 0, len(arr) - 1)
    return arr


def _ordena(arr, inicio, fin):
    if inicio < fin:
        # hay que ordenar
        pivote = particion(arr, inicio, fin)
        _ordena(arr, inicio, pivote - 1)
        _ordena(arr, pivote+1, fin)
    return arr


def particion(arr, inicio, fin):
    v = arr[fin]
    i = inicio - 1
    for j in range(inicio, fin):
        if arr[j] <= v:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[fin] = arr[fin], arr[i+1]
    return i
