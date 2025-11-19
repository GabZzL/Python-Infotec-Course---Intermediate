# Decoradores

# Modificar su ejecución
# Convertir su tipo de comportamiento
# Agregar lógica auxiliar sin cambiar su cuerpo

# @classmethod
class Producto:
    iva = 0.16 # Atributo de clase
    
    def __init__(self, precio):
        self.precio = precio
    
    # metodo a metodo de clase
    # se asocia a la clase
    @classmethod
    def cambiar_iva(cls, nuevo_precio):
        cls.iva = nuevo_precio

Producto.cambiar_iva(0.18)
print(Producto.iva)

# @staticmethod
# método no necesita ni self ni cls.
# Se desea mantener funciones auxiliares
class Matematica:
    @staticmethod
    def es_par(n):
        return n % 2 == 0
    
print(Matematica.es_par(4))

# Decoradores personalizados
def registrar_llamada(func):
    def wrapper(*args, **kwargs):
        print('-' * 40)
        print(f'Funcion: {func.__name__}')
        result = func(*args, **kwargs)
        return result
    
    return wrapper

class Saludo:
    @registrar_llamada
    def decir_hola(self):
        print('Hola')

saludo_uno = Saludo()

saludo_uno.decir_hola()

# Decoradores con parametros
def repetir(n):
    def decorador(func):
        def wrapper(*args, **kwargs):
            print('-' * 40)
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorador

class Alerta:
    @repetir(3)
    def mensaje(self):
        print('ALERTA!!!')
        
a = Alerta()
a.mensaje()

'''
Si se desea aplicar múltiples decoradores, el orden es importante. Primero se
aplica el decorador más interno (el más cercano a la función), y luego los
externos

@staticmethod
@mi_decorador --> se aplica primero
def metodo():
    ....
'''