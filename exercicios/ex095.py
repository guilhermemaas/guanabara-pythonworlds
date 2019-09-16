"""
Aprimore o desafio 93 para que ele funcione com varios jogadores, incluindo um sistema
de visualizacao de detalhes do aproveitamento de cada jogador.
Se digitar 999 cancela a exibicao.
"""

print('=.=' * 18)
print(' ' * 10 + 'Aproveitamento de jogador de futebol')
print('=.=' * 18 + '\n')


golsCampeonato = 0
campeonato = []

while True:
    jogador = {}
    partidas = []

    nome = str(input('Informe o nome do jogador: ')).strip()
    qtPartidas = int(input('Informe a quantidade de partidas: '))

    jogador['jogador'] = nome

    for partida in range(0, qtPartidas):
        totalGols = int(input(f'Informe o o total de gols na partida {partida}: '))
        partidas.append(totalGols)
        golsCampeonato += totalGols
        jogador[f'partida{partida + 1}'] = totalGols

    campeonato.append(jogador.copy())
    partidas.clear()
    jogador.clear()

    continuar = ' '

    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? ')).strip().upper()[0]

    if continuar == 'N':
        break

print(f'{campeonato}')

