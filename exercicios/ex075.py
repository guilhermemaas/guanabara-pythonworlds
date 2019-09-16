"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
A) Quantas vezes apareceu o valor 9:
B) Em que posicao foi digitado o primeiro valor 3.
C) Quais foram os numeros pares.
"""
print('=.=' * 20 + '\n\033[2;32;mDIGITE QUATRO NUMEROS\033[m\n' + '=.=' * 20)

n1 = int(input('Numero 1: '))
n2 = int(input('Numero 2: '))
n3 = int(input('Numero 3: '))
n4 = int(input('Numero 4: '))

numeros = n1, n2, n3, n4

#GUANABARA:

"""
numeros = (int(input('Digite um numero: ')), int(input('Digite um numero: ')),
    int(input('Digite um numero: ')), int(input('Digite um numero: ')) 
"""

print(f'\nA)Quantas vezes aparece o numero 9: {numeros.count(9)}.')

print('B)Em que posicao foi digitado o primeiro valor 3: ', end='')
if 3 in numeros:
    print(numeros.index(3))
else:
    print('Nao ha numero 3 na tupla.')

print('C)Quais foram os numeros pares: ', end='')
for num in numeros:
    if num % 2 == 0:
        print(f'{num}' + ', ', end='')
print('FIM')

for num in range(0, len(numeros)):
    print(num, end=' - ')
    print(numeros[num])