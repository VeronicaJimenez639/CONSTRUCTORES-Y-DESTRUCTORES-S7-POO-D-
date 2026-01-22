# servicios/servicio_inventario.py

from modelos.producto import Producto


class ServicioInventario:
    """
    Servicio: gestiona operaciones del inventario (agregar, listar, vender, eliminar).
    """
    
# Constructor: inicializa la lista de productos.
    def __init__(self) -> None:
        self.productos: list[Producto] = []
        print("[INIT] ServicioInventario creado.")

# Método: agrega un producto al inventario.
    def agregar_producto(self, producto: Producto) -> None:
        self.productos.append(producto)
        print(f"Agregado: {producto.nombre}")

# Método: lista todos los productos en el inventario.
    def listar_productos(self) -> None:
        print("\nINVENTARIO")
        if len(self.productos) == 0:   # Verificar si la lista está vacía
            print("Inventario vacío.")
            return

        # Recorre la lista y muestra información básica de cada producto.
        for producto in self.productos:
            print(f"- {producto.nombre} , Precio: ${producto.precio} , Stock: {producto.stock}")

# Método: vende una cantidad de un producto específico.
    def vender_producto(self, nombre: str, cantidad: int) -> None:
        for producto in self.productos:                             # Buscar el producto por nombre y realiza la venta llamando al método vender()
            if producto.nombre.lower() == nombre.lower():           # Comparación sin distinción de mayúsculas/minúsculas
                producto.vender(cantidad)
                return
        print("Producto no encontrado.")

    def eliminar_producto(self, nombre: str) -> Producto | None:
        """
        Elimina del inventario y devuelve el objeto eliminado (si existe).
        Así main puede hacer 'del producto' para evidenciar __del__.
        """
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                self.productos.remove(producto)
                print(f"Eliminado del inventario: {producto.nombre}")
                return producto
        print("Producto no encontrado.")
        return None