"""
Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa

Seu programa devera realizar a operacao solicitada em cada caso.
"""

print('=' * 35 + '\n\033[4;31;mINFORME DOIS VALORES PARA CALUCLO: \033[m\n' + '=' * 35)

result = 0
choice = 0

while True:
    n1 = float(input('\nVALOR1: '))
    n2 = float(input('\nVALOR2: '))
    print("""
    ESCOLHA UMA DAS OPCOES ABAIXO PARA CALCULO:
    \n[ 1 ] - SOMAR
    [ 2 ] - SUBTRAIR
    [ 3 ] - MULTIPLICAR
    [ 4 ] - DIVIDIR
    [ 5 ] - MAIOR NUMERO
    [ 6 ] - NOVOS NUMEROS
    [ 7 ] - SAIR DO PROGRAMA
    """)
    choice = int(input('\nINFORME UMA OPCAO: \n'))

    if choice == 1:
        result = n1 + n2
        break
    elif choice == 2:
        result = n1 - n2
        break
    elif choice == 3:
        result = n1 * n2
        break
    elif choice == 4:
        result = n1 / n2
        break
    elif choice == 5 and n1 > n2:
        result = n1
        break
    elif choice == 5 and n1 < n2:
        result = n2
        break
    elif choice == 6:
        pass
    elif choice == 7:
        break
    else:
        print('OPCOES INVALIDA INFORMADA.')
        pass

if choice == 0 or choice == 7:
    print('VOCE ESCHOLHEU SAIR OU NAO INFORMOU VALOR.')
else:
    print('\nRESULTADO: {}'.format(result))

print('=' * 20+'\nFIM CALCULADOR\n'+'=' * 20)



