"""
Escreva um programa que pergunte a distancia de uma viagem em km.
Calcule o preco da passagem, cobrando R$0,50 por km para viagens ate 200km e R$0,45 para viagens mais longas.
"""

distancia = float(input('Qual a distancia da sua viagem? '))

print('Voce esta prestes a comecar uma viagem.')

preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
"""
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
"""
print('E ela custara R${:.2f}.'.format(preco))

