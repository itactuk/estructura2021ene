import sys

sys.setrecursionlimit(500000)

# creamos nuestro dict para memoizacion
diccionario = {0: 1, 1: 1}


def factorial(x):
    if x in diccionario:
        return diccionario[x]
    elif x < 0:
        raise Exception(f"Factorial de {x} no es definido")
    diccionario[x] = x * factorial(x - 1)
    return diccionario[x]


if __name__ == '__main__':
    print(factorial(1))
    print(factorial(2))
    print(factorial(3))
    print(factorial(5))
    for i in range(1000):
        factorial(1000)
        factorial(1000)
    print(factorial(1000))
    print(factorial(1000))