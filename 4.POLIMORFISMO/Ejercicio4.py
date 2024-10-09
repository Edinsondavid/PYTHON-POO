class InstrumentoMusical:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def tocar(self):
        pass

class Guitarra(InstrumentoMusical):
    def __init__(self, nombre, tipo, cuerdas):
        super().__init__(nombre, tipo)
        self.cuerdas = cuerdas

    def tocar(self):
        print("--------------------------------------------")
        print(f"Este es un instrumento de tipo {self.tipo}.")
        print(f"Nombre: {self.nombre}")
        print(f"Número de cuerdas: {self.cuerdas}")
        print("--------------------------------------------")

class Piano(InstrumentoMusical):
    def __init__(self, nombre, tipo, teclas):
        super().__init__(nombre, tipo)
        self.teclas = teclas

    def tocar(self):
        print("--------------------------------------------")
        print(f"Este es un instrumento de tipo {self.tipo}.")
        print(f"Nombre: {self.nombre}")
        print(f"Número de teclas: {self.teclas}")
        print("--------------------------------------------")

class Trompeta(InstrumentoMusical):
    def __init__(self, nombre, tipo, material):
        super().__init__(nombre, tipo)
        self.material = material

    def tocar(self):
        print("--------------------------------------------")
        print(f"Este es un instrumento de tipo {self.tipo}.")
        print(f"Nombre: {self.nombre}")
        print(f"Material: {self.material}")
        print("--------------------------------------------")

def mostrar_informacion(instrumento):
    instrumento.tocar()

objeto_guitarra = Guitarra("Guitarra Acústica", "Cuerda", 6)
objeto_piano = Piano("Piano de Cola", "Teclado", 88)
objeto_trompeta = Trompeta("Trompeta B", "Metal", "Latón")

mostrar_informacion(objeto_guitarra)
mostrar_informacion(objeto_piano)
mostrar_informacion(objeto_trompeta)
