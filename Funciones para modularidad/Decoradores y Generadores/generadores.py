# GENERADORES

# Generador basico
def contar():
    yield 1
    yield 2
    yield 3
    
for numero in contar():
    print(numero)
    
# Generador con bucle
def cuadrados(n):
    for i in range(n):
        yield i ** 2

for valor in cuadrados(5):
    print(valor)
    
# Generador infinito
def numeros_infinitos():
    n = 1
    while True:
        yield n
        n += 1
        
for numero in numeros_infinitos():
    if numero > 5:
        break
    
    print(numero)