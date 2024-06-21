### Classes ###
# Classes son plantillas para crear objetos.
# Un objeto tiene propiedades y métodos (funciones) asociados.

class MyClass:
    x = 5

print(MyClass) # <class '__main__.MyClass'>
print(MyClass.x) # 5

class Person:
    pass
    def __init__(self, name, surname, age = None): # Método constructor
        self.full_name = f'{name} {surname}' # Propiedad pública
        self.__name = name  # Propiedad privada
        self.__surname = surname # Propiedad privada
        self.__age = age # Propiedad privada
    
    def get_name(self):
        return self.__name
    
    def get_surname(self):
        return self.__surname
    
    def get_age(self):
        return self.__age
    
my_person = Person("Juan", "García", 30)
print(my_person.full_name) # Juan García
print(my_person.get_name()) # Juan
print(my_person.get_surname()) # García
print(my_person.get_age()) # 30

my_person.full_name = "Ginés García"
print(my_person.full_name) # Ginés García
print(my_person.get_name()) # Juan
print(my_person.get_surname()) # García
print(my_person.get_age()) # 30

