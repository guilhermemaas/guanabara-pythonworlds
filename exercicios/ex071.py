"""
Crie um programa que simule um caixa eletronico. No inicio, pergunte ao usuario qual sera o valor sacado(inteiro).
e o programa vai calcular quantas cedulas de cada valor serao entregues.
Obs.: Considere que o caixa possui cedulas de: R$50, R$20, R$10 e R$1.
"""
print('#!#'*20)
print('{:^60}'.format('BANCO CEV'))
print('#!#'*20)
print("""
\nCEDULAS DISPONIVEIS:\n
\033[31;m50\033[m
\033[32;m20\033[m
\033[33;m10\033[m
\033[34;m1\033[m
\n
""")
valorDesejado = int(input('Informe um valor a ser sacado: R$'))
print('... Calculando Cedulas...')

total50 = total20 = total10 = total1 = 0
valorRestante = valorDesejado

while valorRestante != 0:
    while valorRestante >= 50:
        valorRestante = valorRestante - 50
        total50 += 1
    while valorRestante >= 20:
        valorRestante = valorRestante - 20
        total20 += 1
    while valorRestante >= 10:
        valorRestante = valorRestante - 10
        total10 += 1
    while valorRestante >= 1:
        valorRestante = valorRestante - 1
        total1 += 1

print(f"""\nFIM DO SAQUE.
Total de notas de R$50: {total50}.
Total de notas de R$20: {total20}.
Total de notas de R$10: {total10}.
Total de notas de R$1: {total1}.
""")

