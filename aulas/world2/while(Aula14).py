"""
c = 0

while c != 10:
    print('NUMERO {} - '.format(c), end='')
    c += 1
print('FIM')


n = 0
r = 'SIM'

while r == 'SIM':
    n = int(input('Digite um numero: '))
    print('n')
    r = str(input('Deseja continuar? SIM NAO'))
"""

n = 1

impar = par = 0

while n != 0:
    n = int(input('Digite um numero: '))

    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print('FIM')
print('Total de PARES: {}.\nTotal de IMPARES: {}.'.format(par, impar))
