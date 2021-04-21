# pylint: disable=missing-docstring

# Crea una superclase Vehiculo(color, ruedas).
# Crear el metodo str para que devuelva: 
#   Color:{color del vehiculo}, {ruedas} ruedas.
# Crea una subclase Carro y agregas los atributos:
#   -velocidad, cilindraje.
#   el metodo str deve devolver: 
#   Color:{color del vehiculo}, {ruedas} ruedas, {velocidad} Km/h, {cilindraje}cc''.

class Vehiculo:
    def __init__(self, color, ruedas) -> None:
        self.color = color
        self.ruedas = ruedas

    def __str__(self) -> str:
        return "Color {}, {} ruedas".format(self.color, self.ruedas)


class Carro(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindraje) -> None:
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindraje = cilindraje
    
    def __str__(self) -> str:
        return super.__str__(self) + f", {self.velocidad}Km/h, {self.cilindraje}cc"


toyota = Carro('azul', 4, 150, 1200)
print(toyota)


# crea la subclase Bicicleta(color, ruedas, tipo)
# Crea la subclase Camioneta(color, ruedas, carga) a partir dela clase Carro.
# Crea la subclase Moto(color, ruedas, velocidad, cilindrada) a partir de la clase Bicicleta.
# Crea al menos un objeto de cada subclase y crea la lista vehículos.
# Define la funcion catalogar(ruedas(optativo)). Que muestre los vehículos cuyo número de ruedas coincida con el arg. Debe mostrar el siguiente mendaje:
#   -Se han encontrado {} vehículos con {} ruedas.

class Camioneta(Carro):
    def __init__(self, color, ruedas, velocidad, cilindraje, carga) -> None:
        super().__init__(color, ruedas, velocidad, cilindraje)
        self.carga = carga
    
    def __str__(self) -> str:
        return super().__str__() + f'{self.carga} kg'


class Bicileta(Vehiculo):
    def __init__(self, color, ruedas, tipo) -> None:
        super().__init__(color, ruedas)
        self.tipo = tipo
    
    def __str__(self) -> str:
        return super().__str__() + f', tipo {self.tipo}'


class Moto(Bicileta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada) -> None:
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self) -> str:
        return super().__str__() + f'{self.velocidad} Km/h, {self.cilindrada} cc.'


def catalogar(vehiculos, ruedas=None):
    contador = 0
    if ruedas != None:
        for vehiculo in vehiculos:
            if vehiculo.ruedas == ruedas:
                contador += 1
        print(f'Se encotraron {contador} vehiculos con {ruedas} ruedas')
    
    for vehiculo in vehiculos:
        if ruedas == None:
            print(type(vehiculo).__name__ , vehiculo)
        else:
            if vehiculo.ruedas == ruedas:
                print(type(vehiculo).__name__ , vehiculo)


vehiculos = [
    Carro('azul', 4, 150, 1200),
    Camioneta('negra', 4, 100, 1300, 1500),
    Bicileta('rosa', 3, 'urbana'),
    Moto('blanca', 2, 'deportiva', 150, 1200)
]

catalogar(vehiculos)

catalogar(vehiculos, 4)
