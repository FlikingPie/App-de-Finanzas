import customtkinter
from tkinter import messagebox

def ventana_support() -> None:
    top = customtkinter.CTkToplevel()
    top.title("Support")
    top.geometry("300x200+450+250")
    top.resizable(False, False)

    def version_software():
        version = "Beta"
        autor = "Angel Utrilla"
        mensaje = f'Versión: {version} \n Autor: {autor}'
        messagebox.showinfo("Versión", mensaje)
    customtkinter.CTkButton(top, text="Versión", width=100, command=version_software).pack(pady=5)

    def manual():
        top_manual = customtkinter.CTkToplevel()
        top_manual.title("Manual de usuario")
        top_manual.geometry("500x400")
        top_manual.resizable(False, False)

        textbox = customtkinter.CTkTextbox(top_manual, width=480, height=360)
        textbox.pack(padx=10, pady=10)

        manual_texto = """
                       MANUAL DE USUARIO

                       1. REGISTRAR GASTOS
                       Ingrese el monto, categoría y descripción del gasto
                       y presione el botón 'Agregar'.

                       2. EDITAR GASTOS
                       Seleccione un gasto en la tabla y presione 'Editar'.

                       3. ELIMINAR GASTOS
                       Seleccione un registro y presione 'Eliminar'.

                       4. ESTADÍSTICAS
                       En el menú estadísticas puede visualizar gráficos
                       de los gastos por categoría o fecha.

                       5. RECOMENDACIONES
                       • Revise sus gastos semanalmente.
                       • Mantenga sus categorías organizadas.
                       • Evite registrar datos duplicados.
                        """
        textbox.insert("0.0", manual_texto)
        textbox.configure(state="disabled") #Esto permite NO EDITAR el cuadro de texto
    customtkinter.CTkButton(top,text="Manual", width=100, command=manual).pack(pady=5)

    def futuras_mejoras():
        mensaje = "1. MEJORAR LA INTERFAZ \n 2. SISTEMA PARA DIFERENTES CUENTAS \n 3.RECORDATORIOS"
        messagebox.showinfo("Futuras actualizaciones", mensaje)
    customtkinter.CTkButton(top, text="Futuras actualizaciones", width=100, command=futuras_mejoras).pack(pady=5)