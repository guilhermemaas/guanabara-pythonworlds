"""
Crie um programa onde o usuario digite uma expressao qualquer que use parenteses.
Seu aplicativo devera analisar se expressao passada esta com parenteses abertos
e fechados na ordem correta.
Exemplo NOK: (2 * 2) * (3 * 3
Exemplo OK: (2 + 2) * 3
"""

expressao = str(input('Digite uma expressao: '))

pilha = []

for char in expressao:
    if char == '(':
        pilha.append('(')
    elif char == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressao e valida.')
else:
    print('Sua expressao nao e valida.')
