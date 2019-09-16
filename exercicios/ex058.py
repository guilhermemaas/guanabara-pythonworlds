"""
Melhore o jogo do desafio 028 onde o computador vai pensar em um numero de 0 a 10.
So que agora vai tentar adivinhar ate acertar. Mostrando no final quantos palpites foram
necessarios para vencer.
"""
from random import randint

print('\033[31;m=-=\033[m'*20+'\n'+' '*20+'\033[34;mJOGO ADVINHACAO\033[m'+'\n'+'\033[31;m=-=\033[m'*20)

bot = randint(0, 10)
palpites = 0
acertou = False

while not acertou:
    player_choice = int(input('\nEscolha um numero entre 0 e 10 e veja se adivinha a escolha do bot! '))

    if player_choice == bot:
        acertou = True
    else:
        if player_choice > bot:
            print('DICA: Bot escolheu um numero menor.')
        else:
            print('DICA: Bot escolheu um numero maior.')

    palpites += 1

print("""\n\n
ESCOLHA DO BOT: {}
FORAM NECESSARIAS {} Tentativas para adivinhar.
""".format(bot, palpites))


