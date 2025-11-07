from functools import reduce

# REDUCE

# Reduce, funcion basica
numeros = [1, 2, 3, 4, 5]

suma = reduce(lambda x, y: x + y, numeros)
print(suma)

# Reduce, multiplicar todos los numeros
multiplicacion = reduce(lambda x, y: x * y, numeros)
print(multiplicacion)

# Reduce, concatenar palabras
palabras = ['python', 'es', 'genial']

oracion = reduce(lambda palabra_1, palabra_2: palabra_1 + " " + palabra_2, palabras)
print(oracion)