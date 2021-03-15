# pylint: disable=missing-docstring

# Bucle FOR:

numeros = [1, 2, 3, 4, 5, 6]
INDICE = 0

# cON wHILE
while INDICE < len(numeros):
    print(numeros[INDICE])
    INDICE += 1

# Con FOR
for numero in numeros:
    print(numero)

# Mutabilidad con FOR

for i in range(len(numeros)):
    numeros[i] += 10
    print(numeros[i])
print(numeros)

# Enumerate:

for indice, num in enumerate(numeros):
    numeros[indice] *= 2
print(numeros)

# Cadenas y FOR

CARD = 'Hola'
for letra in CARD:
    print(letra)

CARD_1 = ''
for _ in CARD:
    CARD_1 += 'A'
print(CARD_1)

CARD_2 = ''
for caracter in CARD:
    CARD_2 += caracter * 3
print(CARD_2)
