'''Um programa que simule o jogo de adivinhação, 
em que o usuário deve tentar adivinhar um número escolhido pelo programa. 
O programa deve informar ao usuário se o número digitado
é maior ou menor do que o número escolhido. 
O jogo deve continuar até que o usuário acerte o número escolhido.
'''

import random

print("*********************************")
print("Bem vindo ao jogo da adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)
tentativas = 0
pontos = 100

print("Escolha uma dificuldade! \n")
print("(1) Fácil, (2) Médio, (3) Difícil \n")

level = int(input("Defina a dificuldade: \n"))
if level == 1:
    tentativas = 20
elif level == 2:
    tentativas = 10
elif level == 3:
    tentativas = 5
else:
    print("Você deve escolher entre 1 a 3. Tente novamente! \n")
    
for rodada in range (1, tentativas + 1):
    print(f"Tentativa {rodada} de {tentativas}!")
    palpite_str = int(input("Digite um número: \n"))
    palpite = int(palpite_str)

    if palpite <1 or palpite > 100:
        print("Você deve escolher um número entre 1 a 100!")
        continue

    correto = palpite == numero_secreto
    maior = palpite > numero_secreto
    menor = palpite < numero_secreto

    if(correto):
        print(f"Parabéns! O número secreto é {numero_secreto}")
        print(f"Sua pontuação é {pontos}")
        break
    else:
        pontos -= 5
        if maior:
            print("O seu palpite foi MAIOR do que o número secreto! Tente novamente! \n")
        elif menor:
            print("O seu palpite foi MENOR que o número secreto! Tente novamente! \n")

print("Fim de jogo!")