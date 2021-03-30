# pylint: disable=missing-docstring

# Funciones Lambdas:

# funcion normal
def doblar(num):
    return num * 2


doblar(20)

# lambda: funcion anónima
# lambda num: num * 2

duplicar = lambda num: num * 2
duplicar(4)

impar = lambda num: num % 2 != 0
impar(5)

revertir = lambda cadena: cadena[::-1]
revertir('hola')

sumar = lambda a, b: a + b
sumar(5, 4)
