"""
Faca um programa que leia 5 valores numericos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as
suas respectivas posicoes na lista.
"""

print('INFORME 5 NUMEROS:\n')

numeros = [] #ou list()
maiorNumero = 0
menorNumero = 0

for numero in range(0, 5):
    numeros.append(int(input(f'Informe o {numero+1} para adiciona-lo a lista na posicao {numero}: ')))
    print(f'Indice atual de {numeros[numero]}: {numero}.')

    if numero == 0:
        maiorNumero = menorNumero = numeros[numero]
    else:
        if numeros[numero] > maiorNumero:
            maiorNumero = numeros[numero]

        if numeros[numero] < menorNumero:
            menorNumero = numeros[numero]

    print(f'VOCE DIGITOU: {numeros} ate agora.')

    if numero > 0:
        print(f'O maior numero ate agora: {maiorNumero}. Seu indice: {numeros.index(maiorNumero)}')
        print(f'O menor numero ate agora: {menorNumero}. Seu indice: {numeros.index(menorNumero)}')

print(f"""\n
VOCE DIGITOU: \033[33;m{numeros}\033[m
O MAIOR NUMERO DA LISTA: \033[31;m{max(numeros)}. Seu primeiro indice: {numeros.index(max(numeros))}\033[m
O MAIOR NUMERO {maiorNumero} aparece nos seguintes indices:
""", end='')
for indice, valor in enumerate(numeros):
    if valor == maiorNumero:
        print(f'{indice}...', end='')
print('fim')

print(f'O MENOR NUMERO DA LISTA: \033[32;m{min(numeros)}. Seu primeiro indice: {numeros.index(min(numeros))}\033[m')
print(f'O MENOR NUMERO {menorNumero} aparece nos seguintes indices:')
for indice, valor in enumerate(numeros):
    if valor == menorNumero:
        print(f'{indice}...', end='')
print('fim')
