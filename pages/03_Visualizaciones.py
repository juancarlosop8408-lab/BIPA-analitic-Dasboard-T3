import streamlit as st
import plotly.express as px

from src.carga_datos import cargar_datos

items, prestamos, usuarios, lcc = cargar_datos()

st.title("📈 Visualizaciones Bibliotecarias")

# ==========================
# FILTROS
# ==========================

st.sidebar.header("Filtros")

carrera = st.sidebar.selectbox(
    "Carrera",
    ["Todas"] + sorted(prestamos["Carrera"].dropna().unique().tolist())
)

categoria = st.sidebar.selectbox(
    "Categoría",
    ["Todas"] + sorted(prestamos["Categoria"].dropna().unique().tolist())
)

clasificacion = st.sidebar.selectbox(
    "Clasificación",
    ["Todas"] + sorted(prestamos["Clasificacion"].dropna().unique().tolist())
)

df = prestamos.copy()

if carrera != "Todas":
    df = df[df["Carrera"] == carrera]

if categoria != "Todas":
    df = df[df["Categoria"] == categoria]

if clasificacion != "Todas":
    df = df[df["Clasificacion"] == clasificacion]

# ==========================
# GRÁFICA 1
# ==========================

top_clas = (
    df["Clasificacion"]
    .value_counts()
    .head(10)
    .reset_index()
)

top_clas.columns = ["Clasificacion", "Prestamos"]

fig1 = px.bar(
    top_clas,
    x="Clasificacion",
    y="Prestamos",
    title="Top Clasificaciones"
)

st.plotly_chart(
    fig1,
    use_container_width=True,
    key="clasificaciones"
)

# ==========================
# GRÁFICA 2
# ==========================

top_carreras = (
    df["Carrera"]
    .value_counts()
    .head(10)
    .reset_index()
)

top_carreras.columns = ["Carrera", "Prestamos"]

fig2 = px.bar(
    top_carreras,
    x="Carrera",
    y="Prestamos",
    title="Top Carreras"
)

st.plotly_chart(
    fig2,
    use_container_width=True,
    key="carreras"
)

# ==========================
# GRÁFICA 3
# ==========================

top_titulos = (
    df["Titulo"]
    .value_counts()
    .head(10)
    .reset_index()
)

top_titulos.columns = ["Titulo", "Prestamos"]

fig3 = px.bar(
    top_titulos,
    x="Prestamos",
    y="Titulo",
    orientation="h",
    title="Top Títulos"
)

st.plotly_chart(
    fig3,
    use_container_width=True,
    key="titulos"
)

# ==========================
# GRÁFICA 4
# ==========================

categorias = (
    df["Categoria"]
    .value_counts()
    .reset_index()
)

categorias.columns = ["Categoria", "Cantidad"]

fig4 = px.pie(
    categorias,
    names="Categoria",
    values="Cantidad",
    title="Distribución por Categoría"
)

st.plotly_chart(
    fig4,
    use_container_width=True,
    key="categorias"
)