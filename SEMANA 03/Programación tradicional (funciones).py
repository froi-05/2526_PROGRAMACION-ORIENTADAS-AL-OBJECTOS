# Programa: promedio_clima_tradicional.py
# Descripción: calcula el promedio semanal de temperatura usando funciones

# Función para pedir las temperaturas de los 7 días
def pedir_temperaturas():
    temperaturas = []  # lista vacía para guardar las temperaturas de la semana
    print("=== Registro de temperaturas de la semana ===")
    for i in range(7):
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Entrada no válida. Intente de nuevo con un número.")
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio_semanal(temperaturas):
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio

# Función principal que organiza el programa
def main():
    temps_semana = pedir_temperaturas()
    promedio = calcular_promedio_semanal(temps_semana)
    print("\n=== Resultado ===")
    print("Temperaturas ingresadas:", temps_semana)
    print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
