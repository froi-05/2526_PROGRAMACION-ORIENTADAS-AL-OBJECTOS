# Programa: promedio_clima_poo.py
# Descripción: calcula el promedio semanal de temperatura usando POO

# Clase base que representa un día de clima
class DiaClima:
    def __init__(self, dia, temperatura=0.0):
        # Atributos "encapsulados" con convención de guion bajo
        self._dia = dia
        self._temperatura = temperatura

    # Getter para el día
    def obtener_dia(self):
        return self._dia

    # Getter para la temperatura
    def obtener_temperatura(self):
        return self._temperatura

    # Setter para la temperatura
    def establecer_temperatura(self, temperatura):
        self._temperatura = temperatura


# Clase que representa la semana completa (hereda de object de forma implícita)
class SemanaClima:
    def __init__(self):
        # Lista de objetos DiaClima
        self._dias = []

    # Método para registrar las temperaturas de la semana
    def ingresar_datos_semana(self):
        print("=== Registro de temperaturas de la semana (POO) ===")
        for i in range(7):
            nombre_dia = f"Día {i + 1}"
            while True:
                try:
                    temp = float(input(f"Ingrese la temperatura para {nombre_dia}: "))
                    dia_clima = DiaClima(nombre_dia, temp)
                    self._dias.append(dia_clima)
                    break
                except ValueError:
                    print("Entrada no válida. Intente de nuevo con un número.")

    # Método para calcular el promedio semanal
    def calcular_promedio(self):
        if not self._dias:
            return 0.0
        suma = 0
        for dia in self._dias:
            suma += dia.obtener_temperatura()
        return suma / len(self._dias)

    # Método para mostrar el resumen de la semana (polimorfismo simple: cada objeto se comporta igual al pedir datos)
    def mostrar_resumen(self):
        print("\n=== Resumen de la semana ===")
        for dia in self._dias:
            print(f"{dia.obtener_dia()}: {dia.obtener_temperatura()} °C")
        promedio = self.calcular_promedio()
        print(f"\nEl promedio semanal de temperatura es: {promedio:.2f} °C")


# Función principal
def main():
    semana = SemanaClima()
    semana.ingresar_datos_semana()
    semana.mostrar_resumen()

if __name__ == "__main__":
    main()
