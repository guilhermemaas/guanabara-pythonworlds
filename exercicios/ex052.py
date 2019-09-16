"""
Faca um programa que leia um numero inteiro e diga se ele e ou nao um numero primo.
"""

n = int(input('Informe um numero inteiro: '))
cont = 0

for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        cont += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')

print('\n\033[mO numero {} foi divisivel {} vezes.'.format(n, cont))

if cont == 2:
    print('O numero e primo')
else:
    print('O numero nao e primo.')
