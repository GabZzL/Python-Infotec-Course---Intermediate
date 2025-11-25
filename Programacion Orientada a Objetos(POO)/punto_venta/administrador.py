from usuario import Usuario
# Subclase de la clase Usuario
class Administrador(Usuario):
    def __init__(self, nombre: str, correo: str, permisos: list[str]):
        super().__init__(nombre, correo)
        self.permisos = permisos
        
    def mostrar_info(self) -> str:
        return f'Administrador: {self.nombre}, Correo: {self.correo}, Permisos: {', '.join(self.permisos)}'