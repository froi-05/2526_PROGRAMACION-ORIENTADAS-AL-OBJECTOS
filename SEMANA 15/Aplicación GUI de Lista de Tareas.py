# Aplicación GUI de Lista de Tareas - Tarea POO
# Autor: Tejada De La Cruz Froilan
# Fecha: 29 de marzo de 2026
# Descripción: App con Tkinter para añadir tareas con Enter, marcar completadas (✓ y doble clic),
# eliminar seleccionadas. Listbox muestra todo, clase principal maneja eventos y lógica.

import tkinter as tk
from tkinter import messagebox


class ListaTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas - Froilan Tejada")
        self.root.geometry("450x500")
        self.root.resizable(False, False)

        self.tareas = []  # Almacena tareas (pendientes/completadas)

        # 1. Campo de entrada
        tk.Label(self.root, text="Nueva tarea:", font=("Arial", 11, "bold")).pack(pady=10)
        self.entry = tk.Entry(self.root, font=("Arial", 12), width=35, relief="solid", bd=1)
        self.entry.pack(pady=5)
        self.entry.focus()
        self.entry.bind("<Return>", self.add_tarea)

        # 2. Botones
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=15)

        self.btn_add = tk.Button(btn_frame, text="➕ Añadir Tarea",
                                 command=self.add_tarea, bg="#90EE90", fg="darkgreen",
                                 font=("Arial", 10, "bold"), width=14)
        self.btn_add.pack(side=tk.LEFT, padx=8)

        self.btn_complete = tk.Button(btn_frame, text="✅ Completar",
                                      command=self.mark_complete, bg="#87CEEB", fg="navy",
                                      font=("Arial", 10, "bold"), width=14)
        self.btn_complete.pack(side=tk.LEFT, padx=8)

        self.btn_delete = tk.Button(btn_frame, text="🗑️ Eliminar",
                                    command=self.delete_tarea, bg="#F08080", fg="darkred",
                                    font=("Arial", 10, "bold"), width=14)
        self.btn_delete.pack(side=tk.LEFT, padx=8)

        # 3. Listbox con scroll
        tk.Label(self.root, text="Lista de Tareas:", font=("Arial", 11, "bold")).pack(anchor="w", padx=15, pady=(20, 5))
        frame_list = tk.Frame(self.root)
        frame_list.pack(pady=5, padx=15, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(frame_list)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(frame_list, font=("Arial", 11), height=18,
                                  selectmode=tk.SINGLE, yscrollcommand=scrollbar.set,
                                  relief="solid", bd=1, selectbackground="#ADD8E6")
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.listbox.yview)

        self.listbox.bind("<Double-Button-1>", self.on_double_click)

        # Estadísticas
        self.stats_label = tk.Label(self.root, text="Tareas totales: 0 | Completadas: 0",
                                    font=("Arial", 10), fg="gray")
        self.stats_label.pack(pady=10)

    def add_tarea(self, event=None):
        texto = self.entry.get().strip()
        if len(texto) >= 3:
            self.tareas.append(texto)
            self.actualizar_listbox()
            self.entry.delete(0, tk.END)
            self.entry.focus()
        else:
            messagebox.showwarning("¡Error!", "La tarea debe tener al menos 3 caracteres.")

    def mark_complete(self):
        seleccion = self.listbox.curselection()
        if seleccion:
            idx = seleccion[0]
            if not self.tareas[idx].startswith("✓"):
                self.tareas[idx] = f"✓ {self.tareas[idx]}"
                self.actualizar_listbox()
        else:
            messagebox.showwarning("¡Selecciona!", "Debes seleccionar una tarea.")

    def delete_tarea(self):
        seleccion = self.listbox.curselection()
        if seleccion:
            respuesta = messagebox.askyesno("Confirmar", "¿Eliminar esta tarea?")
            if respuesta:
                del self.tareas[seleccion[0]]
                self.actualizar_listbox()
        else:
            messagebox.showwarning("¡Selecciona!", "Debes seleccionar una tarea.")

    def on_double_click(self, event):
        self.mark_complete()

    def actualizar_listbox(self):
        self.listbox.delete(0, tk.END)
        completadas = sum(1 for t in self.tareas if t.startswith("✓"))
        total = len(self.tareas)
        self.stats_label.config(text=f"Tareas totales: {total} | Completadas: {completadas}")
        for tarea in self.tareas:
            self.listbox.insert(tk.END, tarea)


if __name__ == "__main__":
    root = tk.Tk()
    app = ListaTareasApp(root)
    root.mainloop()
