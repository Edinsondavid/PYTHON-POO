class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        print("--------------------------------------------")
        print(f"Vehículo: {self.marca} {self.modelo}")
        print("--------------------------------------------")

class Carro(Vehiculo):
    def __init__(self, marca, modelo, placa, fabricante):
        super().__init__(marca, modelo)
        self.placa = placa
        self.fabricante = fabricante

    def descripcion(self):
        super().descripcion()
        print(f"Tipo: Carro")
        print(f"Placa: {self.placa}")
        print(f"Fabricante: {self.fabricante}")
        print("--------------------------------------------")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, velocidad_final, potencia):
        super().__init__(marca, modelo)
        self.velocidad_final = velocidad_final
        self.potencia = potencia

    def descripcion(self):
        super().descripcion()
        print(f"Tipo: Moto")
        print(f"Velocidad Final: {self.velocidad_final} km/h")
        print(f"Potencia: {self.potencia} HP")
        print("--------------------------------------------")

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo_terreno, velocidad_alcanzada, modo_manejo, precio):
        super().__init__(marca, modelo)
        self.tipo_terreno = tipo_terreno
        self.velocidad_alcanzada = velocidad_alcanzada
        self.modo_manejo = modo_manejo
        self.precio = precio

    def descripcion(self):
        super().descripcion()
        print(f"Tipo: Bicicleta")
        print(f"Tipo de Terreno: {self.tipo_terreno}")
        print(f"Velocidad Alcanzada: {self.velocidad_alcanzada} km/h")
        print(f"Modo de Manejo: {self.modo_manejo}")
        print(f"Precio: {self.precio}")
        print("--------------------------------------------")

def mostrar_descripcion(vehiculo):
    vehiculo.descripcion()

objeto_carro = Carro("Toyota", "Corolla", "ABC123", "Toyota Motor Corporation")
objeto_moto = Moto("Honda", "CBR600RR", 250, 100)
objeto_bicicleta = Bicicleta("Giant", "Talon", "Montaña", 60, "Deportiva", 600000)

mostrar_descripcion(objeto_carro)
mostrar_descripcion(objeto_moto)
mostrar_descripcion(objeto_bicicleta)
