import tkinter as tk
import customtkinter
from tkinter import messagebox, simpledialog
from datetime import datetime
from rich import print
from database import insertar_gasto_sql
from database import eliminar_gasto_sql
from database import modificar_gasto_sql
from config import categorias

categorias=[
        "Comida",
        "Entretenimiento",
        "Trabajo",
        "Transporte",
        "Educación",
        "Salud",
        "Deudas",
        "Servicios"
    ]

def ventana_gastos(tree):
    top = customtkinter.CTkToplevel()
    top.title("Ventana gastos")
    top.geometry("300x350+450+250")
    top.resizable(False, False)
    top.grab_set()

    def agregar_gasto():
        top_add = customtkinter.CTkToplevel()
        top_add.title("Agregar gasto")
        top_add.geometry("350x380+400+250")
        top_add.resizable(False, False)
        top_add.grab_set()
        
        customtkinter.CTkLabel(top_add, text="Fecha").pack(pady=5)
        fecha_entry = customtkinter.CTkEntry(top_add, width=100)
        fecha_entry.pack(pady=5)

        customtkinter.CTkLabel(top_add, text="Categoría").pack(pady=5)
        categoria_entry = customtkinter.CTkEntry(top_add, width=100)
        categoria_entry.pack(pady = 5)

        customtkinter.CTkLabel(top_add, text="Descripción").pack(pady=5)
        descp_entry = customtkinter.CTkEntry(top_add, width=100)
        descp_entry.pack(pady=5)

        customtkinter.CTkLabel(top_add, text="Monto S/").pack(pady=5)
        monto_entry = customtkinter.CTkEntry(top_add, width=100)
        monto_entry.pack(pady=5)

        def guardar():
            fecha=fecha_entry.get().strip()
            categoria = categoria_entry.get().strip()
            descripcion = descp_entry.get().strip()
            monto = monto_entry.get().strip()

            if not fecha or not categoria or not descripcion or not monto:
                messagebox.showwarning("Advertencia", "Complete todos los campos.")
                return
            
            if categoria not in categorias:
                messagebox.showerror("Error", "Ingrese una categoría válida.")
                return
            
            try:
                f=fecha_entry.get().strip()
                f_f = datetime.strptime(f, "%d/%m/%Y") #Pasa de string a clase date
                fecha_string = f_f.strftime("%d/%m/%Y") #Pasa de clase DATE a string --> f_f es una clase y strftime un metodo

            except ValueError:
                messagebox.showerror("Error", "Formato de fecha inválido.")
                return
            
            try:
                monto = float(monto_entry.get().strip())
            except ValueError:
                messagebox.showerror("Error", "Ingrese un monto válido.")
                return
            
            insertar_gasto_sql(fecha_string, categoria, descripcion, monto)
            tree.insert("", "end", values=(fecha_string, categoria, descripcion, monto))
            top_add.destroy()
            
        customtkinter.CTkButton(top_add, text="GUARDAR", command=guardar, width=100).pack(pady=5)
            
    customtkinter.CTkButton(top, width=100, command=agregar_gasto, text="Agregar gasto").pack(pady=5)

    def eliminar_gasto():
        if not tree.get_children():
            messagebox.showerror("Error", "Tabla vacía.")
            return
        else:
            search_descp = simpledialog.askstring("Buscar gasto", "Ingrese la descripción:")
            if not search_descp:
                messagebox.showerror("Error", "No se encontro el gasto.")
                return
        
            for item in tree.get_children():
                datos = tree.item(item, "values")
                if search_descp in datos[2]:
                   tree.delete(item)
                   break
            else:
                messagebox.showerror("Error", f'No se encontro la descripción: {search_descp}')
                return
        eliminar_gasto_sql(search_descp)
    customtkinter.CTkButton(top, text="Eliminar gasto", width=100, command=eliminar_gasto).pack(pady=5)

    def modificar_gasto():
        if not tree.get_children():
            messagebox.showerror("Error", "Tabla vacía")
            return
        else:
            search_descp = simpledialog.askstring("Descripción", "Ingrese la descripción:")
            if not search_descp:
                messagebox.showerror("Error", "No se encontro el gasto")
                return
            
            for item in tree.get_children():
                datos = tree.item(item, "values")
                if search_descp in datos[2]:
                    try:
                        f = simpledialog.askstring("Nueva fecha", "Ingrese la nueva fecha:")
                        f_f = datetime.strptime(f, "%d/%m/%Y")
                        new_fecha = f_f.strftime("%d/%m/%Y")
                    except ValueError:
                        messagebox.showerror("Error", "Formato de fecha inválido.")
                        return
                    
                    new_cat = simpledialog.askstring("Nueva cat", "Ingrese la nueva categoría:")
                    new_descp = simpledialog.askstring("Nueva descp", "Ingrese la nueva descripción:")
                    new_monto = simpledialog.askfloat("Nuevo monto", "Ingrese el nuevo monto S/:")
                    
                    modificar_gasto_sql(new_fecha, new_cat, new_descp, new_monto, search_descp)
                    tree.item(item, values=(new_fecha, new_cat, new_descp, new_monto))
                    break
            else:
                messagebox.showerror("Error", f'No se encontro la descripción: {search_descp}.')
                return
    customtkinter.CTkButton(top, text="Modificar gasto", width=100, command=modificar_gasto).pack(pady=5)

    def buscar_gasto():
        if not tree.get_children():
            messagebox.showerror("Error","Tabla vacía.")
            return
        else:
            items = []
            for item in tree.get_children():
                items.append(tree.item(item, "values"))

            search_gasto = simpledialog.askstring("Buscar gasto", "Ingrese la descripción:")
            filtrado = list(filter(lambda x: x[2] == search_gasto, items))
            print(filtrado)
    customtkinter.CTkButton(top, text="Buscar gasto", width=100, command=buscar_gasto).pack(pady=5)

    def filtrar_por_fecha():
        if not tree.get_children():
            messagebox.showerror("Error", "Tabla vacía")
            return
        else:
            gastos_items=[]
            for item in tree.get_children():
                gastos_items.append(tree.item(item, "values"))

            try:
                f = simpledialog.askstring("Filtrar fecha", "Ingrese la fecha:")
                f_f = datetime.strptime(f, "%d/%m/%Y")
                fecha = f_f.strftime("%d/%m/%Y")
            except ValueError:
                messagebox.showerror("Error", "Formato de fecha inválido.")
                return
            
            gatos_fecha = list(filter(lambda x: x[0] == fecha, gastos_items))
            print(gatos_fecha)
    customtkinter.CTkButton(top, text="Filtrar por fecha", width=100, command=filtrar_por_fecha).pack(pady=5)

    def filtrar_por_categoria():
        if not tree.get_children():
            messagebox.showerror("Error", "Tabla vacía.")
            return
        else:
            categorias_items=[]
            for item in tree.get_children():
                categorias_items.append(tree.item(item, "values"))

            cat = simpledialog.askstring("Filtrar categoría", "Ingrese la categoría:")
            
            filtrados = list(filter(lambda x: x[1] == cat, categorias_items))
            print(filtrados)
            
    customtkinter.CTkButton(top, text="Filtrar por categoría", width=100, command=filtrar_por_categoria).pack(pady=5)

    def filtrar_por_monto():
        if not tree.get_children():
            messagebox.showerror("Error", "Tabla vacía.")
            return
        else:
            monto_items = []
            for item in tree.get_children():
                monto_items.append(tree.item(item, "values"))
            
            monto = simpledialog.askfloat("Filtrar monto", "Ingrese el monto:")
            filtrados = list(filter(lambda x: float(x[3]) == monto, monto_items))
            print(filtrados)

    customtkinter.CTkButton(top, text="Filtrar por monto", width=100, command=filtrar_por_monto).pack(pady=5)
