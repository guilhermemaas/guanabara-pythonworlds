"""
Faca um programa que leia de 0 a 9999 e mostre na tela cada um dos digitos separados. Exemplo:
Digita 1834.
Unidade = 4
Dezena = 3
Centena = 8
Milhar = 1
"""

"""
numero = input('Digite um numero de 0 a 9999: ')


print('O numero digitado e {}, sua unidade e {}, sua dezena e {}, sua centena e {}, seu milhar e {}.'.format(numero, numero[3], numero[2:], numero[1:], numero))
"""

"""
numero = int(input('Digite um numero de entre 0 e 9999: '))
num = str(numero)

print('Analisando o numero {}'.format(numero))
print('Unidade: {}.'.format(num[3]))
print('Dezena: {}.'.format(num[2]))
print('Centena: {}.'.format(num[1]))
print('Milhar: {}.'.format(num[0]))
"""

numero = int(input('Informe um numero entre 0 e 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print('Analisando o numero {}.'.format(numero))
print('Unidade: {}.'.format(u))
print('Dezena: {}.'.format(d))
print('Centena: {}.'.format(c))
print('Milhar: {}.'.format(m))
