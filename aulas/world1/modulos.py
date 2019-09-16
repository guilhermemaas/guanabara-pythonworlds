"""
import math
ceil - Arredondar para cima
floor - Arredondar para baixo
trunc - Truncar um valor
pow - potencia (**)
sqrt - rais quadrada
factorial - calcular fator

import math
#from math import sqrt

num = int(input('Digite um numero para calcular sua raiz quadrada: '))
raiz = math.sqrt(num)
print('A raiz quadrada de {} e {}.'.format(num, raiz))

num2 = int(input('Digite um numero para calcular sua raiz quadrada: '))
raiz2 = math.sqrt(num2)
print('A raiz quadrada de {} e {}.'.format(num2, math.ceil(raiz2)))

num3 = int(input('Digite um numero para calcular sua raiz quadrada: '))
raiz3 = math.sqrt(num3)
print('A raiz quadrada de {} e {}.'.format(num3, math.floor(raiz3)))

num4 = int(input('Digite um numero para calcular sua raiz quadrada: '))
raiz4 = math.sqrt(num4)
print('A raiz quadrada de {} e {:.2f}.'.format(num4, raiz4))


import random

num = random.random()
num2 = random.randint(1, 10)
print(num)
print(num2)
"""

import emoji

print(emoji.emojize('Teste de emoji :crocodile:', use_aliases=True))
