"""
Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla
Depois disso, mostre a listagem de numeros gerados e tambem indique o
menor e o maior valor que estao na tupla.
"""
from time import sleep
from random import randint

print('...\n')
sleep(0.5)
print('GERANDO NUMEROS ALEATORIOS\n')

numeros = []

for count in range(0, 5):
    numeros.append(randint(0, 11))

tupla_numeros = numeros

sleep(0.5)
print('...\n')

print(f'\033[31;mNUMEROS ALEATORIOS SELECIONADOS: \033[m\033[33;m{tupla_numeros}\033[m')

print(f"""
O MAIOR NUMERO: {max(tupla_numeros)}
O MENOR NUMERO: {min(tupla_numeros)}
""")