n1 = input('Digite um numero: ')
print(type(n1))
print(type(int(n1)))
n1int = int(n1)
print(type(n1int))

n2 = int(input('Digite outro numero:'))
print(type(n2))

n3 = int(input('Digite um terceiro numero para soma: '))
n4 = int(input('Digite um quarto numero para soma: '))
total = n3+n4
print('A soma dos numeros {} e {} e:{}.'.format(n3, n4, total))
