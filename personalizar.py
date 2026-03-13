import customtkinter
import tkinter as tk
from tkinter import messagebox


def ventana_personalizar():

    tema_oscuro = False
    texto = "Cambiar fondo ☀️"

    top = customtkinter.CTkToplevel()
    top.title("Ventana personalizar")
    top.geometry("300x300+450+200")
    top.resizable(False, False)

    # CAMBIAR TEMA DARK / LIGHT
    def cambiar_fondo():
        nonlocal texto, tema_oscuro

        if tema_oscuro: #Si es TRUE
            customtkinter.set_appearance_mode("light") #Cambia a ligth
            tema_oscuro = False #Cambia la variable
            texto = "Cambiar fondo 🌑"
            messagebox.showinfo("Apariencia", "Light")

        else:
            customtkinter.set_appearance_mode("dark")
            tema_oscuro = True
            texto = "Cambiar fondo ☀️"
            messagebox.showinfo("Apariencia", "Dark")

        switch.configure(text=texto)

    switch = customtkinter.CTkSwitch(
        top,
        text=texto,
        command=cambiar_fondo
    )
    switch.pack(pady=10)

    # CAMBIAR COLOR DE WIDGETS
    def cambiar_color_widgets():

        colores_disponibles = [
            "blue",
            "green",
            "dark-blue"
        ]

        vent_color = customtkinter.CTkToplevel()
        vent_color.title("Seleccione el color")
        vent_color.geometry("250x200+460+200")
        vent_color.resizable(False, False)

        combo = customtkinter.CTkComboBox(
            vent_color,
            values=colores_disponibles
        )
        combo.pack(pady=20)

        def guardar():
            color = combo.get()

            if color:
                customtkinter.set_default_color_theme(color)
                messagebox.showinfo("Configuración", "Color aplicado correctamente")
            else:
                messagebox.showwarning("Advertencia", "Debe seleccionar un color")

        boton = customtkinter.CTkButton(
            vent_color,
            text="Aplicar",
            command=guardar
        )
        boton.pack(pady=10)

    customtkinter.CTkButton(
        top,
        text="Cambiar color widgets",
        command=cambiar_color_widgets,
        width=150
    ).pack(pady=10)