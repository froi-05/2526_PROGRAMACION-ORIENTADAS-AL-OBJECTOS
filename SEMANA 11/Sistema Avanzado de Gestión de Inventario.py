# Sistema AVANZADO Inventarios - Con DICCCIONARIO + JSON

# Autor: Froilán Tejada
# Fecha: 01 mar 2026
# Colección: dict {ID: Producto} → Búsqueda O(1)
# Archivo: JSON para serializar fácil

import json  # Para guardar/cargar diccionario como JSON
import os


class Producto:
    """Producto con getters/setters"""

    def __init__(self, id_prod, nombre, cantidad, precio):
        self.id = id_prod
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_dict(self):
        """Para guardar en JSON"""
        return {
            'id': self.id,
            'nombre': self.nombre,
            'cantidad': self.cantidad,
            'precio': self.precio
        }

    @classmethod
    def from_dict(cls, data):
        """Crea Producto desde dict JSON"""
        return cls(data['id'], data['nombre'], data['cantidad'], data['precio'])

    def __str__(self):
        return f"{self.id} | {self.nombre} | {self.cantidad} uds | ${self.precio:.2f}"


class Inventario:
    """USA DICCIONARIO como colección principal! {ID: Producto}"""

    def __init__(self, archivo="inventario_avanzado.json"):
        self.archivo = archivo
        self.productos = {}  # DICT: clave=ID, valor=Producto → búsqueda instantánea
        self.cargar()

    def guardar(self):
        """Serializa dict a JSON"""
        try:
            data = {id: prod.to_dict() for id, prod in self.productos.items()}
            with open(self.archivo, 'w') as f:
                json.dump(data, f, indent=2)
            print(f"💾 Guardado en {self.archivo} ({len(self.productos)} productos)")
        except Exception as e:
            print(f"❌ Error guardando: {e}")

    def cargar(self):
        """Deserializa JSON → dict"""
        if not os.path.exists(self.archivo):
            print("📄 Nuevo archivo JSON creado")
            self.guardar()
            return
        try:
            with open(self.archivo, 'r') as f:
                data = json.load(f)
                self.productos = {id: Producto.from_dict(prod_data) for id, prod_data in data.items()}
            print(f"📂 Cargados {len(self.productos)} productos")
        except json.JSONDecodeError:
            print("❌ JSON corrupto, creo nuevo")
            self.productos = {}
            self.guardar()
        except Exception as e:
            print(f"❌ Error cargando: {e}")

    def agregar(self, id_prod, nombre, cantidad, precio):
        if id_prod in self.productos:
            print(f"❌ ID {id_prod} ya existe")
            return False
        self.productos[id_prod] = Producto(id_prod, nombre, cantidad, precio)
        self.guardar()
        print(f"✅ '{nombre}' AGREGADO")
        return True

    def eliminar(self, id_prod):
        if id_prod in self.productos:
            nombre = self.productos[id_prod].nombre
            del self.productos[id_prod]
            self.guardar()
            print(f"🗑️ '{nombre}' ELIMINADO")
            return True
        print(f"❌ ID {id_prod} no existe")
        return False

    def actualizar(self, id_prod):
        if id_prod not in self.productos:
            print(f"❌ ID {id_prod} no existe")
            return
        prod = self.productos[id_prod]
        print(f"Actual: {prod.nombre} | Cant: {prod.cantidad} | ${prod.precio}")
        try:
            opc = input("1:cantidad 2:precio → ")
            if opc == '1':
                prod.cantidad = int(input("Nueva cantidad: "))
            else:
                prod.precio = float(input("Nuevo precio: "))
            self.guardar()
            print("✏️ ACTUALIZADO")
        except ValueError:
            print("❌ ¡Números enteros/flotantes!")

    def buscar(self, texto):
        resultados = []
        for id_prod, prod in self.productos.items():
            if texto.lower() in prod.nombre.lower():
                resultados.append(prod)
        if resultados:
            print("🔍 RESULTADOS:")
            for p in resultados:
                print(f"  {p}")
        else:
            print("❌ Nada encontrado")

    def mostrar_todos(self):
        if not self.productos:
            print("📭 Inventario vacío")
            return
        print("\n📊 INVENTARIO COMPLETO:")
        for prod in self.productos.values():
            print(f"  {prod}")


def menu():
    inv = Inventario()
    print("🚀 SISTEMA AVANZADO - Diccionario + JSON listo!")

    while True:
        print("\n=== MENÚ AVANZADO ===")
        print("1.Agregar 2.Eliminar 3.Actualizar 4.Buscar 5.Todos 0.Salir")
        opc = input("→ ")

        if opc == '1':
            id_p = input("ID: ")
            nom = input("Nombre: ")
            try:
                cant = int(input("Cantidad: "))
                prec = float(input("Precio: "))
                inv.agregar(id_p, nom, cant, prec)
            except ValueError:
                print("❌ Números válidos!")
        elif opc == '2':
            inv.eliminar(input("ID: "))
        elif opc == '3':
            inv.actualizar(input("ID: "))
        elif opc == '4':
            inv.buscar(input("Texto: "))
        elif opc == '5':
            inv.mostrar_todos()
        elif opc == '0':
            print("👋 Guardado final!")
            break


if __name__ == "__main__":
    menu()
