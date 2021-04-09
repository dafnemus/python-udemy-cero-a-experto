# pylint: disable=missing-docstring

# Crear la clase Punto que reciba dos cordenadas:
#   -Metodo constructor, valores por defecto 0 de cada punto
#   -Metodo que imprima los puntos así (X, Y)
#   -Define el metodo cuadrante, que diga en cual se encuentra
#   -Metodo Vector, que reciba un punto y calcule el vector que une puntos.
#   -Metodo Distancia que reciba un punto y calcule la distancia.
import math


class Punto:
    def __init__(self, punto_x=0, punto_y=0) -> None:
        self.punto_x = punto_x
        self.punto_y = punto_y

    def __str__(self) -> str:
        return f'({self.punto_x},{self.punto_y})'

    def cuadrante(self):
        if self.punto_x > 0 and self.punto_y > 0:
            print('Primer Cuadrante')
        elif self.punto_x < 0 < self.punto_y:
            print('Segundo Cuadrante')
        elif self.punto_x < 0 and self.punto_y < 0:
            print('Tercer Cuadrante')
        elif self.punto_x > 0 > self.punto_y:
            print('Cuarto Cuadrante')
        elif self.punto_x == 0 and self.punto_y > 0:
            print('Sobre el eje Y')
        elif self.punto_y == 0 and self.punto_x > 0:
            print('Sobre el eje X')
        else:
            print('Origen')

    def vector(self, point):
        valor_x = point.punto_x - self.punto_x
        valor_y = point.punto_y - self.punto_y
        print(f'Vector entre ({point}) y {self} = ({valor_x},{valor_y})')

    def distancia(self, point):
        calculo = math.sqrt((point.punto_x - self.punto_x)**2 + (point.punto_y - self.punto_y)**2)
        print(f'L a distancia es {calculo}')


a = Punto(5, 8)
b = Punto(10, 2)
a.cuadrante()
b.cuadrante()
a.vector(b)
a.distancia(b)


# Crear la Clase Rectangulo:
#   -Constructor reciba 2 puntos, el origen por defecto.
#   -Metodo Mostrar_base
#   -Metodo Mostrar_altura
#   -Metodo Mostrar_area


class Rectangulo:
    def __init__(self, inicio=Punto(), fin=Punto()) -> None:
        self.inicio = inicio
        self.fin = fin
        self.base = abs(self.fin.punto_x - self.inicio.punto_x)
        self.altura = abs(self.fin.punto_y - self.fin.punto_y)
        self.area = self.base * self.altura

    def mostrar_base(self):
        print(f'La base del rectanfulo es {self.base}')

    def mostrar_altura(self):
        print(f'La altura del rectangulo es {self.altura}')

    def mostrar_area(self):
        print(f'El area del rectangulo es {self.area}')


rec = Rectangulo(a, b)
rec.mostrar_altura()
rec.mostrar_base()
rec.mostrar_area()
