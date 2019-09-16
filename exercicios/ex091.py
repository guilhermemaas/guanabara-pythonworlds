"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios.
Guarde esses resultados em um dicionario. No final, coloque esse dicionario
em ordem, sabendo que o vencedor tirou o maior numero no dado.
"""
from random import randint
from time import sleep
import operator

rpg_rodada = []
jogador = {}

for indice in range(0, 4):
    print(f'Jogando dados do jogar {indice + 1}')
    jogador['jogador'] = indice + 1
    jogador['dado'] = randint(1, 6)
    rpg_rodada.append(jogador.copy())
    print('...')
    sleep(0.5)

print('\n' + '=' * 30)
print('RESULTADO')
print('=' * 30 + '\n')
print(f'Dados da partida: {rpg_rodada}')

rpg_rodada.sort(key=operator.itemgetter('dado'), reverse=True)
#guanabara
#joga numa lista e ordena.
#ranking = sorted(rpg_rodada.items(), key=itemgetter(1), reverse=True)
#print(ranking) #faz for pra exibir os itens da lista

print('\n')

for jogador in rpg_rodada:
    print(f'Jogador {jogador["jogador"]} - {jogador["dado"]}')

