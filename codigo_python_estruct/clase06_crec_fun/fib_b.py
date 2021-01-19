import time


def fibB(x):
    if x <= 1:
        return x  # 2t
    f = 1
    fa = 1  # 3t
    for _ in range(2, x):  # (x * ( 5t )) + t
        tmp = f
        f += fa
        fa = tmp
        
    return f          #t


for i in range(20000, 100000, 2000):
    a = [0] * 10
    for j in range(len(a)):
        tiempo_inicial = time.time()  # segundos
        fibB(i)
        duracion = time.time() - tiempo_inicial
        a[j] = duracion

    acc = 0
    promedio = sum(a)/len(a)
    for j in a:
        acc += (j - promedio)**2
    des_std = (acc/(len(a)-1))**0.5
    print(i, promedio, des_std)

