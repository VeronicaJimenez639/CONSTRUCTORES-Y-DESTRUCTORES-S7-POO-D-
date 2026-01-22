# main.py
# Punto de entrada del programa.
# Aquí se ejecuta el flujo principal y se evidencia el uso de __init__ y __del__.

from modelos.producto import Producto
from servicios.servicio_inventario import ServicioInventario


def main() -> None:
    # Se crea el servicio (inventario) que administrará los productos.
    inventario = ServicioInventario()

    # Crear un producto (se evidencia __init__)
    producto = Producto("Arroz", 1.25, 10)

    # Agregar el producto al inventario y mostrar el estado actual.
    inventario.agregar_producto(producto)
    inventario.listar_productos()

    # Vender unidades del producto usando el servicio (se actualiza el stock).
    inventario.vender_producto("Arroz", 3)
    inventario.listar_productos()

    # Eliminar el producto del inventario.
    # El servicio devuelve el objeto eliminado para poder evidenciar el destructor.
    eliminado = inventario.eliminar_producto("Arroz")
    inventario.listar_productos()

    # Evidenciar __del__ (el destructor se ejecuta cuando el objeto deja de tener referencias)
    if eliminado is not None:
        del eliminado

    # Si también quieres, elimina la otra referencia (producto) por si acaso:
    del producto


if __name__ == "__main__":
    main()                  # Ejecuta el programa solo si este archivo es el principal.