import streamlit as st

st.set_page_config(
    page_title="BIPA Analytics Dashboard",
    page_icon="📚",
    layout="wide"
)

st.title("📚 BIPA Analytics Dashboard")

st.subheader("Sistema Inteligente de Analítica Bibliotecaria")

st.markdown("""
## Problemática

Las bibliotecas universitarias generan grandes volúmenes de datos relacionados con préstamos, usuarios y colecciones.

## Justificación

La analítica de datos permite identificar patrones de uso, tendencias de consulta y apoyar la toma de decisiones bibliotecarias.

## Objetivo

Analizar el comportamiento de uso de la colección bibliográfica mediante préstamos, usuarios y clasificación LCC.
""")
