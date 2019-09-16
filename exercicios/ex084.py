"""
Faca um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""

pessoas = []
pessoa = []

while True:
    pessoa.append(str(input('Informe o nome: ')).strip().upper())
    pessoa.append(float(input('Informe o peso: ')))
    pessoas.append(pessoa[:])
    pessoa.clear()
    continuar = str(input('Deseja cadastrar mais pessoas? [S],[N]'))
    if continuar not in 'Ss':
        break

peso_total = 0

for cadastro in pessoas:
    print(f'Nome: {cadastro[0]}, Peso:{cadastro[1]}')
    peso_total += cadastro[1]
    print(peso_total)

media_peso = peso_total/len(pessoas)

pessoasPesadas = []
pessoasLeves = []

for cadastro in pessoas:
    if cadastro[1] > media_peso:
        pessoasPesadas.append(cadastro[0])
    else:
        pessoasLeves.append(cadastro[0])


print(f'Pessoas cadastradas: {pessoas}.')
print(f'Quantidade de pessoas cadastradas: {len(pessoas)}')
print(f'A media de peso da galera e: {media_peso}')
print(f'Lista de pessoas mais pesadas: {pessoasPesadas}')
print(f'Lista de pessoas mais leves: {pessoasLeves}')

