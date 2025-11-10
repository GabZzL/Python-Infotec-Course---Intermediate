from functools import reduce
from functools import wraps
import time

# Generador de datos
tempuraturas_datos = [("CDMX", 26), ("Monterrey", 34), ("Toluca", 19), ("Cancún", 38), ('Oaxaca', 30)]
registros = []

def leer_temparaturas(registros):    
    for registro in registros:
        yield registro
        
for temperatura in leer_temparaturas(tempuraturas_datos):
    registros.append(temperatura)

# Filtrado con filter() y Lambda
temperaturas_mayores = list(filter(lambda registro: registro[1] >= 30, registros))

# Tranformacion con map() y Lambda
alertas = list(map(lambda registro: f'Alerta de calor en {registro[0]}: {registro[1]}°C.', temperaturas_mayores))

# Ordenamiento con sorted() y Lambda
temperaturas_ordenadas = list(sorted(temperaturas_mayores))

# Resumen con reduce()
temparaturas_valores = list(map(lambda valor: valor[1], temperaturas_ordenadas))
suma_temperaturas = reduce(lambda x, y: x + y, temparaturas_valores)

promedio_temperaturas = suma_temperaturas / len(temparaturas_valores)

# Decorador perzonalizado
def auditar_funcion(funcion):
    # Variable para contar el numero de llamadas
    n = 0
    # Preversar metadatos de la funcion originial
    @wraps(funcion)
    # El decorador puede aceptar argumentos posicionales o por nombre
    def wrapper(*args, **kwargs):
        # Inicio de ejecucion
        inicio = time.time()
        # Imprimir nombre de la funcion
        print('\n' + '-' * 40)
        print(f'Nombre de la funcion: {funcion.__name__}')
        # Habilitar el retorno de valores para la funcion wrapper()
        resultado = funcion(*args, **kwargs)
        # Aumentar el numero de llamadas de la funcion
        nonlocal n
        n += 1
        # Fin de ejecucion
        fin = time.time()
        # Veces que la funcion fue llamada
        print(f'Veces que la funcion fue llamada: {n}')
        # Tiempo de ejecucion
        print(f'Tiempo de ejecucion: {fin - inicio:.4f}')
        return resultado
        
    return wrapper

# Aplicar el decorador a la funcion imprimir
@auditar_funcion
def imprimir(datos):
    print(datos)
# Ejecutar la funcion
imprimir(temperaturas_ordenadas)
imprimir(temparaturas_valores)
# Mostrar el promedio de las temperaturas
print('\n' + '-' * 40)
print(f'Temperatura promedio de alertas: {promedio_temperaturas}°C')


