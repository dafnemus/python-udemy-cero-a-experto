# pylint: disable=missing-docstring

# Tuplas:
#   -Inmutables

mi_tupla = ('lunes', 'martes', 'miércoles')

print(mi_tupla, type(mi_tupla))

# primer elemento de mi tupla:

print('El primer elemento de mi tupla es ', mi_tupla[0])

# Metodos de las tuplas:

# index:
lunes = mi_tupla.index('lunes')
print(f'En qué posición está lunes en mi tupla? {lunes}')

# count:
jueves = mi_tupla.count('jueves')
print(f'Cuántos jueves hay en mi tupla? {jueves}')
