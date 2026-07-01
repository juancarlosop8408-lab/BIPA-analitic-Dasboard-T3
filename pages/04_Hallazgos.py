import streamlit as st

from src.carga_datos import cargar_datos

items, prestamos, usuarios, lcc = cargar_datos()

st.title("🔎 Hallazgos Bibliotecarios")

prestamos_validos = prestamos[
    prestamos["Carrera"].notna()
]

prestamos_validos = prestamos_validos[
    prestamos_validos["Carrera"] != "No Aplica"
]

top_carrera = (
    prestamos_validos["Carrera"]
    .value_counts()
    .idxmax()
)

top_carrera_total = (
    prestamos_validos["Carrera"]
    .value_counts()
    .max()
)

top_clasificacion = (
    prestamos["Clasificacion"]
    .value_counts()
    .idxmax()
)

top_clasificacion_total = (
    prestamos["Clasificacion"]
    .value_counts()
    .max()
)

top_titulo_total = (
    prestamos["Titulo"]
    .value_counts()
    .max()
)

st.success(
    f"La carrera con mayor uso de la biblioteca es {top_carrera}, con {top_carrera_total} préstamos."
)

st.success(
    f"La clasificación más consultada es {top_clasificacion}, con {top_clasificacion_total} préstamos."
)

st.success(
    f"El título más prestado registra {top_titulo_total} préstamos."
)

st.info("""
Los resultados muestran patrones de uso claramente identificables.
Las áreas académicas más activas generan una demanda importante de recursos documentales.

Estos hallazgos apoyan la toma de decisiones relacionadas con el desarrollo de colecciones y la asignación de recursos bibliográficos.
""")

