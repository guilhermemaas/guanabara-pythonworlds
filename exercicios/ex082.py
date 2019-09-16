"""
Crie um programa que vai ler varios numeros e colocar em uma lista.

Depois disso, crie duas listas extras que vao conter apenas os valores
pares e os impares digitados, respectivamente.

Ao final, mostre o conteudo das tres listas geradas.
"""

lista = []

while True:
    lista.append(int(input('Informe um valor para adicionar a lista: ')))

    continuar = ' '

    while continuar not in 'SN':
        continuar = str(input('Continuar? [S/N]')).strip().upper()[0]

    if continuar == 'N':
        break

impares = []
pares = []
for val in range(0, len(lista)):
    if lista[val] % 2 == 0:
        pares.append(lista[val])
    else:
        impares.append(lista[val])

print(f'\nTodos os numeros: {lista}.')
print(f'Todos os pares: {pares}')
print(f'Todos os impares: {impares}')

#Guanabara:

for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)