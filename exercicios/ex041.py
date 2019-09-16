"""
A confederacao Nacional de Natacao precisa de um programa que leia o ano de nascimento de um atleta e mostre
sua categoria, de acordo com a idade:
- Ate 9 anos: MIRIM
- Ate 14 anos: INFANTIL
- Ate 19 anos: JUNIOR
- Ate 30 anos: SENIOR
- Acima de 30 anos: MASTER
"""
from datetime import date

nome = str(input('Informe o nome do atleta: ')).strip()
nascimento = int(input('Informe o ano de nascimento do atleta: '))

idade = date.today().year - nascimento

if idade <= 0:
    categoria = 'INVALIDA'
    print('IDADE INVALIDA, PRECISA SER PELO MENOS 1.')
if idade > 0 and idade <= 9:
    categoria = 'MIRIM'
elif idade <=14:
    categoria = 'INFANTIL'
elif idade <= 19:
    categoria = 'JUNIOR'
elif idade <= 30:
    categoria = 'SENIOR'
elif idade > 30:
    categoria = 'MASTER'

print('A categoria do atleta {} e {}.'.format(nome, categoria))
