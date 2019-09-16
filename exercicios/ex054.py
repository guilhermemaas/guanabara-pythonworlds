"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ja atingiram a maioridade, e quantas ainda nao atingiram. Considerar 21 anos.
"""
from datetime import date

print('INFORME A DATA de NASCIMENTO DE 7 PESSOAS:')

ano_corrente = date.today().year
total_maiores = 0
total_menores = 0

for c in range(1, 8):
    dn = int(input('Informe a data de nascimento da {} pessoa: '.format(c)))
    if ano_corrente - dn < 21:
        total_menores += 1
    else:
        total_maiores += 1

print('MAIORES: {}.\nMENORES: {}.'.format(total_maiores, total_menores))
