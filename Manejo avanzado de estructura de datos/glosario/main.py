from collections import ChainMap, Counter, defaultdict, deque, namedtuple, OrderedDict

# ChainMap, agrupar diccionarios
dict1 = {'a': 1, 'b':2}
dict2 = {'c': 3, 'd': 4}

cm = ChainMap(dict1, dict2)

print(cm)
print(cm['c'])

print('-' * 50)

# Conjuntos disjuntos, no comparten elementos
list_1 = {1, 2, 3}
list_2 = {3, 4, 5}
list_3 = {4, 5, 6}

print(list_1.isdisjoint(list_2))
print(list_1.isdisjoint(list_3))

print('-' * 50)

# Counter, frecuencia de elementos
paises = ['canada', 'us', 'us', 'mexico', 'canada', 'us']
conteo = Counter(paises)

print(conteo)

print('-' * 50)

# DefaultDict, variante de diccionario (valor default)
def default_score():
    return 50

player_score = defaultdict(default_score)

player_score['Juan'] = 78
player_score['Daniel'] = 90
player_score['Jony']

print(player_score)

print('-' * 50)

# Deque, insertar, y eliminar datos en ambos extremos
numeros = deque([1, 2, 3])

numeros.append(4)
numeros.appendleft(0)
numeros.appendleft(-1)

print(numeros)

numeros.pop()
numeros.popleft()

print(numeros)

print('-' * 50)

# Dict Comprehension, creacion de diccionarios en una sola linea
cuadrados_dict = {x: x**2 for x in range(1, 20)}

print(cuadrados_dict)

print('-' * 50)

# Diferencia, obtener elementos que entan en primer conjunto pero no es el segundo
a = {1, 2, 3}
b = {2, 3, 4}

print(a - b)

print('-' * 50)

# Diferencia Simetrica, tomar elementos que no se comparten
print(a ^ b)

print('-' * 50)

# Interseccion, conjunto con elementos que se repiten
print(a & b)

print('-' * 50)

# List Comprehension, expresion compacta para crear listas
cuadrados_list = [x**2 for x in range(1, 20)]

print(cuadrados_list)

print('-' * 50)

# NamedTuple, tupla en la que se puede acceder por nombre
Persona = namedtuple('Persona', ['nombre', 'edad'])
p1 = Persona('Ivan', 24)

print(p1.nombre)
print(p1.edad)

print('-' * 50)

# OrderedDict, mantiene el orden de insercion de los elementos
dict_orden = OrderedDict()
values = ['a', 'b', 'c', 'd']
i = 1

for value in values:
    dict_orden[value] = i
    i += 1

print(dict_orden)

print('-' * 50)

# Set, almacenar elementos unicos y evita duplicados
# performan operaciones como union, interseccion, y diferencia
animales = {'perro', 'gato', 'gato', 'perico'}

print(animales)

print('-' * 50)

# Subconjunto, un conjunto A es subconjunto de B, si todos sus elementos están contenidos en B.
conjunto_a = {1, 2}
conjunto_b = {1, 2, 3, 4}
conjunto_c = {11, 12}

print(conjunto_a.issubset(conjunto_b))
print(conjunto_c.issubset(conjunto_b))

print('-' * 50)

# Superconjunto, Un conjunto A es un superconjunto de B, si contiene todos los elementos de b
conjunto_d = {1, 2, 3, 4, 5}

print(conjunto_d.issuperset(conjunto_b))
print(conjunto_a.issuperset(conjunto_b))

print('-' * 50)

# Union, produce un nuevo conjunto con los elementos unicos presente al meno en uno de ellos
print(conjunto_a | conjunto_b)

print('-' * 50)

#Update, agregar varios elementos a un conjunto desde otro iterable, sin duplicados:
conjunto_b.update(conjunto_c)
print(conjunto_b)