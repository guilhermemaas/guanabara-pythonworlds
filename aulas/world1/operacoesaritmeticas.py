"""
+ adicao - 5 + 2 == 7
- subtracao - 5 - 2 == 3
/ divisao - 5 / 2 == 2.5
* multiplicacao - 5 * 2 == 10
** potencia - 5 ** 2 == 25
// divisao inteira - 5 // 2 == 2
% resto da divisao (modulo) - 5 % 2 == 1

Ordem de execucao de uma expressao:
1 - ()
2 - **
3 - *, /, //, %
4 - + -

5+3*2
11
5**2
25
3**3
27
5**3
125
19/2
9.5
19//2
9
"""

print(4**3)
print(pow(4, 3))
print('Oi'*5)


nome = input('Escreva o seu nome: ')
print('Bem-vindo {:25}!'.format(nome))
print('Bem-vindo {:>25}!'.format(nome))
print('Bem-vindo {:<25}!'.format(nome))
print('Bem-vindo {:^25}!'.format(nome))
print('Bem-vindo {:=<25}!'.format(nome))

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um segundo numero: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma e {}.\nO produto(multiplicacao) e {}, e a divisao e {:.3f}.'.format(s, m, d), end=' ') #:.3f -> 3 casas apos a virgula | , end='. ') Para nao quebrar linha entre os 2 prints
print('A divisao inteira e {}.\nA potencia e {}.'.format(di, e)) #\n para quebrar linha no print

"""
64
64
OiOiOiOiOi
Escreva o seu nome: Guilherme
Bem-vindo Guilherme                !
Bem-vindo                 Guilherme!
Bem-vindo Guilherme                !
Bem-vindo         Guilherme        !
Bem-vindo ========Guilherme========!
Digite um numero: 10
Digite um segundo numero: 5
A soma e 15.
O produto(multiplicacao) e 50, e a divisao e 2.000. A divisao inteira e 2.
A potencia e 100000.
"""



