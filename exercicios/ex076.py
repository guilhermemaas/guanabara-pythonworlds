"""
Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos precos na sequencia
No final, mostre uma listagem de precos, organizando os dados em forma tabular
"""

print('=.=' * 20 + '\nPC GAMER\n' + '=.=' * 20)

pecas = ('Monitor', 950.50, 'CPU', 2905.50, 'Teclado', 300, 'Mouse', 45.50, 'Fone', 105.25)

cont = 0
print('\n' + '-' * 40)
while cont < len(pecas):
    print('|{}'.format(pecas[cont]) + '{:.>30}|'.format(pecas[cont+1]))
    cont += 2
print('-' * 40)

#GUANABARA

for pos in range(0, len(pecas)):
    if pos % 2 == 0:
        print(f'{pecas[pos]:.<30}', end='')
    else:
        print(f'R${pecas[pos]:>7.2f}')