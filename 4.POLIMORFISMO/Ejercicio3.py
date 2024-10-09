class Perro:
    def __init__(self, nombre, habitat, raza):
        self.nombre = nombre
        self.habitat = habitat
        self.raza = raza

    def sonido(self):
        print("Guau")

    def descripcion(self):
        print("--------------------------------------------")
        print(f"Este es un perro llamado {self.nombre}.")
        print(f"Hábitat: {self.habitat}")
        print(f"Raza: {self.raza}")
        print(f"Sonido: {self.sonido()}")
        print("--------------------------------------------")

class Gato(Perro):
    def sonido(self):
        print("Miau")

    def descripcion(self):
        print("--------------------------------------------")
        print(f"Este es un gato llamado {self.nombre}.")
        print(f"Hábitat: {self.habitat}")
        print(f"Raza: {self.raza}")
        print(f"Sonido: {self.sonido()}")
        print("--------------------------------------------")

class Conejo(Perro):
    def sonido(self):
        print("Ring") 

    def descripcion(self):
        print("--------------------------------------------")
        print(f"Este es un conejo llamado {self.nombre}.")
        print(f"Hábitat: {self.habitat}")
        print(f"Raza: {self.raza}")
        print(f"Sonido: {self.sonido()}")
        print("--------------------------------------------")

def mostrar_descripcion(animal):
    animal.descripcion()

objeto_perro = Perro("Zeus", "Casa", "Labrador")
objeto_gato = Gato("Carlota", "Casa", "Siames")
objeto_conejo = Conejo("Carloto", "Jardín", "Angora")

mostrar_descripcion(objeto_perro)
mostrar_descripcion(objeto_gato)
mostrar_descripcion(objeto_conejo)
