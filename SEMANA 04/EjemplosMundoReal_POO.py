# archivo: biblioteca.py

# Clase que representa un libro
class Libro:
    def __init__(self, titulo, autor, anio):
        # datos básicos del libro
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        # al inicio el libro está disponible
        self.disponible = True

    # intento de prestar el libro
    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True
        else:
            return False

    # marcar el libro como devuelto
    def devolver(self):
        self.disponible = True

    # cómo se muestra el libro en pantalla
    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} - {self.autor} ({self.anio}) [{estado}]"


# Clase que representa a un usuario de la biblioteca
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        # acá guardo los libros que se lleva el usuario
        self.libros_prestados = []

    def tomar_prestado(self, libro):
        if libro.prestar():
            self.libros_prestados.append(libro)
            print(f"{self.nombre} se llevó el libro: {libro.titulo}")
        else:
            print(f"El libro '{libro.titulo}' no está disponible en este momento.")

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.devolver()
            self.libros_prestados.remove(libro)
            print(f"{self.nombre} devolvió el libro: {libro.titulo}")
        else:
            print(f"{self.nombre} no tiene ese libro prestado.")


# Clase que administra todo
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.catalogo.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def mostrar_catalogo(self):
        print(f"Catálogo de la biblioteca {self.nombre}:")
        for libro in self.catalogo:
            print(" -", libro)

    def buscar_libro(self, titulo):
        for libro in self.catalogo:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None


# Parte de prueba del programa
if __name__ == "__main__":
    # creo la biblioteca
    biblioteca = Biblioteca("Biblioteca del Barrio")

    # creo algunos libros
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
    libro2 = Libro("El principito", "Antoine de Saint-Exupéry", 1943)
    libro3 = Libro("Rayuela", "Julio Cortázar", 1963)

    # los agrego al catálogo
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    # registro un usuario
    usuario1 = Usuario("Ana", 1)
    biblioteca.registrar_usuario(usuario1)

    # muestro el catálogo
    biblioteca.mostrar_catalogo()

    # el usuario busca un libro y lo pide prestado
    libro_buscado = biblioteca.buscar_libro("El principito")
    if libro_buscado:
        usuario1.tomar_prestado(libro_buscado)

    # vuelvo a mostrar el catálogo para ver el cambio de estado
    biblioteca.mostrar_catalogo()

    # ahora el usuario devuelve el libro
    usuario1.devolver_libro(libro_buscado)

    # catálogo final
    biblioteca.mostrar_catalogo()
