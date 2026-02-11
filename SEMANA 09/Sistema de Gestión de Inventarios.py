# Sistema de Gestión de Inventarios - Tarea POO
# Autor: Froilán Tejada
# Fecha: 15 de febrero de 2026
# Descripción: Clases Producto e Inventario con menú en consola. IDs únicos, búsquedas y updates.

class Producto:
    """
    Clase para representar un producto en el inventario.
    Atributos: id (único), nombre, cantidad, precio.
    Tiene getters y setters para acceder y modificar.
    """

    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id = id_producto  # ID único, uso _ para encapsular un poco
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Setters
    def set_cantidad(self, nueva_cantidad):
        if nueva_cantidad >= 0:
            self._cantidad = nueva_cantidad
        else:
            print("¡Error! Cantidad no puede ser negativa.")

    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self._precio = nuevo_precio
        else:
            print("¡Error! Precio debe ser positivo.")

    def __str__(self):
        # Para mostrar el producto bonito
        return f"ID: {self._id} | Nombre: {self._nombre} | Cantidad: {self._cantidad} | Precio: ${self._precio:.2f}"


class Inventario:
    """
    Clase para manejar la lista de productos.
    Usa una lista simple para guardar todo.
    Métodos para agregar, eliminar, actualizar, buscar y mostrar.
    """

    def __init__(self):
        self.productos = []  # Lista vacía al inicio

    def agregar_producto(self, id_producto, nombre, cantidad, precio):
        # Chequeo si el ID ya existe para que sea único
        for prod in self.productos:
            if prod.get_id() == id_producto:
                print(f"¡Error! Ya existe un producto con ID {id_producto}.")
                return

        # Si no existe, lo agrego
        nuevo_prod = Producto(id_producto, nombre, cantidad, precio)
        self.productos.append(nuevo_prod)
        print(f"Producto '{nombre}' agregado con éxito.")

    def eliminar_producto(self, id_producto):
        for i, prod in enumerate(self.productos):
            if prod.get_id() == id_producto:
                eliminado = self.productos.pop(i)
                print(f"Producto '{eliminado.get_nombre()}' eliminado.")
                return
        print(f"No se encontró producto con ID {id_producto}.")

    def actualizar_producto(self, id_producto):
        for prod in self.productos:
            if prod.get_id() == id_producto:
                print(f"Producto actual: {prod}")
                try:
                    opcion = input("¿Qué actualizar? (1: cantidad, 2: precio): ")
                    if opcion == "1":
                        nueva_cant = int(input("Nueva cantidad: "))
                        prod.set_cantidad(nueva_cant)
                    elif opcion == "2":
                        nuevo_prec = float(input("Nuevo precio: "))
                        prod.set_precio(nuevo_prec)
                    print("¡Actualizado!")
                    return
                except ValueError:
                    print("¡Error! Ingresa números válidos.")
                return
        print(f"No se encontró producto con ID {id_producto}.")

    def buscar_por_nombre(self, nombre_buscar):
        encontrados = []
        for prod in self.productos:
            if nombre_buscar.lower() in prod.get_nombre().lower():
                encontrados.append(prod)

        if encontrados:
            print("Productos encontrados:")
            for prod in encontrados:
                print(prod)
        else:
            print("No hay productos con ese nombre.")

    def mostrar_todos(self):
        if not self.productos:
            print("Inventario vacío.")
            return
        print("\n--- Todos los productos ---")
        for prod in self.productos:
            print(prod)
        print("--------------------------")


# Menú principal en consola
def menu():
    inventario = Inventario()  # Creo el inventario aquí para que persista
    while True:
        print("\n=== SISTEMA DE INVENTARIOS ===")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar por nombre")
        print("5. Mostrar todos")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            try:
                id_prod = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                inventario.agregar_producto(id_prod, nombre, cantidad, precio)
            except ValueError:
                print("¡Error! Usa números para cantidad y precio.")

        elif opcion == "2":
            id_prod = input("ID a eliminar: ")
            inventario.eliminar_producto(id_prod)

        elif opcion == "3":
            id_prod = input("ID a actualizar: ")
            inventario.actualizar_producto(id_prod)

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "0":
            print("¡Chao! Inventario guardado en memoria.")
            break

        else:
            print("Opción inválida, intenta de nuevo.")


# Para correr el programa
if __name__ == "__main__":
    menu()
