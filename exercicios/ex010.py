"""
Crie um programa que leia quanto dinheiro a pessoa tem na carteira, e mostre quantos dolares ela pode comprar.
"""

carteira = float(input('Digite o valor atual em sua carteira: R$'))
dolar = 3.77

print('Voce possui R${:.2f}. Com isso voce pode comprar ${:.2f}.'.format(carteira, carteira / dolar))
print('Voce possui R${}. Com isso voce pode comprar ${}.'.format(carteira, carteira / dolar))

