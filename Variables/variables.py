# pylint: disable=missing-docstring

# manejo de variables y methodos:

# definir una variable numerica
PRECIO = 30
print(PRECIO)

# agregar 10 a la variable anterior:
precio_con_envio = PRECIO.__add__(10)
print(precio_con_envio)

# crear una variable string:

LIBRO = 'rapunzel'

# Darle formato TITULO a LIBRO:

TITULO = LIBRO.title()
print(TITULO)

# costo libro sin envio,
print(f'{TITULO} cuesta: ${PRECIO} sin envio')

# costo libro + envio:
print(f'{TITULO} costo + envio: ${precio_con_envio}')

# Mostrar los precios en forma de dict:
# v1 = valor_1
control_precio = {'v1': PRECIO, 'v2': precio_con_envio}
print(control_precio)
