import streamlit as st
import pandas as pd
import plotly.express as px

from src.carga_datos import cargar_datos

items, prestamos, usuarios, lcc = cargar_datos()

st.title("📈 Tendencia de Préstamos")

# Convertir fecha
prestamos["Fecha_prestamo"] = pd.to_datetime(
    prestamos["Fecha_prestamo"],
    errors="coerce"
)

prestamos = prestamos.dropna(subset=["Fecha_prestamo"])

# Agrupar por año
serie = (
    prestamos.groupby(
        prestamos["Fecha_prestamo"].dt.year
    )
    .size()
    .reset_index(name="Prestamos")
)

serie.columns = ["Año", "Prestamos"]

# Gráfico
fig = px.line(
    serie,
    x="Año",
    y="Prestamos",
    markers=True,
    title="Evolución Anual de Préstamos"
)

st.plotly_chart(
    fig,
    use_container_width=True,
    key="tendencia_prestamos"
)

# Indicador de crecimiento

if len(serie) >= 2:

    ultimo = serie["Prestamos"].iloc[-1]
    anterior = serie["Prestamos"].iloc[-2]

    variacion = round(
        ((ultimo - anterior) / anterior) * 100,
        2
    )

    st.metric(
        "Variación del último año",
        f"{variacion}%"
    )

# Tabla resumen

st.subheader("Resumen anual")

st.dataframe(serie)