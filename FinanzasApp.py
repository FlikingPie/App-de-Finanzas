import tkinter as tk
from tkinter import messagebox, ttk
import customtkinter
from datetime import datetime
from gastos import ventana_gastos
from archivos import ventana_archivos
from categorias import ventana_categorias
from estadisticas import ventana_estadisticas
from personalizar import ventana_personalizar
from support import ventana_support

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

class FinanzasApp:
    #Abrir cada menú
    def abrir_vent_gastos(self):
        ventana_gastos(self.tree)

    def abrir_vent_archivo(self):
        ventana_archivos(self.tree)
    
    def abrir_vent_categorias(self):
        ventana_categorias(self.tree)

    def abrir_vent_estadisticas(self):
        ventana_estadisticas(self.tree)
    
    def abrir_vent_config(self):
        ventana_personalizar()
    
    def abrir_vent_ayuda(self):
        ventana_support()

    #Cerrar app
    def exit_app(self, event):
        self.root.destroy()

    def __init__(self,root):
        self.root=root
        self.root.geometry("800x400+450+350")
        self.root.title("Registro de finanzas")

        #Crear tabla
        self.headings=["Fecha", "Categoría", "Descripción", "Monto S/"]
        self.tree = ttk.Treeview(root, show="headings", columns=self.headings)
        for col in self.headings:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor="center")

        self.tree.pack(expand=True, fill="both")

        #Crear menú
        self.barra_menu = tk.Menu(root)
        self.root.config(menu=self.barra_menu)

        #Menus
        self.root.bind("<Escape>", self.exit_app)
        self.menu_archivo = tk.Menu(self.barra_menu, tearoff=0)
        self.menu_gasto = tk.Menu(self.barra_menu, tearoff=0)
        self.menu_categorias = tk.Menu(self.barra_menu, tearoff=0)
        self.menu_estadisticas = tk.Menu(self.barra_menu, tearoff=0)
        self.menu_configuración = tk.Menu(self.barra_menu, tearoff=0)
        self.menu_ayuda = tk.Menu(self.barra_menu, tearoff=0)

        
        self.barra_menu.add_cascade(label="Archivo", menu=self.menu_archivo)
        self.barra_menu.add_cascade(label="Gastos", menu=self.menu_gasto)
        self.barra_menu.add_cascade(label="Categorías", menu=self.menu_categorias)
        self.barra_menu.add_cascade(label="Estadísticas", menu=self.menu_estadisticas)
        self.barra_menu.add_cascade(label="Configuración", menu=self.menu_configuración)
        self.barra_menu.add_cascade(label="Ayuda", menu=self.menu_ayuda)

        self.menu_archivo.add_command(label="Abrir ventana archivos", command=self.abrir_vent_archivo)
        self.menu_gasto.add_command(label="Abiri ventana gastos", command=self.abrir_vent_gastos)
        self.menu_categorias.add_command(label="Abrir ventana categorías", command=self.abrir_vent_categorias)
        self.menu_configuración.add_command(label="Abrir ventana personalizar", command=self.abrir_vent_config)
        self.menu_estadisticas.add_command(label="Abrir ventana estadísticas", command=self.abrir_vent_estadisticas)
        self.menu_ayuda.add_command(label="Abrir ventana support", command=self.abrir_vent_ayuda)
        
if __name__ =="__main__":
    root = customtkinter.CTk()
    app = FinanzasApp(root)
    root.mainloop()