# FILTER

# Filter, funcion basica
numeros = [1, 2, 3, 4, 5, 6]

pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)

# Filter, palabras largas
palabras = ['mar', 'espectacular', 'uva', 'extremo']

palabras_largas = list(filter(lambda palabra: len(palabra) > 4, palabras))
print(palabras_largas)

# Filter, valores positivos
valores = [-1, 5, 22, -100, 0]

valores_positivos = list(filter(lambda valor: valor > 0, valores))
print(valores_positivos)

# Filter, usando 'def'
def obtener_negativos(valor):
    # retornar un valor boleano
    return valor < 0

valores_negativos = list(filter(obtener_negativos, valores))
print(valores_negativos)