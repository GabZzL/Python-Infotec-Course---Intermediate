# Agregacion

# El objeto puede existir, independientemente del contenedor
# Instancia como argumento
# Se puede compartir entre multiples objetos
# Relacion debil

class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre

class Universidad:
    def __init__(self):
        self.profesores = []
        
    def agregar_profesor(self, profesor):
        self.profesores.append(profesor)
        
    def mostrar_profesores(self):
        for profesor in self.profesores:
            print(profesor.nombre)
        
profesor_uno = Profesor('Carlos')
profesor_dos = Profesor('Alan')
profesor_tres = Profesor('Juan')

tec = Universidad()

tec.agregar_profesor(profesor_uno)
tec.agregar_profesor(profesor_dos)
tec.agregar_profesor(profesor_tres)

tec.mostrar_profesores()