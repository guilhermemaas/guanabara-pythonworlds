"""
Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.

A multa vai custar R$7,00 por cada km acima do limite.
"""

velocidade = int(input('Infome a velocidade do carro: '))

if velocidade > 80:
    print('\033[31mVoce foi multado. E sua multa e: {:.2f}!\033[m'.format((velocidade-80)*7))
else:
    print('\033[32mParabens, voce esta andando abaixo do limite!\033[m')