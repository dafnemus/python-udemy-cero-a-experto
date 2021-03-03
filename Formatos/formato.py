# pylint: disable=missing-docstring

# Formateo

# Format por defecto

CADENA = 'valor {}, valor {}'.format(1, 2)
print(CADENA)

# format por designación
TEXTO = 'conteo al reveés {1},{0}'.format(1, 2)
print(TEXTO)

# uso de F
OBRA = 'romeo y julieta'
PRECIO = 3000

print(f'la obra: {OBRA.title()} cuesta ${PRECIO}')
