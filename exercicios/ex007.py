"""
Desenvolva um programa que leia duas notas e calcule e mostre a sua media.
"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2)/2

print('Primeira nota: {:.1f}.\nSegunda nota: {:.1f}.A media e: {:.1f}'.format(n1, n2, m))
