# pylint: disable=missing-docstring
import math

# 1.- Calcula el area de un rectangulo con funcion:


def area_rectangulo(base: int, altura: int) -> int:
    return base * altura


print(area_rectangulo(15, 8))

# Calcula el area de un circulo:


def area_circulo(radio):
    return (radio ** 2) * math.pi


print(area_circulo(12))

# Realiza la funcion relacion() que reciba 2 numeros:
#   - Si el primero > segundo, return 1
#   - Si el primero < segundo, return -1
#   - Si son ==, return 0


def relacion(valor_a, valor_b):
    if valor_a > valor_b:
        return 1
    if valor_a < valor_b:
        return -1
    return 0


print(relacion(2, 1))
print(relacion(2, 5))
print(relacion(4, 4))

# Realiza la funcion que a partir de dos puntos, retorne su punto intermedio


def intermedio(valor_a, valor_b):
    return (valor_a + valor_b) / 2


print(intermedio(-12, 24))


# Realiza la funcion recortar() con 3 parametros:
# p1 = num a recortar, p2 = limite inferior, p3 = limite superior
#   -Devolver el limite inferior si el numero es menorque este
#   -Devolver el limite superior si el num es mayor
#   -Devolver el num sin cambios si no se supera ningun limite


def recortar(num, minimo, maximo):
    if num < minimo:
        return minimo
    if num > maximo:
        return maximo
    return num


print(recortar(15, 0, 10))
print(recortar(8, 12, 15))
print(recortar(5, 3, 7))


# Realiza la separacion de una lista numerica en pares e impares:

pares = []
impares = []


def separar(lista):
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares


numeros = [1, 2, 3, 4, 5, 6]


print(separar(numeros))
