# pylint: disable=missing-docstring

# Realiza un programa que lea dos números:
# Darle opciones al usuario:
#   -1) SUMA
#   -2) RESTA
#   -3) MULTIPLICAR
# Si se ingresa otra cosa, Mostrar el error

num_1 = int(input('Número 1: '))
num_2 = int(input('Número 2: '))

print('Calculadora')
print('1) Sumar')
print('2) Restar')
print('3) Multiplicar')

opcion = input('Elija una opción(1, 2, 3): ')

if opcion == '1':
    suma = num_1 + num_2
    print(f'{num_1} + {num_2} = {suma}')
elif opcion == '2':
    resta = num_1 + num_2
    print(f'{num_1} - {num_2} = {resta}')
elif opcion == '3':
    multiplicacion = num_1 * num_2
    print(f'{num_1} * {num_2} = {multiplicacion}')
else:
    print('Tiene que elegir entre 1, 2 o 3')

# Dada una lista de cadenas:
#   - Agregar a una lista nueva:
#       - Las palabras de más de 4 letras
#       - Y que la primer letra  y la ultima sean iguales

lista = ['avila', 'caja', 'extra', 'agua', 'arbol']
lista_2 = []
for item in lista:
    if len(item) >= 3 and item[0] == item[-1]:
        lista_2.append(item)
print(lista_2)

# Realizar un programa que pida un numero IMPAR:
# Mientras el numero no sea IMPAR se volverá a ejecutar:

while True:
    num = int(input('numero: '))
    if num % 2 != 0:
        break

# Sumar todos los Numeros pares del 0 al 100

pares = range(0, 101, 2)
suma = sum(pares)
print(suma)
