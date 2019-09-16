arquivos = ['file1.xml', 'file2.xml', 'file3.xml', 'file4.xml', 'file5.xml']
dir = 'var/log/'
lista = []

for c in range(0, len(arquivos)-1):
    print(dir)
    print(arquivos[c])
    print(dir.join(arquivos[c]))
    print('===========')
    #lista.append(dir.join(arquivos[c]))

lista = str.join(dir, arquivos)
print('=========')
print(lista)
