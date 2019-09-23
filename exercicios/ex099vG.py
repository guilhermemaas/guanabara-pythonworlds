from time import sleep

def maior(* numeros):
    contador_numeros = maior_numero = 0
    print('ANALISANDO VALORES PASSADOS...')
    for numero in numeros:
        contador_numeros += 1
        print(f'ANALISANDO NUMERO: {numero}.', end='', flush=True)
        sleep(0.5)
        if numero > maior_numero:
            maior_numero = numero
    print(f'TOTAL DE NUMEROS PASSADOS: {contador_numeros}.\nMAIOR NUMERO: {maior_numero}.')


maior(1, 4, 2, 9, 20)
sleep(1)
maior(10, 20, 3, 4, 5, 9)
sleep(1)
maior(1, 2, 100, 45, 255)