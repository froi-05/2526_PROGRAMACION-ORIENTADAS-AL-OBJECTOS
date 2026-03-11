# Gestor de Tareas GUI - Tkinter - Tarea POO
# Autor: Tejada De La Cruz Froilán
# Fecha: 15 marzo 2026
# Funciona: Agregar tarea → Lista → Limpiar selección

import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar


class GestorTareasGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🗒️ Gestor de Tareas - Mi primera GUI")
        self.root.geometry("500x400")
        self.root.resizable(True, True)

        # Lista para guardar tareas (cumple "almacenar datos")
        self.tareas = []

        self.crear_interfaz()

    def crear_interfaz(self):
        # FRAME superior para inputs
        frame_input = tk.Frame(self.root)
        frame_input.pack(pady=10, padx=10, fill="x")

        # Label descriptivo
        tk.Label(frame_input, text="Nueva Tarea:", font=("Arial", 12, "bold")).pack(anchor="w")

        # Campo texto (Entry)
        self.entry_tarea = tk.Entry(frame_input, font=("Arial", 11), width=40)
        self.entry_tarea.pack(pady=5, fill="x")
        self.entry_tarea.focus()  # Cursor listo

        # Frame botones
        frame_botones = tk.Frame(frame_input)
        frame_botones.pack(pady=10)

        # Botón AGREGAR (evento click)
        self.btn_agregar = tk.Button(frame_botones, text="➕ Agregar",
                                     command=self.agregar_tarea,
                                     bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
        self.btn_agregar.pack(side="left", padx=5)

        # Botón LIMPIAR (evento click)
        self.btn_limpiar = tk.Button(frame_botones, text="🗑️ Limpiar",
                                     command=self.limpiar_seleccion,
                                     bg="#f44336", fg="white", font=("Arial", 10, "bold"))
        self.btn_limpiar.pack(side="left", padx=5)

        # Lista con scrollbar (muestra datos)
        frame_lista = tk.Frame(self.root)
        frame_lista.pack(pady=10, padx=10, fill="both", expand=True)

        tk.Label(frame_lista, text="Tareas Agregadas:", font=("Arial", 11, "bold")).pack(anchor="w")

        # Listbox + Scrollbar
        lista_frame = tk.Frame(frame_lista)
        lista_frame.pack(fill="both", expand=True)

        scrollbar = Scrollbar(lista_frame)
        scrollbar.pack(side="right", fill="y")

        self.lista_tareas = Listbox(lista_frame, font=("Arial", 10),
                                    yscrollcommand=scrollbar.set)
        self.lista_tareas.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.lista_tareas.yview)

        # Bind doble click para limpiar
        self.lista_tareas.bind("<Double-Button-1>", self.limpiar_seleccion)

        # Enter para agregar rápido
        self.entry_tarea.bind("<Return>", lambda e: self.agregar_tarea())

    def agregar_tarea(self):
        """FUNCIONALIDAD 1: Agregar desde Entry → Lista"""
        tarea = self.entry_tarea.get().strip()
        if tarea:
            # Agrego con timestamp simple
            tarea_completa = f"[{len(self.tareas) + 1}] {tarea}"
            self.tareas.append(tarea_completa)
            self.lista_tareas.insert(tk.END, tarea_completa)

            # Limpio campo y enfoco
            self.entry_tarea.delete(0, tk.END)
            self.entry_tarea.focus()

            print(f"Tarea agregada: {tarea}")  # Debug consola
        else:
            messagebox.showwarning("Atención", "¡Escribe una tarea!")

    def limpiar_seleccion(self, event=None):
        """FUNCIONALIDAD 2: Limpiar selección o todo"""
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            # Elimina seleccionado
            indice = seleccion[0]
            self.lista_tareas.delete(indice)
            del self.tareas[indice]
            messagebox.showinfo("Listo", f"Tarea {indice + 1} eliminada")
        else:
            # Si nada seleccionado, limpia todo
            respuesta = messagebox.askyesno("Confirmar", "¿Limpiar TODAS las tareas?")
            if respuesta:
                self.tareas.clear()
                self.lista_tareas.delete(0, tk.END)
                messagebox.showinfo("Listo", "¡Todo limpio!")


def main():
    root = tk.Tk()
    app = GestorTareasGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
