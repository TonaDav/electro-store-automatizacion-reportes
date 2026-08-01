from modelos import Producto, Vendedor, Cliente, Inventario, Venta
from random import randint, choice
from datetime import datetime, timedelta

# Productos
productos = [Producto(1, "Arduino Uno R3", "Placas de Desarrollo", 45, 30),
             Producto(2, "ESP32 Dev Board", "Placas de Desarrollo", 38.50, 25),
             Producto(3, "Raspberry Pi 5 (4GB)", "Placas de Desarrollo", 420, 8),
             Producto(4, "Raspberry Pi Pico", "Placas de desarrollo", 22.00, 40),
             Producto(5, "Sensor ultrasónico HC-SR04", "Módulos y sensores", 8.50, 60),
             Producto(6, "Módulo Bluetooth HC-05", "Módulos y sensores", 15.00, 35),
             Producto(7, "Sensor DHT11 (temp/humedad)", "Módulos y sensores", 9.90, 50),
             Producto(8, "Módulo relé 4 canales", "Módulos y sensores", 18.00, 20),
             Producto(9, "Kit de resistencias (600 pzas)", "Componentes electrónicos", 12.00, 15),
             Producto(10, "Kit de capacitores cerámicos", "Componentes electrónicos", 14.50, 15),
             Producto(11, "LEDs 5mm (paquete x100)", "Componentes electrónicos", 10.00, 25),
             Producto(12, "Protoboard 830 puntos", "Componentes electrónicos", 7.50, 45),
             Producto(13, "Batería 18650 (3.7V, 2600mAh)", "Fuentes y energía", 12.90, 40),
             Producto(14, "Fuente AC-DC 12V 2A", "Fuentes y energía", 25.00, 20),
             Producto(15, "Cargador para batería LiPo", "Fuentes y energía", 22.00, 18),
             Producto(16, "Cautín 30W con soporte", "Herramientas y soldadura", 28.00, 12),
             Producto(17, "Estaño para soldar (rollo 50g)", "Herramientas y soldadura", 9.50, 30),
             Producto(18, "Kit chasis para robot 2WD", "Robótica y kits", 55.00, 10)]

# Vendedores
vendedores = [Vendedor(1, "Ana", "Torres Prado", "ana.torres@electrostore.pe"),
              Vendedor(2, "Diego", "Castillo Velarde", "diego.castillo@electrostore.pe"),
              Vendedor(3, "Tomas", "Davila Naveda", "tonadavnav05@gmail.com")]

# Clientes
clientes = [Cliente(1, "Carlos", "Ramírez Cornejo", "carlos.ramirez@gmail.com"),
            Cliente(2, "Lucía", "Mendoza Shua", "lucia.mendoza@gmail.com"),
            Cliente(3, "Jorge", "Salazar Mejía", "jorge.salazar@hotmail.com"),
            Cliente(4, "Fiorella", "Vargas Calderón", "fiorella.vargas@gmail.com"),
            Cliente(5, "Renzo", "Huamán Mendoza", "renzo.huaman@outlook.com"),
            Cliente(6, "Camila", "Rojas Gutierrez", "camila.rojas@gmail.com"),
            Cliente(7, "Miguel", "Espinoza Manzanal", "miguel.espinoza@gmail.com"),
            Cliente(8, "Andrea", "Flores Valera", "andrea.flores@hotmail.com")]

# Inventario
def generar_datos():
    inventario = Inventario()

    for producto in productos:
        inventario.agregar_producto(producto)

    for vendedor in vendedores:
        inventario.agregar_vendedor(vendedor)

    for cliente in clientes:
        inventario.agregar_cliente(cliente)

    # Producto, cliente, vendedor al azar
    mi_catalogo = inventario.get_productos()
    mis_vendedores = inventario.get_vendedores()
    mis_clientes = inventario.get_clientes()

    id_venta = 1

    for item in range(1, 51):
        producto = choice(list(mi_catalogo.values()))
        cliente = choice(list(mis_clientes.values()))
        vendedor = choice(list(mis_vendedores.values()))

        # entre 1 y 5 unidades
        cantidad = randint(1, 5)

        # genera fecha dentro de un rango (e.g. ultima semana, ultimo mes)
        hoy = datetime.now().date()
        dias = randint(1, 7)
        fecha = hoy - timedelta(days=dias)

        try:
            inventario.registrar_venta(Venta(id_venta, producto, cliente, vendedor, cantidad, fecha))
            id_venta += 1
        except ValueError as error:
            print(error)

    return inventario

# Aquí estamos diciendo que vamos a correr esta función
# solo cuando ejecutemos este script directamente
if __name__ == "__main__":
    mi_inventario = generar_datos()