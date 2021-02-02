from collections import deque  # double ended queue. Es una lista doblemente enlazado

x = deque()

x.append("A")  # para introducir valores al final
x.append("B")
x.append("C")

x.appendleft("O")  # para introducir valores al comienzo


print(x.pop())  # sacar valor al final
print(x.popleft())  # sacar valores del comienzo

print(x)