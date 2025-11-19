from abc import ABC, abstractmethod

# Clases Abstractas

# establece una interfaz base, para las clases derivadas

class Animal(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
        
    @abstractmethod
    def hacer_sonido(self):
        pass
    
    def describir(self):
        return 'Animales'

class Perro(Animal):
    def hacer_sonido(self):
        return 'Guau'
    
class Gato(Animal):
    def hacer_sonido(self):
        return 'Miau'
    
# Deteccion de instancias

gato_1 = Gato('Minino')
nombre_1 = gato_1.nombre

print(nombre_1)

print(issubclass(Perro, Animal))
print(isinstance(gato_1, Animal))