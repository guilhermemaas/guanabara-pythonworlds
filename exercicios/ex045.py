"""
Faca um programa que faca o computador jogar jokenpo com voce.
"""

from random import choice
from time import sleep

print('\033[4;34m='*20+'\nJOKENPO MINI GAME\n'+'='*20+'\033[m')

game = 'PEDRA PAPEL TESOURA'
game_options = game.strip().split()

player = str(input("""
DIGITE UMA DAS OPCOES ABAIXO:
[ PEDRA ]
[ PAPEL ]
[ TESOURA ]
"""))
bot = choice(game_options)

print('\nJO')
sleep(0.5)
print('\nKEEEEN')
sleep(1)
print('\nPO!')

print('\nPLAYER ESCOLHEU {}. E O BOT ESCOLHEU: {}.'.format(player, bot))

if player not in (game_options):
    print('\n\033[31mVOCE ESCOLHEU UMA OPCAO INVALIDA. DIGITE PEDRA, PAPEL OU TESOURA!\033[m')
    win = 'INVALIDO'
elif player == 'PEDRA' and bot == 'TESOURA':
    win = 'PLAYER'
elif player == 'PEDRA' and bot == 'PAPEL':
    win = 'BOT'
elif player == 'PEDRA' and bot == 'PEDRA':
    win = 'EMPATE'
elif player == 'PAPEL' and bot == 'PEDRA':
    win = 'PLAYER'
elif player == 'PAPEL' and bot == 'TESOURA':
    win = 'BOT'
elif player == 'PAPEL' and bot == 'PAPEL':
    win = 'EMPATE'
elif player == 'TESOURA' and bot == 'PEDRA':
    win = 'BOT'
elif player == 'TESOURA' and bot == 'PAPEL':
    win = 'PLAYER'
elif player == 'TESOURA' and bot == 'TESOURA':
    win = 'EMPATE'

if win == 'PLAYER' or win == 'BOT' or win == 'EMPATE':
    print('\n'+'='*20+'\nGRANDE VENCEDOR:\n'+'='*20)
    if win == 'PLAYER':
        print('\n\033[4;32m{}!!!\033[m'.format(win))
    elif win == 'BOT':
        print('\n\033[4;31m{}!!!\033[m'.format(win))
    else:
        print('\n\n\033[3;35mEMPATE! NAO HOUVE VENCEDOR, OS DOIS ESCOLHERAM A MESMA OPCAO.\033[m')
    print('\n'+'='*20)
else:
    print('OPCOES INVALIDAS. NAO HA VENCEDOR')