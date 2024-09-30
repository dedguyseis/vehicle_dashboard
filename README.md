# Panel de Control de Vehículos Usados en EE.UU.

## Descripción
Este proyecto consiste en el desarrollo de un panel de control interactivo para analizar el mercado de vehículos usados en EE.UU. La aplicación web fue construida usando **Streamlit** y permite a los usuarios visualizar la distribución del kilometraje de los vehículos, la relación entre el precio y el año de fabricación, y otros insights útiles para explorar el mercado de vehículos.

## Características de la aplicación
1. **Visualización interactiva**:
   - **Histograma**: Muestra la distribución del kilometraje de los vehículos (odómetro).
   - **Gráfico de dispersión**: Visualiza la relación entre el año de fabricación y el precio de los vehículos.
2. **Filtros interactivos**:
   - Selección de gráficos mediante botones y casillas de verificación.
   - Filtro por condición del vehículo (nuevo, usado, reconstruido, etc.) para ajustar las visualizaciones.
3. **Interfaz sencilla** basada en Streamlit para facilitar la navegación y el análisis de los datos.

## Estructura del proyecto
```
.
├── README.md              # Descripción del proyecto
├── app.py                 # Código de la aplicación principal
├── vehicles_us.csv        # Conjunto de datos utilizado
├── requirements.txt       # Librerías necesarias para ejecutar el proyecto
├── notebooks              # Análisis exploratorio en Jupyter Notebooks
│   └── EDA.ipynb
└── .streamlit
    └── config.toml        # Configuración para desplegar la app en Render
```

## Requisitos
Para ejecutar el proyecto localmente, asegúrate de tener las siguientes librerías instaladas:
- **pandas**
- **streamlit**
- **plotly-express**

Puedes instalar las dependencias con:
```
pip install -r requirements.txt
```

## Cómo ejecutar el proyecto localmente
1. Clona este repositorio:
   ```bash
   git clone https://github.com/dedguyseis/vehicle_dashboard.git
   ```

2. Cambia al directorio del proyecto:
   ```bash
   cd vehicle_dashboard
   ```

3. Crea un entorno virtual y actívalo:
   ```bash
   python -m venv vehicles_env
   source vehicles_env/bin/activate  # En Windows: vehicles_env\Scripts\activate
   ```

4. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

5. Ejecuta la aplicación localmente:
   ```bash
   streamlit run app.py
   ```


## Despliegue
La aplicación está desplegada en [Render.com](https://render.com) y se puede acceder a través del siguiente enlace:

- **URL de la aplicación**: [https://vehicle-dashboard.onrender.com](https://vehicle-dashboard.onrender.com) 

## Estructura de los datos
El archivo de datos `vehicles_us.csv` contiene la siguiente información:

- **price**: Precio del vehículo.
- **model_year**: Año de fabricación.
- **model**: Modelo del vehículo.
- **condition**: Condición del vehículo (nuevo, usado, etc.).
- **cylinders**: Número de cilindros.
- **fuel**: Tipo de combustible.
- **odometer**: Kilometraje del vehículo.
- **transmission**: Tipo de transmisión.
- **type**: Tipo de vehículo (SUV, sedán, etc.).
- **paint_color**: Color de la pintura.
- **is_4wd**: Indica si el vehículo es de tracción en las cuatro ruedas.
- **date_posted**: Fecha en que se publicó el anuncio.
- **days_listed**: Número de días que el vehículo estuvo listado.

## Funcionalidades de la Aplicación
1. **Visualización de datos**:
   - Un **histograma** interactivo para mostrar la distribución del kilometraje de los vehículos.
   - Un **gráfico de dispersión** para visualizar la relación entre el año de fabricación y el precio.
   
2. **Interactividad**:
   - Uso de botones y casillas de verificación para activar/desactivar visualizaciones.
   - Filtro para mostrar la distribución del precio según la condición del vehículo.

## Posibles mejoras
1. Incluir filtros adicionales para explorar el conjunto de datos según marca, tipo de combustible y transmisión.
2. Agregar más visualizaciones, como gráficos de caja (boxplots) para analizar la variación de precios según la condición.
3. Mejorar la interfaz para incluir gráficos dinámicos y ajustes de color.

## Contribuciones
Si deseas contribuir a este proyecto, realiza un fork del repositorio y envía un pull request con tus mejoras.

## Contacto
Si tienes alguna pregunta o sugerencia, no dudes en contactarme en [mm131018@hotmail.com](mailto:mm131018@hotmail.com).