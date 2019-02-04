lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

print("max:", max(lista))
print('min:', min(lista))
print('pares:', [i for i in lista if i % 2 == 0])
print('primeiro:', lista.count(lista[0]))
print('média:', sum(lista)/len(lista))
print('negativo:', sum([i for i in lista if i < 0]))
