"""
Crie um programa que leia o numero e mostre o seu dobro, o seu triplo, e a sua raiz quadrada.
"""

n = int(input('Digite um numero para calcular o dobro, o triplo e a raiz quadrada: '))
d = n * 2
t = n * 3
r = n ** (1/2)

print('O numero digitado foi: {}.\nO dobro do numero e {}.\nO triplo e {}.\nA raiz quadrada e {:.2f}'.format(n, d, t, r))



