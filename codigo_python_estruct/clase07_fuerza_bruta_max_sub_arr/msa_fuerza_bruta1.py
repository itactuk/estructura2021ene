from typing import Tuple


def encuentra_arreglo_suma_max(arr) -> Tuple[int, int, int]:
    """

    :param arr:
    :return: es una tupla con 3 enteros.
    El primer elemento es el inidice inicial del sub arreglo, el segundo es el indice final y el tercero es la suma
    """
    suma_max = None  # O(1)
    i_arr_max = None  # O(1)
    j_arr_max = None  # O(1)
    for i, v in enumerate(arr):  # O(n^2) * n -> O(n^3)
        for j in range(i, len(arr)):  # O(n) * n -> O(n^2)
            suma_actual = sum(arr[i:j+1])  # O(n)
            suma_actual = sum(arr[i:j + 1])  # O(n)
            if suma_max is None or suma_actual > suma_max:
                suma_max = suma_actual
                i_arr_max = i
                j_arr_max = j
    return i_arr_max, j_arr_max, suma_max  # O(1)

