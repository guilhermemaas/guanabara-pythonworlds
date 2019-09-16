"""
Faca um programa que mostre na tela uma contagem regressiva para estouro de fogos de artificio,
indo de 10 ate 0, com uma pasa de 1 segundo entre eles.
"""
from time import sleep

print('*.*'*20+'\n'+' '*20+'SHOW DA VIRADA'+'\n'+'*.*'*20)
print('\nCONTAGEM REGRESSIVA!!!\n')

for c in range(10, -1, -1):
    print('{}!!!'.format(c))
    sleep(1)

print('\n'+'*.*'*20+'\n'+' '*20+'HAPPY NEW YEAR!!!'+'\n'+'*.*'*20)


