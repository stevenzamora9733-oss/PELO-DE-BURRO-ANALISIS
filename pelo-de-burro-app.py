import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Pelo de Burro Análisis", page_icon="🐴", layout="wide")

st.markdown("""<style>.main { background-color: #0e1117; color: white; } .stMetric { background-color: #1f2937; padding: 20px; border-radius: 15px; border: 2px solid #f59e0b; }</style>""", unsafe_allow_html=True)

if 'historial' not in st.session_state: st.session_state.historial = []

st.title("🐴 Pelo de Burro Análisis")
tabs = st.tabs(["📊 ANALIZADOR", "📜 HISTORIAL", "📺 EN VIVO"])

with tabs[0]:
    col1, col2 = st.columns(2)
    with col1:
        local = st.text_input("Equipo Local", "Real Madrid")
        c_l = st.slider("Córners (L)", 0, 15, 6)
        f_l = st.slider("Faltas (L)", 0, 25, 12)
    with col2:
        visita = st.text_input("Equipo Visitante", "Barcelona")
        c_v = st.slider("Córners (V)", 0, 15, 5)
        f_v = st.slider("Faltas (V)", 0, 25, 13)
    
    prob_c = min(((c_l + c_v) / 12) * 100, 99.8)
    prob_t = min(((f_l + f_v) / 30) * 100, 99.0)
    
    c1, c2 = st.columns(2)
    c1.metric("🚩 PROB. CÓRNERS (+8.5)", f"{prob_c:.1f}%")
    c2.metric("🟨 PROB. TARJETAS (+4.5)", f"{prob_t:.1f}%")

    if st.button("💾 GUARDAR DIAGNÓSTICO"):
        st.session_state.historial.insert(0, {"Fecha": datetime.now().strftime("%H:%M"), "Partido": f"{local}-{visita}", "Córners": f"{prob_c:.1f}%"})
        st.success("Guardado en el historial.")

with tabs[2]:
    st.link_button("📺 Ver en Roja Directa", "https://www.rojadirectatv.tv/")
    st.link_button("📊 Estadísticas Sofascore", "https://www.sofascore.com/")

st.sidebar.write("© 2024 Pelo de Burro Análisis")
