"""
Faca um algoritmo que leia o salario, e que exiba-o com 15% de aumento.r
"""

salario = float(input('Informe seu salario: '))
salario_final = salario + (salario * 4 / 100)

print('Seu salario com aumento de 15% fica: {:.2f}.'.format(salario_final))
