import random
import sys


def jogar():
    print('-' * 39)
    print('seja bem vindo ao jogo de adivinhação'.upper())
    print('-' * 39)

    numero_secreto = random.randint(1, 15)
    #  tentativas = 0
    pontos = 100
    print('(F)ácil (M)édio (D)ifícil')
    nivel = input('Defina a Dificuldade: '.upper()).upper()

    if nivel == 'F':
        tentativas = 15

    elif nivel == 'M':
        tentativas = 10

    elif nivel == 'D':
        tentativas = 5

    else:
        print('Error: você não digitou uma dificuldade válida')
        sys.exit()
    print(numero_secreto)
    for rodadas in range(1, tentativas + 1):

        print(f'rodada {rodadas} de {tentativas}')
        chute = int(input('digite seu número: '))
        # print('Você Digitou', chute)

        if chute < 0 or chute > 15:
            print('Error: digitou um número inválido')
            continue

        maior = chute > numero_secreto
        menor = chute < numero_secreto
        acertou = chute == numero_secreto

        if acertou:
            print('você acertou e fez {} pontos'.format(pontos).upper())
            #  print('O número secreto é', numero_secreto)
            break
        elif menor:
            print('Você errou, o número secreto é MAIOR que o chute')
            # print('O número secreto era', numero_secreto)
        elif maior:
            print('Você errou, o numero secreto é MENOR que o chute')
            #  print('O número secreto era', numero_secreto)

        pontos_perdidos = abs(chute - numero_secreto)
        pontos = pontos - pontos_perdidos

    print('-' * 20)
    print('FIM DE JOGO\nSUA PONTUAÇÃO: {}'.format(pontos))
    print('-' * 20)


if __name__ == "__main__":
    jogar()
