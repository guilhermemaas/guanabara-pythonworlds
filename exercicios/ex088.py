"""
Faca um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serao gerados e vai sortear 6 numeros
entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta
"""
from random import randint
print('*' * 30)
print(' ' * 6 + 'SORTEIO DE NUMEROS PARA MEGA SENA')
print('*' * 30)

qtJogos = int(input('\nQuantos jogos deseja Jogar? '))

jogosMega = []
numeros = []
totalSorteados = 0

for jogos in range(0, qtJogos):
    while totalSorteados < 6:
        numero = randint(1, 60)
        if numero not in (numeros):
            numeros.append(numero)
            totalSorteados += 1

    jogosMega.append(numeros[:])
    numeros.clear()
    totalSorteados = 0

for jogos in range(0, len(jogosMega)):
    jogosMega[jogos].sort()
    print(f'Jogo [{jogos+1}] - {jogosMega[jogos]}')

for indice, jogo in enumerate(jogosMega):
    jogosMega[indice].sort()
    print(f'Jogo {indice+1}: {jogo}')