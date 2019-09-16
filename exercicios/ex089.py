"""
Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta. No final, mostre
um boletim contendo media de cada um e permita que o usuario possa mostrar as notas de cada aluno individualmente.
"""

print('*' * 30)
print(' ' * 5 + 'CADASTRO DE NOTAS')
print('*' * 30)

aluno = []
bimestre = []

while True:
    nome = str(input('Informe o nome do aluno: ')).strip().title()
    nota1 = float(input('Informe a primeira nota: '))
    nota2 = float(input('Informe a segundan nota: '))
    media = (nota1 + nota2) / 2
    aluno.append(nome)
    aluno.append(nota1)
    aluno.append(nota2)
    aluno.append(media)

    bimestre.append(aluno[:])
    aluno.clear()

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja cadastrar notas de mais alunos? [S][N] ')).upper()[0]

    if continuar == 'N':
        break

print('*' * 30)
print(' ' * 5 + 'NOTAS DO BIMESTRE')
print('*' * 30)

for indice, aluno in enumerate(bimestre):
    if aluno[3] >= 7:
        situacao = 'Aprovado'
    else:
        situacao = 'Reprovado'

    print(f'Aluno {indice+1}: {aluno[0]} | Nota 01: {aluno[1]} | Nota 02: {aluno[2]} | Media: {aluno[3]} | Situacao: {situacao}')
print('*' * 30)

while True:
    visualizar = ' '

    while visualizar not in 'SN':
        visualizar = str(input('Deseja visualizar algum cadastro em especifico? [S][N]')).strip().upper()[0]

    if visualizar == 'N':
        break

    cadastroAluno = int(input('Informe o codigo do aluno: '))

    print(bimestre[cadastroAluno-1])
    print('*' * 30)

print('*' * 30)
