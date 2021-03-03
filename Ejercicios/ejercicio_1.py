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

# 2. Al realiza una consulta, recibimos valores corruptos:
# aparcen al revés ñpd datos del alummno.
# Qué puede hacer para obtener el siguiente resultado:
#   -NOMBRE APELLIDO ha sacado un NOTA.

VALOR_CORRUPTO = 'etnasuM enfaD, 01'

VALOR_VALIDO = VALOR_CORRUPTO[::-1]
print(VALOR_VALIDO)

dato = f'{VALOR_VALIDO[4::]} ha sacado {VALOR_VALIDO[:2]}'
print(dato)
