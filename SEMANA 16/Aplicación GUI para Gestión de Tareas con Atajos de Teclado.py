# Gestión de Tareas con Atajos de Teclado - Tarea POO
# Autor: Tejada De La Cruz Froilán
# Fecha: 05 de abril de 2026
# Descripción: App Tkinter con botones + ATAJOS: Enter(añadir), C(completar), Delete/D(eliminar), Esc(cerrar)
# Feedback visual ✓, stats, scroll, validaciones completas.

import tkinter as tk
from tkinter import messagebox


class GestionTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 Gestión de Tareas - Atajos: Enter/C/Delete/Esc")
        self.root.geometry("500x580")
        self.root.resizable(False, False)

        self.tareas = []

        # ========================================
        # ATAJOS GLOBALES - FUNCIONAN SIEMPRE
        # ========================================
        self.root.bind("<Escape>", self.cerrar_app)
        self.root.bind("<c>", self.mark_tecla)
        self.root.bind("<C>", self.mark_tecla)  # Mayús + C también
        self.root.bind("<Delete>", self.delete_tecla)
        self.root.bind("<d>", self.delete_tecla)
        self.root.bind("<D>", self.delete_tecla)

        # Título grande
        tk.Label(root, text="📋 GESTIÓN DE TAREAS", font=("Arial", 18, "bold"), fg="#2C3E50").pack(pady=20)

        # ATAJOS VISIBLES
        atajos_frame = tk.Frame(root, bg="#ECF0F1", relief="ridge", bd=2)
        atajos_frame.pack(pady=10, padx=20, fill="x")
        tk.Label(atajos_frame, text="🔥 ATAJOS: Enter=añadir | C=Completar | Delete/D=Eliminar | Esc=Cerrar",
                 font=("Arial", 10, "bold"), fg="#E74C3C", bg="#ECF0F1").pack(pady=8)

        # Entry para nueva tarea
        tk.Label(root, text="✏️ Escribe nueva tarea:", font=("Arial", 12, "bold")).pack(pady=(20, 5))
        self.entry = tk.Entry(root, font=("Arial", 13), width=45, relief="solid", bd=2)
        self.entry.pack(pady=10)
        self.entry.focus()
        self.entry.bind("<Return>", self.add_tarea)  # Enter específico

        # Botones backup
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=20)
        tk.Button(btn_frame, text="➕ AÑADIR", command=self.add_tarea, bg="#27AE60", fg="white",
                  font=("Arial", 12, "bold"), width=13, height=1).pack(side=tk.LEFT, padx=15)
        tk.Button(btn_frame, text="✅ COMPLETAR (C)", command=self.mark_complete, bg="#3498DB", fg="white",
                  font=("Arial", 12, "bold"), width=13, height=1).pack(side=tk.LEFT, padx=15)
        tk.Button(btn_frame, text="🗑️ ELIMINAR (Del/D)", command=self.delete_tarea, bg="#E74C3C", fg="white",
                  font=("Arial", 12, "bold"), width=13, height=1).pack(side=tk.LEFT, padx=15)

        # Listbox PROFESIONAL
        tk.Label(root, text="📂 LISTA DE TAREAS:", font=("Arial", 13, "bold")).pack(anchor="w", padx=25, pady=(25, 8))

        list_container = tk.Frame(root)
        list_container.pack(pady=10, padx=25, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(list_container)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(list_container, font=("Consolas", 12), height=22,
                                  selectmode=tk.SINGLE,
                                  yscrollcommand=self.scrollbar.set,
                                  relief="groove", bd=3,
                                  selectbackground="#85C1E9",
                                  bg="#FEFEFE",
                                  fg="#2C3E50")
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.listbox.yview)

        # DOBLE CLIC bonus
        self.listbox.bind("<Double-Button-1>", self.doble_clic)

        # ========================================
        # STATS - SE ACTUALIZAN DESDE PRIMERA TAREA
        # ========================================
        self.stats_frame = tk.LabelFrame(root, text="📊 ESTADÍSTICAS", font=("Arial", 11, "bold"), padx=20, pady=10)
        self.stats_frame.pack(pady=20, fill="x", padx=25)
        self.stats_label = tk.Label(self.stats_frame, text="Total: 0 | Completadas: 0 | Pendientes: 0",
                                    font=("Arial", 12, "bold"), fg="#34495E")
        self.stats_label.pack(pady=5)

        # Actualizar stats inicial
        self.actualizar_stats()

    def add_tarea(self, event=None):
        texto = self.entry.get().strip()
        if len(texto) >= 2:
            self.tareas.append(texto)
            self.entry.delete(0, tk.END)
            self.entry.focus()
            self.actualizar_lista()
            print("✅ Tarea añadida:", texto)  # Debug consola
        else:
            messagebox.showerror("❌ Error", "¡Tarea muy corta! Mínimo 2 caracteres.")

    def mark_tecla(self, event=None):
        print("🔥 Tecla C presionada!")  # Debug
        self.mark_complete()

    def mark_complete(self):
        seleccion = self.listbox.curselection()
        if seleccion:
            idx = seleccion[0]
            if not self.tareas[idx].startswith("✓"):
                self.tareas[idx] = f"✓ {self.tareas[idx]}"
                self.actualizar_lista()
                print("✅ Tarea completada")
        else:
            messagebox.showwarning("⚠️", "Selecciona una tarea primero (Clic).")

    def delete_tecla(self, event=None):
        print("💥 Tecla Delete/D presionada!")
        self.delete_tarea()

    def delete_tarea(self):
        seleccion = self.listbox.curselection()
        if seleccion:
            if messagebox.askyesno("🗑️ Confirmar", "¿Eliminar tarea seleccionada?"):
                del self.tareas[seleccion[0]]
                self.actualizar_lista()
                print("🗑️ Tarea eliminada")
        else:
            messagebox.showwarning("⚠️", "Selecciona tarea para eliminar (Delete/D).")

    def doble_clic(self, event):
        self.mark_complete()

    def cerrar_app(self, event=None):
        if messagebox.askokcancel("🚪 Salir", "¿Cerrar Gestión de Tareas?"):
            print("👋 App cerrada con ESC")
            self.root.quit()

    def actualizar_lista(self):
        self.listbox.delete(0, tk.END)
        for tarea in self.tareas:
            self.listbox.insert(tk.END, tarea)
        self.actualizar_stats()

    def actualizar_stats(self):
        total = len(self.tareas)
        completadas = sum(1 for t in self.tareas if t.startswith("✓"))
        pendientes = total - completadas
        self.stats_label.config(text=f"Total: {total} | Completadas: {completadas} | Pendientes: {pendientes}")
        print(f"📊 Stats: {total}/{completadas}/{pendientes}")  # Debug


if __name__ == "__main__":
    root = tk.Tk()
    app = GestionTareasApp(root)
    root.mainloop()
