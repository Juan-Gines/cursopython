### Tuples ###
# Tuples son una colección ordenada e inmutable de elementos. Se pueden definir con paréntesis o con la función tuple()

my_tuple = tuple()
my_other_tuple = ()

print(len(my_tuple)) # 0

my_tuple = (49, 'Juan Ginés', 'Alentà', 1.75, True)
print(my_tuple) # (49, 'Juan Ginés', 'Alentà', 1.75, True)
print(type(my_tuple)) # <class 'tuple'>

# Acceso a elementos de una tupla
print(my_tuple[0]) # 49
print(my_tuple[4]) # True
print(my_tuple[-1]) # True
print(my_tuple[-3]) # 'Alentà'
# print(my_tuple[-6]) # IndexError
# print(my_tuple[5]) # IndexError

name, age, surname, height, is_developer = my_tuple
print(name) # 49
print(age) # 'Juan Ginés'
print(surname) # 'Alentà'
print(height) # 1.75
print(is_developer) # True

# métodos de las tuplas
print(my_tuple.count(49)) # 1 # Cuenta cuantas veces aparece un elemento en la tupla
print(my_tuple.index('Alentà')) # 2 # Devuelve el índice del primer elemento que coincida con el valor indicado
# my_tuple[0] = 50 # TypeError
# my_tuple.append(50) # AttributeError
# my_tuple.insert(0, 50) # AttributeError
# my_tuple.remove(49) # AttributeError
# my_tuple.pop() # AttributeError
# my_tuple.reverse() # AttributeError
# my_tuple.sort() # AttributeError
# my_tuple.clear() # AttributeError
# my_tuple_copy = my_tuple.copy() # AttributeError
# my_tuple.extend((50, 51, 52)) # AttributeError
# my_tuple += (50, 51, 52) # AttributeError
# no se puede sobreescribir una tupla, pero si se puede sobreescribir una variable que contenga una tupla

my_other_tuple = (50, 51, 52)
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple) # (49, 'Juan Ginés', 'Alentà', 1.75, True, 50, 51, 52)

print(my_tuple * 2) # (49, 'Juan Ginés', 'Alentà', 1.75, True, 49, 'Juan Ginés', 'Alentà', 1.75, True)

print(my_tuple[0:3]) # (49, 'Juan Ginés', 'Alentà')

del my_other_tuple
# print(my_other_tuple) # NameError
