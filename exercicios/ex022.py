"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiusculas
O nome com todas as letras minusculas
Quantas letras ao todo sem considerar espacos
Quantas letras tem o primeiro nome
"""

nome_completo = input('Digite seu nome completo: ').strip() #Pra pegar ja sem espacos no comeco e no fim
maiusculas = nome_completo.upper()
minusculas = nome_completo.lower()
letras_sem_espacos = len(nome_completo.replace(' ', ''))
letras_sem_espacos2 = len(nome_completo) - nome_completo.count(' ')
nome_em_lista = nome_completo.split()
tamanho_primeiro_nome = len(nome_em_lista[0])
tamanho_primeiro_nome2 = nome_completo.find(' ') #O find encontra a posicao do primeiro espaco, logo mostra o tamanho do primeiro nome antes deste.

print("""
Seu nome em minusculuas: {}.
Seu nome em maiusculas: {}.
Seu nome possui {} letras sem considerar espacos.
Seu nome possui {} letras sem considerar espacos.
Seu primeiro nome tem {} letras.
Seu primeiro nome tem {} letras.
""".format(maiusculas, minusculas, letras_sem_espacos, letras_sem_espacos2, tamanho_primeiro_nome, tamanho_primeiro_nome2))


