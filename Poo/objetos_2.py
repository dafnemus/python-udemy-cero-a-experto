# pylint: disable=missing-docstring

# Atributos y metodos

class Torta:
    pass

# Asignar atributos despues de crear la clase


torta_fresa = Torta()
torta_fresa.sabor = 'Fresa'
torta_fresa.color = 'rosa'

print(f'la torta es de {torta_fresa.sabor}')
# Definir internamente los atributos


class Tarta:
    membrillo = False


tarta = Tarta()
print(f'la tarta tiene mebrillo {tarta.membrillo}')
tarta.membrillo = True
print(f'la tarta tiene mebrillo {tarta.membrillo}')


# Uso de init

class Alfajor:
    def __init__(self, sabor: str, relleno: str) -> None:
        self.glaseado = False
        self.sabor = sabor
        self.relleno = relleno

    def __str__(self) -> str:
        return f'Alfador de {self.sabor} relleno de {self.relleno}'

    def glasear(self):
        self.glaseado = True

    def esta_glaseado(self) -> bool:
        if self.glaseado:
            return f'Alfajor de {self.sabor} glaseado'
        return f'Alfajor de {self.sabor} no tiene glaseado'


alfajor = Alfajor('chocolate', 'ddl')
print(alfajor.esta_glaseado())

alfajor.glasear()
print(alfajor.esta_glaseado())
