"""
Escreva um programa que leia o salario de um funcionario e calcule o valor do seu aumento.

Para salarios superiores a R$1.250,00, calcule aumento de 10%.

Para os inferiores ou iguais, o aumento e de 15%.
"""

salario = float(input('Informe o salario: R$'))

if salario > 1.250:
    salario_aumento = salario * 1.10 #ou salario_aumento = salario + (salario * 10 / 100)
    print('Seu salario atual e de R${:.2f}, e com 10% de aumento ficara {}.'.format(salario, salario_aumento))
else:
    salario_aumento = salario * 1.15 #ou salario_aumento = salario + (salario * 15 / 100)
    print('Seu salario atual e de R${:.2f}, e com 15% de aumento fica R${}.'.format(salario, salario_aumento))
