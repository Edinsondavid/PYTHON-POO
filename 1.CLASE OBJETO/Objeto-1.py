class Celular:
    # Método Constructor
    def __init__(self, color, marca, bateria, precio, modelo, nombre):
        self.color = color
        self.marca = marca
        self.bateria = bateria 
        self.precio = precio
        self.modelo = modelo 
        self.nombre = nombre

    # Método para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Información del Celular")
        print("Color: " + self.color)
        print("Marca: " + self.marca)
        print("Batería: " + self.bateria)
        print("Precio: " + self.precio)
        print("Modelo: " + self.modelo)
        print("Nombre: " + self.nombre)
        print("-----------------------------")

    # Método para encender el celular
    def encender(self):
        self.energia = int(input("Digite el valor de la carga (en %): "))
        
        if self.energia > 0:
            print("El celular " + self.modelo + " se puede encender")
            print(f" |||||||| {self.energia} % de carga")
            print("-----------------------------------------------")
        else:
            print("El celular " + self.modelo + " no se puede encender")

# Creamos los Objetos a partir de instanciar la clase Celular       
objecto1 = Celular("Azul", "Xiaomi", "80 %", "Redmi Note 11", "128mpx", "Redmi Note 11")
objecto2 = Celular("Negro", "Samsung", "75 %", "Galaxy A20", "32MPX", "Galaxy A20")
objecto3 = Celular("Gris", "Apple", "100 %", "iphone 11", "64mpx", "iphone 11")

# Imprimimos los detalles de cada objeto
objecto1.mostrar_detalles()
objecto1.encender() #Metodo que evaluar el encendimiento del celular
objecto2.mostrar_detalles()
objecto2.encender()
objecto3.mostrar_detalles()
objecto3.encender()

