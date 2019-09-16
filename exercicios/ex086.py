"""
Crie um programa que crie uma matriz de dimensao 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatacao correta.
"""

matriz = [[], [], []]

contador = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[contador].append(int(input('Digite um numero inteiro: ')))
    contador += 1

for linha in range(0, len(matriz)):
    for coluna in range(0, 3):
        print(f'[ {matriz[linha][coluna]} ]', end='')
    print()

matriz2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para {linha}, {coluna}: '))

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

