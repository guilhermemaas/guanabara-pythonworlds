"""
Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar
quando o usuario digitar 999, que e a condicao de parada. No final, mostre quantos
numeros foram digitados e qual foi a soma entre eles(Desconsiderando o flag).
"""
digitado = qtdigitado = smdigitado = 0

while digitado != 999:
    digitado = int(input('Informe um numero: '))

    if digitado != 999:
        smdigitado += digitado
        qtdigitado += 1
    elif digitado == 999:
        qtdigitado == qtdigitado -1

print("""\n
Numeros digitados: {}.\n
Soma destes: {}.
""".format(qtdigitado, smdigitado))