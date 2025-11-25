from cliente import Cliente
from producto import Producto
from venta import Venta
from tienda import Tienda

# Crear el cliente
cliente_1 = Cliente('Luis', 'luis@gmail.com', 1000)

# Crear productos
producto_1 = Producto('Teclado', 250)
producto_2 = Producto('Mouse', 150)

# Crear venta y agregar productos
venta_1 = Venta(cliente_1)
venta_1.agregar_productos(producto_1)
venta_1.agregar_productos(producto_2)

# Crear tienda y registrar venta
tienda = Tienda('TechStore')
tienda.registrar_venta(venta_1)

# Mostrar resultado
print(cliente_1.mostrar_info())
print(f'Total de la venta: ${venta_1.total()}')
print(f'Ventas registradas: {len(tienda.ventas)}')
