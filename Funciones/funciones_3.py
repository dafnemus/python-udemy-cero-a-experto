# pylint: disable=missing-docstring

# Argumentos Indeterminados:
argumentos = 3, 'hola', [0, 1, 2, 3]


def argumentar(*args):
    print(args)


argumentar(argumentos)


def listar_argumentos(*args):
    for i in args:
        print(i)


listar_argumentos(argumentos)


# Variables como argumentos:

def nombrar(**kwargs):
    print(kwargs)


nombrar(num=2, nombre='lola', notas=[1, 2, 3])


def informar(**kwargs):
    for clave in kwargs:
        print(f'{clave}, {kwargs[clave]}')


informar(num=2, nombre='lola', notas=[1, 2, 3])
