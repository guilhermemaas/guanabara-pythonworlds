print('CADASTRO DE FICHAS DE PERFOMANCE DE GOLS - CAMPEONATO\n')

lista_fichas = []

while True:
    ficha_atual = {}

    nome_jogador = str(input('Favor informar o nome do jogador: ')).upper().strip()
    ficha_atual['nome_jogador'] = nome_jogador

    quantidade_gols = int(input('Favor informar a quantidade de gols que o jogador marcou no campeonato: '))
    ficha_atual['quantidade_gols'] = quantidade_gols

    lista_fichas.append(ficha_atual.copy())
    ficha_atual.clear()

    continuar_cadastro = str(input('Deseja continuar cadastrando mais resultados de jogadores? S - SIM, N - NAO.')).upper().strip()

    if continuar_cadastro == 'N':
        break
    elif continuar != 'S' or continuar != 'N':
        print('Favor informar uma opcao valida: S - SIM, N - NAO. Para continuar ou sair do cadastro.')

print(lista_fichas)
