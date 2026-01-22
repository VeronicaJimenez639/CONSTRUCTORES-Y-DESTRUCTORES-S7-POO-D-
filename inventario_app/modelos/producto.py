# modelos/producto.py

class Producto:
    """
    Modelo: representa un producto del inventario.
    Demuestra constructor (__init__) y destructor (__del__).
    """

# Constructor: se ejecuta al crear el objeto Producto().
# Inicializa los atributos para que el producto quede listo para usarse.
    def __init__(self, nombre: str, precio: float, stock: int) -> None:  
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

# Recurso: se abre un archivo de registro para simular el uso de un recurso externo.
# Esto permite demostrar una "limpieza" real en el destructor (__del__).
        self.archivo = open("inventario_log.txt", "a", encoding="utf-8") # Abrir archivo de registro
        self.archivo.write(f"[INIT] Producto creado: {self.nombre}\n")   # Registrar la creación del producto

        print(f"[INIT] Producto '{self.nombre}' creado.")

# Método de acción: reduce el stock si hay unidades suficientes.
    def vender(self, cantidad: int) -> None:
        if cantidad <= 0:
            print("La cantidad debe ser mayor que 0.")
            return

        if cantidad <= self.stock:
            self.stock -= cantidad
            print(f"Venta: {cantidad} unidad(es) de {self.nombre}")
        else:
            print("Stock insuficiente.")

# Destructor: se ejecuta cuando el objeto Producto() es eliminado.
# Cierra el archivo de registro para liberar el recurso externo.
    def __del__(self) -> None:
        try:                              # Cerrar el archivo si está abierto
            if not self.archivo.closed:   # Verificar si el archivo está abierto
                self.archivo.close()      # Cerrar el archivo
        except Exception:                 # Manejar posibles errores al cerrar el archivo
            pass                          # Ignorar errores en el destructor

        print(f"[DEL] Producto eliminado: {self.nombre}")
