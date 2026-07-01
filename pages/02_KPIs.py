import streamlit as st

from src.carga_datos import cargar_datos
from src.indicadores import calcular_kpis

items, prestamos, usuarios, lcc = cargar_datos()

(
    total_prestamos,
    usuarios_activos,
    titulos_unicos,
    promedio_usuario
) = calcular_kpis(prestamos)

st.title("📊 KPIs Bibliotecarios")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Préstamos",
    total_prestamos
)

col2.metric(
    "Usuarios Activos",
    usuarios_activos
)

col3.metric(
    "Títulos Consultados",
    titulos_unicos
)

col4.metric(
    "Promedio por Usuario",
    promedio_usuario
)
st.write(prestamos.columns.tolist())