from abc import abstractmethod, ABC

# Clase abstracta, clase base para las demas
class Usuario(ABC):
    def __init__(self, nombre: str, correo: str):
        self.nombre = nombre
        self.correo = correo
    # Metodo que debera ser implementado para las subclases
    @abstractmethod
    def mostrar_info(self) -> str:
        pass