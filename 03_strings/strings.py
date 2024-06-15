### Strings ###
# Strings son cadenas de texto, se pueden definir con comillas simples o dobles

my_string = 'Mi String'
my_other_string = 'Mi otro String'

print(len(my_string)) # 9
print(len(my_other_string)) # 14

print(my_string + ' ' + my_other_string) # 'Mi String Mi otro String'

my_new_line_string = 'Este es un String\ncon un salto de linea'
print(my_new_line_string) # 'Este es un String\ncon un salto de linea'

my_tab_string = '\tEste es un String con un tabulado'
print(my_tab_string) # '    Este es un String con un tabulado'

my_scape_string = '\\tEste es un String con un \\n escapado'
print(my_scape_string) # '\tEste es un String con un \n escapado'

# Formateo de Strings
name, surname, age = 'Juan Ginés', 'Alentà', 49

print('Hola, me llamo {} {} y tengo {} años'.format(name, surname, age))
print('Hola, me llamo {1} {0} y tengo {2} años'.format(surname, name, age))
print('Hola, me llamo %s %s y tengo %d años' %(surname, name, age))
print('Hola, me llamo ' + name + ' ' + surname + ' y tengo ' + str(age) + ' años')
print(f'Hola, me llamo {name} {surname} y tengo {age} años')

# Desempaquetado de Strings
my_string = 'Python'
a, b, c, d, e, f = my_string
print(a) # 'P'
print(e) # 'o'

# División de Strings
my_string_slice = my_string[0:2]
print(my_string_slice) # 'Py'

my_string_slice = my_string[2:]
print(my_string_slice) # 'thon'

my_string_slice = my_string[:2]
print(my_string_slice) # 'Py'

my_string_slice = my_string[::-1]
print(my_string_slice) # 'nohtyP'

my_string_slice = my_string[-2]
print(my_string_slice) # 'o'

my_string_slice = my_string[-2:]
print(my_string_slice) # 'on'

my_string_slice = my_string[0:6:2]
print(my_string_slice) # 'Pto'

# Métodos de Strings
print(my_string.upper()) # 'PYTHON'
print(my_string.lower()) # 'python'
print(my_string.capitalize()) # 'Python'
print(my_string.replace('P', 'J')) # 'Jython'
print(my_string.find('t')) # 2
print(my_string.find('x')) # -1
print(my_string.count('t')) # 1
print(my_string.split('t')) # ['Py', 'hon']
print("1".isnumeric()) # True
print(my_string.isnumeric()) # False
print(my_string.isalpha()) # True
print(my_string.isalnum()) # True
print(my_string.islower()) # False
print(my_string.startswith('P')) # True
print(my_string.endswith('n')) # True
