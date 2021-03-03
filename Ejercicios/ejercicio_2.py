# pylint: disable=missing-docstring

# Usando operadores lógicos:
#   - Determine si una cadena introducida por el usuario es >= 3 y <= 12
#   - Resultado tiene que ser True/False

texto = input('Ingrese un mensaje: ')

if len(texto) >= 3 and len(texto) <= 12:
    print(f'su mensaje {texto} es valido? {True}')
else:
    print(f'su mensaje {texto} es valido? {False}')
