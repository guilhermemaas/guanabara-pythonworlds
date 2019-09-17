def mostraLinha():
    print('-' * 30)

def tituloCustom(texto):
    mostraLinha()
    print(texto)
    mostraLinha()

def soma(a, b):
    mostraLinha()
    print(f'A = {a} e B = {b}.')
    s = a + b
    print(f'A soma A + B = {s}.')
    mostraLinha()

def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e sao ao todo {tam} numeros.')
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')

def dobraLista(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

def soma2(* num2):
    soma_numeros = 0
    for valor_num in num2:
        soma_numeros += valor_num
    print(f'Somando os valores: {num2}, temos: {soma_numeros}.')


tituloCustom('SISTEMA DE ALUNOS')
tituloCustom('SISTEMA DE CARROS')
tituloCustom('SISTEMA DE PREDIOS')

soma(25, 25)
soma(35, 25)
soma(45, 25)
soma(b = 45, a = 25)

contador(2, 1, 7)
contador(3, 4, 5, 9)

numeros = [1, 2, 4]
print(numeros)
dobraLista(numeros)
print(numeros)

soma2(1, 4, 5)

