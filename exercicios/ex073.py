"""
Crie uma tupla preenchida com os 8 primeiros colocados da tabela
de campeonato brasileiro de LoL, na ordem de colocacao. Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os ulitmos 4 colocados.
C) Uma lista com os times em ordem alfabetica
D) Em que posicao na tabela esta o time da INTZ.
"""

cblol = ('Kabum! e-Sports', 'Flamengo eSports', 'CNB e-Sports Club', 'Vivo Keyd',
         'INTZ e-Sports Club', 'IDM Gaming', 'ProGaming Esports', 'Red Canids')

print(f"""
\033[4;33;mCBLOL: DADOS\033[m\n
TABELA DE COLOCACAO:
""")

print('-' * 32)
for colocacao in range(0, len(cblol)):
    print('|{}:'.format(colocacao+1) + '{:.>28}|'.format(cblol[colocacao]))
print('-' * 32)

print(f"""\n
A) Cinco primeiro colocados: {cblol[0:5]}.
B) Os ultimos quatro colocados: {cblol[len(cblol)-4:len(cblol)]}.
B) Os ultimos quatro colocados: {cblol[-4:]}.
C) Times do CBLOL em ordem alfabetica: {sorted(cblol)}
D) Em que posicao da tabela esta o time da INTZ: {cblol.index('INTZ e-Sports Club')+1}
D) Em que posicao da tabela esta o time da INZT: {'INTZ' in cblol}
""")

