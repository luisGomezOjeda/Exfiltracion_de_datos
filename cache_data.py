import polars as pl
import plotly.express as px
from pathlib import Path
import streamlit as st



@st.cache_data
def load_data() :
    datos_cargados_csv = {}
    datos_cargados_png = {}
    ruta = Path('resources/')
    for file in ruta.glob('*.csv') :
        datos_cargados_csv[file.stem] = pl.read_csv(file)
    for file in ruta.glob('*.png') :
        datos_cargados_png[file.stem] = 'resources/' + file.name
        print('resources/' + file.name)

    
    return datos_cargados_csv, datos_cargados_png

