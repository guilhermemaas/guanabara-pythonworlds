"""
Faca um programa que tenha uma funcao notas() que pode receber varias notas de alunos e vai retornar um dicionario
com as seguintes informacoes:
- Quantidade de notas
- A maior nota
- A menor nota
- A media da turma
- A situacao(opcional)
Adicione tambem as docstrings da funcao.
"""

def print_rabbit():
    return '(\__/)\n(@.@)'


print('Sistema de calculo de medias')
alunos_notas = []

while True:
    notas = []
    aluno = {}
    nome_aluno = str(input('Informe o nome do aluno:\n'))
    contador_notas = 1
    while True:
        nota = int(input(f'Informe a {contador_notas} do aluno {nome_aluno}:\n'))
        notas.append(nota)
        continuar_adicionando_notas = str(input('Deseja adicionar mais notas de provas S para SIM, N para NAO.\n')).upper().strip()
        if continuar_adicionando_notas == 'N':
            break
        contador_notas += 1
    aluno['nome'] = nome_aluno
    aluno['notas'] = notas
    alunos_notas.append(aluno.copy)
    aluno.clear()
    continuar_adicionando_alunos = str(input('Deseja cadastrar mais alunos? S para SIM, N para NAO.\n')).upper().strip()
    if continuar_adicionando_alunos == 'N':
        break

print('Alunos e notas cadastrados: ')
for indice, aluno in enumerate(alunos_notas):
    print(f'Nome: {aluno["nome"]}.')
    print(print_rabbit())
print('...Finalizando programa...\n')
