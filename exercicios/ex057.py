"""
Faca um programa que leia o sexo de uma pessoa, mas so aceite F e M.
Caso esteja errado, faca a digitacao novamente ate digitar corretamente.
"""

print('\033[4;33m=' * 20 + '\nCadastro de Pessoa: ' + '\n' + '=' * 20 + '\033[m')

# sexo = 'fFMm'
nome = str(input('Informe o seu nome: ')).strip().upper()

while True:
    print('Digite o seu sexo: ')
    sexo = str(input('\n{}, Informe o seu sexo: \n[ M ] - Masculino\n[ F ] - Feminino.'.format(nome))).strip().upper()[
        0]  # pega a primeira letra caso o usuario digite duas
    if sexo in 'FM':
        break
    else:
        print('INFORME UM SEXO VALIDO.')
        pass
print('SEXO: {}.\nNOME: {}.'.format(sexo, nome))

####GUANABARA

sexo = str(input('\n{}, Informe o seu sexo: \n[ M ] - Masculino\n[ F ] - Feminino.'.format(nome))).strip().upper()[
    0]

while sexo not in 'MmFf':
    sexo = \
    str(input('\n{}, Informe um Sexo valido: '.format(nome))).strip().upper()[
        0]

print('SEXO: {}.\nNOME: {}.'.format(sexo, nome))
