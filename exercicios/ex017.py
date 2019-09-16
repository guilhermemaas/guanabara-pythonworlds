"""
Faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule
e mostre o comprimento da hipotenusa.
"""

import math

cateto_oposto = float(input('Informe o comprimento do cateto adjacente do triangulo: '))
cateto_adjacente = float(input('Informe o comprimento do cateto oposto do triangulo: '))

hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
hipotenusa2 = math.hypot(cateto_oposto, cateto_adjacente)

print('O comprimento da hipotenusa e: {:.2f}.'.format(hipotenusa))
print('O comprimento da hipotenusa e: {:.2f}.'.format(hipotenusa2))
