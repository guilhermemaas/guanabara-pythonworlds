"""
Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestacao mensal, sabendo que ele nao pode exceder 30% do salario ou entao
o emprestimo e negado.
"""
print('='*50+'\n\033[4;31mVALIDACAO DE APROVACAO DE CREDITO\033[m\n'+'='*50+'\n\033[34mInforme os dados abaixo:\033[m')

continua_cadastro = 1
cadastro = []

while continua_cadastro != 0:
    aprovado = False

    nome = str(input('\nInforme o nome do cliente: ')).strip()
    valor_imovel = float(input('\nInforme o valor do imovel: '))
    salario = float(input('\nInforme o salario do cliente: '))
    meses = int(input('\nInforme em quantos meses sera realizado o pagamento: '))

    maximo_mensal_permitido = (salario * 30) / 100
    valor_mes = valor_imovel / meses

    if valor_mes < maximo_mensal_permitido:
        print('\033[32mCREDITO APROVADO!\033[m Pagamento ficara: R${:.2f} em {}X, totalizando R${}.\n'.format(valor_mes,
            meses, valor_imovel))
        aprovado = True
    else:
        print('\033[31mCREDITO REPROVADO!\033[m O valor mensal de R${:.2f} excede o valor maximo ao mes de '
              'R${:.2f} ao mes.\n'.format(valor_mes, maximo_mensal_permitido))

    cadastro.append([nome, valor_imovel, salario, meses, valor_mes, aprovado])

    continua = int(input('\nDeseja realizar outro cadastro? 1 - SIM | 2 - NAO\n'))

    if continua == 1:
        continua_cadastro = 1
    else:
        continua_cadastro = 0

print('='*50+'\nFIM DO CADASTRO\n'+'='*50)
print('\nOS CADASTROS REALIZADOS FORAM:\n')
print(cadastro)
