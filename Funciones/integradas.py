# pylint: disable=missing-docstring

# Funciones Integradas:

# Númericas:

NUM = int('8')

print(f'Entero: {NUM}')

FLOTANTE = float('1.5')
print(f'flotante: {FLOTANTE}')

BINARIO = bin(19)
print(f'Binario de 19: {BINARIO}')

ENTERO = int('0b10011', 2)
print(f'pasaje de binario 0b10011 a entero: {ENTERO}')

HEXADECIMAL = hex(1)
print(f'Hexadecimal de 1: {HEXADECIMAL}')

ABSOLUTO = abs(-10)
print(f'Absoluto de -10: {ABSOLUTO}')

REDONDEO = round(4.6)
print(f'redondeo de 4.6: {REDONDEO}')

POW = pow(2, 3)
print(F'Potencia de 2 al cubo {POW}')


# de Cadena:

CADENA = 'hola mundo'

print(f'split: {CADENA.split()}')

print(f'mayúsculas: {CADENA.upper()}')

CADENA_2 = 'CHAU MUNDO'
print(f'Minúsculas: {CADENA_2.lower()}')

print(f'capitaliza: {CADENA.title()}')

# ZIP: crea tuplas a partir de 2 listas.
a, b, c, d = zip(['A', 'B', 'C', 'D'], [10, 12, 13, 14])

print(a, b, c, d)

# diccionario con ZIP

diccionario = dict(zip(['A', 'B', 'C', 'D'], [10, 12, 13, 14]))
print(diccionario)
