"""
Faca um programa que jogue par ou impar com o computador
O jogo sera interrompido quando o jogador PERDER.
Mostrando o total de vitorias consecutivas que ele conquistou no final do jogo
"""
from random import randint

print('\033[2;34;m====Jogo do Par ou Impar====\033[m\n')

vencedor = jogador = bot = ''
cont = 0

while True:
    dedosbot = randint(1, 11)
    opcaojogador = str(input('Informe Par ou Impar [P/I]:' )).strip().upper()[0]
    if opcaojogador in ('IP'):
        dedosjogador = int(input('Informe um numero para jogar, de 1 a 10: '))

        if opcaojogador == 'P':
            opcaobot = 'I'
        else:
            opcaojogador = 'I'
            opcaobot = 'P'

        if (dedosjogador + dedosbot) % 2 == 0 and opcaojogador == 'P':
            vencedor = 'Jogador'
            #print(f'DEBUG - VENCEDOR: {vencedor}')
        elif (dedosjogador + dedosbot) % 2 == 1 and opcaojogador == 'I':
            vencedor = 'Jogador'
            #print(f'DEBUG - VENCEDOR: {vencedor}')
        elif (dedosjogador + dedosbot) % 2 == 0 and opcaobot == 'P':
            vencedor = 'Bot'
            #print(f'DEBUG - VENCEDOR: {vencedor}')
        elif (dedosjogador + dedosbot) % 2 == 1 and opcaobot == 'I':
            vencedor = 'Bot'
            #print(f'DEBUG - VENCEDOR: {vencedor}')

        print(f'\nBOT ESCOLHOU: {dedosbot}.({opcaobot})')
        print(f'VENCEDOR: {vencedor}.')

        if vencedor == 'Bot':
            break

        cont += 1
    else:
        print('Opcao invalida, digite novamente, P para par, ou I para Impar: ')
        pass

print('\n\033[31;mFIM\033[m')
print(f'Voce teve {cont} vitorias antes de perder.')
