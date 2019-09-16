"""
Refaca o desafio 009, mostrando a tabuada de um numero que o usuario escolher
so que agora utilizando um laco for
"""

n = int(input('Informe um numero para exibir sua tabuada: '))

for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, n*c))

print('FIM')