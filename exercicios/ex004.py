"""
Retornar o tipo primitivo de uma variavel, e todas as afirmacoes possiveis sobre ela.
"""

print('Digite um valor qualquer, de qualquer tipo, para validarmos!')
valor = input('Digite um valor de entrada:')

print('O tipo deste valor e: {}.'.format(type(valor)))

if valor.isnumeric():
    print('O valor digitado "{}" e numerico.'.format(valor))
else:
    print('O valor digitado "{}" nao e numerico.'.format(valor))

if valor.isalpha():
    print('O valor digitado "{}" e alfabetico.'.format(valor))
else:
    print('O valor digitado "{}" e alfabetico.'.format(valor))

if valor.isalnum():
    print('O valor digitado "{}" e alfanumerico.'.format(valor))
else:
    print('O valor digitado "{}" e alfanumerico.'.format(valor))

print('O valor digitado "{}" esta totalmente maiusculo? {}.'.format(valor, valor.isupper()))

print('O valor digitado "{}" esta totalmente minusculo? {}.'.format(valor, valor.islower()))

print('O valor digitado "{}" e um espaco? {}.'.format(valor, valor.isspace()))

print('O valor digitado "{}" esta capitalizado? {}.'.format(valor, valor.istitle()))
