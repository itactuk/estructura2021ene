import time
import timeit


print(timeit.timeit('salida = 10*5'))

importar_modulo = "import random"
codigo_a_probar = ''' 
def prueba(): 
    return random.randint(10, 100)
'''
print(timeit.repeat(stmt=codigo_a_probar, setup=importar_modulo, repeat=5))

# En línea de comando
# python -m timeit -h

x = {}
t_inicial = time.time()  # en segundos
for i in range(100000):
    x[i] = 1
duracion = time.time() - t_inicial  # segundos

print(duracion)



