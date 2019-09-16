"""
Faca um algoritmo que leia o preco de um produto e informe o seu novo preco com desconto.
desconto = ((5/100)*900)/100
produto = 900 - desconto
print(produto)
"""

preco_produto = float(input('Informe o valor do produto: R$'))
valor_final = preco_produto - (preco_produto * 5 / 100)


print('Preco final do produto e R${:.2f}.'.format(valor_final))
