### Dicts ###
# Un diccionario es una colección de pares clave-valor, donde cada clave es única.

my_dict = dict()
my_other_dict = {} # Inicialmente esto es un diccionario, no un set

print(type(my_dict)) # <class 'dict'>
print(type(my_other_dict)) # <class 'dict'>

my_other_dict = {'Nombre': 'Juan Ginés', 'Apellido': 'Alentà', 'Altura': 1.75, 'Edad' :49, 'Programador': True, 1: 'Javascript'}
print(my_other_dict) # {'nombre': 'Juan Ginés', 'apellido': 'Alentà', 'altura': 1.75, 'programador': True}

my_dict = {'Nombre': 'Juan Ginés', 'Apellido': 'Alentà', 'Altura': 1.75, 'Edad' :49, 'Programador': True, 'Lenguajes': {'Javascript', 'Python', 'Java', 'C#'}}
print(my_dict) # {'Nombre': 'Juan Ginés', 'Apellido': 'Alentà', 'Altura': 1.75, 'Edad': 49, 'Programador': True, 'Lenguajes': {'Java', 'Python', 'Javascript', 'C#'}}

print(len(my_dict)) # 6
print(len(my_other_dict)) # 6

# Acceso a elementos de un diccionario
print(my_dict['Nombre']) # Juan Ginés
print(my_dict['Altura']) # 1.75
# print(my_dict[0]) # KeyError

my_dict['Edad'] = 50 # Modificar un valor
print(my_dict['Edad']) # 50

my_dict['Peso'] = 70 # Añadir un nuevo par clave-valor
print(my_dict) # {'Nombre': 'Juan Ginés', 'Apellido': 'Alentà', 'Altura': 1.75, 'Edad': 50, 'Programador': True, 'Lenguajes': {'Java', 'Python', 'Javascript', 'C#'}, 'Peso': 70}

del my_dict['Peso'] # Eliminar un par clave-valor
print(my_dict) # {'Nombre': 'Juan Ginés', 'Apellido': 'Alentà', 'Altura': 1.75, 'Edad': 50, 'Programador': True, 'Lenguajes': {'Java', 'Python', 'Javascript', 'C#'}}

print('Juan Ginés' in my_dict) # False porque 'Juan Ginés' no es una clave
print('Nombre' in my_dict) # True porque 'Nombre' es una clave

# Métodos de los diccionarios

print(my_dict.keys()) # dict_keys(['Nombre', 'Apellido', 'Altura', 'Edad', 'Programador', 'Lenguajes'])
print(my_dict.values()) # dict_values(['Juan Ginés', 'Alentà', 1.75, 50, True, {'Java', 'Python', 'Javascript', 'C#'}])
print(my_dict.items()) # dict_items([('Nombre', 'Juan Ginés'), ('Apellido', 'Alentà'), ('Altura', 1.75), ('Edad', 50), ('Programador', True), ('Lenguajes', {'Java', 'Python', 'Javascript', 'C#'})])
print(my_dict.get('Nombre')) # Juan Ginés
print(my_dict.fromkeys(('Nombre', 'Apellido', 'Altura'))) # {'Nombre': None, 'Apellido': None, 'Altura': None}

my_new_dict = dict.fromkeys(my_dict, 'Sin valor')
print(my_new_dict) # {'Nombre': 'Sin valor', 'Apellido': 'Sin valor', 'Altura': 'Sin valor', 'Edad': 'Sin valor', 'Programador': 'Sin valor', 'Lenguajes': 'Sin valor'}

my_dict.clear()
print(my_dict) # {}
