from collections import OrderedDict, Counter

# Datos sugeridos
compras = [
 "Luis", "Ana", "Luis", "Carlos", "Marta", "Ana", "Sofía",
"Elena", "Luis", "Carlos"
]

registrados = [
 "Ana", "Carlos", "Marta", "Elena"
]

# Tranformar a lista a sets
compras_set = set(compras)
registrados_set = set(registrados)

# 1. Filtrar clientes nuevos (Diferencia)
clientes_nuevos = compras_set - registrados_set

print(clientes_nuevos)

print('-' * 40)

# 2. Eliminar duplicados y mantener el orden
# OrderedDict, mantiene valores unicos y el orden de insercion
compras_orden_dict = OrderedDict()

for compra in compras:
    compras_orden_dict[compra] = None
    
compras_orden = list(compras_orden_dict.keys())

print(compras_orden)

print('-' * 40)

# 3. Contar cuántas veces se repite cada nombre
contador = Counter(compras)

print(contador)

print('-' * 40)

# 4. Crear un resumen perzonalizado
clientes_dict = {cliente: f'Ha comprado {num} veces' for cliente, num in contador.items() if num > 1}

print(clientes_dict)

print('-' * 40)

# 5. Formato final, Imprime tres bloques
clientes_no_registrados = compras_set - registrados_set

print('Clientes no registrados')
print(clientes_no_registrados)

print('\nClientes unicos')
clientes_unicos = {cliente: num for cliente, num in contador.items() if cliente in clientes_no_registrados and num == 1}
print(clientes_unicos)

print('\nResumen por cliente frecuente (más de 1 compra)')
clientes_frecuentes = {cliente: num for cliente, num in contador.items() if num > 1}
print(clientes_frecuentes)