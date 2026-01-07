# Programa: cálculo de área de un rectángulo.
# Descripción: pide los datos al usuario, calcula el área
# y muestra si el área es grande o pequeña según un umbral.

def calcular_area_rectangulo():
    # pedimos el nombre de la persona (string)
    nombre_usuario = input("Ingresa tu nombre: ")

    # pedimos las medidas del rectángulo (float)
    print("\nVamos a calcular el área de un rectángulo.")
    base_rectangulo = float(input("Ingresa la base del rectángulo en metros: "))
    altura_rectangulo = float(input("Ingresa la altura del rectángulo en metros: "))

    # calculamos el área (float)
    area_rectangulo = base_rectangulo * altura_rectangulo

    # definimos un umbral como número entero (int)
    umbral_area_grande = 20

    # usamos un boolean para saber si el área es grande
    area_es_grande = area_rectangulo > umbral_area_grande

    # mostramos resultados
    print("\nHola,", nombre_usuario)
    print(f"El área del rectángulo es: {area_rectangulo} m²")

    # usamos el boolean en una condición
    if area_es_grande:
        print("El área es grande (mayor que 20 m²).")
    else:
        print("El área es pequeña o mediana (20 m² o menos).")


# llamamos a la función principal del programa
calcular_area_rectangulo()
