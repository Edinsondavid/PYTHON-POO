# Clase Libro con atributos privados y públicos
class Libro:
    # Método constructor
    def __init__(self, titulo, autor, isbn, editorial):
        self.__titulo = titulo      # Atributo privado
        self.__autor = autor        # Atributo privado
        self.__isbn = isbn          # Atributo privado
        self.editorial = editorial  # Atributo público

    # Métodos getter
    def obtener_titulo(self):
        return self.__titulo

    def obtener_autor(self):
        return self.__autor

    def obtener_isbn(self):
        return self.__isbn

    # Métodos setter
    def establecer_titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo

    def establecer_autor(self, nuevo_autor):
        self.__autor = nuevo_autor

    def establecer_isbn(self, nuevo_isbn):
        self.__isbn = nuevo_isbn

    # Método para mostrar la información completa del libro
    def mostrar_informacion(self):
        print(f"\nTítulo: {self.__titulo}")
        print(f"Autor: {self.__autor}")
        print(f"ISBN: {self.__isbn}")
        print(f"Editorial: {self.editorial}")

# Crear un objeto Libro
libro = Libro("Cien años de soledad", "Gabriel García Márquez", "978-84-376-0494-7", "Editorial Sudamericana")

# Mostrar la información completa del libro
libro.mostrar_informacion()

print("\n----------------------")

# Modificar los atributos privados usando setters
libro.establecer_titulo("El amor en los tiempos del cólera")
libro.establecer_autor("Gabriel García Márquez")
libro.establecer_isbn("978-84-376-0495-4")

# Modificar el atributo público directamente
libro.editorial = "Editorial Planeta"

# Mostrar la información actualizada del libro
libro.mostrar_informacion()
