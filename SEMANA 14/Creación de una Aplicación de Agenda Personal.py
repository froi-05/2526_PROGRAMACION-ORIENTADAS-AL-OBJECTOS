# Agenda Personal GUI - Tkinter Treeview - Tarea POO
# Autor: Tejada De La Cruz Froilán
# Fecha: 22 marzo 2026
# Treeview eventos + Date Entry + Frames organizados

import tkinter as tk
from datetime import datetime
from tkinter import ttk, messagebox


class Evento:
    """Clase para representar un evento de la agenda"""

    def __init__(self, fecha, hora, descripcion):
        self.fecha = fecha
        self.hora = hora
        self.descripcion = descripcion

    def __str__(self):
        return f"{self.fecha} - {self.hora}: {self.descripcion}"


class AgendaPersonal:
    """Clase principal de la aplicación de agenda personal"""

    def __init__(self, root):
        self.root = root
        self.root.title("Mi Agenda Personal")
        self.root.geometry("750x550")
        self.root.resizable(True, True)

        # Lista para almacenar los eventos
        self.eventos = []

        # Crear las 4 secciones
        self.crear_interfaz()

    def crear_interfaz(self):
        """Crea las 4 secciones organizadas de la agenda"""

        # ===== SECCIÓN 1: CABECERA =====
        seccion1 = ttk.LabelFrame(self.root, text="CABECERA", padding="15")
        seccion1.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5, padx=10)
        titulo = ttk.Label(seccion1, text="📅 AGENDA PERSONAL", font=("Arial", 18, "bold"))
        titulo.grid(row=0, column=0)

        # ===== SECCIÓN 2: EVENTOS PROGRAMADOS =====
        seccion2 = ttk.LabelFrame(self.root, text="EVENTOS PROGRAMADOS", padding="10")
        seccion2.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5, padx=10)

        # TreeView con columnas
        columnas = ("Fecha", "Hora", "Descripción")
        self.tree = ttk.Treeview(seccion2, columns=columnas, show="headings", height=10)

        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")

        self.tree.column("Fecha", width=110)
        self.tree.column("Hora", width=90)
        self.tree.column("Descripción", width=400)

        # Scrollbar vertical
        scrollbar = ttk.Scrollbar(seccion2, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)

        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

        # ===== SECCIÓN 3: NUEVO EVENTO =====
        seccion3 = ttk.LabelFrame(self.root, text="NUEVO EVENTO", padding="10")
        seccion3.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5, padx=10)

        # Campos de entrada
        ttk.Label(seccion3, text="Fecha (DD/MM/YYYY):").grid(row=0, column=0, sticky=tk.W, pady=5, padx=(0, 10))
        self.entry_fecha = ttk.Entry(seccion3, width=15, font=("Arial", 10))
        self.entry_fecha.grid(row=0, column=1, pady=5, padx=5)

        ttk.Label(seccion3, text="Hora (HH:MM):").grid(row=0, column=2, sticky=tk.W, padx=(20, 0), pady=5)
        self.entry_hora = ttk.Entry(seccion3, width=10, font=("Arial", 10))
        self.entry_hora.grid(row=0, column=3, pady=5, padx=5)

        ttk.Label(seccion3, text="Descripción:").grid(row=1, column=0, sticky=tk.W, pady=(10, 5), padx=(0, 10))
        self.entry_desc = ttk.Entry(seccion3, width=50, font=("Arial", 10))
        self.entry_desc.grid(row=1, column=1, columnspan=3, sticky=(tk.W, tk.E), pady=5, padx=5)

        seccion3.columnconfigure(1, weight=1)

        # ===== SECCIÓN 4: ACCIONES =====
        seccion4 = ttk.LabelFrame(self.root, text="ACCIONES", padding="15")
        seccion4.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10, padx=10)

        ttk.Button(seccion4, text="Agregar Evento", command=self.agregar_evento).grid(row=0, column=0, padx=8, pady=5)
        ttk.Button(seccion4, text="Eliminar Seleccionado", command=self.eliminar_evento).grid(row=0, column=1, padx=8,
                                                                                              pady=5)
        ttk.Button(seccion4, text="Limpiar Todo", command=self.limpiar_todo).grid(row=0, column=2, padx=8, pady=5)
        ttk.Button(seccion4, text="Salir", command=self.root.quit).grid(row=0, column=3, padx=8, pady=5)

        # Configuración de expansión
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        seccion2.columnconfigure(0, weight=1)
        seccion2.rowconfigure(0, weight=1)

    def agregar_evento(self):
        """Agrega nuevo evento validando formato"""
        fecha = self.entry_fecha.get().strip()
        hora = self.entry_hora.get().strip()
        desc = self.entry_desc.get().strip()

        # Validar campos vacíos
        if not all([fecha, hora, desc]):
            messagebox.showwarning("Error", "¡Completa todos los campos!")
            return

        # Validar formatos
        try:
            datetime.strptime(fecha, "%d/%m/%Y")
            datetime.strptime(hora, "%H:%M")
        except ValueError:
            messagebox.showerror("Error", "Formato:\n• Fecha: DD/MM/YYYY\n• Hora: HH:MM")
            return

        # Crear y agregar evento
        evento = Evento(fecha, hora, desc)
        self.eventos.append(evento)
        self.tree.insert("", "end", values=(fecha, hora, desc))

        # LIMPIAR CAMPOS AUTOMÁTICAMENTE
        self.entry_fecha.delete(0, tk.END)
        self.entry_hora.delete(0, tk.END)
        self.entry_desc.delete(0, tk.END)

        messagebox.showinfo("¡Éxito!", "Evento agregado correctamente ✓")

    def eliminar_evento(self):
        """Elimina el evento seleccionado"""
        seleccion = self.tree.selection()

        if not seleccion:
            messagebox.showwarning("Advertencia", "¡Selecciona un evento de la lista!")
            return

        if messagebox.askyesno("Confirmar", "¿Eliminar este evento?"):
            item = self.tree.index(seleccion[0])
            self.tree.delete(seleccion[0])
            if 0 <= item < len(self.eventos):
                del self.eventos[item]
            messagebox.showinfo("¡Listo!", "Evento eliminado ✓")

    def limpiar_todo(self):
        """Elimina todos los eventos"""
        if not self.eventos:
            messagebox.showinfo("Info", "La agenda ya está vacía")
            return

        if messagebox.askyesno("Confirmar", f"¿Eliminar TODOS los {len(self.eventos)} eventos?"):
            # Limpiar TreeView
            for item in self.tree.get_children():
                self.tree.delete(item)
            # Limpiar lista
            self.eventos.clear()
            messagebox.showinfo("¡Listo!", "¡Agenda completamente limpia! 🧹")


def main():
    """Ejecuta la aplicación"""
    root = tk.Tk()
    app = AgendaPersonal(root)
    root.mainloop()


if __name__ == "__main__":
    main()
