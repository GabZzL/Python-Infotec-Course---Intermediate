from collections import defaultdict

# defaultdict
# Contadores acumulativos (con int).
# Agrupar valores sin inicializar listas manualmente.
# Inicializar estructuras complejas de forma automática.

pares = [('rojo', 1), ('azul', 2), ('rojo', 3), ('rojo', 4)]

pares_default = defaultdict(list)

for color, numero in pares:
    pares_default[color].append(numero)

print(pares_default)

print('-' * 40)

nombres_default = defaultdict(str)

nombres_default[1] = 'victor'
nombres_default[2] = 'jose'
nombres_default[3] 

print(nombres_default)