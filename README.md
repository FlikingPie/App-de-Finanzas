# 💰 Finanzas APP

Aplicación de escritorio desarrollada en **Python** para la gestión de gastos personales.  
Permite registrar gastos, organizarlos por categorías, generar archivos, visualizar estadísticas y personalizar la interfaz.

La aplicación está construida utilizando **Tkinter**, **CustomTkinter** y una base de datos **SQLite**.

---

# 📌 Características

✔ Registrar gastos con fecha, categoría, descripción y monto  
✔ Editar y eliminar gastos  
✔ Filtrar gastos por fecha, categoría o monto  
✔ Gestión de categorías personalizadas  
✔ Generación de archivos:

- PDF
- Excel
- TXT

✔ Visualización de estadísticas con gráficos  
✔ Base de datos SQLite para persistencia  
✔ Personalización del tema (Dark / Light)  
✔ Cambio de color de widgets  
✔ Manual de usuario integrado  

---

# 🖥 Interfaz de la aplicación

La aplicación utiliza **CustomTkinter**, lo que permite una interfaz moderna con soporte para:

- Tema **Dark / Light**
- Colores personalizados
- Ventanas emergentes para cada módulo

---

# 📂 Estructura del proyecto

```
FinanzasApp/
│
├── main.py                # Aplicación principal
├── gastos.py              # Gestión de gastos
├── archivos.py            # Exportación de archivos
├── categorias.py          # Gestión de categorías
├── estadisticas.py        # Gráficos y estadísticas
├── personalizar.py        # Configuración de interfaz
├── support.py             # Ayuda y manual
├── database.py            # Funciones de base de datos
├── config.py              # Configuración global
│
├── Finanzas.db            # Base de datos SQLite
│
└── README.md
```

---

# ⚙️ Tecnologías utilizadas

- Python 3
- Tkinter
- CustomTkinter
- SQLite3
- Plotly
- Pandas
- FPDF
- Tabulate
- Rich

---

# 📦 Instalación

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/tuusuario/finanzas-app.git
cd finanzas-app
```

---

### 2️⃣ Instalar dependencias

```bash
pip install customtkinter pandas plotly fpdf tabulate rich
```

---

### 3️⃣ Ejecutar la aplicación

```bash
python main.py
```

---

# 🗄 Base de datos

La aplicación utiliza **SQLite** con la siguiente estructura:

Tabla `gastos`

| Campo | Tipo |
|------|------|
| Fecha | TEXT |
| Categoria | TEXT |
| Descripcion | TEXT |
| Monto | DOUBLE |

---

# 📊 Estadísticas

El sistema genera gráficos utilizando **Plotly**:

- Gastos por categoría
- Gastos por día
- Gastos por mes
- Gastos por año

Los gráficos se exportan automáticamente como archivos **HTML**.

---

# 📁 Exportación de datos

El sistema permite exportar registros en:

- **PDF**
- **Excel (.xlsx)**
- **TXT**

---

# 🎨 Personalización

Desde el menú **Configuración** se puede:

- Cambiar entre **modo oscuro y claro**
- Cambiar el **color del tema de los widgets**

---

# 📖 Manual de usuario

La aplicación incluye un manual integrado en la sección **Ayuda**, donde se explican:

- Registro de gastos
- Edición de registros
- Eliminación
- Uso de estadísticas

---

# 🚀 Futuras mejoras

- Mejorar interfaz gráfica
- Sistema de múltiples cuentas
- Recordatorios de gastos
- Importación de archivos
- Dashboard avanzado

---

# 👨‍💻 Autor

**Angel Utrilla**

Proyecto desarrollado como aplicación de gestión de finanzas personales en Python.