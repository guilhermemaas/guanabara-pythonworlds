"""
Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla
Depois disso, mostre a listagem de numeros gerados e tambem indique o
menor e o maior valor que estao na tupla.
"""
from random import randint

numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10),
           randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10),
           randint(0, 10), randint(0, 10))

print(f'Numeros sorteados: {numeros}')
print(f'Maior: {max(numeros)}')
print(f'Menor: {min(numeros)}')
