# Herencia

# Hereda atributos y metodos de una clase padre
# Clase base
# Usar jerarquia

class Animales:
    def sonido(self):
        print ('Hacer sonido')

class Perro(Animales):
    def sonido(self):
        print('guau')
        
perro_uno = Perro()

perro_uno.sonido()