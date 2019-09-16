"""
Escreva um programa que leia dois numeros inteiros e compare-os.
mostrando na tela a mensage:
- O primeiro valor e maior;
- O segundo valor e maior;
- Nao existe valor maior, os dois sao iguais.
"""

n1 = int(input('Informe um primeiro numero: '))
n2 = int(input('Informe um segundo numero: '))

if n1 > n2:
    print('O primeiro numero({}), e o maior.'.format(n1))
elif n2 > n1:
    print('O segundo numero({}), e o maior.'.format(n2))
else:
    print('Nao existe numero maior. {} e {} sao iguais.'.format(n1, n2))
