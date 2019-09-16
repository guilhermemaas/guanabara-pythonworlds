"""
Faca um programa que leia o nome completo de uma pessoa e mostre em seguida o primeiro e o ultimo nome separadamente.
todo arrumar isso depois
"""

nome = str(input('Dige um nome completo: ')).strip().split()

primeiro_nome = nome[0]
len_nome = len(nome)
ultimo_nome = nome[-1]
ultimo_nome2 = nome[len(nome)-1]

#print(len_nome_em_lista)
print(len_nome)

print("""
Nome completo: {}.
Primeiro nome: {}.
Ultimo nome: {}.
Ultimo nome2: {}.
""".format(nome, primeiro_nome, ultimo_nome, ultimo_nome2))


