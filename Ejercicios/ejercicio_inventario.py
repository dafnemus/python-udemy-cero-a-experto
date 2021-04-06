# pylint: disable=missing-docstring

# Registro de inventario de un negocio:
# Debe incluir:
#   - Código identfiador del producto
#   - Nombre del producto
#   - Categoría del producto
#   - PVP
# Mostrar/borrar los datos de cada producto a partir del Código identificador.


productos = [
    {
        'cod': '10001',
        'Nombre': 'Jabón',
        'Categoría': 'Higiene',
        'pvp': 10
    },
    {
        'cod': '10002',
        'Nombre': 'Cereal',
        'Categoría': 'Desayuno',
        'pvp': 20
    },
    {
        'cod': '10003',
        'Nombre': 'Limón',
        'Categoría': 'Fruta',
        'pvp': 8
    }
]


def mostrar(lista, cod):
    for prod in lista:
        if cod == prod['cod']:
            return print(prod['Nombre'], prod['pvp'])
    return print('Producto no encontrado')


mostrar(productos, '10002')
mostrar(productos, '111')


def borrar(lista, cod):
    for i, prod in enumerate(lista):
        if cod == prod['cod']:
            del productos[i]
            return print(str(prod), 'ELIMINADO')
    return print('Producto no encontrado')


borrar(productos, '10003')
borrar(productos, '0002')
