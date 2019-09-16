"""
Crie um programa que leia um numero inteiro e mostre na tela se ele [e par ou impar.
"""

num = int(input('Informe um numero para validar se par ou impar: '))

if num % 2 == 0:
    print('O numero {} e par.'.format(num))
else:
    print('O numero {} e impar.'.format(num))

