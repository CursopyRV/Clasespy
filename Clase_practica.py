"""Ejercicio 1: Promedio móvil de cotizaciones
Enunciado:

Desarrollá una clase ActivoFinanciero que permita almacenar un historial de precios de un activo (por ejemplo, una acción o un bono).

La clase debe permitir:

Agregar nuevos precios al historial.

Calcular el promedio móvil de N días sobre el historial.

"""

class ActivoFinanciero:
    def __init__(self,nombre, historial_precios):
        self.nombre = nombre
        self.historial_precios = historial_precios

    def nuevo_precio(self, precio):
        if precio <= 0:
            raise ValueError("El precio debe ser positivo.")
        self.historial_precios.append(float(precio))
        print(f"Los precios guardados para el activo {self.nombre} son: {self.historial_precios}")

    def promedio_movil(self, n):

        if n <= 0:
            print("La cantidad de días debe ser mayor que cero.")
            return []

        if len(self.historial_precios) < n:
            print("No hay suficientes datos para calcular el promedio móvil.")
            return []

        promedios = []
        for i in range(n - 1, len(self.historial_precios)):
            ventana = self.historial_precios[i+1-n : i+1]
            promedio = sum(ventana) / n
            promedios.append(promedio)
        return promedios
             
activo_x = ActivoFinanciero("Accion X", [100,105,110,115,95,102,110])
activo_x.nuevo_precio(120)
print(activo_x.promedio_movil(3))

