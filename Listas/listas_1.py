# pylint: disable=missing-docstring

# Listas:
productos = ['Huevos', 'Leche', 'Queso']
precios = [1.5, 2, 5, 10]

# tipo de dato:
print(productos, type(productos))

print(f'Los {productos[0]} cuestan ${precios[0]}')

# Mutabilidad: Aumento de precio.
precios[0] = 15
print(f'Los {productos[0]} ahora cuestan ${precios[0]}')

# lista con range(a, b, in):
#   - a = limite inferior de la secuencia de números
#   - b = limite superior(se excluye)
#   - in = incremento(opcional)
numeros = range(0, 20, 2)
print(numeros)
lista = list(numeros)
print(lista)

# añadir elementos:

lista.append(20)
print(lista)
