"""
Crie um programa que leia uma frase qualquer e diga ela e um palindromo,
desconsiderando os espacos.
Anotaram a data da maratona
"""

frase = str(input('Informe uma frase: ')).strip()
frase2 = ''

for c in range(len(frase)-1, -1, -1):
    frase2 += frase[c]

print(frase.upper().replace(' ', ''))
print(frase2.upper().replace(' ', ''))

if frase.upper().replace(' ', '') == frase2.upper().replace(' ', ''):
    print('A frase e palindromo.')
else:
    print('A frase nao e palindromo')
