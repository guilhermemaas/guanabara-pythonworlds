"""
Faça um programa que tenha uma função chamada area(), que receba as dimensoes de um terreno retangular(largura e comprimento)
e mostre a área do terreno
"""

def area(largura, comprimento):
    return largura * comprimento


print('Controle de Terrenos')
print('_' * 20)

largura = float(input('LARGURA(m): '))
comprimento = float(input('COMPRIMENTO(m): '))

print(f'Largura: {largura}m. Comprimento: {comprimento}m. ', end='')
print(f'Área: {area(largura, comprimento)}m.')

