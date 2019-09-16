"""
Crie um programa onde o usuario possa digitar sete valores numericos e cadastre-os em uma lista unica
que mantenha separados os valores pares e impares.
No final, mostre os valores pares e impares em ordem crescente.
"""
from time import sleep

numeros = []
impares = []
pares = []
numeros.append(pares)
numeros.append(impares)

#para declarar uma lista dentro de outra: listas = [[]. []]

for numero in range(0, 7):
    n = int(input('Digite um valor inteiro: '))

    if n % 2 == 0:
        if len(pares) == 0:
            pares.append(n)
        elif n < pares[0]:
            pares.insert(0, n)
        else:
            pares.append(n)
    else:
        if len(impares) == 0:
            impares.append(n)
        elif n < impares[0]:
            impares.insert(0, n)
        else:
            impares.append(n)

print(f'Numeros digitados: {numeros}')
print(f'Pares: {pares}')
print(f'Impares: {impares}')
sleep(1)
impares.sort()
print(f'Impares em ordem crescente: {impares}')
impares.sort(reverse=True)
print(f'Impares em ordem decrescente: {impares}')
pares.sort()
print(f'Pares em ordem crescente: {pares}')
pares.sort(reverse=True)
print(f'Pares em ordem decrescente: {pares}')
