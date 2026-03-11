# Biblioteca Digital - REQUISITOS EXACTOS
# Autor: Froilán Tejada - Quito, 18/mar/2026
# Libro: tupla (titulo,autor), Usuario: lista prestados
# Biblioteca: dict{ISBN:Libro}, set IDs usuarios

class Libro:
    """Libro: tupla inmutable (titulo,autor), categoria, isbn"""

    def __init__(self, isbn, titulo, autor, categoria):
        self.isbn = isbn
        self.info = (titulo, autor)  # TUPLE inmutable!
        self.categoria = categoria
        self.disponibles = 1

    def prestar(self):
        if self.disponibles > 0:
            self.disponibles -= 1
            return True
        return False

    def devolver(self):
        self.disponibles += 1

    def buscar(self, texto):
        titulo, autor = self.info
        return texto.lower() in titulo.lower() or texto.lower() in autor.lower() or texto.lower() in self.categoria.lower()

    def __str__(self):
        titulo, autor = self.info
        return f"ISBN {self.isbn} | {titulo} | {autor} | {self.categoria} | Disp: {self.disponibles}"


class Usuario:
    """Usuario: ID único, nombre, lista libros prestados (ISBNs)"""

    def __init__(self, id_usuario, nombre):
        self.id = id_usuario
        self.nombre = nombre
        self.prestados = []  # LISTA ISBNs

    def agregar_prestamo(self, isbn):
        if isbn not in self.prestados:
            self.prestados.append(isbn)
            return True
        return False

    def quitar_prestamo(self, isbn):
        if isbn in self.prestados:
            self.prestados.remove(isbn)
            return True
        return False

    def listar_prestados(self):
        return self.prestados.copy()

    def __str__(self):
        return f"ID {self.id} | {self.nombre} | Prestados: {len(self.prestados)} libros"


class Biblioteca:
    """Dict libros{ISBN:Libro}, set usuarios únicos"""

    def __init__(self):
        self.libros = {}  # DICT ISBN: Libro
        self.usuarios = set()  # SET IDs únicos
        self.usuarios_data = {}  # {ID: Usuario}

    def agregar_libro(self, isbn, titulo, autor, categoria):
        if isbn not in self.libros:
            self.libros[isbn] = Libro(isbn, titulo, autor, categoria)
            print(f"✅ '{titulo}' agregado")
            return True
        print("❌ ISBN existe")
        return False

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("✅ Libro eliminado")
            return True
        print("❌ No encontrado")
        return False

    def registrar_usuario(self, id_usuario, nombre):
        if id_usuario not in self.usuarios:
            self.usuarios.add(id_usuario)
            self.usuarios_data[id_usuario] = Usuario(id_usuario, nombre)
            print(f"✅ '{nombre}' registrado")
            return True
        print("❌ ID ya existe")
        return False

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios_data[id_usuario]
            self.usuarios.remove(id_usuario)
            print("✅ Usuario dado de baja")
            return True
        print("❌ No encontrado")
        return False

    def prestar(self, isbn, id_usuario):
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios_data[id_usuario]
            if libro.prestar() and usuario.agregar_prestamo(isbn):
                print(f"✅ {usuario.nombre} prestó {libro.info[0]}")
                return True
        print("❌ Error préstamo")

    def devolver(self, isbn, id_usuario):
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios_data[id_usuario]
            if usuario.quitar_prestamo(isbn):
                libro.devolver()
                print(f"✅ {usuario.nombre} devolvió {libro.info[0]}")
                return True
        print("❌ Error devolución")

    def buscar_libros(self, texto):
        encontrados = []
        for libro in self.libros.values():
            if libro.buscar(texto):
                encontrados.append(libro)
        if encontrados:
            print("🔍 ENCONTRADOS:")
            for l in encontrados:
                print(f"  {l}")
        else:
            print("❌ Nada encontrado")

    def listar_prestados_usuario(self, id_usuario):
        if id_usuario in self.usuarios_data:
            usuario = self.usuarios_data[id_usuario]
            print(f"\n📚 {usuario.nombre} tiene prestados:")
            for isbn in usuario.listar_prestados():
                if isbn in self.libros:
                    print(f"  - {self.libros[isbn]}")
        else:
            print("❌ Usuario no existe")


def menu():
    bib = Biblioteca()

    while True:
        print("\n=== BIBLIOTECA DIGITAL ===")
        print("1.Libro nuevo  2.Usuario nuevo")
        print("3.Quitar libro  4.Baja usuario")
        print("5.Prestar  6.Devolver")
        print("7.Buscar libros  8.Prestados usuario")
        print("0.Salir")
        opc = input("→ ")

        if opc == "1":
            isbn = input("ISBN: ")
            tit = input("Título: ")
            aut = input("Autor: ")
            cat = input("Categoría: ")
            bib.agregar_libro(isbn, tit, aut, cat)

        elif opc == "2":
            idu = input("ID usuario: ")
            nom = input("Nombre: ")
            bib.registrar_usuario(idu, nom)

        elif opc == "3":
            bib.quitar_libro(input("ISBN: "))
        elif opc == "4":
            bib.dar_baja_usuario(input("ID usuario: "))

        elif opc == "5":
            isbn = input("ISBN: ")
            idu = input("ID usuario: ")
            bib.prestar(isbn, idu)

        elif opc == "6":
            isbn = input("ISBN: ")
            idu = input("ID usuario: ")
            bib.devolver(isbn, idu)

        elif opc == "7":
            bib.buscar_libros(input("Buscar: "))
        elif opc == "8":
            bib.listar_prestados_usuario(input("ID usuario: "))
        elif opc == "0":
            break


if __name__ == "__main__":
    menu()
