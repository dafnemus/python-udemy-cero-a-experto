# pylint: disable=missing-docstring

# Manejo de Numeros:

# INT:
numero = 3
print(f'esto es un {type(numero)} = {numero}')
# sumar numeros:

suma = numero + numero.__add__(5) # 3 + (3+5)

print(f'resultado = {suma}')

# FLOAT
flotante = 2.5
print(f'esto es un {type(flotante)} = {flotante}')


# COMPLEX

complejo = 1+2j;
print(f'esto es un {type(complejo)} = {complejo}')

parte_real = complejo.real
print(f'parte real = {parte_real}')

parte_imaginaria = complejo.imag
print(f'parte imaginaria = {parte_imaginaria}')
