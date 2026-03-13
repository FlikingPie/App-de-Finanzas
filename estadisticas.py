import customtkinter, time
import plotly.graph_objects as go
from plotly.offline import plot
from gastos import categorias
from database import cantidades
from database import cantidades_dia
from database import contar_categorias
from database import contar_gastos_dia
from database import cantidades_mes
from database import contar_gastos_mes
from database import cantidades_año
from database import contar_gastos_año
from rich.progress import track


def ventana_estadisticas(tree):
    top = customtkinter.CTkToplevel()
    top.title("Ventana estadísticas")
    top.geometry("300x300+450+250")
    top.resizable(False, False)

    def gastos_categoria():
        for _ in track(range(10), description="CARGANDO GRÁFICO..."):
            time.sleep(0.5)
            
        contar_categorias()
        fig = go.Figure(data=go.Bar(x=categorias, y=cantidades))

        #CREAR EL GRAFICO
        fig.update_layout(
            template = "plotly_dark",
            xaxis_title = "Categorias",
            yaxis_title = "Cantidades",
            title = "Gráfico de categorias",
            font = dict(color="white")
        )  

        plot(fig, filename="grafico_cat.html")
    customtkinter.CTkButton(top, text="Gastos categorías", width=100, command=gastos_categoria).pack(pady=5)

    def gasto_dia():
        for _ in track(range(10), description="CARGANDO GRÁFICO..."):
            time.sleep(0.5)
            
        contar_gastos_dia()
        fig = go.Figure(data=go.Bar(x=categorias, y=cantidades_dia))
        fig.update_layout(
            template = "plotly_dark",
            xaxis_title = "Categorias",
            yaxis_title = "Cantidades",
            title = "Gráfico de gastos por día",
            font = dict(color = "white")
        )
        plot(fig, filename="grafico_cat_dia.html")

    customtkinter.CTkButton(top, text="Gastos por día", width=100, command=gasto_dia).pack(pady=5)

    def gasto_mes():
        for _ in track(range(10), description="CARGANDO GRÁFICO..."):
            time.sleep(0.5)

        contar_gastos_mes()
        fig = go.Figure(data=go.Bar(x=categorias, y=cantidades_mes))
        fig.update_layout(
            template ="plotly_dark",
            xaxis_title ="Categorias",
            yaxis_title = "Cantidades",
            title = "Gráfico de gastos por mes",
            font = dict(color = "white")
        )
        plot(fig, filename="grafico_cat_mes.html")
    customtkinter.CTkButton(top, text="Gastos por mes", width=100, command=gasto_mes).pack(pady=5)

    def gasto_año():
        for _ in track(range(10), description="CARGANDO GRÁFICO..."):
            time.sleep(0.5)
        
        contar_gastos_año()
        fig = go.Figure(data=go.Bar(x = categorias, y = cantidades_año))
        fig.update_layout(
            template = "plotly_dark",
            xaxis_title = "Categorias", 
            yaxis_title = "Cantidades",
            title = "Gráfico de gastos por año",
            font = dict(color = "white")
        )
        plot(fig, filename="grafico_cat_año.html")
    customtkinter.CTkButton(top, text="Gastos por año", command=gasto_año, width=100).pack(pady=5)