import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header('Panel de Control de Análisis de Vehículos')

if st.button('Construir Histograma'):
    st.write('Creando histograma para la columna odómetro')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

if st.button('Construir Gráfico de Dispersión'):
    st.write('Creando gráfico de dispersión: odómetro vs precio')
    fig2 = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig2, use_container_width=True)
