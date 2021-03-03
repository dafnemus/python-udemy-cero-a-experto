# pylint: disable=missing-docstring

# Usando operadores lógicos:
#   - Determine si una cadena introducida por el usuario es >= 3 y <= 12
#   - Resultado tiene que ser True/False

texto = input('Ingrese un mensaje: ')

if len(texto) >= 3 and len(texto) <= 12:
    print(f'su mensaje {texto} es valido? {True}')
else:
    print(f'su mensaje {texto} es valido? {False}')

# Realiza un programa que ingrese 2 núm y determine:
#   -Si son iguales
#   -Si son distintos
#   -Si el primero es > que el segundo
#   -Si el segundo es > que el primero

numero_1 = int(input('ingrese un número: '))
numero_2 = int(input('ingrese un número: '))

iguales = numero_1 == numero_2
desiguales = numero_1 != numero_2
mayor = numero_1 > numero_2
mayor_igual = numero_2 >= numero_1

print(f'{numero_1} y {numero_2} son iguales? {iguales}')
print(f'{numero_1} y {numero_2} son desiguales? {desiguales}')
print(f'{numero_1} es > que {numero_2}? {mayor}')
print(f'{numero_2} es >= que {numero_1}? {mayor_igual}')
