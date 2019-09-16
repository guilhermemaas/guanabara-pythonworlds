"""
Desenvolva um programa que leia o primeiro termo e a razao de um PA. No final,
mostre os 10 primeiros termos dessa progressa.
"""

pt = int(input('Infome o primeiro termo para calcular uma PA: '))
r = int(input('Infore uma razao para calcular uma PA: '))

for c in range(pt, pt+10*r, r):
    print('{} -> '.format(c), end='')

print('FIM')