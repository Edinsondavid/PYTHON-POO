class Profesiones:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

    def describir(self):
        pass

class Medico(Profesiones):
    def __init__(self, nombre, especialidad, años_experiencia):
        super().__init__(nombre, especialidad)
        self.años_experiencia = años_experiencia

    def describir(self):
        print("--------------------------------------------")
        print(f"Este es un médico llamado {self.nombre}.")
        print(f"Especialidad: {self.especialidad}")
        print(f"Años de experiencia: {self.años_experiencia}")
        print("--------------------------------------------")

class Ingeniero(Profesiones):
    def __init__(self, nombre, especialidad, proyectos_realizados):
        super().__init__(nombre, especialidad)
        self.proyectos_realizados = proyectos_realizados

    def describir(self):
        print("--------------------------------------------")
        print(f"Este es un ingeniero llamado {self.nombre}.")
        print(f"Especialidad: {self.especialidad}")
        print(f"Proyectos realizados: {self.proyectos_realizados}")
        print("--------------------------------------------")

class Docente(Profesiones):
    def __init__(self, nombre, especialidad, años_experiencia):
        super().__init__(nombre, especialidad)
        self.años_experiencia = años_experiencia

    def describir(self):
        print("--------------------------------------------")
        print(f"Este es un docente llamado {self.nombre}.")
        print(f"Especialidad: {self.especialidad}")
        print(f"Años de experiencia: {self.años_experiencia}")
        print("--------------------------------------------")

def mostrar_informacion(profesion):
    profesion.describir()

objeto_medico = Medico("Dr. Juan", "Cardiología", 10)
objeto_ingeniero = Ingeniero("Ing. María", "Civil", 5)
objeto_docente = Docente("Prof. Carlos", "Matemáticas", 8)

mostrar_informacion(objeto_medico)
mostrar_informacion(objeto_ingeniero)
mostrar_informacion(objeto_docente)
