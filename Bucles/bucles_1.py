# pylint: disable=missing-docstring

# WHILE:

CONTADOR = 0

while CONTADOR <= 5:
    print(f'Conteo: {CONTADOR}')
    CONTADOR += 1
print(f'se realizaon {CONTADOR} iteraciones')

print()

# BREAK:

CONTEO = 0

while CONTEO <= 6:
    CONTEO += 1
    if CONTEO == 4:
        print(f'El CONTEO rompe cuando es {CONTEO}')
        break
    print(f'CONTEO {CONTEO}')
print(f'iteraciones {CONTEO}')

# Menu de Usuario:

print('Bienvenido')

while True:
    opciones = input('Ingrese una opción: 1(hola), 2(suma) o 3(salir)')
    if opciones == '1':
        print(' Holaa')
    elif opciones == '2':
        num_1 = int(input('Ingrese un numero: '))
        num_2 = int(input('Ingrese otro numero: '))
        suma = num_2 + num_1
        print(f'Sus números son {num_1, num_2} y suman {suma}')
    elif opciones == '3':
        print('Nos vemos, más tarde')
        break
    else:
        print('Error')
