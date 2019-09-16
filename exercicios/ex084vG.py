"""
Faca um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""

pessoas = []
pessoa = []
maiorPeso = menorPeso = 0

while True:
    pessoa.append(str(input('Digite o nome de uma pessoa: ')))
    pessoa.append(float(input('Digite o peso de uma pessoa: ')))
    pessoas.append(pessoa[:])
    if len(pessoas) == 1:
        maiorPeso = menorPeso = pessoa[1]
    else:
        if pessoa[1] > maiorPeso:
            maiorPeso = pessoa[1]
        elif pessoa[1] < menorPeso:
            menorPeso = pessoa[1]
    pessoa.clear()

    continuar = str(input('Deseja continuar? [S, N]: '))

    if continuar in 'Nn':
        break

print(f'Pessoas cadastradas: {pessoas}')
print(f'Total de pessoas cadastradas: {len(pessoas)}')
print(f'Pessoas com mais peso: ', end='')
for indice in range(0, len(pessoas)):
    print(f'validando pessoa {indice}')
    if pessoas[indice][1] == maiorPeso:
        print(f'{pessoas[indice][0]}', end='')
print(f'\nPessoas menor peso: ', end='')
for indice in range(0, len(pessoas)):
    print(f'validando pessoa {indice}')
    if pessoas[indice][1] == menorPeso:
        print(f'{pessoas[indice][0]}', end='')
print('\nFIM')

print('Pessoas com maior peso: ', end='')
for pessoa in pessoas:
    if pessoa[1] == maiorPeso:
        print(f'{pessoa[0]}, ', end='')
print('.')

print('Pessoas com menor peso: ', end='')
for pessoa in pessoas:
    if pessoa[1] == menorPeso:
        print(f'{pessoa[0]}, ', end='')
print('.')