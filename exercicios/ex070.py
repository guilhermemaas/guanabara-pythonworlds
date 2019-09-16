"""
Crie um programa que leia o nome e o preco de varios produtos.
O programa devera perguntar se o usuario vai continuar.
No final, mostre:
A) Qual e o total gasto na compra.
B) Quantos produtos custam mais de R$1.000.
C) Qual e o nome do produto mais barato.
"""

print('=.='*20)
print(' '*5+'Cadastro de produtos')
print('=.='*20+'\n')

totalGasto = 0
produtosMaisMil = 0
produtoMaisBarato = 0
nomeProdutoMaisBarato = ''
count = 0

while True:
    p = str(input('Informe o nome de um produto: ')).strip().upper()
    v = float(input('Informe o valor de um produto: '))

    if count == 0 or v < produtoMaisBarato:
        produtoMaisBarato = v
        nomeProdutoMaisBarato = p

    if v > 1000:
        produtosMaisMil += 1

    totalGasto += v
    count += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja cadastrar mais produtos? S para SIM, N para NAO: ')).strip().upper()[0]

    if continuar == 'N':
        break

print(f"""
TOTAL GASTO {totalGasto:.2f}.
PRODUTOS ACIMA DE 1.000 REAIS: {produtosMaisMil}.
PRODUTO MAIS BARATO: {nomeProdutoMaisBarato}.
""")
