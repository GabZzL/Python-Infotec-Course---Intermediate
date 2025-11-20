class Producto():
    # Datos compartidos atraves de todas las instancias
    contador_productos = 0
    # self, indica la instancia
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio
        Producto.contador_productos += 1
    # logicamente pertenece a la clase(no requiere acceso a la clase o instancia)
    @staticmethod
    def es_precio_valido(precio: float) -> bool:
        return precio > 0 and isinstance(precio, float)
    # acceso a la clase
    @classmethod
    def total_productos(cls) -> int:
        return cls.contador_productos
        