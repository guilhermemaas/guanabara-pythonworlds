"""
Elabore um programa que calcule o valor a ser pago por um produto, considere o seu preco normal e condicoes de pagamento:
- A vista dinheiro/cheque: 10% de desconto.
- A vista no cartao: 5% de desconto.
- Em ate 2x no cartao: Preco normal.
- 3x ou mais no cartao: 20% de juros.
"""

print('Calculo de produto em condicoes de pagamento.')

valor_original = float(input('Informe o valor original do produto: '))
forma_pagamento = int(input('Informe o metodo de pagamento\n1 - A VISTA: DINHEIRO OU CHEQUE COM 10% DE DESCONTO.'
                            '\n2 - A VISTA NO CARTAO COM 5% de DESCONTO.\n3 - EM ATE 2X NO CARTAO COM PRECO NORMAL.'
                            '\n4 - 3 X OU MAIS NO CARTAO COM 20% DE JUROS.\n'))

if forma_pagamento == 1:
    valor_final = valor_original - (valor_original * 10) / 100
elif forma_pagamento == 2:
    valor_final = valor_original - (valor_original * 5) / 100
elif forma_pagamento == 3:
    valor_final = valor_original
elif forma_pagamento == 4:
    valor_final = valor_original + (valor_original * 20) / 100

print('O Valor original do produto e: R${:.2f}.\nO valor final do produto ficou: R${:.2f}.'.format(valor_original,
                                                                                                   valor_final))
