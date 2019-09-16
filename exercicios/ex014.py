"""
Recebe um valor em graus Celcius, e converte para Farenheit
"""

c = float(input('Informe os graus celcius: '))
f = ((9 * c) / 5) + 32

print('{:.1f}C sao {:.1f}F'.format(c, f))
