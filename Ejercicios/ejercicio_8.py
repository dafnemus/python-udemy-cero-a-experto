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
c = Punto(-2, 4)
d = Punto(1, -3)

a.cuadrante()
b.cuadrante()
c.cuadrante()
d.cuadrante()

a.vector(b)
c.vector(d)

a.distancia(c)
b.distancia(d)
