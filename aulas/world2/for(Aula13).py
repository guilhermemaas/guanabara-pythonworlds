"""
for c in range(0, 1): #significa que faz de 0 ate 0, por que no 1 e onde le para.
    print('passo')
    print('pula')
print('passo')
print('pega')

for c in range(0, 6): #signfica que faz de 0 ate 5 (6 * oi), e no 6 ele para.
    print('oi')
print('fim')

for c in range(6, 0, -1):
    print(c)
print('FIM')
6
5
4
3
2
1
FIM

for c in range(0, 7, 2):
    print(c)
print('FIM')

0
2
4
FIM
"""

#numero = int(input('Digite um numero: '))
#for c in range(0, numero):
#    print(c)


inicio = int(input('Informe o inicio: '))
fim = int(input('Informe o fim'))
passo = int(input('Informe o passo: '))

for c in range(inicio, fim+1, passo):
    print(c)
print('FIM')


s = 0
for c in range(0, 4):
    v = int(input('Informe um valor: '))
    s += v
print('A soma e {}.'.format(s))
