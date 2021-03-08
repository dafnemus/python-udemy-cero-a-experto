# pylint: disable=missing-docstring

# IF/ELSE/ELIF

# IF
X = 6
if X == 6:
    print('x es igual a 6')

# IF anidados:
A = 5
B = 10

if A == 5:
    print('A es igual a 5')
    if B == 10:
        print('b es igual a 10')

# IF y operador lógico and
if A == 5 and B == 10:
    print('a vale {}, y b vale {}'.format(A, B))

# IF/ELSE
Z = 13
if Z % 2 == 0:
    print(f'{Z} es par')
else:
    print(f'{Z} es impar')

# Respuestas dinámicas
texto = input('Qué desea hacer? ')
if texto == 'saludar':
    print('Hola')
elif texto == 'irse':
    print('Adiós')
else:
    print('Por ahora no contamos con ese servicio')

# Clasificador:
puntaje = float(input('Introduce la calificación: '))

if puntaje == 10:
    print('Excelente')
elif puntaje >= 8:
    print('Muy Bueno')
elif puntaje >= 6:
    print('Bueno')
else:
    print('Reprobado')
