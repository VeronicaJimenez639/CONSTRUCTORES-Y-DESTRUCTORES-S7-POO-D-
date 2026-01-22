# Servicio Inventario (Constructores y Destructores)

## ¿De qué trata el programa?
Este programa simula un inventario básico de productos. Permite crear un producto, agregarlo al inventario, listar productos, vender unidades y eliminar un producto del sistema.

## ¿Cómo ejecutar main.py?
1. Abre la carpeta del proyecto en tu IDE (PyCharm o VS Code).
2. Ejecuta el archivo `main.py`:

```bash
python main.py

## **¿Dónde se evidencia el uso de __init__ y __del__?**

__init__: se ejecuta al crear el objeto Producto(), inicializando sus atributos (nombre, precio y stock) y escribiendo un registro en el archivo inventario_log.txt.

__del__: se evidencia cuando el producto deja de tener referencias (en main.py se usa del). En ese momento se cierra el archivo inventario_log.txt (limpieza del recurso) y se muestra un mensaje en consola.
