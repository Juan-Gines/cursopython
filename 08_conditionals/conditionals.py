### Conditionals ###
# Conditionals son bloques de código que se ejecutan si se cumple una condición.
# Los condicionales se utilizan para tomar decisiones en el código.
# Los condicionales se crean con la palabra clave if, seguida de la condición y dos puntos.
# Ejemplo:

# if condition:
#     # code block

my_condition = False

if my_condition:
    print("Se ejecutó el primer bloque de código.")

my_condition = 5 * 2

if my_condition == 10:
    print("Se ejecutó el segundo bloque de código.")

if my_condition > 10:
    print("Es mayor que 10.")
elif my_condition == 10:
    print("Es igual a 10.")
else:
    print("Es menor o igual que 10.")

print('La ejecución continúa...')