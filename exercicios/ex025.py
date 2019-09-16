"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
"""

nome = input('Digite seu nome completo: ').strip()

nome_em_lista = nome.lower().split()

print('Existe "Silva" no seu nome?')
print('silva' in nome_em_lista)
