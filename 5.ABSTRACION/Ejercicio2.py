"""
Define una clase abstracta TareaEmpleado con un método abstracto realizar_tarea().
Implementa las clases Ingeniero y Doctor que heredan de TareaEmpleado e implementan 
el método realizar_tarea() de manera específica según su especialidad.
"""

from abc import ABC, abstractmethod

class TareaEmpleado(ABC):
    @abstractmethod
    def realizar_tarea(self):
        pass

class Ingeniero(TareaEmpleado):
    def realizar_tarea(self):
        return "El ingeniero está diseñando un sistema."

class Doctor(TareaEmpleado):
    def realizar_tarea(self):
        return "El doctor está atendiendo a un paciente."

ingeniero = Ingeniero()
print(ingeniero.realizar_tarea())

doctor = Doctor()
print(doctor.realizar_tarea())
