dic = {}
nome = input('Digite o nome: ')
idade = input('Digite a idade: ')
cidade = input('Digite a cidade: ')

dic['nome'] = nome
dic['idade'] = idade
dic['cidade'] = cidade

for k, v in dic.items():
    print(k + ":", v)
