
x = 'hash(100)'
print(f"{x}={eval(x)}")

x = 'hash("a")'
print(f"{x}={eval(x)}")

x = 'hash(1000000000000000000)'
print(f"{x}={eval(x)}")

x = 'hash(10000000000000000000)'
print(f"{x}={eval(x)}")


class MyClase:
    def __hash__(self):
        return hash(id(self))


y = MyClase()
z = MyClase()
x = '(hash(y),hash(z))'
print(f"{x}={eval(x)}")
print(f"{x}={eval(x)}")


class MyClaseSinHash:
    pass  # por defecto python tiene una implementacion de hash


y = MyClaseSinHash()
z = MyClaseSinHash()
x = '(hash(y),hash(z))'
print(f"{x}={eval(x)}")
print(f"{x}={eval(x)}")


class MyClaseMismoHash:
    def __hash__(self):
        return 1  # malo


y = MyClaseMismoHash()
z = MyClaseMismoHash()
x = '(hash(y),hash(z))'
print(f"{x}={eval(x)}")
print(f"{x}={eval(x)}")


# las llaves deben de ser hashable. los valores no deben de ser hashables
# Para ser hashables deben de ser inmutables

d = {}
# int son inmutables
d[1] = {}
# str son inmutables
d["sfd"] = []
# tuplas son inmutables
d[(1, 2)] = {}

# dict ni list son inmutables
# d[[1, 2]] = {}
# d[{1:2}] = {}