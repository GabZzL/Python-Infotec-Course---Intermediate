# FUNCIONES DE ORDEN SUPERIOR

# Funciones basicas
def aplicar_funcion(f, valor):
    return f(valor)

def cuadrado(x):
    return x * x

print(aplicar_funcion(cuadrado, 5))

# map, map(funcion, iterable)
numeros = [1, 2, 3, 4, 5]

duplicados = list(map(lambda x: x * 2, numeros))
print(duplicados)

# map, convertir a mayusculas
palabras = ['hola', 'perdon', 'corazon']

palabras_mayusculas = list(map(lambda palabra: palabra.upper(), palabras))
print(palabras_mayusculas)

# map, longitudes de palabras
longitudes = list(map(lambda palabra: len(palabra), palabras))
print(longitudes)

# map, usando funciones definidas con 'def'
def capitalizar(palabra):
    return palabra.capitalize()

palabras_capitalizadas = list(map(capitalizar, palabras))
print(palabras_capitalizadas)