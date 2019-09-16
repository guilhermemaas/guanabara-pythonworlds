"""
Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada,
o programa devera perguntar se o usuario quer ou nao continuar. No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantas homes foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.
"""

print('=.='*20)
print(' '*20+'\033[33;mCADASTRO DE PESSOAS\033[m')
print('=.='*20)

continua = 1
totalMaiores = 0
totalHomens = 0
totalMulheresMenos20 = 0

while continua != 0:
    idade = int(input('Informe a idade da pessoa: '))
    sexo = str(input('Informe o sexo da pessoa (M ou F): ')).strip().upper()[0]
    if sexo in 'FM':
        if idade > 18:
            totalMaiores += 1
        if sexo == 'M':
            totalHomens += 1
        elif sexo == 'F' and idade < 20:
            totalMulheresMenos20 += 1
    else:
        print('Sexo informado incorretamente, precisa ser F ou M.')
        pass
    continua = int(input('\nDeseja cotinuar? 1 para SIM, 0 para NAO: '))
    if continua != 1 and continua != 0:
        while continua != 1 and continua != 0:
            print('Opcao invalida, precisa ser 1 ou 0.')
            continua = int(input('\nDeseja cotinuar? 1 para SIM, 0 para NAO: '))
print(f"""\033[4;36;m
\nTotal de maiores de 18 anos: {totalMaiores}.
Total de homens cadastrados: {totalHomens}.
Total de mulheres que tem menos de 20 anos: {totalMulheresMenos20}.\033[m
""")

# print('=.='*20)
# print(' '*20+'\033[33;mCADASTRO DE PESSOAS\033[m')
# print('=.='*20)
#
# continua = 1
# totalMaiores = 0
# totalHomens = 0
# totalMulheresMenos20 = 0
#
# while continua != 0:
#     idade = int(input('Informe a idade da pessoa: '))
#     sexo = str(input('Informe o sexo da pessoa (M ou F): ')).strip().upper()[0]
#
#     if sexo not in 'FM':
#         print('Sexo informado incorretamente, precisa ser F ou M.')
#         pass
#
#     if idade > 18:
#         totalMaiores += 1
#     if sexo == 'M':
#         totalHomens += 1
#     elif sexo == 'F' and idade < 20:
#         totalMulheresMenos20 += 1
#
#     continua = int(input('\nDeseja cotinuar? 1 para SIM, 0 para NAO: '))
#     if continua != 1 and continua != 0:
#         while continua != 1 and continua != 0:
#             print('Opcao invalida, precisa ser 1 ou 0.')
#             continua = int(input('\nDeseja cotinuar? 1 para SIM, 0 para NAO: '))
# print(f"""\033[4;36;m
# \nTotal de maiores de 18 anos: {totalMaiores}.
# Total de homens cadastrados: {totalHomens}.
# Total de mulheres que tem menos de 20 anos: {totalMulheresMenos20}.\033[m
# """)