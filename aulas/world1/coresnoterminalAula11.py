"""time
Python suporta o padrao ANSI:

\33[0;33;44m

\33 -> Obrigatorio
[0 -> style:
    0 - none
    1 - bold
    4 - underline (Sublinhado)
    7 - Nagative
33 -> text color:
    30 - White
    31 - Red
    32 - Green
    33 - Yellow
    34 - Blue
    35 - Purple
    36 - Blue Pool
    37 - Grey

44 -> background color:
    30 - White
    31 - Red
    32 - Green
    33 - Yellow
    34 - Blue
    35 - Purple
    36 - Blue Pool
    37 - Grey
"""

print('\033[4;31;32mTEXTO\033[m COM CORES!')


cores = {'limpa': '\033[m',
         'red': '\033[4;31m',
         'green': '\033[4;32m'}

print('{}ESSE TEXTO AQUI VERMELHO{}, e {}ESSE AQUI VERDE{}.'.format(cores['red'], cores['limpa'], cores['green'], cores['limpa']))
