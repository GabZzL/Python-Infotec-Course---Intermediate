# Composicion

# Contiene instancias de otras clases
# Instancia dentro del contructor(__init__)
# fuerte dependencia

class Motor:
    def encender(self):
        print('Motor encendido')

class Auto:
    def __init__(self):
        self.motor = Motor()
        
    def arrancar(self):
        self.motor.encender()
        
auto_uno = Auto()

auto_uno.arrancar()