"""
Faca um programa que leia o ano de um nascimento de um jovem, e de acordo com a sua idade:
- Se ele ainda vai se alistar ao servico militar.
- Se e a hora de se alistar.
- Se ja passou do tempo do alistamento.

Seu programa tambem vai ter que mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date

print('#'*50+'\n\033[4;31mCADASTRO DE ALISTAMENTO\033[m\n'+'#'*50)
print('\n\n\033[35mINFORME NOME E IDADE PARA VALIDAR O STATUS DO JOVEM:\033[m\n\n')

nome = str(input('Informe o nome do jovem: ')).strip().upper()
nascimento = int(input('Informe o ano de nascimento do jovem: '))

current_ano = date.today().year
idade_atual = current_ano - nascimento

if idade_atual < 18:
    print('\n\033[32mO jovem apresentado {} ainda ira se alistar, pos tem {}. '
          'Faltam {} anos!\033[m'.format(nome, idade_atual, 18 - idade_atual))
elif idade_atual == 18:
    print('\n\033[32mO jovem apresentado {} deve se apresentar IMEDIATAMENTE'
          ', pois faz {} esse ano.\033[m'.format(nome, idade_atual))
elif idade_atual > 18:
    print('\n\033[31mO jovem apresentado {} ja passou do tempo de alistamento.'
          ' Ja passou {} anos.\033[m'.format(nome, current_ano - (nascimento + 18)))

print('\n'+'#'*50+'\n\033[4;37mFIM DO CADASTRO\033[m\n'+'#'*50)







