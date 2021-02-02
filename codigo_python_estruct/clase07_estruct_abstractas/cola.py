from collections import deque

cola = deque()

cola.append("Ricardo")
cola.append("Enmanuel")
cola.append("Pedro")
print(cola.popleft())

 # https://leetcode.com/problems/number-of-recent-calls/