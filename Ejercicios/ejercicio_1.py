# pylint: disable=missing-docstring

# 1. Define una variable edad y asignale un valor entero.
#   -a: Muestra su valor por pantalla.
#   -b: Define otra variable que tenga edad como cadena de caracteres.
#   -c: Comprueba el tipo de la nueva variable
#   -d: Usando edad calcula cuantos años tendría en 2035.

EDAD = 22
print(EDAD, type(EDAD))

EDAD_TEXTO = str(EDAD)

print(EDAD_TEXTO, type(EDAD_TEXTO))

AÑOS_2035 = (2035 - 2021) + EDAD
print(f'An 2035 tendría {AÑOS_2035} años')
