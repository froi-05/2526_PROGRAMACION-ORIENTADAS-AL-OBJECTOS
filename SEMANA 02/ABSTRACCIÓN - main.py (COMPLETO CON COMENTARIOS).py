# EJEMPLO DE ABSTRACCIÓN: Ocultamos detalles internos, solo mostramos lo esencial
# Propósito: El usuario solo ve "atacar()", no cómo se calcula el daño

class Personaje:
    def __init__(self, nombre, vida):
        # Constructor: Inicializa datos básicos del personaje
        self.nombre = nombre  # Nombre visible para el usuario
        self.vida = vida  # Vida visible para el usuario

    def atacar(self):
        # MÉTODO PÚBLICO: Lo único que el usuario necesita saber
        # Aquí ABSTRAEMOS el cálculo complejo del daño
        dano = self.calcular_dano()  # Llamamos método interno OCULTO
        print(f"{self.nombre} ataca causando {dano} de daño!")

    def calcular_dano(self):
        # MÉTODO PRIVADO: Detalles de implementación OCULTOS al usuario
        # En un juego real aquí irían fórmulas complejas (nivel, arma, etc.)
        return 20  # Simplificado para el ejemplo


# PRUEBA DEL EJEMPLO
if __name__ == "__main__":
    # Creamos objeto y usamos solo la interfaz simple
    guerrero = Personaje("Conan", 100)
    guerrero.atacar()  # Usuario NO ve calcular_dano(), pura abstracción [file:21]
