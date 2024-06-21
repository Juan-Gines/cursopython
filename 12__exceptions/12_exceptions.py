### Exception Handling ###
# Exceptions son errores que ocurren durante la ejecución de un programa.
# El código que puede causar una excepción se coloca en un bloque try.
# El bloque try se sigue de uno o más bloques except.

number_one = 5
number_two = 3
number_two = '3'

# try - except
try:
    print(number_one + number_two)
    print('No se ha producido ninguna excepción')  
except:
    print("Ha ocurrido un error")

# try - except - else
try:
    print(number_one + number_two)
    print('No se ha producido ninguna excepción')    
except:
    print("Ha ocurrido un error")
else:
    print("La suma se ha realizado correctamente")

# try - except - else - finally
try:
    print(number_one + number_two)
    print('No se ha producido ninguna excepción')
except:
    print("Ha ocurrido un error")
else:
    print("La suma se ha realizado correctamente")
finally:
    print("Este bloque se ejecuta siempre")

# Captura de excepciones específicas
try:
    print(number_one + number_two)
    print('No se ha producido ninguna excepción')
except TypeError as e:
    print("Ha ocurrido un error de tipo")
    print(e)

# Captura de la información de la excepción
try:
    print(number_one + number_two)
    print('No se ha producido ninguna excepción')
except Exception as e:
    print("Ha ocurrido un error")
    print(e) # AttributeError: 'Exception' object has no attribute 'add_note'
