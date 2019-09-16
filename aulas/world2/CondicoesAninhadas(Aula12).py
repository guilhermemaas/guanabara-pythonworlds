nome = str(input('Qual o seu nome? '))
perfect_name = 'Guilherme'

if nome == perfect_name:
    print('Que nome bonito heim, {}!'.format(nome))
elif nome == 'Dyego' or nome == 'Ursula':
    print('Nao e Guilherme, mas ate que o seu nome e legalzinho heim, {}!'.format(nome))
elif nome in 'Picachu Blastoize Charizard':
    print('POKEMON! {}, voce e um POKEMON =O!'.format(nome))
else:
    print('Que nome comum heim, {}!'.format(nome))

print('Tenha um bom dia, {}!'.format(nome))
