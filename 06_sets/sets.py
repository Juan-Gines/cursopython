### Sets ###
# Sets son una colección desordenada y no indexada de elementos. Se pueden definir con llaves o con la función set()

my_set = set()  
my_other_set = {} # Inicialmente esto es un diccionario, no un set

print(type(my_set)) # <class 'set'>
print(type(my_other_set)) # <class 'dict'>

my_other_set = {'Juan Ginés', 'Alentà', 1.75, True}
print(type(my_other_set)) # <class 'set'>

print(len(my_other_set)) # 4

# Acceso a elementos de un set
# print(my_other_set[0]) # TypeError
# print(my_other_set[4]) # TypeError
# No se puede acceder a elementos de un set porque no están indexados

# métodos de los sets
my_other_set.add(49)
print(my_other_set) # {True, 1.75, 'Alentà', 'Juan Ginés', 49}
my_other_set.add(49) # No se añade porque ya existe
print(my_other_set) # {True, 1.75, 'Alentà', 'Juan Ginés', 49}

print("Alentà" in my_other_set) # True
print("alenta" in my_other_set) # False

my_other_set.remove(49)
print(my_other_set) # {True, 1.75, 'Alentà', 'Juan Ginés'}

my_other_set.clear()
print(my_other_set) # set()
print(len(my_other_set)) # 0

my_set = {'Juan Ginés', 'Alentà', 1.75, True}

my_other_set = {'Javascript', 'Python', 'Java', 'C#'}

my_new_set = my_set.union(my_other_set)
print(my_new_set) # {True, 1.75, 'Alentà', 'Juan Ginés', 'Python', 'Java', 'Javascript', 'C#'}

print(my_new_set.difference(my_set)) # {'Python', 'Java', 'Javascript', 'C#'}

my_new_set.issubset(my_set) # False los elementos de my_new_set no están en my_set
my_new_set.issuperset(my_set) # True los elementos de my_set están en my_new_set