notas = []
for i in range(4):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

media = sum(notas)/4
for nota in notas:
    print("Uma nota:", nota)
print("Média: {:.2f}".format(media))
    
