from collections import namedtuple

# NamedTuple
# Representar registros de datos de forma clara (personas, vehículos, productos)
# Estructuras inmutables fáciles de leer y documentar.
# Situaciones donde se necesita algo más legible que una tupla, pero más ligero que una clase.


Animal = namedtuple('Animal', ['nombre', 'edad'])
a = Animal(nombre='Kali', edad=5)

print(a)
print(a.nombre)
print(a.edad)