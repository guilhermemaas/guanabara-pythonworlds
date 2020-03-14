"""
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros, início, fim, e passo e realize
a contagem.

Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
r) de 10 até 0, de 2 em 2

Faça um programa que tenha uma função chamada contador(), que receba três parâmetros, início, fim, e passo e realize
a contagem.

Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""
from time import sleep

def imprimir_linha(quantidade):
    print(f'=' * quantidade)

def montar_titulo(titulo):
    total_caracteres = len(titulo)
    imprimir_linha(total_caracteres + 10)
    print(f'{" " * 5}' + f'{titulo}')
    imprimir_linha(total_caracteres + 10)

def contador(numero_inicial, numero_final, passo, tipo_contador):
    """
    1) de 1 até 10, de 1 em 1
    2) de 10 até 0, de 2 em 2
    3) uma contagem personalizada
    """
    if passo == 0:
        print('PASSO 0 nao permitido, alterando para 1.')
        passo = 1
    if tipo_contador == 1:
        for valor in range(1, 10 + 1, 1):
            print(f'Imprimindo Valor: {valor}.')
    elif tipo_contador == 2:
        for valor in range(10, 0 - 1, -2):
            print(f'Imprimindo Valor: {valor}.')
    elif tipo_contador == 3:
        if numero_final > 0:
            numero_final += 1
        else:
            numero_final -= 1
        for valor in range(numero_inicial, numero_final, passo):
            print(f'Imprimindo Valor: {valor}.')


montar_titulo('FUNCAO CONTADOR')
print('TRES OPCOES:\n1 - Exibir contador de 1 ate 10, de 1 em 1.\n2 - Exibir de 10 a 0, de 2 em 2.\n'
      '3 - Contagem customizada, nesse caso, informar VALOR INICIAL, VALOR FINAL e PASSO.')
sleep(0.5)

while True:
    montar_titulo('INFORME A SUA ESCOLHA')
    tipo_contador = 0
    valores_validos = [1, 2, 3]
    while tipo_contador not in valores_validos:
        tipo_contador = int(input('Valores validos para escolha: 1, 2 ou 3: \n'))
    if tipo_contador == 3:
        numero_inicial = int(input('Informe um valor de Inicio: \n'))
        numero_final = int(input('Informe um valor de Fim: \n'))
        numero_passo = int(input('Informe um numero de Passo: \n'))
        contador(numero_inicial, numero_final, numero_passo, tipo_contador)
    elif tipo_contador == 1:
        contador(0, 0, 0, 1)
    else:
        contador(0, 0, 0, 2)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('DESEJA RODAR MAIS CONTADOR? S/N\n')).upper().strip()
        if continuar not in 'SN':
            print('Digite um valor valido para continuar: S/N')
    if continuar == 'N':
        break

montar_titulo('FIM - PROGRAMA')
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros, início, fim, e passo e realize
a contagem.

Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""
from time import sleep

def imprimir_linha(quantidade):
    print(f'=' * quantidade)

def montar_titulo(titulo):
    total_caracteres = len(titulo)
    imprimir_linha(total_caracteres + 10)
    print(f'{" " * 5}' + f'{titulo}')
    imprimir_linha(total_caracteres + 10)

def contador(numero_inicial, numero_final, passo, tipo_contador):
    """
    1) de 1 até 10, de 1 em 1
    2) de 10 até 0, de 2 em 2
    3) uma contagem personalizada
    """
    if passo == 0:
        print('PASSO 0 nao permitido, alterando para 1.')
        passo = 1
    if tipo_contador == 1:
        for valor in range(1, 10 + 1, 1):
            print(f'Imprimindo Valor: {valor}.')
    elif tipo_contador == 2:
        for valor in range(10, 0 - 1, -2):
            print(f'Imprimindo Valor: {valor}.')
    elif tipo_contador == 3:
        if numero_final > 0:
            numero_final += 1
        else:
            numero_final -= 1
        for valor in range(numero_inicial, numero_final, passo):
            print(f'Imprimindo Valor: {valor}.')


montar_titulo('FUNCAO CONTADOR')
print('TRES OPCOES:\n1 - Exibir contador de 1 ate 10, de 1 em 1.\n2 - Exibir de 10 a 0, de 2 em 2.\n'
      '3 - Contagem customizada, nesse caso, informar VALOR INICIAL, VALOR FINAL e PASSO.')
sleep(0.5)

while True:
    montar_titulo('INFORME A SUA ESCOLHA')
    tipo_contador = 0
    valores_validos = [1, 2, 3]
    while tipo_contador not in valores_validos:
        tipo_contador = int(input('Valores validos para escolha: 1, 2 ou 3: \n'))
    if tipo_contador == 3:
        numero_inicial = int(input('Informe um valor de Inicio: \n'))
        numero_final = int(input('Informe um valor de Fim: \n'))
        numero_passo = int(input('Informe um numero de Passo: \n'))
        contador(numero_inicial, numero_final, numero_passo, tipo_contador)
    elif tipo_contador == 1:
        contador(0, 0, 0, 1)
    else:
        contador(0, 0, 0, 2)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('DESEJA RODAR MAIS CONTADOR? S/N\n')).upper().strip()
        if continuar not in 'SN':
            print('Digite um valor valido para continuar: S/N')
    if continuar == 'N':
        break

montar_titulo('FIM - PROGRAMA')
c) uma contagem personalizada
"""
from time import sleep

