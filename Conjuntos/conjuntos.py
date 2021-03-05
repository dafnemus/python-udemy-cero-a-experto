# pylint: disable=missing-docstring

# Conjuntos:
#   - cada elemento es único.
#   - los elementos no estan ordenados

conjunto_vacio = set()
print(conjunto_vacio, type(conjunto_vacio))

conjunto = {1, 2, 3}
print(conjunto, type(conjunto))

# Agregar elementos al conjunto:

conjunto_vacio.add(3)
conjunto_vacio.add(7)
conjunto_vacio.add(7)
print(conjunto_vacio)

# Verificar pertenencia;

grupo = {'lola', 'luis', 'camila'}

print('lola' in grupo)
print('lola' not in grupo)

# los elementos duplicados se eliminan automaticamente
nombres = {'lola', 'luis', 'camila', 'camila'}
print(nombres)

lista = [1, 2, 2, 2, 3, 3, 1]
print(lista)
conjunto_lista = set(lista)
print(conjunto_lista)

# set con una CADENA:
CADENA = 'hola mundo, adios mundo'
print(set(CADENA))
