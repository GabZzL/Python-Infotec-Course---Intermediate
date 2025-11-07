# SORTED

# Sorted, funcion basica
numeros = [4, 1, -2, 100, 0]

ordenados = sorted(numeros)
print(ordenados)

# Sorted, Ordenar palabras alfabeticamente
palabras = ['Zorro', 'Alebrije', 'Musica', 'Beso']

palabras_ordenadas = sorted(palabras)
print(palabras_ordenadas)

# Sorted, Ordenar por longitud de palabras
palabras_longitud = sorted(palabras, key=len)
print(palabras_longitud)

# Sorted, Ordenar por longitus en descendente
palabras_decendente = sorted(palabras, key=len, reverse=True)
print(palabras_decendente)