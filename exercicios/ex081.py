"""
Crie um programa que vai ler varios numeros e colocar em uma lista.
Depois disso, mostre:
A) Quantos numeros foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e esta ou nao na lista.
"""

lista = []
while True:
    lista.append(int(input('Digite um valor: ')))

    continua = ' '
    while continua not in 'SN':
        continua = str(input('Cadastrar mais numeros? [S/N]')).strip().upper()[0]

    if continua == 'N':
        break

print(f'A)QUANTOS NUMEROS: {len(lista)}')
lista.sort(reverse=True)
print(f'B)NUMEROS EM ORDEM DECRESCENTE: {lista}')

if 5 in lista:
    numeroCinco = 'SIM'
else:
    numeroCinco = 'NAO'
print(f'C)SE O VALOR 5 FOI DIGITADO: {numeroCinco}')
