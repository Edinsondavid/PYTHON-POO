class Empleado:
    # Método Constructor
    def __init__(self, nombre, edad, profesion, cargo):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
        self.cargo = cargo

    # Método para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Información del Empleado")
        print("Nombre: " + self.nombre)
        print("Edad: " + self.edad)
        print("Profesión: " + self.profesion)
        print("Cargo: " + self.cargo)
        print("-----------------------------")

    # Método para verificar disponibilidad del empleado
    def disponible_para_trabajar(self):
        self.disponibilidad = int(input("Digite el número de horas disponibles para trabajar hoy: "))
        
        if self.disponibilidad > 0:
            print("El empleado " + self.nombre + " está disponible para trabajar.")
            print(f" |||||||| {self.disponibilidad} horas disponibles.")
            print("-----------------------------------------------")
        else:
            print("El empleado " + self.nombre + " no está disponible para trabajar.")

# Creamos los Objetos a partir de instanciar la clase Empleado       
empleado1 = Empleado("Valery Siolo", "35 años", "Ingeniera de Software", "Desarrolladora")
empleado2 = Empleado("Juan Cossi", "30 años", "Diseñador Gráfico", "Diseñador")
empleado3 = Empleado("Valeria Peña", "23 años", "Administración de Empresas", "Gerente")

# Imprimimos los detalles de cada objeto
empleado1.mostrar_detalles()
empleado1.disponible_para_trabajar()  # Método que evalúa la disponibilidad del empleado
empleado2.mostrar_detalles()
empleado2.disponible_para_trabajar()
empleado3.mostrar_detalles()
empleado3.disponible_para_trabajar()
