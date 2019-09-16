"""
Crie um programa onde o usuario possa digitar 5 valores numericos e
cadastre-os em uma lista, ja na posicao correta de insercao(sem usar o sort()).
No final, mostre a lista ordenada na tela.
"""

valores = []

for val in range(0, 5):
    numero = int(input('Informe um valor para continuar: '))

    if len(valores) == 0:
        valores.append(numero)
    elif len(valores) == 1:
        if numero > valores[0]:
            valores.append(numero)
        else:
            valores[0] = numero
    else:
        for val in range(0, len(valores)):
            if numero >= valores[val]:
                valores[val] = numero
            elif numero >= valores[val] and numero not in valores:
                valores.append(numero)

print(f'\nSegue numeros digitados em ordem: {valores}')

#GUANABARA:

lista = []

for contador in range(0, 5):
    n = int(input('Digite um numero para inserir na lista: '))

    if contador == 0 or n > lista[-1]: #ou lista[len(lista)-1] - Ultimo valor da lista
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1

print('=.=' * 20)
print(f'Os valores digitados foram: {lista}')
