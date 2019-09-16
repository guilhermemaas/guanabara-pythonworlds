"""
Faca um programa que leia nome e media de um aluno, guardando tambem a situacao em um dicionario.
No final, mostre o conteudo da estrutura na tela.
"""

print('=.=' * 20)
print(' ' * 15 + 'CADASTRO DE ALUNO + MEDIA')
print('=.=' * 20 + '\n')

aluno = {}

aluno['nome'] = str(input('Informe o nome do aluno: '))
aluno['media'] = float(input('Informe a media do aluno: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Exame'
else:
    aluno['situacao'] = 'Reprovado'

print('\n' + '=======SITUACAO=======')
print(aluno.items())
for key, value in aluno.items():
    print(f'{key} = {value}')
print('=======FIM=======')
