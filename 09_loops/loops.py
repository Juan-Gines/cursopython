### Loops ###
# Loops son bloques de código que se ejecutan repetidamente.
# Los loops se utilizan para iterar sobre una secuencia de elementos.
# Los loops se crean con la palabra clave for, seguida de la variable de iteración y la secuencia de elementos.

# While loop
# El while loop se ejecuta mientras una condición sea verdadera.

my_condition = 0

while my_condition < 10:
    print("El valor de my_condition es:", my_condition)
    my_condition += 1
else: # El bloque else es opcional y se ejecuta al final del loop.
    print("El loop ha terminado.")

while my_condition < 20:
    print("El valor de my_condition es:", my_condition)
    my_condition += 1
    if my_condition == 15:
        print('terminemos el loop')
        break # La palabra clave break se utiliza para salir del loop.
else:
    print("El loop ha terminado.")

# For loop
# El for loop se ejecuta para cada elemento de una secuencia.

my_list = [1, 2, 3, 4, 5, 25, 12, 56]

for element in my_list:
    print("El elemento es:", element)
else:
    print("El loop ha terminado.")

my_tuple = (49, 'Juan Ginés', 'Alentà', 1.75, True)

for element in my_tuple:
    print("El elemento es:", element)
else:
    print("El loop ha terminado.")

my_set = {'Juan Ginés', 'Alentà', 1.75, True}

for element in my_set:
    print("El elemento es:", element) 
else:
    print("El loop ha terminado.")

my_dict = {'Nombre': 'Juan Ginés', 'Apellido': 'Alentà', 'Altura': 1.75, 'Edad' :49, 'Programador': True, 'Lenguajes': {'Javascript', 'Python', 'Java', 'C#'}}

for key in my_dict:
    print("La clave es:", key)
else:
    print("El loop ha terminado.")

for value in my_dict.values():
    print("El valor es:", value)
else:
    print("El loop ha terminado.")

for key, value in my_dict.items():
    print("La clave es:", key, "y el valor es:", value)
else:
    print("El loop ha terminado.")

# Range function
# La función range() se utiliza para generar una secuencia de números.

for i in range(10):
    print("El valor de i es:", i)
else:
    print("El loop ha terminado.")
