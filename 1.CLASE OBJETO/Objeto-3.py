class Carro:
    # Método Constructor
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color

    # Método para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Información del Carro")
        print("Marca: " + self.marca)
        print("Modelo: " + self.modelo)
        print("Año:", self.año)
        print("Color: " + self.color)
        print("-----------------------------")

    # Método para arrancar el carro
    def arrancar(self):
        respuesta = input("¿Quiere arrancar el carro? (Si/No): ")
        
        if respuesta.lower() == "si":
            print("Arrancando el " + self.modelo + " de la marca " + self.marca)  
            print("-----------------------------------------------")
        else:
            print("No arrancó el " + self.modelo + " de la marca " + self.marca) 

# Creamos los Objetos a partir de instanciar la clase Carro
objeto1 = Carro("Toyota", "Corolla", 2020, "Rojo")
objeto2 = Carro("Ford", "Mustang", 2021, "Negro")
objeto3 = Carro("Audi", "Model S", 2022, "Blanco")

# Imprimimos los detalles de cada objeto
objeto1.mostrar_detalles()
objeto1.arrancar() 
objeto2.mostrar_detalles()
objeto2.arrancar()
objeto3.mostrar_detalles()
objeto3.arrancar()
