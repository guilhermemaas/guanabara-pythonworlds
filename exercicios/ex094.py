"""
Crie um programa que leia nome, sexo, e idade de varias pessoas, guardando os dados de cada pessoa em um
dicionario e todos os dicionarios em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) A media de idade do grupo.
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da media.
"""

cadastroPessoas = []
totalIdade = 0

while True:
    pessoa = {}

    pessoa['nome'] = str(input('Informe o nome da pessoa: ')).strip().title()
    while True:
        pessoa['sexo'] = str(input('Informe o sexo da pessoa [M][F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Sexos disponiveis: M(Masculino) ou F(Feminino).')

    pessoa['idade'] = int(input('Informe a idade da pessoa: '))
    totalIdade += pessoa['idade']

    cadastroPessoas.append(pessoa.copy())
    pessoa.clear()

    continuar = ' '

    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S][N]: ')).strip().upper()[0]
    if continuar == 'N':
        break

#Lista com todas as mulheres
listaMulheres = []

for cadastro in cadastroPessoas:
    if cadastro['sexo'] == 'F':
        listaMulheres.append(cadastro.copy())

#Lista com pessoas acima da media
mediaIdade = totalIdade / len(cadastroPessoas)
listaPessoasAcimaIdade = []

for cadastro in cadastroPessoas:
    if cadastro['idade'] > mediaIdade:
        listaPessoasAcimaIdade.append(cadastro.copy())

print(f'MEDIA DE IDADE: {mediaIdade}')

print('=' * 20)
print('       EXIBINDO CADASTROS REGISTRADOS')
print('=' * 20)
print(f'A media de idade foi: {mediaIdade:5.2f}')
print('=' * 20)
for indice, cadastro in enumerate(cadastroPessoas):
    print(f'Cadastro{indice + 1} - {cadastro}')
print('=' * 20)
print(f'Foram cadastradas ao todo {len(cadastroPessoas)}.')
print('=' * 20)
print('Lista de Mulheres cadastradas:', end='')
for mulher in listaMulheres:
    print(f'Nome: {mulher["nome"]} - Idade: {mulher["idade"]}.', end='')
print('')
print('=' * 20)
print('Lista com todas as pessoas com idade acima da media:')
for pessoa in listaPessoasAcimaIdade:
    print(f'Nome: {pessoa["nome"]} - Idade: {pessoa["idade"]} - Sexo: {pessoa["sexo"]}.')
print('=' * 20)
