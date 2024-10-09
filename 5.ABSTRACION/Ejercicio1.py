"""
Define una clase abstracta Empleado con un método abstracto calcular_salario().
Crea dos clases concretas: EmpleadoTiempoCompleto y EmpleadoPorHoras que implementen 
calcular_salario() de manera distinta.
"""

from abc import ABC, abstractmethod

class Empleado(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, salario_mensual):
        self.salario_mensual = salario_mensual

    def calcular_salario(self):
        return self.salario_mensual

class EmpleadoPorHoras(Empleado):
    def __init__(self, horas_trabajadas, tarifa_por_hora):
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def calcular_salario(self):
        return self.horas_trabajadas * self.tarifa_por_hora

empleado1 = EmpleadoTiempoCompleto(3000)
print(f"Salario del empleado a tiempo completo: {empleado1.calcular_salario()}")

empleado2 = EmpleadoPorHoras(160, 20)
print(f"Salario del empleado por horas: {empleado2.calcular_salario()}")
