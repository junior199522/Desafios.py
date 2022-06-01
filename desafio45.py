from random import randint
from time import sleep

itens = ('pedra', 'papel', 'tesoura')
computador = randint(0,2)
print('Sua opções \n[ 0 ] Pedra \n[ 1 ] Papel \n[ 2 ] Tesoura')
jogador = int(input('Qual sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 20)
print('Computador escolheu: {}'.format(itens[computador]))
print('Jogador escolheu: {}'.format(itens[jogador]))
print('-=' * 20)

if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador ganhou!!!')
    elif jogador == 2:
        print('Maquina ganhou!!!')

elif computador == 1:
    if jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador ganhou!!!')
    elif jogador == 0:
        print('Maquina ganhou!!!')

elif computador == 2:
    if jogador == 2:
        print('Empate')
    elif jogador == 0:
        print('Jogador ganhou!!!')
    elif jogador == 1:
        print('Maquina ganhou!!!')




