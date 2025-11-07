import time
# DECORADORES

# Funcion basica
def mi_decorador(funcion):
    def nueva_funcion():
        print('Antes de la funcion')
        funcion()
        print('Despues de la funcion')
    return nueva_funcion
        
    
@mi_decorador
def saludar():
    print('Hola!')
    
@mi_decorador
def despedir():
    print('Adios!')

saludar()
despedir()

# Medir tiempo
def medir_tiempo(funcion):
    def wrapper():
        inicio = time.time()
        funcion()
        fin = time.time()
        
        print(f'Tiempo: {fin - inicio:.4f} segundos')
    return wrapper
        
@medir_tiempo
def contar():
    suma = 0
    for i in range(1000000):
        suma += i
        
    print('suma terminada')

contar()

# Decorador con argumentos
def repetir(n):
    def decorador(funcion):
        def wrapper():
            for _ in range(n):
                funcion()
        return wrapper
    return decorador

@repetir(3)
def hola():
    print('hola mundo!')
    
hola()