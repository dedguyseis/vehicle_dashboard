
# Vehículos Usados - Panel de Control

### Descripción
Este proyecto consiste en el desarrollo de un panel de control interactivo para explorar un conjunto de datos de anuncios de vehículos usados en EE.UU. La aplicación web fue construida usando **Streamlit** y permite a los usuarios visualizar la distribución del kilometraje de los vehículos, la relación entre el precio y el año de fabricación, y otros insights útiles para analizar el mercado de vehículos.

### Características de la aplicación
1. **Visualización interactiva**:
   - **Histograma**: Distribución del kilometraje de los vehículos.
   - **Gráfico de dispersión**: Relación entre el año de fabricación y el precio del vehículo.
2. **Filtros interactivos**: Botones y casillas de verificación para seleccionar y visualizar distintos gráficos.
3. **Carga y lectura de datos desde un archivo CSV**.
4. **Interfaz sencilla y fácil de usar** basada en Streamlit.

### Estructura del proyecto
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

### Requisitos
Para ejecutar el proyecto localmente, asegúrate de tener las siguientes librerías instaladas:
- **pandas**
- **streamlit**
- **plotly-express**

Puedes instalar las dependencias con:
```
pip install -r requirements.txt
```

### Cómo ejecutar el proyecto
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
   source vehicles_env/bin/activate
   ```

4. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

5. Ejecuta la aplicación localmente:
   ```bash
   streamlit run app.py
   ```

6. Abre la aplicación en tu navegador en: `http://0.0.0.0:10000`

### Despliegue
La aplicación está desplegada en [Render.com](https://render.com) y se puede acceder a través del siguiente enlace:

- **URL de la aplicación**: https://vehicle-dashboard.onrender.com

### Estructura de los datos
El archivo de datos `vehicles_us.csv` contiene la siguiente información:

- **price**: Precio del vehículo.
- **year**: Año de fabricación.
- **odometer**: Kilometraje del vehículo.
- **manufacturer**: Marca del vehículo.
- **condition**: Condición del vehículo (nuevo, usado, etc.).
- **cylinders**: Número de cilindros.
- **fuel**: Tipo de combustible.
- **title_status**: Estado del título del vehículo.
- **transmission**: Tipo de transmisión.
- **drive**: Tipo de tracción (4x4, delantera, trasera, etc.).
- **size**: Tamaño del vehículo (compacto, SUV, etc.).

### Posibles mejoras
1. Incluir filtros adicionales para explorar el conjunto de datos según marca, tipo de combustible y transmisión.
2. Agregar más visualizaciones, como gráficos de caja (boxplots) para analizar la variación de precios según la condición.
3. Mejorar la interfaz para incluir gráficos dinámicos y ajustes de color.

### Contribuciones
Si deseas contribuir a este proyecto, realiza un fork del repositorio y envía un pull request con tus mejoras.

### Contacto
Si tienes alguna pregunta o sugerencia, no dudes en contactarme en mm131018@hotmail.com.
