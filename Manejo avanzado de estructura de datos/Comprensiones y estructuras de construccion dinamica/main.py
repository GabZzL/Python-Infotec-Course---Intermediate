# List Comprehensions, [expresion for elemento in iterable if condicion]
lista = [numero for numero in range(1, 21) if numero % 2 == 0]

print(lista)

# Dict Comprehensions, {clave: valor for elemento in iterable if condicion}
potencias = {n: n ** 2 for n in range(1, 21) if n % 3 == 0}

print(potencias)