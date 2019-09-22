"""
Faça um programa que tenha uma função chamada area(), que receba as dimensoes de um terreno retangular(largura e comprimento)
e mostre a área do terreno
"""

def area(largura, comprimento):
    return largura * comprimento

largura = 5
comprimento = 10

print(f'Largura: {largura}m. Comprimento: {comprimento}. ', end='')
print(f'Área: {area(largura, comprimento)}.')

