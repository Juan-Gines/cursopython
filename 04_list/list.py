### Listas ###
# Las listas son un tipo de dato que permite almacenar varios valores en una sola variable.
# Se pueden definir con corchetes o con la función list()

my_list = [1, 2, 3, 4, 5]
my_other_list = list(('Juan', 'Ginés', 6, 7, 8, 9, 10))

print(len(my_list)) # 5 # Devuelve la longitud de la lista
print(my_list) # [1, 2, 3, 4, 5]
print(my_other_list) # ['Juan', 'Ginés', 6, 7, 8, 9, 10]

print(type(my_list)) # <class 'list'>
print(type(my_other_list)) # <class 'list'>

# Acceso a elementos de una lista
print(my_list[0]) # 1
print(my_list[4]) # 5
print(my_other_list[0]) # 'Juan'
print(my_other_list[-3]) # 8
print(my_other_list.count(9)) # 1 # Cuenta cuantas veces aparece un elemento en la lista
# print(my_other_list[-8]) # IndexError
# print(my_other_list[7]) # IndexError

my_new_list= ["Juan Ginés", 49, "Alentà", 1.75, True]
name, age, surname, height, is_developer = my_new_list
print(name) # 'Juan Ginés'
print(age) # 49
print(surname) # 'Alentà'
print(height) # 1.75
print(is_developer) # True

print(my_list + my_other_list) # [1, 2, 3, 4, 5, 'Juan', 'Ginés', 6, 7, 8, 9, 10]

# Métodos de las listas
my_list.append(6) # Añade un elemento al final de la lista
print(my_list) # [1, 2, 3, 4, 5, 6]

my_list.insert(0, 0) # Añade un elemento en la posición indicada
print(my_list) # [0, 1, 2, 3, 4, 5, 6]

my_list.remove(0) # Elimina el primer elemento que coincida con el valor indicado
print(my_list) # [1, 2, 3, 4, 5, 6]

element = my_list.pop() # Elimina el último elemento de la lista y lo devuelve
print(element) # 6
print(my_list) # [1, 2, 3, 4, 5]

my_list.pop(0) # Elimina el elemento de la posición indicada
print(my_list) # [2, 3, 4, 5]

my_list.reverse() # Invierte el orden de los elementos de la lista
print(my_list) # [5, 4, 3, 2]

my_list.sort() # Ordena los elementos de la lista
print(my_list) # [2, 3, 4, 5]

my_list.clear() # Elimina todos los elementos de la lista
print(my_list) # []

my_list = [1, 2, 3, 4, 5]
my_list_copy = my_list.copy() # Copia la lista
print(my_list_copy) # [1, 2, 3, 4, 5]

my_list_copy.sort(reverse=True) # Ordena los elementos de la lista en orden inverso
print(my_list_copy) # [5, 4, 3, 2, 1]





