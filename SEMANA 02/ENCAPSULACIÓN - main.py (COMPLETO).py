# EJEMPLO DE ENCAPSULACIÓN: Datos privados, acceso controlado
# Propósito: Proteger el mana del mago, solo accesible por métodos públicos

class Mago:
    def __init__(self, nombre):
        # ATRIBUTOS PRIVADOS: El __ hace que sean "ocultos" desde fuera
        self.__nombre = nombre  # Nombre protegido
        self.__mana = 50  # Mana protegido (no se puede modificar directo)

    def lanzar_hechizo(self):
        # MÉTODO PÚBLICO: Controla el acceso al mana
        if self.__mana >= 10:
            self.__mana -= 10  # MODIFICA INTERNO de forma CONTROLADA
            print(f"{self._Mago__nombre} lanza bola de fuego! Mana: {self.__mana}")
        else:
            print("¡No hay mana suficiente! Descansa mago.")

    def get_mana(self):
        # GETTER: Permite VER el mana sin modificarlo
        return self.__mana

    def descansar(self):
        # MÉTODO PÚBLICO: Recarga mana de forma controlada
        self.__mana = 50
        print("¡Mago descansó! Mana lleno.")


# PRUEBA
if __name__ == "__main__":
    mago = Mago("Gandalf")
    mago.lanzar_hechizo()
    mago.lanzar_hechizo()
    print(f"Mana actual: {mago.get_mana()}")  # Control total [file:21]
    # print(mago.__mana)  # ¡ERROR! No se puede acceder directo
