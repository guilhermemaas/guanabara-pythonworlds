"""
Um professor quer sortear um dos seus 4 alunos para apagar o quadro. Faca um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

lista_de_alunos = []
total_alunos = 0

while total_alunos < 4:
    print(lista_de_alunos)
    lista_de_alunos.append(input('Digite o nome de um aluno: '))
    total_alunos = total_alunos + 1
    print(total_alunos)

print(random.choice(lista_de_alunos))

"""

import random

n1 = str(input('Informe o nome do primeiro aluno: '))
n2 = str(input('Informe o nome do segundo aluno: '))
n3 = str(input('Informe o nome do terceiro aluno: '))
n4 = str(input('Informe o nome do quarto aluno: '))
alunos = [n1, n2, n3, n4]

print(random.choice(alunos))

