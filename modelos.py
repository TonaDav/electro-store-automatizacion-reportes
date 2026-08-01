from collections import defaultdict
# Aquí encontramos las entidades del dominio del problema.
class Producto:
    def __init__(self, id_producto, nombre, categoria, precio, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def __str__(self):
        # return f"[Id Producto: {self.id_producto} / Nombre: {self.nombre} / Categoria: {self.categoria} / Precio: {self.precio:1.2f} / Stock: {self.stock}]"
        return "[Id Producto: {id} / Nombre: {nombre} / Categoria: {categoria} / Precio: S/.{precio:1.2f} / Stock: {stock}]".format(id = self.id_producto, nombre = self.nombre, categoria = self.categoria, precio = self.precio, stock = self.stock)

    def reducir_stock(self, cantidad):
        if cantidad > self.stock:
            raise ValueError(f"Sin unidades suficientes (Stock actual: {self.stock}) (Cantidad pedida: {cantidad})")
        self.stock = self.stock - cantidad

class Cliente:
    def __init__(self, id_cliente, nombres, apellidos, email):
        self.id_cliente = id_cliente
        self.nombres = nombres
        self.apellidos = apellidos
        self.email = email
        self.nombre_completo = self.nombres + " " + self.apellidos

    def __str__(self):
        # return f"[Id Cliente: {self.id_cliente} / Nombre: {self.nombre_completo} / Email: {self.email}]"
        return "[Id Cliente: {id} / Nombre: {nombre} / email: {email}]".format(id = self.id_cliente, nombre = self.nombre_completo, email = self.email)

class Vendedor:
    def __init__(self, id_vendedor, nombres, apellidos, email):
        self.id_vendedor = id_vendedor
        self.nombres = nombres
        self.apellidos = apellidos
        self.email = email
        self.nombre_completo = self.nombres + " " + self.apellidos

    def __str__(self):
        return f"[Id Vendedor: {self.id_vendedor} / Nombre: {self.nombre_completo} / Email: {self.email}]"

class Venta:
    def __init__(self, id_venta, producto, cliente, vendedor, cantidad, fecha):
        self.id_venta = id_venta
        self.producto = producto
        self.cliente = cliente
        self.vendedor = vendedor
        self.cantidad = cantidad
        self.fecha = fecha

    def __str__(self):
        return f"[Id Venta: {self.id_venta} / Producto: {self.producto.nombre} / Cantidad: {self.cantidad} unid. / Vendedor: {self.vendedor.nombre_completo} / Total: S/.{self.calcular_total():1.2f}]"

    def calcular_total(self):
        return self.cantidad*self.producto.precio

class Inventario:
    def __init__(self):
        self.productos = {}
        self.clientes = {}
        self.vendedores = {}
        self.ventas = []

    def get_productos(self):
        return dict(self.productos) # Con dict() devolvemos una copia, mas no una referencia directa al diccionario original.

    def get_clientes(self):
        return dict(self.clientes) # Con dict() devolvemos una copia, mas no una referencia directa al diccionario original.

    def get_vendedores(self):
        return dict(self.vendedores) # Con dict() devolvemos una copia, mas no una referencia directa al diccionario original.

    def get_ventas(self):
        return self.ventas

    def agregar_producto(self, producto):
        self.productos[producto.id_producto] = producto

    def agregar_cliente(self, cliente):
        self.clientes[cliente.id_cliente] = cliente

    def agregar_vendedor(self, vendedor):
        self.vendedores[vendedor.id_vendedor] = vendedor

    def registrar_venta(self, venta):
        venta.producto.reducir_stock(venta.cantidad)
        self.ventas.append(venta)

    def ingresos_totales(self):
        # total = 0
        # for venta in self.ventas:
        #    total += venta.calcular_total()
        #return total
        return sum(v.calcular_total() for v in self.ventas)

    def producto_mas_vendido(self):
        # Creamos un diccionario que asigna un valor predeterminado
        # a las llaves que aún no existen. Al colocar "int", el valor
        # predeterminado es 0.
        unidades_vendidas_producto = defaultdict(int)

        for venta in self.ventas:
            unidades_vendidas_producto[venta.producto.nombre] += venta.cantidad

        # Al usar el argumento "key", la función max() no compara las llaves directamente
        # sino que compara los valores. Además, max() devuelve la llave, mas no el valor.
        return max(unidades_vendidas_producto, key=unidades_vendidas_producto.get)

    def mejor_vendedor(self):
        # Creamos un diccionario que asigna un valor predeterminado
        # a las llaves que aún no existen. Al colocar "float", el valor
        # predeterminado es 0.0.
        totales_vendedor = defaultdict(float)

        for venta in self.ventas:
            totales_vendedor[venta.vendedor.nombre_completo] += venta.calcular_total()

        # Al usar el argumento "key", la función max() compara los valores
        # de las llaves. Devuelve la llave, mas no el valor.
        return max(totales_vendedor, key=totales_vendedor.get)

    def cliente_mas_frecuente(self):
        # Creamos un diccionario que asigna un valor predeterminado
        # a las llaves que aún no existen. Al colocar "int", el valor
        # predeterminado es 0.
        total_pedidos_cliente = defaultdict(int)

        for venta in self.ventas:
            total_pedidos_cliente[venta.cliente.nombre_completo] += 1

        # Al usar el argumento "key", la función max() compara los valores
        # de las llaves. Devuelve la llave, mas no el valor.
        return max(total_pedidos_cliente, key=total_pedidos_cliente.get)

    def productos_bajos_stock(self, umbral=10):
        # bajos_en_stock = []

        # for producto in self.productos.values():
        #     if producto.stock <= umbral:
        #         bajos_en_stock.append(producto)

        # return bajos_en_stock

        return [producto for producto in self.productos.values() if producto.stock <= umbral]