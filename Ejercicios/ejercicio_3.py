# pylint: disable=missing-docstring

# Sacar el promedio de tres números,

num_1 = 7
num_2 = 13
num_3 = 23

suma_notas = num_1 + num_2 + num_3

promedio = suma_notas / 3

print(promedio)

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
