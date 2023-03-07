import sys
import adivinhacao
import forca

print('-' * 17)
print('ESCOLHA SEU JOGO\n(1) Forca | (2) Adivinhação')
print('-' * 17)
jogo = int(input('qual jogo? '))
if jogo == 1:
    forca.jogar()
elif jogo == 2:
    adivinhacao.jogar()
else:
    sys.exit()
