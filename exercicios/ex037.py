"""
Escreva um programa que leia um numero inteiro e peca para o usuario escolher a base de conversao:
1 para binario;
2 para octal;
3 para hexadecimal.
"""

num = int(input('Informe um numero inteiro: '))
print("""
Escolha uma das bases para conversao abaixo:
[ 1 ] - converter para BINARIO
[ 2 ] - converter para OCTAL
[ 3 ] - converter para HEXADECIMAL
""")
base = int(input('Sua opcao: '))

if base == 1:
    print('A BASE BINARIA DE {} e: {}.'.format(num, bin(num)[2:]))
elif base == 2:
    print('A BASE OCTAL DE {} e: {}.'.format(num, oct(num)[2:]))
elif base == 3:
    print('A BASE HEXADECIMAL DE {} e: {}.'.format(num, hex(num)[2:]))
else:
    print('\033[31mOPCAO INVALIDA.')
