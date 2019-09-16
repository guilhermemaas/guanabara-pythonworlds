lanche2 = ['Hamburger', 'Suco', 'Pizza', 'Pudim'] #lista
lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim') #tupla
#lanche3 = {['Hamburger', 'Coca-Cola', 'Fritas'], ['Sorvete','Suco de Laranja']}
print(lanche) #lista tudo
print(lanche[0:2]) #lista entre 0 e 1
print(lanche[1:]) #lista de 1 em diante
print(lanche[-1]) #lista o ultimo item
print(len(lanche)) #lista quantos itens tem a lista
print(type(lanche)) #tipo tupla
print(type(lanche2))
print(lanche[-3:])


# Tuplas = ()
# Listas = []
# Dicionarios {}

for comida in lanche:
    print(comida)

#TUPLAS SAO IMUTAVEIS
#lanche[1] = 'Churrasco'
#TypeError: 'tuple' object does not support item assignment

for comida in lanche:
    print(f'Vou comer...hmmm: {comida}.')

for cont in range(0, len(lanche)):
    print(f'Por {cont}. Vou comer...hmmm: {lanche[cont]}')

for pos, comida in enumerate(lanche):
    print(f'Por {pos}. Vou comer {comida}.')

print('\n')

#Ordem alfabetica:
print(sorted(lanche))

print('\n\n')

a = (2, 5, 4, 9, 3)
b = (3, 6, 9, 12)
c = a + b
print(c)
print(len(c)) #tamanho da tupla, lista
print(c.count(3)) #conta quantas vezes o 3 aparece
print(c.index(3)) #mostra o primeiro indice onde [e encontrado 3.
print(c.index(3, 5)) #mostra o primeiro indice onde encontra 3 a partir do indice 5.

del(lanche) #apaga da memoria
del(lanche[0]) # nao roda, pois nao pode mudar uma tupla, so se fosse lista