# pylint: disable=missing-docstring

# Funciones:

# Saludo Mundo:

def saludar() -> str:
    print('Hola Mundo')


saludar()


def mostrar_tabla_del_5() -> str:
    for i in range(10):
        print(f'5 * {i} = {5*i}')


mostrar_tabla_del_5()

# Retorno de valores:


def sumar() -> int:
    return 2 + 2


def listar() -> list:
    return [1, 2, 3, 4, 5]

# print un return


print(listar())