def imprimir_linha(quantidade):
    print(f'=' * quantidade)

def montar_titulo(titulo):
    total_caracteres = len(titulo)
    imprimir_linha(total_caracteres + 10)
    print(f'{" " * 5}' + f'{titulo}')
    imprimir_linha(total_caracteres + 10)

def contador(numero_inicial, numero_final, passo, tipo_contador):
    """
    1) de 1 até 10, de 1 em 1
    2) de 10 até 0, de 2 em 2
    3) uma contagem personalizada
    """
    if passo == 0:
        print('PASSO 0 nao permitido, alterando para 1.')
        passo = 1
    if tipo_contador == 1:
        for valor in range(1, 10 + 1, 1):
            print(f'Imprimindo Valor: {valor}.')
    elif tipo_contador == 2:
        for valor in range(10, 0 - 1, -2):
            print(f'Imprimindo Valor: {valor}.')
    elif tipo_contador == 3:
        if numero_final > 0:
            numero_final += 1
        else:
            numero_final -= 1
        for valor in range(numero_inicial, numero_final, passo):
            print(f'Imprimindo Valor: {valor}.')


montar_titulo('FUNCAO CONTADOR')
print('TRES OPCOES:\n1 - Exibir contador de 1 ate 10, de 1 em 1.\n2 - Exibir de 10 a 0, de 2 em 2.\n'
      '3 - Contagem customizada, nesse caso, informar VALOR INICIAL, VALOR FINAL e PASSO.')
sleep(0.5)

while True:
    montar_titulo('INFORME A SUA ESCOLHA')
    tipo_contador = 0
    valores_validos = [1, 2, 3]
    while tipo_contador not in valores_validos:
        tipo_contador = int(input('Valores validos para escolha: 1, 2 ou 3: \n'))
    if tipo_contador == 3:
        numero_inicial = int(input('Informe um valor de Inicio: \n'))
        numero_final = int(input('Informe um valor de Fim: \n'))
        numero_passo = int(input('Informe um numero de Passo: \n'))
        contador(numero_inicial, numero_final, numero_passo, tipo_contador)
    elif tipo_contador == 1:
        contador(0, 0, 0, 1)
    else:
        contador(0, 0, 0, 2)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('DESEJA RODAR MAIS CONTADOR? S/N\n')).upper().strip()
        if continuar not in 'SN':
            print('Digite um valor valido para continuar: S/N')
    if continuar == 'N':
        break

montar_titulo('FIM - PROGRAMA')
