# pylint: disable=missing-docstring

# Adición para concatenar dos listas

lista_1 = [2, 4, 5, 6, 7]
lista_2 = [1, 3, 8, 9]

lista_total = lista_1 + lista_2
print(lista_total)

# Conteo de elementos en una lista:

print(f'{lista_1} tiene {len(lista_1)} elementos')

# Operaciones de pertenecia con IN:

print(f'3 esta en {lista_1} {3 in lista_1}')

# Listas Anidadas:

lista_anidada = [lista_1, lista_2]
print(f'esto es una lista anidada {lista_anidada}', end=' ')
print(f'entre {lista_1} y {lista_2}')
