# EJEMPLO DE POLIMORFISMO: Mismo método, comportamiento diferente
# Propósito: Un mismo comando "atacar()" hace cosas distintas

class Personaje:  # CLASE BASE (interfaz común)
    def atacar(self):
        # Método abstracto: Los hijos lo SOBREESCRIBEN
        raise NotImplementedError("Debes implementar atacar()")

class Guerrero(Personaje):
    def atacar(self):
        # SOBREESCRITURA: Guerrero ataca con espada
        return "¡GOLPE ESPADA! +30 daño físico"

class Mago(Personaje):
    def atacar(self):
        # SOBREESCRITURA: Mago usa magia
        return "¡BOLA DE FUEGO! +25 daño mágico"

# FUNCIÓN POLIMÓRFICA: No sabe qué tipo recibe, pero funciona igual
def batalla_lista(personajes):
    print("=== COMIENZA LA BATALLA ===")
    for personaje in personajes:
        print(personaje.atacar())  # ¡POLIMORFISMO! Cada uno responde diferente

# PRUEBA
if __name__ == "__main__":
    equipo = [Guerrero(), Mago()]
    batalla_lista(equipo)  # Funciona sin saber qué personaje es cada uno [file:21]
