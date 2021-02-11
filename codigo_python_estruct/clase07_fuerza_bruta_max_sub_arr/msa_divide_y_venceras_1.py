from typing import Tuple


def _encuentra_max_cruzado(arr, inicio, medio, fin):
    ind_max_izq = None
    ind_max_dcha = None

    sum_izq = None
    acc = 0
    for i in range(medio, inicio - 1, -1):
        acc += arr[i]
        if sum_izq is None or acc > sum_izq:
            sum_izq = acc
            ind_max_izq = i

    sum_dcha = None
    acc = 0
    for i in range(medio + 1, fin + 1):
        acc += arr[i]
        if sum_dcha is None or acc > sum_dcha:
            sum_dcha = acc
            ind_max_dcha = i
    return ind_max_izq, ind_max_dcha, sum_izq + sum_dcha


def _encuentra_arr_suma_max(arr, inicio, fin):
    if inicio == fin:
        return inicio, fin, arr[inicio]
    medio = (inicio + fin) // 2

    ind_inicial_izq, ind_final_izq, suma_izq = _encuentra_arr_suma_max(arr, inicio, medio)  # T(n/2)
    ind_inicial_dcha, ind_final_dcha, suma_dcha = _encuentra_arr_suma_max(arr, medio + 1, fin)  # T(n/2)
    ind_inicial_cruz, ind_final_cruz, suma_cruz = _encuentra_max_cruzado(arr, inicio, medio, fin)

    if suma_izq >= suma_dcha and suma_izq >= suma_cruz:
        return ind_inicial_izq, ind_final_izq, suma_izq
    elif suma_dcha >= suma_izq and suma_dcha >= suma_cruz:
        return ind_inicial_dcha, ind_final_dcha, suma_dcha
    # si ninguno de esos casos se cumple, nuestra solucion seria el resultado cruzado
    return ind_inicial_cruz, ind_final_cruz, suma_cruz


def encuentra_arreglo_suma_max(arr) -> Tuple[int, int, int]:
    """

    :param arr:
    :return: es una tupla con 3 enteros.
    El primer elemento es el inidice inicial del sub arreglo, el segundo es el indice final y el tercero es la suma
    """
    i_arr_max, j_arr_max, suma_max = _encuentra_arr_suma_max(arr, 0, len(arr)-1)  # O(nlogn)
    return i_arr_max, j_arr_max, suma_max  # O(1)

