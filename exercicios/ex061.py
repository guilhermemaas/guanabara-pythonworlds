"""
Refaca o exercicio 051, lendo o primeiro termo e a razao de uma PA. Mostrando os 10 primeiros
termos da progressao aritmetica usando while.
"""
print('='*20+'\n\033[36;mPROGRESSAO ARITMETICA\033[m\n'+'='*20)
pt = int(input('Informe o primeiro termo da sua PA: '))
r = int(input('Informe a razao da sua PA: '))

n = pt

print('CALCULADO: {}, '.format(pt), end='')
while n != pt + 9 * r:
    n += r
    if n != pt + 9 * r:
        print('{}, '.format(n), end='')
    else:
        print('{}.'.format(n))

print('\nESPERADO: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19.')

###Guanabara

print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
cont = 1

while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')