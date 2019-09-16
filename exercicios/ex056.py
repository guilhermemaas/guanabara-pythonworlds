"""
Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A media de idade do grupo.
- Qual o nome do homem mais velho.
- Quantas mulheres tem menos de 20 anos.
"""

total_idade = 0
total_mulher = 0
h_mais_velho = 0
n_h_mais_velho = ''
total_pessoas = 4

for c in range(1, total_pessoas + 1):
    print('---------{} PESSOA ----------'.format(c))
    nome = str(input('Informe o nome: ')).strip()
    idade = int(input('Informe a idade: '))
    sexo = str(input('Informe o sexo (M ou F): ')).strip()

    total_idade += idade

    if sexo in 'mM' and idade > h_mais_velho:
        h_mais_velho = idade
        n_h_mais_velho = nome

    if sexo in 'fF' and idade > 20:
        total_mulher += 1

media_idade = total_idade / total_pessoas
print("""
MEDIA DE IDADE DO GRUPO: {} anos.
HOMEM MAIS VELHO: {}.
TOTAL DE MULHERES COM MAIS DE 20 ANOS: {}.
""".format(media_idade, n_h_mais_velho, total_mulher))