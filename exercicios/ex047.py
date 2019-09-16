"""
Crie um programa que mostre todos os numeros pares que estao no intervalo de 1 e 50.
"""

print('Todos os numeros pares entre 1 e 50: ')

for c in range(1, 51):
    if c % 2 == 0:
        print('{} e par.'.format(c))
print('FIM')

"""
for n in range(2, 51, 2):
    print(n)
print('FIM')
"""