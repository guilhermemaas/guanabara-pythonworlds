"""
Crie um programa onde o usuario possa digitar sete valores numericos e cadastre-os em uma lista unica
que mantenha separados os valores pares e impares.
No final, mostre os valores pares e impares em ordem crescente.
"""

numeros = []
totalPares = 0
totalImpares = 0
#ePar = True

for indice in range(0, 7):
    n = int(input('Digite um numero inteiro: '))

    if len(numeros) == 0:
        numeros.append(n)
    elif n % 2 == 0:
        numeros.insert(len(numeros), n)
    else:
        numeros.insert(0, n)
    """
        ePar = True
    else:
        ePar = False

    if ePar == True:
        numeros.insert(len(numeros), n)
    else:
        numeros.insert(0, n)
    """

print(f'Segue numeros digitados, separados pares de impares: {numeros}.')
numeros.sort()
print(f'Segue numeros digitados em ordem crescente: {numeros}.')
numeros.sort(reverse=True)
print(f'Segue numeros digitados em ordem decrescente: {numeros}.')


