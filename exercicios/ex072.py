"""
Crie um programa que tenha uma tupla totalmente preenchida com uma
contagem por extenso, de 0 ate vinte.
Seu programa devera ler um numero pelo teclado(entre 0 e 20)
e mostra-lo por extenso.
"""
numeros = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
           'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

print('=*='*20 + '\n\033[31;mNUMEROS ATE 20\033[m\n' + '=*=' * 20)

while True:
    n = -1
    while n < 0 or n > 20:
        n = int(input('Informe um numero de 0 a 20 para visualiza-lo por extenso: '))

    print(f'\nSegue: {numeros[n]}\n')

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja visualizar mais numeros? Digite S para SIM, N para NAO: \n')).strip().upper()[0]

    if continuar == 'S':
        pass
    else:
        break

print('\nFIM DO PROGRAMA')
