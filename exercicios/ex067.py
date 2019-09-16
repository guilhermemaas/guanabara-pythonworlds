"""
Faca um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario
o programa sera interrompido quando o valor digitado for negativo.
"""

print('=.='*20)
print('CALCULADORA DE TABUADA')
print('=.='*20)

n = 0
while True:
    n = int(input('Informe um numero inteiro(Negativo interrompe): '))
    if n < 0:
        break
    else:
        print(f'\nTabuada de {n}:')
        for t in range(1, 11):
            print('{} x {} = {}'.format(n, t, n * t))
            t += 1
print('FIM')

