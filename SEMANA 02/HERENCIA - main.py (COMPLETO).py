# EJEMPLO DE HERENCIA: Reutilizamos código de clase padre
# Propósito: Guerrero y Mago comparten código básico de Personaje

class Personaje:  # CLASE PADRE (Superclase)
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

    def mostrar_info(self):
        # MÉTODO heredado por todos los hijos
        print(f"{self.nombre} tiene {self.vida} HP")


class Guerrero(Personaje):  # HIJO 1: HEREDA de Personaje
    def __init__(self, nombre, vida, fuerza):
        super().__init__(nombre, vida)  # LLAMA constructor del PADRE
        self.fuerza = fuerza  # Atributo PROPIO del guerrero

    def golpe_fuerte(self):
        # MÉTODO PROPIO del hijo
        print(f"¡{self.nombre} golpea con {self.fuerza} de fuerza!")


class Mago(Personaje):  # HIJO 2: También hereda
    def __init__(self, nombre, vida, mana):
        super().__init__(nombre, vida)
        self.mana = mana

    def lanzar_hechizo(self):
        print(f"¡{self.nombre} lanza hechizo con {self.mana} mana!")


# PRUEBA DE HERENCIA
if __name__ == "__main__":
    guerrero = Guerrero("Aragorn", 120, 30)
    guerrero.mostrar_info()  # HEREDADO del padre
    guerrero.golpe_fuerte()  # PROPIO del hijo [file:21]
