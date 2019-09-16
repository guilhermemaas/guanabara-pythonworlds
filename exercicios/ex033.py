"""
Faca um programa que leia 3 numeros e diga qual e o menor e qual e o maior.
"""

num1 = int(input('Informe um numero qualquer: '))
num2 = int(input('Informe um segundo numero qualquer: '))
num3 = int(input('Informe um terceiro numero qualquer: '))

menor = num1

if num2 < num1 and num2 < num3:
    menor = num2

if num3 < num1 and num3 < num2:
    menor = num3

print('O menor numero e {}.'.format(menor))

#qual e o maior:

maior = num1

if num2 > num1 and num2 > num3:
    maior = num2

if num3 > num1 and num3 > num2:
    maior = num3

print('O maior numero e {}'.format(maior))

"""
maior = 0
menor = 0
if num1 < num2:
    if num1 < num3:
        menor = num1
else:
    if num2 < num3:
        menor = num2
    else:
        menor = num3

if num1 > num2:
    if num1 > num3:
        maior = num1
else:
    if num2 > num3:
            maior = num2
    else:
        maior = num3


print('O maior numero e {}.'.format(maior))
print('O menor numero e {}.'.format(menor))

"""