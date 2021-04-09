# pylint: disable=missing-docstring

# Objetos dentro de objetos

class VideoJuego:

    def __init__(self, titulo, genero):
        self.titulo = titulo
        self.genero = genero

    def __str__(self):
        return f'Juego: {self.titulo}, Genero: {self.genero}'


video_juego = VideoJuego('Mario Bross', 'Plataformas')
video_juego_2 = VideoJuego('Pac-man', 'Persecución')
video_juego_3 = VideoJuego('Pokemon', 'RPG')

print(str(video_juego))


class Catalogo:

    def __init__(self) -> None:
        self.juegos = []
    
    def agregar_vg(self, juego):
        self.juegos.append(juego)

    def mostar(self):
        for j in self.juegos:
            print(j)


catalogo_juegos = Catalogo()
catalogo_juegos.agregar_vg(video_juego)
catalogo_juegos.agregar_vg(video_juego_2)
catalogo_juegos.agregar_vg(video_juego_3)
catalogo_juegos.mostar()
