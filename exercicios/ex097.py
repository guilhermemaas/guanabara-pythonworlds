"""
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
mensagem com tamanho adaptável.
print(f'{" " * 50}' + '{string}')
print(f'{string:.<30}')
"""

def imprimeLinha(quantidade):
    print(f'=' * quantidade)

def montaTitulo(titulo):
    total_caracteres = len(titulo)
    imprimeLinha(total_caracteres + 10)
    print(f'{" " * 5}' + f'{titulo}')
    imprimeLinha(total_caracteres + 10)


while True:

    texto = str(input('Digite um título qualquer: ')).upper().strip()
    montaTitulo(texto)

    continuar = ' '

    while continuar not in 'NS':
        continuar = str(input('Deseja exibir imprimir mais um título? S/N: \n')).upper().strip()
        
    if continuar == 'N':
        break