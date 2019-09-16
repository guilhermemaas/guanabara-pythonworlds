"""
Faca um programa que calcule a soma entre todos os numeros impares que sao
multiploes de 3 que se encontram no intervalo de 1 ate 500.
"""

count = 0
soma = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 != 0:
        print(c, end=' ')
        count += 1
        soma += c
print('\nA soma de todos os valores impares entre 1 e 500 e {}.'.format(soma))
print('\nO total de numeros impares entre 1 e 500 e {}.'.format(count))
