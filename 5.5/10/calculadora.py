def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def calculadora(a, b):
    return (soma(a, b), subtracao(a, b), multiplicacao(a, b), divisao(a, b))

n1 = int(input("Digite o número 1: "))
n2 = int(input("Digite o número 2: "))

print(calculadora(n1, n2))
