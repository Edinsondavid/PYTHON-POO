class Moto:
    # Método Constructor
    def __init__(self, marca, modelo, combustible, color):
        self.marca = marca
        self.modelo = modelo
        self.combustible = combustible
        self.color = color

    # Método para mostrar detalles de la moto
    def mostrar_detalles(self):
        print("Información de la Moto")
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Combustible:", self.combustible)
        print("Color:", self.color)
        print("-----------------------------")

    # Método para arrancar la moto
    def arrancar(self):
        respuesta = input("¿Quiere arrancar la moto? (Si/No): ")
        
        if respuesta.lower() == "si":
            print("Arrancando la " + self.modelo + " de la marca " + self.marca)
            print("-----------------------------------------------")
        else:
            print("No ha arrancó la " + self.modelo + " de la marca " + self.marca)

# Creamos los objetos a partir de instanciar la clase Moto
objecto1 = Moto("Yamaha", "YZF-R3", "Gasolina", "Blanca")
objecto2 = Moto("Biwis", "CBR500R", "Gasolina", "Negra ")
objecto3 = Moto("Kawasaki", "Ninja 400", "Gasolina", "Negra")

# Imprimimos los detalles de cada moto
objecto1.mostrar_detalles()
objecto1.arrancar()
objecto2.mostrar_detalles()
objecto2.arrancar()
objecto3.mostrar_detalles()
objecto3.arrancar()
