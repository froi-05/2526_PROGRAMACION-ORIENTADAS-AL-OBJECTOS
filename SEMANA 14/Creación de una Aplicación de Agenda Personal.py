# Agenda Personal GUI - Tkinter Treeview - Tarea POO
# Autor: Tejada De La Cruz Froilán
# Fecha: 22 marzo 2026
# Treeview eventos + Date Entry + Frames organizados

import tkinter as tk
from tkinter import ttk, messagebox


class AgendaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("📅 AGENDA PERSONAL - Mis Eventos")
        self.root.geometry("700x500")

        # Lista eventos: {id: {'fecha','hora','desc'}}
        self.eventos = {}
        self.next_id = 1

        self.crear_interfaz()

    def crear_interfaz(self):
        # FRAME 1: TÍTULO
        frame_titulo = tk.Frame(self.root, bg="#2c3e50", height=60)
        frame_titulo.pack(fill="x")
        frame_titulo.pack_propagate(False)
        tk.Label(frame_titulo, text="📅 AGENDA PERSONAL", font=("Arial", 18, "bold"),
                 bg="#2c3e50", fg="white").pack(expand=True)

        # FRAME 2: INPUTS (Entry fecha/hora/descripción)
        frame_inputs = tk.LabelFrame(self.root, text="Nuevo Evento", font=("Arial", 12, "bold"))
        frame_inputs.pack(pady=10, padx=10, fill="x")

        # Fecha (DatePicker simple: Entry formato DD/MM/YYYY)
        tk.Label(frame_inputs, text="Fecha (DD/MM):").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.entry_fecha = tk.Entry(frame_inputs, width=12, font=("Arial", 11))
        self.entry_fecha.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_inputs, text="Hora (HH:MM):").grid(row=0, column=2, sticky="w", padx=5, pady=5)
        self.entry_hora = tk.Entry(frame_inputs, width=10, font=("Arial", 11))
        self.entry_hora.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(frame_inputs, text="Descripción:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.entry_desc = tk.Entry(frame_inputs, width=50, font=("Arial", 11))
        self.entry_desc.grid(row=1, column=1, columnspan=3, sticky="ew", padx=5, pady=5)
        frame_inputs.columnconfigure(1, weight=1)

        # Botones inputs
        frame_botones_input = tk.Frame(frame_inputs)
        frame_botones_input.grid(row=2, column=1, columnspan=3, pady=10)

        self.btn_agregar = tk.Button(frame_botones_input, text="➕ AGREGAR EVENTO",
                                     command=self.agregar_evento,
                                     bg="#27ae60", fg="white", font=("Arial", 10, "bold"))
        self.btn_agregar.pack(side="left", padx=5)

        self.btn_limpiar = tk.Button(frame_botones_input, text="🧹 LIMPIAR CAMPOS",
                                     command=self.limpiar_campos,
                                     bg="#3498db", fg="white", font=("Arial", 10, "bold"))
        self.btn_limpiar.pack(side="left", padx=5)

        # FRAME 3: LISTA EVENTOS (Treeview)
        frame_lista = tk.LabelFrame(self.root, text="Eventos Programados", font=("Arial", 12, "bold"))
        frame_lista.pack(pady=10, padx=10, fill="both", expand=True)

        # Treeview columnas: ID, Fecha, Hora, Descripción
        columnas = ("ID", "Fecha", "Hora", "Descripción")
        self.tree = ttk.Treeview(frame_lista, columns=columnas, show="headings", height=12)

        # Definir headings
        self.tree.heading("ID", text="ID")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")

        # Columnas ancho
        self.tree.column("ID", width=50)
        self.tree.column("Fecha", width=100)
        self.tree.column("Hora", width=80)
        self.tree.column("Descripción", width=300)

        # Scrollbars
        v_scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=self.tree.yview)
        h_scrollbar = ttk.Scrollbar(frame_lista, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

        # Pack Treeview + scrolls
        self.tree.grid(row=0, column=0, sticky="nsew")
        v_scrollbar.grid(row=0, column=1, sticky="ns")
        h_scrollbar.grid(row=1, column=0, sticky="ew")
        frame_lista.grid_rowconfigure(0, weight=1)
        frame_lista.grid_columnconfigure(0, weight=1)

        # Selección Treeview → Eliminar
        self.tree.bind("<ButtonRelease-1>", self.seleccionar_evento)

        # FRAME 4: BOTONES ACCIONES
        frame_acciones = tk.Frame(self.root)
        frame_acciones.pack(pady=10, fill="x")

        self.btn_eliminar = tk.Button(frame_acciones, text="🗑️ ELIMINAR SELECCIONADO",
                                      command=self.eliminar_evento,
                                      bg="#e74c3c", fg="white", font=("Arial", 10, "bold"))
        self.btn_eliminar.pack(side="left", padx=10)

        self.btn_salir = tk.Button(frame_acciones, text="❌ SALIR",
                                   command=self.root.quit,
                                   bg="#95a5a6", fg="white", font=("Arial", 10, "bold"))
        self.btn_salir.pack(side="right", padx=10)

    def agregar_evento(self):
        """Agrega evento validando formato fecha/hora"""
        fecha = self.entry_fecha.get().strip()
        hora = self.entry_hora.get().strip()
        desc = self.entry_desc.get().strip()

        # Validaciones
        if not all([fecha, hora, desc]):
            messagebox.showwarning("Error", "¡Completa todos los campos!")
            return

        try:
            # Validar fecha formato DD/MM
            if len(fecha) != 5 or fecha[2] != "/":
                raise ValueError("Fecha debe ser DD/MM")
            dia, mes = map(int, fecha.split("/"))
            if not (1 <= dia <= 31 and 1 <= mes <= 12):
                raise ValueError("Fecha inválida")

            # Validar hora HH:MM
            if len(hora) != 5 or hora[2] != ":":
                raise ValueError("Hora debe ser HH:MM")
            hora_int, minuto = map(int, hora.split(":"))
            if not (0 <= hora_int <= 23 and 0 <= minuto <= 59):
                raise ValueError("Hora inválida")

        except ValueError as e:
            messagebox.showerror("Formato", f"Error: {e}")
            return

        # AGREGAR a Treeview
        evento_id = str(self.next_id)
        self.eventos[evento_id] = {'fecha': fecha, 'hora': hora, 'desc': desc}

        self.tree.insert("", "end", values=(evento_id, fecha, hora, desc))
        self.next_id += 1

        self.limpiar_campos()
        messagebox.showinfo("¡Listo!", f"Evento '{desc[:20]}...' agregado ✓")

    def eliminar_evento(self):
        """Elimina evento seleccionado con confirmación"""
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Atención", "¡Selecciona un evento primero!")
            return

        # Confirmación opcional
        evento_sel = self.tree.item(seleccion)
        desc = evento_sel['values'][3][:30]
        if messagebox.askyesno("Confirmar", f"¿Eliminar?\n{desc}"):
            evento_id = evento_sel['values'][0]
            del self.eventos[evento_id]
            self.tree.delete(seleccion)
            messagebox.showinfo("Eliminado", "Evento borrado ✓")

    def seleccionar_evento(self, event):
        """Destaca selección Treeview"""
        pass  # Solo visual

    def limpiar_campos(self):
        """Limpia todos Entries"""
        self.entry_fecha.delete(0, tk.END)
        self.entry_hora.delete(0, tk.END)
        self.entry_desc.delete(0, tk.END)
        self.entry_fecha.focus()


def main():
    root = tk.Tk()
    app = AgendaGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
