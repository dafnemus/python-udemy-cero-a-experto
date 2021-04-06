# pylint: disable=missing-docstring
# Registro de inventario de un negocio:
# Debe incluir:
#   - Código identfiador del producto
#   - Nombre del producto
#   - Categoría del producto
#   - PVP
# Mostrar/borrar los datos de cada producto a partir del Código identificador.

class Producto:
    def __init__(self, cod: str, nombre: str, categoria: str, pvp: float):
        self.cod = cod
        self.nombre = nombre
        self.categoria = categoria
        self.pvp = pvp

    def __str__(self) -> str:
        return '{}: ${}'.format(self.nombre, self.pvp)


class Inventario:

    def __init__(self) -> None:
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_producto(self, codigo: str) -> str:
        for i in self.productos:
            if i.cod == codigo:
                return print(i)
        return 'Producto no encontrado'

    def borrar_producto(self, codigo: str) -> str:
        for i, prod in enumerate(self.productos):
            if prod.cod == codigo:
                del self.productos[i]
                return str(prod), 'ELIMINADO'
        return 'Producto no encontrado'


limones = Producto('10001', 'limones', 'fruta', 10)
jabon = Producto('10002', 'jabon', 'Higiene', 15)
cereal = Producto('10003', 'cereal', 'Desayuno', 12)

inventario = Inventario()
inventario.agregar_producto(limones)
inventario.agregar_producto(jabon)
inventario.agregar_producto(cereal)

print(inventario.mostrar_producto('10001'))
print(inventario.mostrar_producto('1222'))

print(inventario.borrar_producto('10003'))
print(inventario.borrar_producto('00002'))
