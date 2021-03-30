# pylint: disable=missing-docstring

# OPEN

# escritura
with open('ejemplo.txt', 'w+') as f:
    f.write('Escritura en archivos txt')
    f.write('\n')
    f.write('Hola')

# lectura

with open('ejemplo.txt', 'r') as f:
    print(f.read())

with open('ejemplo.txt', 'r') as f:
    data = f.readlines()
    print(data)


lista = []
with open('ejemplo.txt', 'r') as f:
    for linea in f:
        print(linea)
        palabras = linea.split()
        for i in palabras:
            lista.append(i)
        print(lista, type(lista))
