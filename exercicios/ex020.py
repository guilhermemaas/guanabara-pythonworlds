"""
O mesmo professor do exercicio anterior quer sortear a ordem de apresentacao de trabalho dos alunos.Faca um programa
que leia o nome dos quatro alunos e mostre a ordem sorteada
"""
import random

lista_de_alunos = []
total_alunos = 0

while total_alunos < 4:
    print(lista_de_alunos)
    lista_de_alunos.append(input('Digete um nome de aluno: '))
    total_alunos = total_alunos + 1
    print(total_alunos)

names = random.sample(lista_de_alunos, 4)
ordem_alunos = random.shuffle(lista_de_alunos)
print(names)
print(ordem_alunos)





