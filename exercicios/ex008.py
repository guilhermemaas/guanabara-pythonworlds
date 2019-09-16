"""
Constura um programa que solicite um valor em Metros, e retorne em Centimetros e Milimetros.
"""

m = float(input('Informe os metros: '))
c = m * 100
mm = m * 1000

print('Foram informados {}m, totalizando {}cm, e {}mm.'.format(m, c, mm))
print('Foram informados {:.0f}m, totalizando {:.0f}cm, e {:.0f}mm.'.format(m, c, mm))
