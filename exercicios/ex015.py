"""
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
e a quantidade de dias pelos quais foi alugado. Calcule o preco a pagar,
sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.
"""

dias = int(input('Informe quantos dias rodou com o carro: '))
km = float(input('Informe quantos km rodou com o carro: '))

total_a_pagar = (60 * dias) + (0.15 * km)

print('O carro foi alugado por {} dias.\nForam rodados {}km ao todo.\nO total a pagar e: R${}.'.format(dias, km, total_a_pagar))
