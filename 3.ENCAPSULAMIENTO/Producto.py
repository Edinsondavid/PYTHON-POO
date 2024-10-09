# Clase Producto con atributos encapsulados o privados
class Producto:
    # Método constructor
    def __init__(self, nombre, precio, cantidad, categoria):
        self.__nombre = nombre     # Atributo privado
        self.__precio = precio     # Atributo privado
        self.cantidad = cantidad   # Atributo público
        self.categoria = categoria # Atributo público

    # Método getter para obtener el nombre
    def obtener_nombre(self):
        return self.__nombre

    # Método getter para obtener el precio
    def obtener_precio(self):
        return self.__precio

    # Método setter para establecer el nombre
    def establecer_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    # Método setter para establecer el precio
    def establecer_precio(self, nuevo_precio):
        self.__precio = nuevo_precio

    # Método para mostrar los detalles del producto
    def mostrar_detalles(self):
        print(f"\nNombre: {self.__nombre}")
        print(f"Precio: {self.__precio}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Categoría: {self.categoria}")

# Crear un objeto Producto
producto = Producto("Camisa", 25.999, 100, "Ropa")

# Mostrar los detalles del producto
producto.mostrar_detalles()

print("\n----------------------")

# Modificar los atributos privados utilizando setters
producto.establecer_nombre("Pantalón")
producto.establecer_precio(45.999)

# Modificar los atributos públicos directamente
producto.cantidad = 50
producto.categoria = "Moda"

# Mostrar los detalles actualizados del producto
producto.mostrar_detalles()
