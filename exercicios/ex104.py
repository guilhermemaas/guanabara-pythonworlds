"""
Crie um programa que tenha a funcao leiaint(), que vai funcionar de forma semelhante a funcao input() do Python,
so que a validacao para aceitar apenas um valor numerico.
Ex.: n = leiaint('Digite um n')
"""

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        numero = str(input(msg))
        if numero.isnumeric():
            valor = int(numero)
            ok = True
        else:
            print('ERRO - Informe um numero inteiro compativel.')
        if ok:
            break
    return numero

n = leiaint('Informe um numero inteiro: \n')
print(f'Voce acabou de digitar o numero {n}.')
