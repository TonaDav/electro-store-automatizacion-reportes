from modelos import Producto, Cliente, Vendedor, Venta, Inventario

# Creamos el inventario vacío
inventario = Inventario()

# Creamos algunos productos de prueba
arduino = Producto(1, "Arduino Uno R3", "Placas de desarrollo", 45.00, 30)
esp32 = Producto(2, "ESP32 Dev Board", "Placas de desarrollo", 38.50, 25)
raspberry = Producto(3, "Raspberry Pi 5", "Placas de desarrollo", 420.00, 8)

inventario.agregar_producto(arduino)
inventario.agregar_producto(esp32)
inventario.agregar_producto(raspberry)

# Creamos un cliente y un vendedor de prueba
cliente1 = Cliente(1, "Carlos", "Ramírez", "carlos@email.com")
vendedor1 = Vendedor(1, "Ana", "Torres", "ana@electrostore.pe")

inventario.agregar_cliente(cliente1)
inventario.agregar_vendedor(vendedor1)

# Registramos algunas ventas de prueba
venta1 = Venta(1, arduino, cliente1, vendedor1, 3, "2026-07-28")
venta2 = Venta(2, esp32, cliente1, vendedor1, 5, "2026-07-29")
venta3 = Venta(3, arduino, cliente1, vendedor1, 2, "2026-07-30")

inventario.registrar_venta(venta1)
inventario.registrar_venta(venta2)
inventario.registrar_venta(venta3)

# Probamos que __str__ funciona bien en cada clase
print(cliente1)
print(vendedor1)
print(venta1)

print()

# Probamos los métodos de Inventario
print("Ingresos totales:", inventario.ingresos_totales())
print("Producto más vendido:", inventario.producto_mas_vendido())
print("Mejor vendedor:", inventario.mejor_vendedor())
print("Cliente más frecuente:", inventario.cliente_mas_frecuente())
print("Productos con bajo stock:", [p.nombre for p in inventario.productos_bajos_stock(umbral=10)])

# Verificamos que el stock se redujo correctamente
print("\nStock actual de Arduino:", arduino.stock)  # debería ser 30 - 3 - 2 = 25
print("Stock actual de ESP32:", esp32.stock)         # debería ser 25 - 5 = 20