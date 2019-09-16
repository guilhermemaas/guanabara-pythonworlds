"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
cadastre-os(com idade) em um dicionario, se por acaso o CTPS for diferente
de ZERO, o dicionario recebera tambem o ano de contratacao e o salario.
Calcule e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar.
Considerar 35 anos de contribuicao para se aposentar
"""
from datetime import datetime

funcionarios = []
pessoa = {}

while True:
    pessoa['nome'] = str(input('Informe o nome da pessoa: ')).strip()
    nascimento = int(input('Informe a data de nascimento: '))
    pessoa['idade'] = datetime.now().year - nascimento
    pessoa['ctps'] = int(input('Informe o numero da carteira de trabalho (0 se nao tiver): '))

    if pessoa['ctps'] != 0:
        pessoa['ano_contratacao'] = int(input('Informe o ano da contratacao: '))
        pessoa['salario'] = float(input('Informe o seu salario: '))
        pessoa['aposentadoria'] = pessoa['idade'] + (35 - (datetime.now().year - pessoa['ano_contratacao']))

    funcionarios.append(pessoa.copy())

    continuar = ' '

    while continuar not in 'SsNn':
        continuar = str(input('Deseja cadastrar mais pessoas? [S]/[N]: ')).strip()[0]

    if continuar in 'Nn':
        break

print(funcionarios)
print('='*30)
print('PROCESSANDO DADOS')

for pessoa in funcionarios:
    print(pessoa)
    print('')