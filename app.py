import pandas as pd
import plotly.express as px
import streamlit as st

# Carga del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Título de la aplicación
st.header('Panel de control de vehículos usados')

# Botón para construir histograma
hist_button = st.button('Mostrar histograma de odómetro')

# Histograma de Odómetro
if hist_button:
    st.write('Distribución de odómetro para los vehículos usados')
    fig = px.histogram(car_data, x='odometer', title='Distribución del Odómetro')
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir gráfico de dispersión
scatter_button = st.button('Mostrar gráfico de dispersión precio vs año')

# Gráfico de dispersión
if scatter_button:
    st.write('Relación entre el precio y el año del vehículo')
    fig = px.scatter(car_data, x='year', y='price', title='Precio vs Año')
    st.plotly_chart(fig, use_container_width=True)
