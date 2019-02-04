print('******************************')
print('*    Jogo da adivinhação     *')
print('******************************')

total_de_pontos = 1000
numero_secreto = 42
nivel = int(input("Digite um nível de dificuldade (1, 2, 3): "))

while nivel not in (1, 2, 3):
    print('Você digitou um nível indisponível!')
    nivel = int(input("Digite um nível de dificuldade (1, 2, 3): "))

if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
elif nivel == 3:
    total_de_tentativas = 5
    
for rodada in range(1, total_de_tentativas + 1):
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
    
    chute = int(input('Digite o seu número: '))
    print('Você digitou: ', chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
        break
    elif (maior):
        print("Você errou! O seu chute foi maior que o número secreto")
    elif (menor):
        print('Você errou! O seu chute foi menor que o número secreto')
    total_de_pontos -= abs(chute - numero_secreto)

    rodada = rodada + 1

print("Você ganhou {} pontos!".format(total_de_pontos))
print('Fim do jogo')
