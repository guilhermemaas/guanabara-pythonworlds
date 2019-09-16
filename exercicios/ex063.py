"""
Escreva um programa que leia um numero n inteiro qualquer e mostre na tela
os n primeiros elementos de uma sequencia de Fibonacci.
Ex.: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8 
"""
print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)
"""
n = int(input('Informe um numero inteiro inicial: '))
"""
qt = int(input('Informe a quantidade de termos da sequencia de Fibonacci deseja visualizar: '))
t1 = 0
t2 = 1
print('~'*30)
cont = 3
print(' {} -> {}'.format(t1, t2), end='')
while cont <= qt:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
