# pylint: disable=missing-docstring

# Diccionarios y listas

scooby_doo = []
personaje_1 = {
    'Nombre': 'Scooby',
    'Clase': 'Perro',
    'Comida': 'Scooby-galleta'
}

print(personaje_1)

scooby_doo.append(personaje_1)

print(scooby_doo)

personaje_2 = {
    'Nombre': 'Shaggy',
    'Clase': 'Humano',
    'Comida': 'Scooby-galleta'
}

scooby_doo.append(personaje_2)
print(scooby_doo)

for miembro in scooby_doo:
    print(miembro)
