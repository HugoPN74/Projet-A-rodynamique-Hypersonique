from cmath import sqrt
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
st.sidebar.slider('Température', 0, 10000)
st.sidebar.slider('Pression', 0, 100)



def detente_isentropique(M0,gamma):
    
    