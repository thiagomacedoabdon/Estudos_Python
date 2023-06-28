from random import randint
from time import sleep

print('{:=^40}'.format(' VAMOS JOGAR??? '))
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Escolha sua opção: 
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual a sua jogada? '))

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(0.5)

print('-='*11)
print('O computador escolheu {}.'.format(itens[computador]))
print('Jogador escolheu {}.'.format(itens[jogador]))
print('-='*11)

if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador venceu')
    elif jogador == 2:
        print('Computador venceu')
    else:
        print('Jogada inválida!')
elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print('Computador venceu')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador venceu')
    else:
        print('Jogada inválida!')
elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        print('Jogador venceu')
    elif jogador == 1:
        print('Computador venceu')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada inválida!')
