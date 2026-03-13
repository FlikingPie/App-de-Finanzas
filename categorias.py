import customtkinter
from tkinter import messagebox, simpledialog
from gastos import categorias
from rich import print

def ventana_categorias(tree):
    top = customtkinter.CTkToplevel()
    top.title("Ventana categorías")
    top.geometry("300x300+450+200")
    top.resizable(False, False)

    def agregar_categoria():
        global categorias
        new_cat = simpledialog.askstring("Nueva cat", "Ingrese la nueva categoría:")
        if new_cat in categorias:
            messagebox.showerror("Error", f'La categoría: {new_cat} ya se encuentra en la lista.')
            return
        else:
            categorias.append(new_cat)
    customtkinter.CTkButton(top, text="Agregar categoría", width=100, command=agregar_categoria).pack(pady=5)

    def eliminar_categoria():
        global categorias
        delete_cat = simpledialog.askstring("Eliminar cat", "Ingrese la categoría:")
        if delete_cat not in categorias:
            messagebox.showerror("Error", f'No se encontró la categoría: {delete_cat}')
            return
        else:
            categorias.remove(delete_cat)
    customtkinter.CTkButton(top, text="Eliminar categoría", width=100, command=eliminar_categoria).pack(pady=5)

    def mostrar_categorías():
        global categorias
        if not categorias:
            messagebox.showerror("Error", "No hay categorías.")
            return
        else:
            for i, categoria in enumerate(categorias, start=1):
                print(f'[{i}] {categoria}.')
            print("")
    customtkinter.CTkButton(top, text="Mostrar categorías", width=100, command=mostrar_categorías).pack(pady=5)

