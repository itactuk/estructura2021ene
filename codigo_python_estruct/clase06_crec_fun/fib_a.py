import time


def fibA(x):
    if x == 1:
        return 1  # t
    if x < 1:
        return 0  # t
    return fibA(x-1) + fibA(x-2)  # t + tfibA + tfibB


for i in range(1, 50):
    tiempo_inicial = time.time()  # segundos
    fibA(i)
    duracion = time.time() - tiempo_inicial
    print(i, duracion)

