"""
Escreva um programa que faca o computador "pensar" em um numero inteiro entre 0 e 5 e peca para o usuario tentar
descobrir qual foi o numero escolhido pelo computador.

O programa devera escrever na tela se o usuario perdeu ou vence.
"""
from random import *

print('Sorteando num numero.')

num = randint(0, 9)
#print(num)

if input('Digite um numero para tentar adivinhar: ') == num:
    print('Voce acertou =)')
else:
    print('Voce errou. =(, o numero certo e {}.'.format(num))
