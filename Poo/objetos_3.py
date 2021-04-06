# pylint: disable=missing-docstring

# Métodos especiales:

class Video:

    # constructor de clase
    def __init__(self, titulo, duracion) -> None:
        self.titulo = titulo
        self.duracion = duracion

    # metodo str
    def __str__(self) -> str:
        return f'pelicula: {self.titulo}, duracion: {self.duracion}'

    # metodo len
    def __len__(self):
        return self.duracion

    # destructor de clase
    def __del__(self):
        print('se elimino el video', self.titulo)


pelicula = Video('Vengadores', 146)

str(pelicula)
len(pelicula)
