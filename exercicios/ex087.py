"""
Aprimore o desafio anterior, mostrando no final:

A)A soma de todos os valores pares digitadas.
B)A soma dos valores da terceira coluna.
C)O maior valor da segunda coluna.
"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para {linha}, {coluna}: '))

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            spar += matriz[linha][coluna]
    print()

print(f'A) A soma dos numeros pares: {spar}')

somaLinha = 0
somaTotal = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        somaTotal += matriz[linha][coluna]
print(f'A) A soma de todos os valores da matriz: {somaTotal}')

somaTerceiraColuna = 0
for linha in range(0, 3):
    somaTerceiraColuna += matriz[linha][2]
print(f'B) A soma dos valores da terceira coluna: {somaTerceiraColuna}')

segundaColuna = []
for linha in range(0, 3):
    for coluna in range(0, 3):
        segundaColuna.append(matriz[linha][1])
print(f'C) O maior valor da segunda coluna: {max(segundaColuna)}')

