geosp = ['SP', '192.168.1.2']
geosul = ['SUL', '192.168.1.3']
georj = ['RJ', '192.168.1.4']

geografias = []

geografias.append(geosp)
geografias.append(geosul)
geografias.append(georj)

#print(geografias)

teste = []
teste.append('Guilherme')
teste.append(27)
print(teste)

galera = []

galera.append(teste[:]) #Pra criar uma copia e nao interligar a lista com a outra lista
print(galera)

teste[0] = 'Maria'
teste[1] = '22'
print(teste)

galera.append(teste[:]) #Pra criar uma copia e nao interligar a lista com outra lista
print(galera)

galera = [['Guilherme', 27], ['Dyego', 29], ['Ursula', 50], ['Andressa', 24]]
print(galera)
print(galera[0][0], galera[0][1])
print(galera[1][0], galera[1][1])
print(galera[2][0], galera[2][1])

for pessoa in galera:
    print(f'O nome da pessoa e: {pessoa[0]} e sua idade e: {pessoa[1]}')


timesCblol = []
jogadores = []

for contador in range(0, 3):
    jogadores.append(str(input('Digite o nome do jogador: ')))
    jogadores.append(int(input('Digite a idade do jogador: ')))
    timesCblol.append(jogadores[:])
    jogadores.clear()

print(jogadores)
print(timesCblol)

for jogador in timesCblol:
    print(f'Jogador {jogador[0]} tem {jogador[1]}')

for jogador in timesCblol:
    if jogador[1] >= 20:
        print(f'Jogador {jogador[0]} tem {jogador[1]} anos.')
