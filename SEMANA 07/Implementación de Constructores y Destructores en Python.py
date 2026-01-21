# Tarea: Implementación de Constructores y Destructores en Python
# Autor: Froilán Tejada
# Fecha: 25 de enero de 2026
# Descripción: Programa que demuestra el uso de __init__ (constructor) y __del__ (destructor)
# en una clase NotasDiarias. El constructor abre un archivo, inicializa contadores,
# y el destructor cierra el archivo y guarda stats. [web:1][web:4]

class NotasDiarias:
    """
    Clase para manejar un archivo de notas diarias.
    - Constructor (__init__): Se llama automáticamente al crear un objeto.
      Abre el archivo, inicializa atributos como contador de notas y lista de entradas.
    - Destructor (__del__): Se llama cuando el objeto se destruye (al salir del scope o con 'del').
      Cierra el archivo y escribe un resumen de notas agregadas.
    """

    def __init__(self, nombre_archivo="notas.txt"):
        """
        Constructor: Inicializa el objeto.
        - Abre el archivo en modo append ('a') para agregar notas sin borrar lo viejo.
        - Inicializa lista de notas vacía y contador en 0.
        """
        print(f"Constructor llamado: Abriendo archivo {nombre_archivo}")
        self.nombre_archivo = nombre_archivo
        self.archivo = open(nombre_archivo, 'a', encoding='utf-8')  # Abre archivo [web:10]
        self.notas = []  # Lista para guardar notas en memoria
        self.contador_notas = 0
        print("Objeto NotasDiarias creado e inicializado correctamente.")  # [web:5]

    def agregar_nota(self, nota):
        """Método para agregar una nota al archivo y a la lista en memoria."""
        timestamp = f"{self.contador_notas + 1}. {nota}\n"
        self.archivo.write(timestamp)
        self.notas.append(nota)
        self.contador_notas += 1
        print(f"Nota agregada: {nota}")

    def mostrar_resumen(self):
        """Muestra un resumen de notas en memoria."""
        print(f"Resumen: {self.contador_notas} notas agregadas.")
        for i, nota in enumerate(self.notas, 1):
            print(f"  {i}. {nota}")

    def __del__(self):
        """
        Destructor: Se activa automáticamente cuando no hay más referencias al objeto.
        - Escribe un resumen final en el archivo.
        - Cierra el archivo para liberar recursos (buena práctica para evitar leaks). [web:1][web:7]
        """
        print("Destructor llamado: Limpiando recursos...")
        if hasattr(self, 'archivo') and not self.archivo.closed:
            resumen = f"\n--- Resumen del día: {self.contador_notas} notas totales ---\n"
            self.archivo.write(resumen)
            self.archivo.close()
            print(f"Archivo {self.nombre_archivo} cerrado. Recursos liberados.")
        else:
            print("Archivo ya estaba cerrado.")


# Programa principal para demostrar el uso
if __name__ == "__main__":
    print("=== DEMO DE CONSTRUCTORES Y DESTRUCTORES ===\n")

    # Creando objeto: Llama automáticamente a __init__
    libreta = NotasDiarias("mis_notas_hoy.txt")

    # Usando el objeto
    libreta.agregar_nota("Comprar leche y pan.")
    libreta.agregar_nota("Estudiar POO para la tarea.")
    libreta.agregar_nota("Llamar a  mamá.")
    libreta.mostrar_resumen()

    print("\nFin del programa. El destructor se llamará automáticamente al salir.")

    # Opcional: Forzar destrucción explícita con 'del'
    # del libreta  # Descomenta para ver el destructor en acción antes de salir
