# Variables
# La variable es un espacio de memoria que se utiliza para almacenar valores.
# La convención de nombres de variables en Python es snake_case.

my_string_variable = 'My String variable'
my_integer_variable = 5
my_float_variable = 5.5
my_complex_variable = 5 + 5j
my_boolean_variable = True
my_list_variable = [1, 2, 3]
my_tuple_variable = (1, 2, 3)
my_set_variable = {1, 2, 3}
my_dict_variable = {1: "uno", 2: "dos", 3: "tres"}

# Concatena variables en el print con un separador
print(my_string_variable, my_integer_variable, my_float_variable, my_complex_variable, my_boolean_variable, my_list_variable, my_tuple_variable, my_set_variable, my_dict_variable, sep='\n')
print(type(print(my_string_variable))) # <class 'NoneType'>

# Transformar un tipo de dato a otro
my_integer_variable_to_string = str(my_integer_variable)
print(type(my_integer_variable_to_string)) # <class 'str'>

# Algunas funciones del sistema
print(len(my_string_variable)) # 18 caracteres

# Variables en una sola línea
a, b, c = 1, 2, 3
name, age, country = 'John', 25, 'USA'
print(a, b, c, name, age, country)

# Inputs
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')
print(f'Hola {name}, tienes {age} años')

# Convertir un tipo de dato a otro, aprovechando que python es dinámico y de tipado no fuerte
name = 35
age = 'John'
print(f'Hola {name}, tienes {age} años')

# ¿Forzamos el tipo de dato?
address: str = 'Calle 123'
address = 123
print(type(address)) # <class 'int'>