"""
tempo = int(input('Quantos anos tem seu carro? '))

if tempo <= 3:
    print('Seu carro esta novo!')
else:
    print('Seu carro esta velho!')

print('Carro Novo' if tempo <= 3 else 'Carro Velho')


nome = str(input('Digite seu nome: '))

if nome == 'Gustavo':
    print('Que nome lindo voce tem!')
else:
    print('Seu nome e tao normal!')

print('Bom dia {}!.'.format(nome))
"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

if (n1+n2)/2 >= 7:
    print('Aprovado!')
else:
    print('Reprovado!')