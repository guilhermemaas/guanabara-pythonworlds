"""
Crie um programa que leia o nome de uma cidade e diga se ela comeca ou nao com o nome "Santo"
"""

cidade = str(input('Digite um nome de uma cidade: '))
cidade_lista = cidade.lower().strip().split()

print('A cidade digitada foi {}. Existe "Santo" no nome dela? '.format(cidade))
print(cidade_lista)
print('santo' in cidade_lista[0])
