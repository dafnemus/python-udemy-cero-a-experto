# pylint: disable=missing-docstring

# Errores y exceociones:

while True:
    try:
        num = int(input('Ingrese un numero: '))
        TEXTO = '{} dividido por si mismo da: {}'.format(num, num / num)
        print(TEXTO)
    except Exception:
        print('Por favor, intente otra vez ')
    else:
        print('Código ejecutado')
        break
    finally:
        print('Fin del bucle')

# Excepciones multiples:

try:
    num = int(input('Ingrese un numero: '))
    TEXTO = '9/{} = {}'.format(num, 9 / num)
    print(TEXTO)
except ValueError:
    print('No se pueden dividr 9 con letras')
except ZeroDivisionError:
    print('No se puede dividir por 0')
except Exception as error:
    print('Ocurrio el siguiente error: ', type(error).__name__)
