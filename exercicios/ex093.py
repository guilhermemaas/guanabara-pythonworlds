"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso sera guardado em um dicionario, incluindo o total
de gols feitos durante o campeonato.
"""

print('=.=' * 18)
print(' ' * 10 + 'Aproveitamento de jogador de futebol')
print('=.=' * 18 + '\n')

nome = str(input('Informe o nome do jogador: ')).strip()
qtPartidas = int(input('Informe a quantidade de partidas: '))
partidas = []
golsCampeonato = 0
campeonato = {}

campeonato['jogador'] = nome

for partida in range(0, qtPartidas):
    totalGols = int(input(f'Informe o o total de gols na partida {partida}: '))
    partidas.append(totalGols)
    golsCampeonato += totalGols
    campeonato[f'partida{partida+1}'] = totalGols

campeonato['totalGols'] = golsCampeonato

print(campeonato)