import os, psutil
process = psutil.Process(os.getpid())
ram_inicial = process.memory_info().rss  # in bytes
x = {}
for i in range(100000):
    x[i]=1
ram_usada = process.memory_info().rss - ram_inicial  # in bytes
print(ram_usada)