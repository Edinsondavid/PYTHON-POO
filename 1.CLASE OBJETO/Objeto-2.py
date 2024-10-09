class Animal:
    # Método Constructor
    def __init__(self, especie, nombre, edad, color, peso):
        self.especie = especie
        self.nombre = nombre
        self.edad = edad 
        self.color = color
        self.peso = peso

    # Método para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Información del Animal")
        print("Especie: " + self.especie)
        print("Nombre: " + self.nombre) 
        print("Edad: " + self.edad)
        print("Color: " + self.color)
        print("Peso: " + self.peso)
        print("-----------------------------")

    # Método para comer
    def comer(self):
        respuesta = input("¿Quiere alimentar a la mascota? (Si/No): ")
        
        if respuesta.lower() == "si":
            print("Alimentando al " + self.especie)
            print("-----------------------------------------------")
        else:
            print("No se alimentó al " + self.especie)

# Creamos los Objetos a partir de instanciar la clase Animal       
objecto1 = Animal("Gato", "Carlota", "6 Años", "Blanco", "10 Kg")
objecto2 = Animal("Cerdo", "Pirulo", "5 Años", "Negro", "400 Kg")
objecto3 = Animal("Perro", "Manolo", "2 Años", "Negro", "4 Kg")

# Imprimimos los detalles de cada objeto
objecto1.mostrar_detalles()
objecto1.comer() 
objecto2.mostrar_detalles()
objecto2.comer()
objecto3.mostrar_detalles()
objecto3.comer()
