"""
Desenvolva um programa que leia seis numeros inteiros, e mostre apenas aqueles que forem
pares. Se o valor digitado for impar, desconsidere-os.
"""

lista_n = []

for c in range(1, 7):
    num = int(input('Digite o numero {}: '.format(c)))
    if num % 2 == 0:
        lista_n.append(num)

print(lista_n)

