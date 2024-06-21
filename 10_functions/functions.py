### Functions ###
# Functions son bloques de código que se ejecutan cuando se les llama.
# Se pueden pasar datos, llamados parámetros, a una función.
# Una función puede devolver datos como resultado.

def my_function():
    print("Hola desde una función")

my_function() # Hola desde una función

def sum(a, b):
    print(a + b)

sum(5, 3) # 8

def sum(a, b):
    return a + b

result = sum(10, 5)
print(result) # 15

def sum(a, b):
    if type(a) == int and type(b) == int:
        return a + b
    else:
        return "Los argumentos deben ser números enteros"
    
result = sum(10, 5)
print(result) # 15
result = sum(10, "5")
print(result) # Los argumentos deben ser números enteros

def print_name_with_default(name="Juan"):
    print(name)

print_name_with_default() # Juan
print_name_with_default("Ginés") # Ginés

def print_list(my_list):
    for element in my_list:
        print(element)

print_list([1, 2, 3, 4, 5]) # 1 2 3 4 5

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())

print_upper_texts("Hola", "desde", "una", "función") # HOLA DESDE UNA FUNCIÓN