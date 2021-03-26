# pylint: disable=missing-docstring

# Parametros y Argumentos:

def restar(parametro_a: int, parametro_b: int) -> int:
    return parametro_a - parametro_b


restar(5, 3)

# Valor por defecto:


def sumar(num_1=1, num_2=1) -> int:
    return num_1 + num_2


sumar()

# Argumentos por valor:


def duplicar(numero: int) -> int:
    return numero * 2


NUM = 10


duplicar(NUM)

# Argumentos por referencia:


def duplicar_notas(numeros: list) -> list:
    for i, _ in enumerate(numeros):
        numeros[i] *= 2
    return numeros


notas_a = list(range(5))
# copia de una lista a una funcion
notas = duplicar_notas(notas_a[:])

print(notas_a, notas)
