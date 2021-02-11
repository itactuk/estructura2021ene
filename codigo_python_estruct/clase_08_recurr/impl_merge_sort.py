

def ordena(arr):
    return _ordena_merge(arr, 0, len(arr) - 1)


def _ordena_merge(arr, inicio, fin):
    if inicio < fin:
        # no hay un solo elemento
        # hay que ordenar
        medio = (inicio + fin) // 2
        _ordena_merge(arr, inicio, medio)
        _ordena_merge(arr, medio + 1, fin)
        _merge(arr, inicio, medio, fin)
    return arr


def _merge(arr, inicio, medio, fin):
    n1 = medio - inicio + 1  # 3 - 1 = 3
    n2 = fin - medio
    arr_izq = []
    arr_dcha = []
    for i in range(0, n1):
        arr_izq.append(arr[i + inicio])
    for i in range(0, n2):
        arr_dcha.append(arr[medio + 1 + i])
    arr_izq.append(None)
    arr_dcha.append(None)

    i = 0
    j = 0
    for k in range(inicio, fin + 1):  # 1 a 6
        if arr_dcha[j] is None or (arr_izq[i] is not None and arr_izq[i] <= arr_dcha[j]):
            arr[k] = arr_izq[i]
            i += 1
        else:
            arr[k] = arr_dcha[j]
            j += 1

    return arr
