"""
Faca um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e menor peso lido.
"""

lista_pesos = []

for c in range(0, 5):
    peso = float(input('Informe o peso da pessoa: '))
    lista_pesos.append(peso)

print('MAIOR PESO: {:.2f}.\nMENOR PESO: {:.2f}.'.format(max(lista_pesos), min(lista_pesos)))





