dados = dict()
dados2 = {}

dados = {'nome': 'Pedro', 'idade': 25}

print(dados['nome'])
print(dados['idade'])

dados['sexo'] = 'M'
print(dados['sexo'])

del dados['idade']

try:
    print(dados['idade'])
except Exception as e:
    print(e)

print(dados)

#print(f'O {dados['nome']} tem {dados['idade']}.')

filme = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}

print(filme)
print(filme.values())
print(filme.keys())
print(filme.items())

for k, v in filme.items():
    print(f'O {k} e {v}.')


locadora = []
locadora.append(dados.items())
locadora.clear()
locadora.append(filme.items())

print(locadora[0])

locadora.append({'nome': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whedon'})

print(locadora)
print(locadora[:1])

locadora.append({'nome': 'Matrix', 'ano': 1999, 'diretor': 'Wachowski'})

print(locadora[:3])

print(locadora[1]['diretor'])

print('-*-'* 30 + '\n\n\n')

pessoas = {'nome': 'Guilherme', 'sexo': 'M', 'idade': 27}

chave = 1
for key in pessoas.keys():
    print(f'A chave {chave} e {key}')
    chave += 1

chave = 1
for value in pessoas.values():
    print(f'O valor {chave} e {value}')
    chave += 1

chave = 1
for item in pessoas.items():
    print(f'O item {chave} e {item}')
    chave += 1

del pessoas['sexo']

for key, value in pessoas.items():
    print(f'{key} = {value}.')

brasil = []
estado = {'uf': 'Santa Catarina', 'sigla': 'SC'}
estado2 = {'uf': 'Sao Paulo', 'sigla': 'SP'}

brasil.append(estado)
brasil.append(estado2)

print(brasil)
print(brasil[0]['uf'])

print('\n')
print('=_=' * 10)

estado = {}
brasil = []

for c in range (0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
print(brasil)

for estado in brasil:
    for key, valor in estado.items():
        print(f'O Campo {key} tem Valor {valor}.')