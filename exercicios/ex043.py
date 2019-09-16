"""
Desenvolva um programa que leia o peso e altura de uma pessoa, calcule seu IMC e
mostre o status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso.
- Entre 18.5 e 25: Peso Ideal.
- 25 ate 30: Sobrepeso.
- 30 ate 40: Obesidade.
- Acima de 40: Obesidade morbida.
"""

print('CALCULO DE IMC (Indice de massa corporal).')
nome = str(input('\nInforme o seu nome: ')).strip()
altura = float(input('\nInforme sua altura: '))
peso = float(input('\nInforme seu peso: '))

imc = peso / (altura ** altura)

if imc <= 18.5:
    print('{}. Seu IMC e {:.2f}. Voce esta abaixo do peso.'.format(nome, imc))
elif imc > 18.5 and imc <= 25:
    print('{}. Seu IMC e {:.2f}. Voce esta com o peso ideal.'.format(nome, imc))
elif imc > 25 and imc <= 30:
    print('{}. Seu IMC e {:.2f}. Voce esta com Sobrepeso.'.format(nome, imc))
elif imc > 30 and imc <= 40:
    print('{}. Seu IMC e {:.2f}. Voce esta com Obesidade.'.format(nome, imc))
else:
    print('{}. Seu IMC e {:.2f}. Voce esta com Obesidade morbida'.format(nome, imc))

