### Operadores ###

# Operadores aritméticos
print('Operadores aritméticos')
print(2 + 3) # Suma
print(2 - 3) # Resta
print(2 * 3) # Multiplicación
print(6 / 3) # División
print(4 // 3) # División entera (sin decimales)
print(5 % 3) # Módulo (residuo de la división)
print(2 ** 3) # Potencia  (2^3)

# Operadores aritméticos con strings
print('Operadores aritméticos con strings')
print('Hola ' + 'Python') # Concatenación de cadenas
print('Hola ' + str(3)) # Conversión de entero a cadena
print('Hola ' * 3) # Repetición de cadenas

# Operadores de comparación
print('Operadores de comparación')
print(2 == 3) # Igualdad
print(2 != 3) # Diferente
print(2 > 3) # Mayor que
print(2 < 3) # Menor que
print(2 >= 3) # Mayor o igual que
print(2 <= 3) # Menor o igual que

# Operadores lógicos
print('Operadores lógicos')
print(True and False) # AND
print(True or False) # OR
print(not True) # NOT

# Operadores de asignación
print('Operadores de asignación')
a = 2
a += 3 # a = a + 3
print(a)
a -= 3 # a = a - 3
print(a)
a *= 3 # a = a * 3
print(a)
a /= 3 # a = a / 3
print(a)
a //= 3 # a = a // 3
print(a)
a %= 3 # a = a % 3
print(a)
a **= 3 # a = a ** 3
print(a)

# Operadores de identidad
print('Operadores de identidad')
b = 2
print(a is b) # a es b
print(a is not b) # a no es b

# Operadores de membresía
print('Operadores de membresía')
c = [1, 2, 3]
print(1 in c) # 1 está en c
print(4 not in c) # 4 no está en c

# Operadores de bits
print('Operadores de bits')
print(2 & 3) # AND
print(2 | 3) # OR
print(2 ^ 3) # XOR
print(~2) # NOT
print(2 << 3) # Desplazamiento a la izquierda
print(2 >> 3) # Desplazamiento a la derecha

# Operadores ternarios
print('Operadores ternarios')
d = 2
e = 3
f = d if d > e else e
print(f)
f = d if d < e else e
print(f)
f = d if d == e else e
print(f)
