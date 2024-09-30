import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.title('Panel de Control de Vehículos Usados en EE.UU.')
st.subheader('Análisis Interactivo del Mercado de Vehículos Usados')

st.markdown("""
Esta aplicación permite explorar visualmente el conjunto de datos de vehículos usados en EE.UU.
Puedes utilizar los botones y filtros disponibles para visualizar distribuciones de kilometraje y analizar la relación entre el precio y el año de fabricación de los vehículos.
""")

st.write('### Vista Previa del Conjunto de Datos')
st.write(car_data.head())

hist_button = st.button('Mostrar Histograma de Kilometraje')

if hist_button:
    st.write('#### Distribución del Kilometraje de los Vehículos')
    fig = px.histogram(car_data, x='odometer', title='Distribución del Kilometraje (Odómetro)')
    st.plotly_chart(fig, use_container_width=True)

scatter_checkbox = st.checkbox('Mostrar Gráfico de Dispersión Precio vs Año de Fabricación')

if scatter_checkbox:
    st.write('#### Relación entre el Precio y el Año de Fabricación del Vehículo')
    fig = px.scatter(car_data, x='model_year', y='price', title='Precio vs Año de Fabricación')
    st.plotly_chart(fig, use_container_width=True)

st.write('### Filtro por Condición del Vehículo')
condition_filter = st.selectbox('Selecciona la condición del vehículo:', car_data['condition'].unique())

filtered_data = car_data[car_data['condition'] == condition_filter]
st.write(f'#### Precio vs Año de Fabricación para vehículos en condición: {condition_filter}')
fig_condition = px.scatter(filtered_data, x='model_year', y='price', title=f'Precio vs Año de Fabricación - {condition_filter}')
st.plotly_chart(fig_condition, use_container_width=True)
