arreglo = [1, 2, 3]  # equivalente a ArrayList de Java
# En CPython ver implementacion: https://github.com/python/cpython/blob/master/Objects/listobject.c

print(f"Id arreglo: {id(arreglo)} original")
arreglo.append(1)  # O(1) casi siempre. En caso de que se llene el arreglo y hacer realloc seria O(n)
print(f"Id arreglo: {id(arreglo)} depués de append")
arreglo+=[1]  # no crea nuevo arreglo
print(f"Id arreglo: {id(arreglo)} depués de concat")

arr2 = [3, 4]
print(f"Id arr2: {id(arr2)} original")

print(f"Id arreglo+arr2: {id(arreglo+arr2)}")  # crea nuevo arreglo
print(f"Id arr2+arreglo: {id(arr2+arreglo)}")

arreglo.insert(1, 2); # more i>0.... o sea O(n)
arreglo.insert(2, 2);
arreglo.insert(3, 2);

# https://docs.python.org/3/library/array.html
from array import array
arr = array('l', [1, 2, 3, 4, 5])
arr.append(2)
print(arr)
for a in arr:
    print(a)


