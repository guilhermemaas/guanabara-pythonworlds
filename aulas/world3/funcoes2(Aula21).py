#print(print.__doc__)
#help(help)

def contador(i, f, p):
    """
    ->Faz uma contagem e mostra na tela
    :param i: inicio da contagem.
    :param f: fim da contagem.
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM')

contador(1, 10, 2)
contador(0, 100, 10)

help(contador)

#Parametros opcionais:

def somar(a = 0, b = 0, c =0):
    s = a + b + c
    return s

print(somar(3, 2, 5))
print(somar(3, 2))
print(somar(0, 0, 0))
print(somar(15, 0, 0))
print(somar(b = 15, c = 20))

#Ecopo de variaveis, local x global
def teste(b):
    global a
    a = 10

def teste2(b):
    a = 8

a = 5
print(a)
teste(a)
print(a)
teste2(a)
print(a)

#Retorno
def somar2(a = 0, b = 0, c =0):
    s = a + b + c
    return s

print(somar2(10, 10, 10))

#Fatorial de 5:
#5 = 5.4.3.2.1
#    20.6.1
#       120.1
#       120

def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
print(f'O resultado e: {f1}.')

def verifica_par(n = 0):
    if n % 2 == 0: #Se o resto for 0
        return True
    else:
        return False

print(f'10 e par?: {verifica_par(10)}.')

num = int(input('ESCRAVA UM NUMERO PARA VERIFICAR SE PAR: '))
if verifica_par(num):
    print('E PAR!')
else:
    print('NAO E PAR!')