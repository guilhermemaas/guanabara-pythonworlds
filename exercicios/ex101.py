"""
Crie um programa que tenha uma funcao chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL, OBRIGATORIA nas eleicoes.
"""
from datetime import date

hoje = date.today()
ano_atual = int(hoje.strftime("%Y"))

def voto(nome, data_nascimento):
    idade = ano_atual - data_nascimento
    if idade >= 16 and idade < 18 or idade > 70:
        return f'OPCIONAL - Idade: {idade}'
    elif idade >=18 and idade < 70:
        return f'OBRIGATORIA - Idade: {idade}'
    elif idade < 16:
        return f'NEGADA - Idade: {idade}' 
        
print(f'Verificacao de idade para votar. Informe os dados.')
nome = str(input('Favor informar o seu nome: \n')).upper().strip()
data_nascimento = int(input('Favor informar o seu ano de nascimento: \n'))
print(f'Resultado: {voto(nome, data_nascimento)}.')
