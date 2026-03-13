import customtkinter
import time
import pandas as pd
from rich import print
from rich.console import Console
from rich.theme import Theme
from rich.progress import track
from tkinter import messagebox
from fpdf import FPDF
from tabulate import tabulate


def ventana_archivos(tree):
    top = customtkinter.CTkToplevel()
    top.title("Ventana archivos")
    top.geometry("300x300+450+250")
    top.resizable(False, False)

    custom_theme=Theme({"succes":"green", "error":"red"})
    console=Console(theme=custom_theme)



    def crear_pdf():
        try:
            item = tree.selection()
            if not tree.get_children():
               messagebox.showerror("Error", "Tabla vacía.")
               return
        
            if not item:
              messagebox.showwarning("Advertencia", "Seleccione una fila.")
              return
        
            item = item[0]
            datos = tree.item(item, "values")

            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", "B", 18)
            pdf.cell(0, 10, "DATOS DEL GASTO", ln=True, align="C")

            pdf.set_font("Arial", size=12)

            pdf.cell(0, 8, f"Fecha: {datos[0]}", ln=True)
            pdf.cell(0, 8, f"Categoría: {datos[1]}", ln=True)
            pdf.cell(0, 8, f"Descripción: {datos[2]}", ln=True)
            pdf.cell(0, 8, f"Monto S/: {datos[3]}", ln=True)

            pdf.ln(10)
            pdf.line(10, pdf.get_y(), 200, pdf.get_y())
            pdf.output("gastos.pdf")

            for _ in track(range(10), description="GENERANDO PDF..."):
                time.sleep(0.5)

            console.print("PDF Generado con éxito ✔ ", style="succes")
        except Exception:
            console.print("ERROR al generar el PDF", style="error")
        
    customtkinter.CTkButton(top, text="Crear PDF", width=100, command=crear_pdf).pack(pady=5)

    def crear_excel():
        if not tree.get_children():
            messagebox.showerror("Error", "Tabla vacía.")
            return
        
        else:
            try:
                gastos_items_xl = []
                for item in tree.get_children():
                   gastos_items_xl.append(tree.item(item, "values"))

                df = pd.DataFrame(gastos_items_xl, columns=["Fecha", "Categoría", "Descripción", "Monto S/"])
                df.to_excel("Gastoss.xlsx", index=False)

                for _ in track(range(10), description="GENERANDO ARCHIVO EXCEL..."):
                    time.sleep(0.5)
                
                console.print("Archivo generado con éxito ✔", style="succes")
            except Exception:
                console.print("ERROR al generad el archivo EXCEL.", style="error")
                return
    customtkinter.CTkButton(top, text="Crear Excel", width=100, command=crear_excel).pack(pady=5)


    def crear_txt():
        if not tree.get_children():
            messagebox.showerror("Error", "Tabla vacía.")
            return
        
        with open("Gastos.txt", "w") as file:
            gastos = []
            for item in tree.get_children():
                gastos.append(tree.item(item, "values"))
            
            tabla = tabulate(gastos, headers=["Fecha", "Categoría", "Descripción", "Monto S/"])
            file.write(tabla)

        try:
            for _ in track(range(10), description="CARGANDO ARCHIVO..."):
                time.sleep(0.5)
                console.print("Contenido generado con éxito ✔", style = "succes" )

            with open("Gastos.txt", "r") as archivo:
                contenido = archivo.read()
                if len(contenido) == 0:
                    messagebox.showerror("Error", "Archivo vacío")
                    return
                else:
                    print("")
                    print(contenido)

        except FileNotFoundError:
            console.print("ERROR... No se encontro el archivo", style="error")
            return
    customtkinter.CTkButton(top, text="Crear TXT", width=100, command=crear_txt).pack(pady = 5)

