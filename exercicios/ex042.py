"""
Reforca o DESAFIO 35 dos triangulos.
Acrescentando o recurso de mostrar o tipo de triangulo que sera formado:
- Equilatero: Todos os lados iguais.
- Isosceles: Dois lados iguais.
- Escaleno: Todos os lados diferentes.

Para que seja um triangulo, todas as retas precisam ser menores do que a soma das outras duas.
"""

print('\033[31m'+'='*25+'\nANALISADOR DE TRIANGULOS\n'+'='*25+'\033[m')

r1 = float(input('Informe a primeira reta do triangulo: '))
r2 = float(input('Informe a segunda reta do triangulo: '))
r3 = float(input('Informe a terceira reta do triangulo: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas informadas foram um triangulo. Abaixo o tipo dele: ')
    if r1 == r2 and r2 == r3: #Poderia ser if r1 == r2 == r3:
        print('O Triangulo e um EQUILATERO.')
    elif (r1 != r2 and r1 != r3 and r2 == r3) or (r2 != r1 and r2 != r3 and r1 == r3) or \
            (r3 != r1 and r3 != r2 and r2 == r1):
        print('O Triangulo e um ISOSCELES.')
    elif r1 != r2 and r2 != r3 and r3 != r1:
        print('O Triangulo e um ESCALENO.')
else:
    print('Lados invalidos para calculo do triangulo.')
