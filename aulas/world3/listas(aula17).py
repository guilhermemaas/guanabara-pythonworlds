"""
tupla = ()
lista = []
tupla = IMUTAVEL
lista = MUTAVEL
"""

cardapio = ['Pizza', 'Suco']
cardapio.append('Cerveja')
cardapio.append('Bolo')
print(cardapio)
cardapio[3] = 'Torta de limao'
cardapio.insert(0, 'Hamburger')
print(cardapio)

cont = 0
for item in cardapio:
    print(f'ITEM {cont + 1} - {item}\n')
    cont += 1

for item in range(0, len(cardapio)):
    print(f'{item+1} - {cardapio[item]}')

#Metodos de remocao
print(cardapio)
#['Hamburger', 'Pizza', 'Suco', 'Cerveja', 'Torta de limao']

del cardapio[0] #Remove Hamburger
print(cardapio)
cardapio.insert(0, 'Hamburger') #Adicionando novamente Cerveja
print(cardapio)
cardapio.pop(3) #Remove Cerveja
print(cardapio)
cardapio.insert(3, 'Cerveja') #Adicionando novamente Cerveja
print(cardapio)
cardapio.remove('Cerveja') #Remove itens iguais a 'Cerveja'
print(cardapio)
cardapio.insert(3, 'Cerveja') #Adicionando novamente Cerveja
print(cardapio)

cardapio.pop() #Elimina o ultimo indice da lista
print(cardapio)
cardapio.append('Torta de limao') #adicionando novamente a torta
print(cardapio)

if 'Torta de limao' in cardapio:
    cardapio.remove('Torta de limao')
    print('Torta de limao removida.')

if 'Torta de limao' in cardapio:
    cardapio.remove('Torta de limao')
else:
    print('Nao tem mais torta de limao')

print('Adicionando Torta novamente')
cardapio.append('Torta de limao')
print(cardapio)

#Criando lista em um range de numeros:

valores = list(range(4, 11)) #lista valores recebe numeros em um range de 4 e 10
print(valores)

valores = list(range(0, 20, 2)) #de 2 em 2
print(valores)

#valores ordenados

valores = [1, 3, 10, 4, 92, 21, 9]
print(valores)
valores.sort()
print(valores)
valores.sort(reverse=True)
print(valores)
print(len(valores))

cardapio2 = ['Cerveja', 'Pizza', 'Coca', 'Suco', 'Pizza', 'Vinho', 'Pizza']
print(cardapio2)
cardapio2.remove('Pizza') #Remove o primeiro encontrado. Tem que usar Lacos pra remover todos
print(cardapio2)

valores = []
valores.append(1)
valores.append(5)
valores.append(25)

for v in valores:
    print(f'{v}...', end='')
print('Fim')

#Pra pegar os indices da lista

for i, v in enumerate(valores):
    print(f'{i}-{v}...', end='')
print('Fim')

#Construa uma lista com cinco numeros

valores = list()
for valor in range(0, 5):
    valores.append(int(input('Digite um valor para adiciona-lo a lista: ')))

for index, valor in enumerate(valores):
    print(f'Numero {index}: {valor}.')
print('Fim')

for valor in valores:
    print(f'Valor: {valor}')
print('Fim')

a = [1, 2, 3, 4, 5]
b = a #DESSA MANEIRA O PYTHON FAZ UMA LIGACAO

print(f'Lista A: {a}')
print(f'Lista B: {b}')

b[2] = 25

print(f'Lista A: {a}')
print(f'Lista B: {b}')

b = a[:] #FATIAMENTO, Dessa forma o python joga todos os valores para essa nova lista. Ou entao como voce fizer o fatiamento -> [0:4], [5:4], [:-5]
b[2] = 42

print(f'Lista A: {a}')
print(f'Lista B: {b}')
