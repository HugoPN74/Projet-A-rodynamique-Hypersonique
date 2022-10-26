import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
    page_title="Hypersonique",
    page_icon="👋",
)

st.header("Outil de prévision rapide des propriétés aérodynamiques en régime hypersonique ")

st.sidebar.title("Configuration")
st.sidebar.multiselect('Geométrie', ['Nez pointu', 'sphère'])

st.sidebar.slider('Nombre de Mach', 5, 8)
st.sidebar.slider('Température', 0, 100)
st.sidebar.slider('Pression', 0, 100)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.write("Reapartion de la température")

st.line_chart(chart_data)