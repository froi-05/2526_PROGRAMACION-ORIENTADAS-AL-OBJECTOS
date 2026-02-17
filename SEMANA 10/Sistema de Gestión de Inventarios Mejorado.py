# Sistema de Gestión de Inventarios MEJORADO - Con ARCHIVOS y EXCEPCIONES
# Autor: Froilán Tejada
# Fecha: 22 de febrero de 2026
# Cambios: Guarda/lee en inventario.txt, try-except para FileNotFoundError, PermissionError, etc.

import os  # Para chequear si existe el archivo


class Producto:
    """Igual que antes, sin cambios"""

    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    def set_cantidad(self, nueva_cantidad):
        if nueva_cant >= 0:
            self._cantidad = nueva_cant
        else:
            print("Error: Cantidad >= 0")

    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self._precio = nuevo_precio
        else:
            print("Error: Precio > 0")

    def __str__(self):
        return f"{self._id}|{self._nombre}|{self._cantidad}|{self._precio}"


class Inventario:
    """AHORA CON ARCHIVOS! Guarda/lee en inventario.txt"""

    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = []
        self.cargar_inventario()  # Carga al iniciar

    def guardar_inventario(self):
        """Guarda TODOS los productos en el archivo"""
        try:
            with open(self.archivo, 'w') as f:
                for prod in self.productos:
                    f.write(f"{prod}\n")  # Escribe línea por producto
            print(f"✓ Inventario guardado en {self.archivo}")
        except PermissionError:
            print("❌ Error: No tengo permisos para escribir el archivo. Corre como admin.")
        except Exception as e:
            print(f"❌ Error guardando: {e}")

    def cargar_inventario(self):
        """Lee el archivo y reconstruye la lista"""
        if not os.path.exists(self.archivo):
            print(f"📄 {self.archivo} no existe, creo uno vacío.")
            self.guardar_inventario()  # Crea vacío
            return

        try:
            with open(self.archivo, 'r') as f:
                for linea in f:
                    linea = linea.strip()
                    if linea:  # Salta líneas vacías
                        partes = linea.split('|')
                        if len(partes) == 4:
                            id_p, nombre, cant, prec = partes[0], partes[1], int(partes[2]), float(partes[3])
                            prod = Producto(id_p, nombre, cant, prec)
                            self.productos.append(prod)
            print(f"✓ Cargados {len(self.productos)} productos de {self.archivo}")
        except FileNotFoundError:
            print("❌ Archivo no encontrado, creo nuevo.")
            self.guardar_inventario()
        except PermissionError:
            print("❌ No permisos para leer. Inventario vacío.")
        except ValueError as e:
            print(f"❌ Archivo corrupto (línea mala): {e}. Ignorando...")
        except Exception as e:
            print(f"❌ Error cargando: {e}")

    def agregar_producto(self, id_producto, nombre, cantidad, precio):
        # Chequeo único + agregar + GUARDAR
        for prod in self.productos:
            if prod.get_id() == id_producto:
                print(f"❌ ID {id_producto} ya existe.")
                return
        nuevo_prod = Producto(id_producto, nombre, cantidad, precio)
        self.productos.append(nuevo_prod)
        self.guardar_inventario()  # ¡IMPORTANTE! Guarda cambio
        print(f"✓ '{nombre}' agregado Y guardado en archivo.")

    def eliminar_producto(self, id_producto):
        for i, prod in enumerate(self.productos):
            if prod.get_id() == id_producto:
                self.productos.pop(i)
                self.guardar_inventario()
                print(f"✓ '{prod.get_nombre()}' eliminado Y guardado.")
                return
        print(f"❌ No existe ID {id_producto}")

    def actualizar_producto(self, id_producto):
        for prod in self.productos:
            if prod.get_id() == id_producto:
                print(f"Actual: {prod.get_nombre()} - Cant: {prod.get_cantidad()} - Precio: ${prod.get_precio()}")
                try:
                    opc = input("1:cant 2:precio? ")
                    if opc == "1":
                        prod.set_cantidad(int(input("Nueva cant: ")))
                    elif opc == "2":
                        prod.set_precio(float(input("Nuevo precio: ")))
                    self.guardar_inventario()
                    print("✓ Actualizado Y guardado.")
                    return
                except ValueError:
                    print("❌ Ingresa números!")
                return
        print(f"❌ ID {id_producto} no encontrado")

    def buscar_por_nombre(self, nombre_buscar):
        encontrados = [p for p in self.productos if nombre_buscar.lower() in p.get_nombre().lower()]
        if encontrados:
            print("🔍 Encontrados:")
            for p in encontrados: print(f"  {p.get_id()} {p.get_nombre()}")
        else:
            print("❌ Nada encontrado")

    def mostrar_todos(self):
        if not self.productos:
            print("📭 Vacío")
        else:
            print("\n📋 INVENTARIO:")
            for p in self.productos:
                print(f"  {p.get_id()} | {p.get_nombre()} | {p.get_cantidad()} uds | ${p.get_precio():.2f}")


# Menú igual pero con mensajes de archivo
def menu():
    inv = Inventario()  # Carga automática!
    print("🚀 Sistema INICIADO - Inventario cargado de archivo.")

    while True:
        print("\n=== MENÚ INVENTARIOS MEJORADO ===")
        print("1.Agregar  2.Eliminar  3.Actualizar  4.Buscar  5.Mostrar  0.Salir")
        opc = input("Opción: ")

        if opc == "1":
            try:
                id_p = input("ID: ")
                nom = input("Nombre: ")
                cant = int(input("Cantidad: "))
                prec = float(input("Precio: "))
                inv.agregar_producto(id_p, nom, cant, prec)
            except ValueError:
                print("❌ Números porfa!")

        elif opc == "2":
            inv.eliminar_producto(input("ID: "))
        elif opc == "3":
            inv.actualizar_producto(input("ID: "))
        elif opc == "4":
            inv.buscar_por_nombre(input("Buscar: "))
        elif opc == "5":
            inv.mostrar_todos()
        elif opc == "0":
            inv.guardar_inventario()  # Guarda final
            print("👋 Chao! Todo guardado en inventario.txt")
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()
