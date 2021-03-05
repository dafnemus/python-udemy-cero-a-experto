# pylint: disable=missing-docstring

# Diccionarios:
#   -CLAVE, VALOR

colores_ingles = {
    'azul': 'blue',
    'negro': 'black',
    'rosa': 'pink'
}

print(f'colores en inglés {colores_ingles}')

AZUL = colores_ingles['azul']
print(f'azul es ingles es {AZUL}')

# agrego colores

colores_ingles['naranja'] = 'orange'
colores_ingles['blanco'] = 'white'

print(colores_ingles)

# Diccionario valor números:
edades = {
    'Dafne': 22,
    'Juana': 19
}

print(edades)
edades['Dafne'] += 1
print(edades)

total_años = edades['Dafne'] + edades['Juana']
print(total_años)

# Metódos:

for edad in edades:
    print(edad)
    print(edades[edad])

# items:

for clave, valor in edades.items():
    print(clave, valor)

# del:
del colores_ingles['blanco']
print(colores_ingles)
