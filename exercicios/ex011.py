"""
Faca um programa que leia a altura e a largura de uma parede, calcule a area, e a quantidade de tinta necessaria para pinta-la,
sabendo que cada litro pinta 2 metros quadrados de tinta.
"""

altura = float(input('Informe quantos metros a parede tem de altura: '))
largura = float(input('Informe quantos metros a parede tem de largura: '))

area = altura * largura
total_tinta = area / 2

print('Area total da parede: {:.2f}m2({}x{}). Serao necessarios {:.1f} litros de tinta.'.format(area, altura, largura, total_tinta))
