"""
Faça um programa que tenha uma lista chamada numeros e duas funções chamadas sorteia() e somaPar(). A primeira
função vai sortear 5 númerose e vai colocá-los dentro de uma lista e a segunda função vai mostrar a soma entre todos
os valores PARES sorteados pela função anterior.
"""
from random import randint
from time import sleep

def imprime_linha(quantidade):
    print(f'=' * quantidade)

def monta_titulo(titulo):
    total_caracteres = len(titulo)
    imprime_linha(total_caracteres + 10)
    print(f'{" " * 5}' + f'{titulo}')
    imprime_linha(total_caracteres + 10)

def sortear_numeros():
    numeros_sorteados = []
    contador = 0
    while contador != 5:
        numero_sorteado = randint(0, 100)
        numeros_sorteados.append(numero_sorteado)
        print(f'Primeiro numero sorteado foi: {numero_sorteado}')
        contador += 1
    return(numeros_sorteados)

def somar_pares(numeros):
    soma_par = 0
    for valor in numeros:
        if valor % 2 == 0:
            print(f'{valor} e um par. Sera somado.')
            print('-')
            soma_par += valor
    return soma_par


monta_titulo('SORTEIO DE NUMEROS')
numeros_sorteados = sortear_numeros()
sleep(1)
monta_titulo('SOMA DE NUMEROS PARES')
print(f'A soma de todos os pares foi: {somar_pares(numeros_sorteados)}')
monta_titulo('FIM DO PROGRAMA')




