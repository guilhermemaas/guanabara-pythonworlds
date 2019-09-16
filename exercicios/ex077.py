"""
Crie um programa que tenha uma tupla com varias palavras(Nao usar acentos).
Depois disso, voce deve mostrar, para cada palavra, quais sao as suas vogais.
"""

palavras = ('CARRO', 'CASA', 'AVIAO', 'BORBOLETA', 'HOJE')
vogais_lista = ('AEIOU')

for vogais in palavras:
    print(f'\nNa palavra {vogais} temos: ', end='')
    for letra in vogais:
        if letra == 'A':
            print('A ', end='')
        elif letra == 'E':
            print('E ', end='')
        elif letra == 'I':
            print('I ', end='')
        elif letra == 'O':
            print('O ', end='')
        elif letra == 'U':
            print('U ', end='')

#GUANABARA:

print('\n\n' + 'GUANABARA' * 5)

for p in palavras:
    print(f'\nNa palavra {p} temos: ', end='')
    for letra in p:
        if letra in 'AEIOU':
            print(letra, end='')