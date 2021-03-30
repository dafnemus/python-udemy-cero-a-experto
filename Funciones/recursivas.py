# pylint: disable=missing-docstring

# Funciones Recursivas:

def contar_atras(num):
    num -= 1
    if num > 0:
        print(num)
        contar_atras(num)
    else:
        print(num, 'boom')


contar_atras(5)

# factorial:


def factorial(num):
    print(f'valor inicial: {num}')
    if num > 1:
        num *= factorial(num - 1)
    print(f'valor final {num}')
    return num


factorial(3)
