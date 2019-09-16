"""
frase = 'Curso Python em Video'
print(frase[4:8]) #Pega do caracter 4 ate o 7
print(len(frase))
print(frase[0:21:2])
print([comeca:termina])
print(frase[9::3]) #Do 9 ate o final, pulando de 3 em 3
o Py
21
CroPto mVdo
h  d
"""

frase2 = 'Curso em Video Python'
print(len(frase2))
print(frase2.count('o'))
print(frase2.count('o', 0, 13)) #quantos 'o' tem entre o indice 0 e 12
print(frase2.find('deo')) #retorna onde comecou, posicao 11
print(frase2.find('Android')) #retorna -1, por que nao encontrou um indice contendo a frase
print('curso' in frase2)
print('Python' in frase2)
print(frase2.replace('Python', 'Android'))
print(frase2.upper())
print(frase2.lower())
print(frase2.capitalize()) #joga tudo pra minusculo, e o primeiro caractere fica maiusculo
print(frase2.title())

frase3 = '   Aprendendo Python  '
print(frase3)
print(frase3.strip()) #Remove espacoes antecessores e posteriores da string
print(frase3.rstrip()) #Remove somente os espacos da direita
print(frase3.lstrip()) #Remove somente os espacos da esquerda

"""
21
3
1
11
-1
False
True
Curso em Video Android
CURSO EM VIDEO PYTHON
curso em video python
Curso em video python
Curso Em Video Python
   Aprendendo Python  
Aprendendo Python
   Aprendendo Python
Aprendendo Python 
"""

frase4 = 'Curso em Video Python'
frase5 = frase4.split() #Quebra as palavras em uma lista
print(frase4, frase5)
frasejuntada = '-'.join(frase5)
print(frasejuntada)

dir = '//186.250.125.1/'
arquivos = [' file1.xml', ' file2.xml', ' file3.xml']
print(dir)
print(arquivos)


for arquivo in arquivos:
    print(arquivo)

print(""""
TEXT COMPRIDDDDDDDDDDDDDDDDD
OOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOO
""")

print(frase4.upper().count('o'))
print(frase4.upper().count('O'))

frase6 = '  Curso Python Worlds  '
print(len(frase6))
print(len(frase6.strip()))
print(len(frase6.split()))
print(len(frase6.replace('Python', 'Java')))

frase6 = frase6.replace('Python', 'Java').strip().upper()
print(frase6)
print(len(frase6))

frase7 = 'Curso em Video Python'
dividido = frase7.split()
print(dividido)
print(dividido[2][4]) #Pega o indice 1 da lista dividido, e mostra a 4 posicao dessa

