"""
Faca um programa que leia um angulo qualquer e mostre na tela o valor de seno, cosseno, e tangente desse angulo.
"""

import math

cateto_oposto = float(input('Informe o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Informe o comprimento do cateto adjacente: '))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
seno = cateto_oposto / hipotenusa
cosseno = cateto_adjacente / hipotenusa
tangente = cateto_oposto / cateto_adjacente

print('O valor do cateto oposto e {}.\nO valor do cateto adjacente e {}.\nO valor da hipotenusa e {}.'.format(cateto_oposto, cateto_adjacente, hipotenusa))
print('O valor do seno e {}.\nO valor do cosseno e {}.\nO valor da tangente e {}.'.format(seno, cosseno, tangente))

angulo = float(input('Informe um angulo para calcuar seu seno, cosseno, tangente'))
seno = math.asin(math.radians(angulo))
cosseno = math.acos(math.radians(angulo))
tangente = math.atan(math.radians(angulo))

print('Angulo informado: {}.\nO seno e {:.2f}. O cosseno e {:.2f}. E a tangente e{:.2f}.'.format(angulo, seno, cosseno, tangente))