from random import randint
from time import sleep
print('''Escolha uma opção:
0) Pedra
1) Papel
2) Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep (0.5)
print('KEN')
sleep(0.5)
print('PO!!''')
sleep(0.5)
print('-='*20)
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(f'O computador jogou ... {itens[computador]}')
print(f'O jogador jogou ... {itens[jogador]}')
print('-='*20)
if computador == 0: #Computador jogou pedra
    if jogador == 0:
        print('Empatou!')
    elif jogador == 1:
        print('O jogador venceu!')
    elif jogador == 2:
        print('O computador venceu!')
    else:
        print('Jogada Inválida!')
elif computador == 1: #Computador jogou papel
    if jogador == 0:
        print('O computador venceu!') 
    elif jogador == 1:
        print('Empatou!')
    elif jogador == 2:
        print('O jogador venceu!')
    else:
        print('Jogada Inválida!')
elif computador == 2: #Computador jogou tesoura
    if jogador == 0:
        print('O jogador venceu!')
    elif jogador == 1:
        print('O computador venceu!')
    elif jogador == 2:
        print('Empatou!')
    else:
        print('Jogada Inválida!')
