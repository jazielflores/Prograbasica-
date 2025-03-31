class Inventario:
    def __init__(self):
        # Inicializa una lista vacía para almacenar los productos
        self.productos = []
    
    def agregar_producto(self, nombre, categoria, precio, cantidad):
        # Agrega un nuevo producto al inventario con sus detalles
        self.productos.append({
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio,
            "cantidad": cantidad
        })
        print(f"Producto '{nombre}' agregado exitosamente.")
    
    def eliminar_producto(self, nombre):
        # Elimina un producto del inventario por su nombre si existe
        self.productos = [p for p in self.productos if p["nombre"] != nombre]
        print(f"Producto '{nombre}' eliminado si existía.")
    
    def buscar_producto(self, nombre):
        # Busca un producto por su nombre y muestra su información
        for producto in self.productos:
            if producto["nombre"] == nombre:
                print(f"Producto encontrado: {producto}")
                return producto
        print("Producto no encontrado.")
        return None
    
    def mostrar_productos_ordenados(self):
        # Muestra todos los productos ordenados por precio de menor a mayor
        productos_ordenados = sorted(self.productos, key=lambda x: x["precio"])
        print("Productos ordenados por precio:")
        for producto in productos_ordenados:
            print(producto)

# Ejemplo de uso
inventario = Inventario()

# Agregar productos al inventario
inventario.agregar_producto("Laptop", "Electrónica", 1500, 5)
inventario.agregar_producto("Teclado", "Accesorios", 50, 10)
inventario.agregar_producto("Mouse", "Accesorios", 25, 15)

# Mostrar productos ordenados por precio
inventario.mostrar_productos_ordenados()

# Buscar un producto específico
inventario.buscar_producto("Teclado")

# Eliminar un producto del inventario
inventario.eliminar_producto("Teclado")

# Mostrar productos nuevamente para verificar eliminación
inventario.mostrar_productos_ordenados()
