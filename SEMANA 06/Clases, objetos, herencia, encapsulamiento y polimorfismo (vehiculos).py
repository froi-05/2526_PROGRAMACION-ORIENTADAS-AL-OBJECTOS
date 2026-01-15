# Programa completo POO - Vehiculos (todo en un archivo)
# Autor: (Froilán Tejada)

# === CLASES ===
class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self._marca = marca
        self._modelo = modelo
        self._anio = anio

    def get_marca(self):
        return self._marca

    def set_marca(self, nueva_marca):
        self._marca = nueva_marca

    def describir(self):
        return f"Vehículo {self._marca} {self._modelo} del año {self._anio}"


class Auto(Vehiculo):
    def __init__(self, marca, modelo, anio, puertas):
        super().__init__(marca, modelo, anio)
        self._puertas = puertas

    def describir(self):
        return f"Auto {self._marca} {self._modelo} ({self._anio}) con {self._puertas} puertas"


class Moto(Vehiculo):
    def __init__(self, marca, modelo, anio, tiene_baul):
        super().__init__(marca, modelo, anio)
        self._tiene_baul = tiene_baul

    def describir(self):
        if self._tiene_baul:
            texto_baul = "con baúl"
        else:
            texto_baul = "sin baúl"
        return f"Moto {self._marca} {self._modelo} ({self._anio}) {texto_baul}"


# === PROGRAMA PRINCIPAL ===
def main():
    auto1 = Auto("Chevrolet", "Spark", 2015, 4)
    auto2 = Auto("Toyota", "Corolla", 2020, 4)
    moto1 = Moto("Yamaha", "FZ", 2018, True)
    moto2 = Moto("Honda", "CBR", 2022, False)

    lista_vehiculos = [auto1, auto2, moto1, moto2]

    print("=== Lista de vehículos ===")
    for v in lista_vehiculos:
        print(v.describir())  # Polimorfismo aquí

    # Encapsulación
    print("\n=== Cambiando datos ===")
    print("Marca original auto1:", auto1.get_marca())
    auto1.set_marca("Kia")
    print("Marca nueva:", auto1.get_marca())


if __name__ == "__main__":
    main()
