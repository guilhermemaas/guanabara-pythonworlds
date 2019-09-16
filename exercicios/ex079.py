"""
Crie um programa onde o usuario possa digitar varios valores numericos e
cadastre-os em uma lista. Caso o numero ja exista la dentro, ele nao sera
adicionado. No final, serao exibidos todos os valores unicos digitados
em ortem crescente.
"""
from time import sleep

print('=.='*15)
print('            \033[31;mCADASTRO NUMEROS\033[m')
print('=.='*15)

valores = []

while True:
    numero = int(input('Informe um numero para cadastro: '))

    if numero in valores:
        print('O numero informado ja foi cadastrado. Tente outro.')
    else:
        valores.append(numero)

    continuar = ' '

    while continuar not in 'SN':
        continuar = str(input('Deseja cadastrar mais numeros? [S] para SIM, [N] para NAO')).strip().upper()[0]

    if continuar == 'N':
        break

print(f'\n\033[33;mLista de Numeros digitados:\033[m {valores}\n')
sleep(0.3)
print('Colocando numeros em ordem...')
sleep(0.3)
valores.sort()
print(f'Valores em ordem crescente: {valores}')

"""
RETRABALHO
valoresUnicos = []

for numero in enumerate(valores):
    print(f'Validando Numero {numero}.')
    if numero not in valoresUnicos:
        print('\033[32;mNao existe. Sera inserido.\033[m')
        valoresUnicos.append(numero)
    else:
        print('\033[31;mJa existe na lista. Nao sera inserido\033[m')
"""