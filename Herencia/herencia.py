# pylint: disable=missing-docstring

# Herencia Simple:

class Producto:
    def __init__(self, ref, nombre, pvp) -> None:
        self.ref = ref
        self.nombre = nombre
        self.pvp = pvp

    def __str__(self) -> str:
        return f'nombre: {self.nombre}. precio: {self.pvp}'

producto_1 = Producto('10004', 'jabon', 45)
str(producto_1)

class Ropa(Producto):
    def __init__(self, ref, nombre, pvp, talla) -> None:
        super().__init__(ref, nombre, pvp)
        self.talla = talla

    def __str__(self) -> str:
        return f'nombre: {self.nombre}. precio: {self.pvp}, talle {self.talla}'

remera = Ropa('10394', 'remera manga corta', 1000, 'M')
str(remera)
