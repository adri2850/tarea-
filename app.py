import streamlit as st
import pandas as pd
#import matplot.pyplot as plt

st.write("Estadisticas de goles de Messi")

# Cargar los datos desde la pagina web
pagina = "https://players.fcbarcelona.com/es/jugador/548-messi-lionel-andres-messi-cuccitini"
tablas = pd.read_html(pagina)

# Creac la aplicacion web Streamlit
st.write(tabla[0].head(5))

