"""
Faca um programa que leia um ano qualquer e mostre se ele [e bissexto.
"""
from datetime import date

ano = int(input('Informe um ano: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 and ano % 400 == 0:
    print('O ano {} e bissexto.'.format(ano))
else:
    print('O ano {} nao e bissexto.'.format(ano))
