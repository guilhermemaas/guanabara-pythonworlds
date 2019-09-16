"""
Melhore o exercicio 61, perguntando ao usuario se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
"""
print('='*25+'\n\033[4;32;mCALCULO DE PROGRESSAO ARITMETICA\033[m\n'+'='*25)

pt = int(input('Informe o primeiro termo de uma PA: '))
r = int(input('Informe a razao de uma PA: '))
qt = 1
n = pt

while qt != 0:
    qt = int(input('\n\nInforme quantos termos da PA voce deseja calcular (Informando 0 interrompe o programa): '))
    if qt == 0:
        break
    else:
        pass

    print('\nCALCULADO: {}, '.format(pt), end='')
    while n < pt + qt * r:
        n += r
        if n < pt + qt * r:
            print('{}, '.format(n), end='')
        else:
            print('{}.'.format(n), end='')
    pt = n + r

print('\n\n')
print('='*3+'\nFIM\n'+'='*3)
