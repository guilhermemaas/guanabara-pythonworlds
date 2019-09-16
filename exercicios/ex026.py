"""
Faca um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra "A"
Em que posicao ela aparece pela primeira vez
Em que posicao ela aparece pela ultima vez
"""

frase = str(input('Digite uma frase qualquer: ')).upper().strip()

count_a = frase.count('A')
pos_first_a = frase.find('A') + 1
pos_last_a = frase.rfind('A') + 1

"""
def encontra_posicoes(s, c):
    [pos for pos, char in enumerate(s) if char == c]
"""

print(count_a, pos_first_a, pos_last_a)
