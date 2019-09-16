"""
Crie um programa que leia quatro notas de um aluno, calcule sua media, mostrando uma mensagem no final de
acordo com a media atingida:
- Media abaixdo de 5.0:
REPROVADO
- Media entre 5.0 e 6.9:
RECUPERACAO
- Media entre 7.0 ou superior:
APROVADO
"""

titulo = 'CALCULO DE MEDIA FINAL'

print('\033[4;36m*.*\033[m'*len(titulo))
print(' '*len(titulo)+'\033[34mCALCULO DE MEDIA FINAL\033[34m'+' '*len(titulo))
print('\033[4;36m*.*\033[m'*len(titulo))

print('\nINFORME O NOME DO ALUNO E AS NOTAS DOS QUATRO SEMESTRES: ')

nome = str(input('\nInforme o nome do aluno: ')).strip().upper()
n1 = float(input('\nInforme a nota do primeiro bimestre: '))
n2 = float(input('\nInforme a nota do segundo bimestre: '))
n3 = float(input('\nInforme a nota do terceiro bimestre: '))
n4 = float(input('\nInforme a nota do quarto bimestre: '))
media = (n1 + n2 + n3 + n4) / 4

print('\nMEDIA: {:.1 f}.'.format(media))

if media < 0 or media > 10:
    print('\nNotas invalidas.')
elif media == 0:
    print('\nLOOOOOSER')
elif media < 5:
    print('\nAluno {}. \033[31mREPROVADO.\033[31m'.format(nome))
elif media > 5 and media < 7:
    print('\nAluno {}. \033[33mRECUPERACAO.\033[33m'.format(nome))
elif media >= 7:
    print('\nAluno {}. \033[32mAPROVADO.\033[33m'.format(nome))

rodape = 'FIM'
print('\n'+'\033[4;36m*.*\033[m'*len(rodape))
print(' '*len(rodape)+'\033[34mFINAL\033[34m'+' '*len(rodape))
print('\033[4;36m*.*\033[m'*len(rodape))

