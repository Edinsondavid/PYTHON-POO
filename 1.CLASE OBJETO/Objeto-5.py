class FiguraGeometrica:
    # Método Constructor
    def __init__(self, nombre, angulo, area, lados):
        self.nombre = nombre
        self.angulo = angulo
        self.area = area
        self.lados = lados

    # Método para mostrar detalles de la figura
    def mostrar_detalles(self):
        print("Información de la Figura Geométrica")
        print("Nombre:", self.nombre)
        print("Ángulo:", self.angulo)
        print("Área:", self.area)
        print("Lados:", self.lados)
        print("-----------------------------")

    # Método para calcular el área de la figura
    def calcular_area(self):
        respuesta = input(f"¿Desea calcular el área del {self.nombre}? (Si/No): ")
        
        if respuesta.lower() == "si":
            print(f"Calculando el área del {self.nombre} con {self.lados} lados y ángulo de {self.angulo} grados.")
            print(f"El área es aproximadamente {self.area}.")
            print("-----------------------------------------------")
        else:
            print(f"No se calculó el área del {self.nombre}.")

# Creamos los objetos a partir de instanciar la clase FiguraGeometrica
objecto1 = FiguraGeometrica("Octágono", 64, "2 * (1 + √2) * lado^2", 8)
objecto2 = FiguraGeometrica("Triángulo", 4, "0.5 * base * altura", 3)
objecto3 = FiguraGeometrica("Rectángulo", 22, "base * altura", 4)

# Imprimimos los detalles de cada figura geométrica
objecto1.mostrar_detalles()
objecto1.calcular_area()
objecto2.mostrar_detalles()
objecto2.calcular_area()
objecto3.mostrar_detalles()
objecto3.calcular_area()
