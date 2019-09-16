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

    jogador['nome'] = nome

    for partida in range(0, qtPartidas):
        totalGols = int(input(f'Informe o o total de gols na partida {partida + 1}: '))
        partidas.append(totalGols)
        golsCampeonato += totalGols

    jogador['desempenho'] = partidas[:]

    campeonato.append(jogador.copy())
    partidas.clear()
    jogador.clear()

    continuar = ' '

    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? ')).strip().upper()[0]

    if continuar == 'N':
        break

print('=.=' * 18)
print('    Resultado do Campeonato:')
print('=.=' * 18)
for indice, jogador in enumerate(campeonato):
    print(f'JOGADOR {indice + 1} - {jogador["nome"]}')
    for partida, gols in enumerate(jogador['desempenho']):
        print(f'    PARTIDA {partida} - {gols}.')
print('=.=' * 18)

print('\n')

while True:
    visualizar = ' '
    while visualizar not in 'SN':
        visualizar = str(input('Deseja visualizar os detalhes de um jogador em especifico? [S][N]')).strip().upper()[0]
    if visualizar == 'N':
        break
    nomeJogador = str(input('Informe o Nome do jogador que deseja visualizar os detalhes: ')).strip()
    try:
        for jogador in campeonato:
            if jogador['nome'] == nomeJogador:
                for partida, gols in enumerate(jogador['desempenho']):
                    print(f'    PARTIDA {partida} - {gols}.')
    except Exception as error:
        print('Jogador Nao encontrado.')