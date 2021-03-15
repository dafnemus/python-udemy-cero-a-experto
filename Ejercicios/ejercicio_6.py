# pylint: disable=missing-docstring

# Realiar un programa que pida un numero:
#   -Mostrar el promedio del rango de ese numero

numero = int(input('Numero: '))
suma = 0

for i in range(numero):
    suma += i
print(suma)
promedio = suma / numero
print(promedio)

# Realizar un programa que pida un numero entre 0 y 9
# Mostrar el numero si esta en la lista

lista = [0, 2, 7, 8]
while True:
    numero = int(input('Ingreses un numero del 0 al 9: '))
    if numero > 0 and numero <= 9:
        break
if numero in lista:
    print(f'{numero} esta en la lista {lista}')
else:
    print(f'No esta en la lista')

# Dadas dos listas de letras, generar otra cons las que se repitan:

lista_1 = ['a', 'b', 'b', 'b', 'c', 'd', 'e', 'e']
lista_2 = ['a', 'b', 'c', 'd', 'e']
lista_3 = []
for letra in lista_1:
    if letra in lista_2 and letra not in lista_3:
        lista_3.append(letra)

print(lista_1)
print(f'las letras repetidas en la lista son {lista_3}')
