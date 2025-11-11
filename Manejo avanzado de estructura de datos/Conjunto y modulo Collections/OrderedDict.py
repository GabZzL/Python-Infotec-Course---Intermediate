from collections import OrderedDict

# OrderedDict
# Mantener el orden de claves en reportes o exportaciones.
# Reorganizar datos dinámicamente según criterios específicos.
# Comparar estructuras de datos donde el orden es relevante.

datos = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('z', 30)])
datos.move_to_end('a')
datos.move_to_end('z', last=False)

print(datos)