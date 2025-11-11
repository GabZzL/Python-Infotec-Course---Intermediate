from collections import Counter

# Counter
# Análisis de frecuencia en textos (palabras más usadas).
# Estadísticas rápidas en colecciones de datos
# Identificación de elementos repetidos en listas.

texto = 'localizacion'

texto_conteo = Counter(texto)
print(texto_conteo)

print('-' * 40)

colores = ['rojo', 'azul', 'amarillo', 'rojo']

colores_conteo = Counter(colores)
print(colores_conteo)
