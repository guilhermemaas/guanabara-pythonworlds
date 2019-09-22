"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.

Seu programa tem que analisar todos os valores e dizer qual deles é maior
"""

def maior(numeros):
    maior_numero = 0
    for numero in numeros:
        if numero > maior_numero:
            maior_numero = numero
    return maior_numero

print('DIGITE NUMEROS PARA SABER QUAL O MAIOR: ')

lista_numeros = []
while True:
    lista_numeros.append(int(input('DIGITE UM VALOR:\n')))
    continuar = str(input('DESEJA INFORMAR MAIS NUMEROS? S/N:\n')).upper().strip()
    if continuar == 'N':
        break

print('=' * 20 + f'MAIOR NUMERO:\n {maior(lista_numeros)}.')
