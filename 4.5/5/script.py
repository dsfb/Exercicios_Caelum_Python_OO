lista = []

while True:
    dic = {}
    nome = input('Digite o nome: ')
    idade = input('Digite a idade: ')
    cidade = input('Digite a cidade: ')

    dic['nome'] = nome
    dic['idade'] = idade
    dic['cidade'] = cidade
    lista.append(dic)

    quer = input('Você quer adicionar outras pessoas? (S/N)').upper() == 'S'
    if not quer:
        break

for dic in lista:
    print('---------------')
    print('Dados de uma pessoa:')
    for k, v in dic.items():
        print(k + ":", v)
