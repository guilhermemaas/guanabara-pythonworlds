n = s = 0

while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n

print('A soma vale: {}.'.format(s))
#fstring
print(f'A soma vale {s}.')


nome = 'Jose'
idade = 35
salario = 1605.25

print(f'A pessoa se chama {nome:^20} tem {idade} anos e ganha R${salario:.2f} por mes.')
print(f'A pessoa se chama {nome:-<20} tem {idade} anos e ganha R${salario:.2f} por mes.')
print(f'A pessoa se chama {nome:->20} tem {idade} anos e ganha R${salario:.2f} por mes.')