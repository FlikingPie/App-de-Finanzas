import sqlite3
from tkinter import messagebox
from datetime import datetime
from config import categorias
from tkinter import simpledialog

#FUNCION QUE RETORNA LA CONEXION Y CURSOR 
def conexion_sql():
    conexion = sqlite3.connect("Finanzas.db")
    cursor = conexion.cursor()
    return conexion, cursor

#FUNCION QUE CREA LA TABLA SQL
#def crear_tabla():
#    conexion, cursor = conexion_sql()
#    try:
#        cursor.execute("""
#                   CREATE TABLE IF NOT EXISTS gastos (
#                   Fecha TEXT,
#                   Categoria TEXT,
#                   Descripcion TEXT,
#                   Monto DOUBLE )
#                   """)
#        conexion.commit()
#        print("Tabla creada")
#    except sqlite3.OperationalError:
#        print("Error al crear la tabla.")

#crear_tabla()

#FUNCION AGREGAR 
def insertar_gasto_sql(fecha_string, categoria, descripcion, monto):
    conexion, cursor = conexion_sql()
    cursor.execute ("""
                    INSERT INTO gastos (Fecha, Categoria, Descripcion, Monto)
                    VALUES (?, ?, ?, ?)
                   """, (fecha_string, categoria, descripcion, monto))
    conexion.commit()
    messagebox.showinfo("Info", "Gasto agregado correctamente ✔")

#FUNCION ELIMINAR GASTO
def eliminar_gasto_sql(search_descp):
    conexion, cursor = conexion_sql()
    cursor.execute("""
                   DELETE FROM gastos WHERE Descripcion = ?
                   """,(search_descp,))
    conexion.commit()
    messagebox.showinfo("Info", "Gasto eliminado correctamente ✔")

#FUNCION MODIFICAR GASTO
def modificar_gasto_sql(new_fecha, new_cat, new_descp, new_monto, search_descp):
    conexion, cursor = conexion_sql()
    cursor.execute("""
                   UPDATE gastos SET Fecha = ?,
                   Categoria = ?,
                   Descripcion = ?,
                   Monto = ? 
                   WHERE Descripcion = ?
                   """, (new_fecha, new_cat, new_descp, new_monto, search_descp))
    messagebox.showinfo("Info", "Gasto modificado correctamente ✔")
    
    conexion.commit()

cantidades = []
cantidades_dia= []
cantidades_mes = []
cantidades_año = []
meses = list(range(1,13))




def contar_categorias():
    global categorias
    cantidades.clear()
    conexion, cursor = conexion_sql()
    cursor.execute("""
                   SELECT Categoria, COUNT(*)
                   FROM gastos
                   GROUP BY Categoria
                   ORDER BY Categoria ASC
                   """)

    for cat in categorias:

        cursor.execute("""
        SELECT COUNT(*)
        FROM gastos
        WHERE Categoria = ?
        """,(cat,))

        total = cursor.fetchone()[0]
        cantidades.append(total)

    conexion.commit()


def contar_gastos_dia():
    global cantidades_dia
    cantidades_dia.clear()

    try:
        f = simpledialog.askstring("Fecha", "Ingrese la fecha:")
        f_f = datetime.strptime(f, "%d/%m/%Y")
        fecha_str = f_f.strftime("%d/%m/%Y")

    except ValueError:
        messagebox.showerror("Error", "Formato de fecha inválido.")
        return
    
    conexion, cursor = conexion_sql()

    for cat in categorias:
        cursor.execute("""
        SELECT COUNT(*)
        FROM gastos
        WHERE Fecha = ? AND Categoria = ?
        """, (fecha_str, cat))

        total = cursor.fetchone()[0]
        cantidades_dia.append(total)

    conexion.close()

def contar_gastos_mes():
    global cantidades_mes
    cantidades_mes.clear()

    conexion, cursor = conexion_sql()

    m = simpledialog.askstring("Mes", "Ingrese el mes (1-12):")

    if not m:
        return
    
    if int(m) not in meses:
        messagebox.showerror("Error", "Ingrese un mes válido.")
        conexion.close()
        return

    try:
        mes_str = datetime.strptime(m, "%m").strftime("%m")

        for cat in categorias:
            cursor.execute("""
                SELECT COUNT(*)
                FROM gastos 
                WHERE Fecha LIKE ? AND Categoria = ?
            """, (f"%/{mes_str}/%", cat))

            total = cursor.fetchone()[0]
            cantidades_mes.append(total)

    except ValueError:
        messagebox.showerror("Error", "Mes inválido.")
        conexion.close()
        return

    conexion.close()

def contar_gastos_año():
    global cantidades_año
    cantidades_año.clear()
    conexion, cursor = conexion_sql()
    a = simpledialog.askstring("Año", "Ingrese un año (2026 -->):")
    if not a:
        return
    
    if int(a) < 2026:
        messagebox.showerror("Error", "Debe ingresar un año mayor o igual a 2026.")
        return
    
    try:
        año_str = datetime.strptime(a,"%Y").strftime("%Y")
        for cat in categorias:
            cursor.execute("""
                SELECT COUNT(*)
                FROM gastos 
                WHERE Fecha LIKE ? AND Categoria = ?
            """, (f"%/%/{año_str}", cat))

            total = cursor.fetchone()[0]
            cantidades_año.append(total)

    except ValueError:
        messagebox.showerror("Error", "Año inválido.")
        conexion.close()
        return


