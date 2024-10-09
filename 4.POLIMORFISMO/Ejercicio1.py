class Aprendiz:
    def __init__(self, nombres, apellidos, cedula, sexo):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula = cedula
        self.sexo = sexo
        self.formacion = input("Programa de formación: ")
        self.regional = input("Regional: ")
        print("--------------------------------------------")

    def mostrar_info(self):
        
        print("Hola, soy un aprendiz SENA")
        print(f"{self.nombres} {self.apellidos}")
        print(f"CC: {self.cedula}")
        print(f"Sexo: {self.sexo}")
        print(f"Estudiante del programa: {self.formacion} de la Regional {self.regional}")
        print("--------------------------------------------")

class Instructor:
    def __init__(self, nombres, apellidos, cedula, area):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula = cedula
        self.area = area

    def mostrar_info(self):
        
        print("Hola, soy un instructor del SENA")
        print(f"{self.nombres} {self.apellidos}")
        print(f"CC: {self.cedula}")
        print(f"Área de instrucción: {self.area}")
        print("--------------------------------------------")

class Coordinador:
    def __init__(self, nombres, apellidos, cedula, departamento):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula = cedula
        self.departamento = departamento

    def mostrar_info(self):
        
        print("Hola, soy un coordinador del SENA")
        print(f"{self.nombres} {self.apellidos}")
        print(f"CC: {self.cedula}")
        print(f"Departamento: {self.departamento}")
        print("--------------------------------------------")
        
def mostrar_informacion(persona):
    persona.mostrar_info()

# Instancias de cada clase
objeto_aprendiz = Aprendiz("Samuel Elías", "Vega Barrios", 1231383164, "Masculino")
objeto_instructor = Instructor("Laura", "Rodríguez", 987654321, "Programación")
objeto_coordinador = Coordinador("Carlos", "Martínez", 123456789, "Recursos Humanos")

# Llamada al método mostrar_info para cada objeto
mostrar_informacion(objeto_aprendiz)
mostrar_informacion(objeto_instructor)
mostrar_informacion(objeto_coordinador)
