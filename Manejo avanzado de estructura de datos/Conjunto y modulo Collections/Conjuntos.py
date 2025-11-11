# Subconjunto

# Validar permisos.
# Comprobar si una lista de requisitos está cubierta por otra lista mayor.
# Comparar relaciones de inclusión entre grupos de datos.

a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
c = {1, 2, 3}

print(a.issubset(b))
print(a <= b)
#  <= permite igualdad, < exige que tenga menos elementos
print(a <= c)
print(a < c)

print('-' * 40)

# Superconjunto

# Verificar que una colección de datos incluya a otra completamente.
# Comprobar que un conjunto de permisos contiene a los de otro rol.
# Comparar listas de inventario o catálogos completos, contra otros parciales.

print(b.issuperset(a))
print(b >= a)
# superconjunto y un superconjunto propio
print(a > c)
print(a >= c)

print('-' * 40)

# Conjuntos disjunto, no comparten ningún elemento en común

# Comprobar que dos colecciones de datos no tienen solapamiento.
# Validar listas de valores permitidos/prohibidos.
# Simplificar operaciones lógicas en clasificación de conjuntos.
permitidos = {'pera', 'sandia', 'limon'}
prohibidos = {'banana', 'uva'}

print(permitidos.isdisjoint(prohibidos))

print('-' * 40)

# Diferencia

# Comparar dos colecciones de datos para ver qué falta en una lista respecto a otra.
# Detectar registros exclusivos en un dataset.
# Filtrar elementos de una lista eliminando duplicados que existen en otra
permitidos_dos = {'pera', 'coco', 'naranja'}

print(permitidos.difference(permitidos_dos))

print('-' * 40)

# Diferencia simetrica

# Detectar diferencias exclusivas entre dos listas de datos.
#  Comparar inventarios para saber qué productos pertenecen solo a un conjunto
# Identificar cambios entre versiones de un conjunto de registros.
print(permitidos.symmetric_difference(permitidos_dos))

print('-' * 40)

# Interseccion

# Detectar coincidencias entre listas
# Encontrar registros duplicados en diferentes bases de datos
# Extraer valores comunes en análisis de datos.
print(permitidos.intersection(permitidos_dos))

print('-' * 40)

# Union

# Fusionar datos de varias fuentes sin duplicados.
# Combinar listas de usuarios, productos o registros.
# Crear colecciones globales a partir de subconjuntos

print(permitidos.union(permitidos_dos))
print(permitidos.union(prohibidos))\
    
print('-' * 40)

# Update

# Fusionar datos de diferentes fuentes en un solo conjunto.
# Agregar múltiples valores de una lista sin necesidad de usar un bucle.
# Garantizar que no haya duplicados al ampliar un conjunto.

list_1 = {1, 2, 3}
list_2 = {4, 5, 6}

list_1.update(list_2)

letras = {'a', 'b'}
letras.update('cde')

print(list_1)
print(letras)

