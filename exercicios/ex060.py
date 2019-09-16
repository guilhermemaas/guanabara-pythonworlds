"""
Faca um programa que leia um numero qualquer e mostre o seu fatorial.

Ex:
5! = 5x4x3x2x1 = 120
.
"""
import math

#com lib math
print('Calculo de fatorial')
n = int(input('Informe um numero inteiro: '))

print('O fatorial de {} e {}.'.format(n, math.factorial(n)))

#com for
n = int(input('Informe um numero inteiro: '))
total = 0
for c in range(n-1, 0, -1):
    total = n * c
    n = total

print(total)

#com while
n = int(input('Informe um numero inteiro: '))
total = 0

multiplicador = n-1
print(multiplicador)
while multiplicador > 1:
    total = n * multiplicador
    multiplicador += -1
    n = total

print(total)


####Guanabara:

n = int(input('Digite um numero para calcular seu fatorial: '))
c = n
f = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('\nO Fatorial de {} e {}.'.format(n, f))