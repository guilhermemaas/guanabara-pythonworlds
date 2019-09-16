"""
Crie um programa que leia diversos numeros inteiros. O programa so vai parar quando
o usuario digitar 999, que e a condicao de parada. No final, mostra quantos numeros
foram digitados e qual foi a soma entre eles(desconsiderando o flag).
"""

print('=.='*20+'\n\033[4;31;mDIGITE NUMEROS ALEATORIOS\033[m\n'+'=.='*20)

n = c = s = 0
while n != 999:
    n = int(input('Informe um inteiro: '))
    if n == 999:
        break
    c += 1
    s += n

print(f'FORAM DIGITADOS {c} NUMEROS.\nA SOMA DESTES E {s}.')

