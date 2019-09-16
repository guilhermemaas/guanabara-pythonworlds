"""
Crie um programa que leia varios numeros inteiros pelo teclado.
No final da execucao mostre media entre todos os valores e qual foi a maior e a menor nota.
O programa deve perguntar ao usuario se ele quer continuar a digitar valores.
"""

continua = 1
qtnotas = 0
somanotas = 0
menor_nota = 0
maior_nota = 0

while continua != 0:
    nota = float(input('Informe uma nota: '))
    somanotas += nota

    if qtnotas == 0:
        menor_nota = nota
        maior_nota = nota
    else:
        if nota < menor_nota:
            menor_nota = nota

        if nota > maior_nota:
            maior_nota = nota

    qtnotas += 1
    continua = int(input('Lancar mais notas? [ 1 ] - SIM | [ 0 ] - NAO'))

media = somanotas / qtnotas
print('MENOR NOTA: {:.2f}\nMAIOR NOTA: {:.2f}'.format(menor_nota, maior_nota))
print('QUANTIDADE DE NOTAS: {}\nMEDIA: {:.2f}'.format(qtnotas, media))
