"""
Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo.
"""
print('-='*20)
print('ANALISADOR DE TRIANGULO')
print('-='*20)
r1 = float(input('Informe uma reta: '))
r2 = float(input('Informe uma segunda reta: '))
r3 = float(input('Informe uma terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os 3 segmentos, ou retas, formam um triangulo.')
else:
    print('Os 3 segmentos, ou retas, nao formam um triangulo.')

print('-='*20)
print('FIM')
print('-='*20)
