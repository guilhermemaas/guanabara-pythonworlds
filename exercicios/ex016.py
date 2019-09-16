"""
Faca um programa que leia um numero real e retorne a parte inteira deste
"""
from math import trunc

num = float(input('Informe um numero real: '))

print('A parte inteira de {} e {}.'.format(num, int(num)))
print('A parte inteira de {} e {}.'.format(num, trunc(num)))