# pylint: disable=missing-docstring

# Sacar el SPROMEDIO de tres números,

NUM_1 = 7
NUM_2 = 13
NUM_3 = 23

SUMA_NOTAS = NUM_1 + NUM_2 + NUM_3

SPROMEDIO = SUMA_NOTAS / 3

print(SPROMEDIO)

# en la sig matriz, el cuarto elemento es la suma de los tres anteriores:
#   -Corregir la que no cumpla con la condicón.
#   - Usar indexaxión.

matriz = [
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 9],
    [4, 4, 4, 13]
]

print(f'matriz original {matriz}')

matriz[1][-1] = sum(matriz[1][:-1])

matriz[-1][-1] = sum(matriz[-1][:-1])

print(f'matriz corregida {matriz}')
