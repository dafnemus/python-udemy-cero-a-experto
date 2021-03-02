# pylint: disable=missing-docstring

# Comprobación de Tipos:

ENTERO = 1
print(ENTERO, type(ENTERO))

FLOTANTE = 1.5
print(FLOTANTE, type(FLOTANTE))

CADENA = 'hola'
print(CADENA, type(CADENA))

BOOLEANO = True
print(BOOLEANO, type(BOOLEANO))

VACIO = None
print(VACIO, type(VACIO))

# Conversion:

# ENTERO a CADENA
NUM_STR = str(ENTERO)
print(NUM_STR, type(NUM_STR))

# de FLOTANTE a ENTERO
NUM_INT = int(FLOTANTE)
print(NUM_INT, type(NUM_INT))

# de CADENA a FLOTANTE
VALOR = '1.4'
VALOR_FLOAT = float(VALOR)
print(VALOR_FLOAT, type(VALOR_FLOAT))

# de bool a CADENA
VERDAD = str(BOOLEANO)
print(VERDAD, type(VERDAD))
