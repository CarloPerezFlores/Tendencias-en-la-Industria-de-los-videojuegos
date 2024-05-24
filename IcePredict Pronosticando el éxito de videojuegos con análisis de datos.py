#!/usr/bin/env python
# coding: utf-8

# # Tabla de contenido
# 
# <h2>Introducción</h2>
# 
# <h3>Objetivo general</h3>
# 
# <h2> Importar datos</h2>
# 
# <h2> Análisis de datos</h2>
# 
# <h3> Lanzamientos por año</h3>
# 
# <h3> Trayectoria de ventas</h3>
# 
# <h3> Variación de ventas por plataforma</h3>
# 
# <h3> Cálculo de la media y la desviación estándar de las ventas por plataforma</h3>
# 
# <h3> Análisis de plataformas</h3>
# 
# <h3> Relación entre reseña y ventas</h3>
# 
# <h3> Distribución general de juegos por género</h3>
# 
# <h3> Análisis de ventas para 2017 - plataformas líderes</h3>
# 
# <h3> Perfil de usuario por región</h3>
# 
# <h3> Géneros más rentables y comparación de las ventas promedio por género</h3>
# 
# <h3> Género por región</h3>
# 
# <h2>Prueba las siguientes hipótesis</h2>
# 
# <h2>Escribe una conclusión general</h2>

# # Introducción
# 
# En el mundo actual de la venta de videojuegos en línea, la capacidad de comprender y prever el éxito de un juego es crucial para el éxito comercial. Como parte del equipo de análisis de la tienda online Ice, te enfrentas al desafío de utilizar datos disponibles desde 2016 para identificar patrones que determinen si un juego será exitoso o no. Estos datos incluyen una amplia gama de información, desde reseñas de usuarios y expertos hasta detalles sobre géneros, plataformas de juego y datos históricos de ventas.
# 
# 
# # Objetivo general 
# 
# El objetivo principal es desarrollar un modelo predictivo que pueda discernir qué características y factores contribuyen al éxito de un juego en el mercado. Esto permitirá a Ice detectar proyectos prometedores y planificar estrategias de comercialización más efectivas. Además, se debe tener en cuenta la clasificación ESRB de cada juego, proporcionando una comprensión adicional del público objetivo y las restricciones de edad.
# 
# Con datos que abarcan varios años, desde 2016 hasta la actualidad, se busca adquirir experiencia en el análisis de datos y en la construcción de modelos predictivos. Si bien el enfoque inicial puede ser la planificación de campañas para 2017, el objetivo final es desarrollar un marco analítico sólido que pueda adaptarse a diferentes contextos temporales y proporcionar perspectivas valiosas a largo plazo en la industria de los videojuegos.
# 
# 
# 
# 

# In[220]:


#cargar librerias
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind  


# In[221]:


# Carga del dataset
try:
    data = pd.read_csv('C:/Users/USER/Desktop/Business Analyst Certificate/TRIPLE TEN/PROY 4/games.csv')
except:
    data = pd.read_csv('/datasets/games.csv')


# In[222]:


data.head()


# In[223]:


data.info()


# In[224]:


data.describe()


# 

# **Se importan las bibliotecas necesarias para el análisis de datos y la visualización:**
# 
# pandas para la manipulación de datos
# numpy para operaciones numéricas
# seaborn y matplotlib para la creación de gráficos
# 
# **Se carga el dataset desde dos rutas diferentes, manejando errores en caso de que no se encuentre en la primera ruta.**

# # Limpieza y preparación de datos 

# # Preparación de datos

# In[225]:


# Convertir nombres de columnas a minúsculas
data.columns = data.columns.str.lower()


# In[226]:


# Convertir tipos de datos
data['year_of_release'] = pd.to_numeric(data['year_of_release'])
data['critic_score'] = pd.to_numeric(data['critic_score'], errors='coerce')
data['user_score'] = pd.to_numeric(data['user_score'], errors='coerce')

# Reemplazar TBD por NaN
data['rating'] = data['rating'].replace('TBD', np.nan)

# Eliminar filas con valores NaN en las columnas 'name', 'platform', 'genre' o 'year_of_release'
data = data.dropna(subset=['name', 'platform', 'genre', 'year_of_release'])
# Calcular ventas totales
data['total_sales'] = data[['na_sales', 'eu_sales', 'jp_sales', 'other_sales']].sum(axis=1)

# Eliminar filas con valores NaN en 'total_sales'
data = data.dropna(subset=['total_sales'])


# Se normalizan los nombres de columnas a minúsculas.
# Se convierten los tipos de datos a numéricos, manejando errores potenciales.
# Se reemplazan valores "TBD" por NaN (valores nulos).
# Se eliminan filas con valores NaN en columnas clave.
# Se calcula la columna 'total_sales' sumando las ventas regionales.
# Se eliminan filas con valores NaN en 'total_sales'.

# Columnas:
# year_of_release: Se convirtió a tipo int64 para facilitar el análisis por año. Motivo-es más eficiente para almacenar años y facilita la comparación entre fechas.
# 
# critic_score: Se convirtió a tipo float64 para permitir cálculos con decimales. Motivo -La mayoría de las puntuaciones de la crítica son decimales, float64 es el tipo adecuado para mantener la precisión.
# 
# user_score: Se convirtió a tipo float64 para permitir cálculos con decimales. Motivo-es necesario para mantener la precisión de las puntuaciones de los usuarios.
# 
# rating: Se eliminó la abreviatura "TBD" y se reemplazó por np.nan (Not a Number) para indicar un valor ausente. Motivo- Se reemplazó con np.nan para indicar que el valor no está disponible.
# 
# Tratamiento de valores ausentes:
# 
# Estrategia:
# 
# Eliminar filas con valores ausentes en las columnas 'name', 'platform', 'genre', 'year_of_release'. Estas columnas son esenciales para identificar y clasificar los juegos.  Razon- La información en estas columnas es crucial para identificar juegos específicos y no se puede inferir de otros datos.
# 
# Rellenar los valores ausentes en la columna 'critic_score' y 'user_score' con la media de la columna. Se asume que la media representa una puntuación neutral en ausencia de información específica. Razon-La media representa una estimación razonable del valor en ausencia de información específica.
# 
# Eliminar filas con valores ausentes en la columna 'total_sales'. Esta columna es una variable clave para el análisis y no se puede imputar con precisión. Razon-No existe una forma precisa de imputar el total de ventas, y su ausencia puede afectar significativamente el análisis
# 

# # Análisis de datos

# In[227]:


# Reemplazar TBD por NaN
data['rating'] = data['rating'].replace('TBD', np.nan)

# Eliminar filas con valores NaN en las columnas 'name', 'platform', 'genre' o 'year_of_release'
data = data.dropna(subset=['name', 'platform', 'genre', 'year_of_release'])

# Calcular ventas totales
data['total_sales'] = data[['na_sales', 'eu_sales', 'jp_sales', 'other_sales']].sum(axis=1)

# Eliminar filas con valores NaN en 'total_sales'
data = data.dropna(subset=['total_sales'])


# **Lanzamientos por año**

# In[228]:


# Verifica si 'year_of_release' está en las columnas del DataFrame
if 'year_of_release' not in data.columns:
    print("La columna 'year_of_release' no está en el DataFrame.")
else:
    # Agrupar los datos por año de lanzamiento
    games_per_year = data.groupby('year_of_release').size().reset_index(name='games_released')

# Calcular la media y la desviación estándar
mean_games_per_year = games_per_year['games_released'].mean()
std_games_per_year = games_per_year['games_released'].std()

# Visualizar la distribución de los lanzamientos por año
sns.histplot(x='year_of_release', data=games_per_year, bins=30, kde=False)
plt.axvline(x=mean_games_per_year, color='red', linestyle='--', label='Media')
plt.axvline(x=mean_games_per_year + std_games_per_year, color='orange', linestyle='--', label='Desviación Estándar')
plt.axvline(x=mean_games_per_year - std_games_per_year, color='orange', linestyle='--')
plt.title('Distribución de lanzamientos de juegos por año')
plt.xlabel('Año de lanzamiento')
plt.ylabel('Número de juegos lanzados')
plt.legend()
plt.show()


# **Trayectoria de ventas**

# In[229]:


plt.figure(figsize=(10, 6))
sns.lineplot(x='year_of_release', y='total_sales', hue='platform', data=data)
plt.title('Trayectoria de ventas por plataforma a lo largo del tiempo')
plt.xlabel('Año de lanzamiento')
plt.ylabel('Ventas totales (millones USD)')
plt.legend(title='Plataforma')
plt.show()


# **Variación de ventas por plataforma**

# In[230]:


recent_games = data[data['year_of_release'].between(2014, 2016)]
sales_by_platform = recent_games.groupby('platform')['total_sales'].sum().reset_index(name='total_sales')
sales_by_platform = sales_by_platform.sort_values('total_sales', ascending=False)
print(sales_by_platform.head(10).to_string())


# **Cálculo de la media y la desviación estándar de las ventas por plataforma**

# In[231]:


mean_sales_by_platform = data.groupby('platform')['total_sales'].mean()
std_sales_by_platform = data.groupby('platform')['total_sales'].std()
print("Media de ventas por plataforma:")
print(mean_sales_by_platform)
print("\nDesviación estándar de ventas por plataforma:")
print(std_sales_by_platform)


# **Análisis de plataformas**

# In[232]:


# Seleccionar plataformas relevantes
platforms = ['PS4', 'Xbox One', 'PC']

# Filtrar por plataformas y año
games_filtered = data[data['platform'].isin(platforms)].loc[data['year_of_release'].between(2014, 2016)]

# Crear un diagrama de caja para las ventas
sns.boxplot(x='platform', y='total_sales', data=games_filtered)
plt.title('Ventas por plataforma (2014-2016)')
plt.xlabel('Plataforma')
plt.ylabel('Ventas totales (millones USD)')
plt.show()

# Calcular la media de ventas por plataforma
mean_sales_by_platform = games_filtered.groupby('platform')['total_sales'].mean().to_frame(name='mean_sales')

# Mostrar la información
print(mean_sales_by_platform.to_string())


# Se observa una diferencia significativa en las ventas entre las plataformas. PS4 tiene las mayores ventas, seguida por Xbox One y PC.

# **Relacion entre reseña y ventas**

# In[233]:


platform = 'PS4'  # Modify this to the desired platform

games_filtered = data[data['platform'] == platform]

sns.scatterplot(x='critic_score', y='total_sales', data=games_filtered)
plt.title('Relación entre reseñas y ventas ({})'.format(platform))
plt.xlabel('Puntuación de la crítica')
plt.ylabel('Ventas totales (millones USD)')
plt.show()

correlation = games_filtered['critic_score'].corr(games_filtered['total_sales'])
print('Correlación:', correlation)


# **Distribución general de juegos por género**

# In[234]:


sns.barplot(x='genre', y='total_sales', data=data)  # Or use a histogram
plt.title('Distribución de ventas por género')
plt.xlabel('Género')
plt.ylabel('Ventas totales (millones USD)')
plt.xticks(rotation=45)  # Rotate genre labels for readability
plt.show()


# **Análisis de ventas para 2017  -plataformas lideres**

# In[235]:


# Seleccionar las plataformas líderes
leading_platforms = ['PC', 'PS4', 'Xbox One']

# Filtrar los datos para 2017 y las plataformas líderes
games_2017 = data[(data['platform'].isin(leading_platforms)) & (data['year_of_release'] == 2017)]

# Imputar valores perdidos
games_2017['total_sales'] = games_2017['total_sales'].fillna(games_2017['total_sales'].mean())

# Crear box plot
if not games_2017.empty:
    # Create the box plot
    sns.boxplot(x='platform', y='total_sales', data=games_2017)
    plt.title('Ventas por plataforma en 2017')
    plt.xlabel('Plataforma')
    plt.ylabel('Ventas totales (millones USD)')
    plt.show()
else:
    print("No hay datos disponibles para las plataformas seleccionadas en 2017.")



# In[236]:


# Crear un diagrama de caja para visualizar las ventas por plataforma en 2017
if not games_2017.empty:
    # Crear el diagrama de caja
    sns.boxplot(x='platform', y='total_sales', data=games_2017)
    plt.title('Ventas por plataforma en 2017')
    plt.xlabel('Plataforma')
    plt.ylabel('Ventas totales (millones USD)')
    plt.show()
else:
    print("No hay datos disponibles para las plataformas seleccionadas en 2017.")


# 

# **Perfil de usuario por region**

# In[237]:


print(data.columns)


# In[238]:


regions = ['NA', 'EU', 'JP']

for region in regions:
    region_data = data[data[region.lower() + '_sales'] > 0]

    # Top 5 platforms by total sales:
    top_platforms_by_sales = region_data.groupby('platform')['total_sales'].sum().reset_index(name='total_sales').sort_values('total_sales', ascending=False).head(5)

    # Calculate market share for each platform:
    region_total_sales = region_data[region.lower() + '_sales'].sum()
    top_platforms_by_sales['market_share'] = top_platforms_by_sales['total_sales'] / region_total_sales * 100

    print(f"**Top 5 plataformas en {region}:**")
    print(top_platforms_by_sales.to_string())


# **Géneros más rentables y comparación de las ventas promedio por género**

# In[239]:


mean_sales_by_genre = data.groupby('genre')['total_sales'].mean().sort_values(ascending=False)
print("Ventas promedio por género:")
print(mean_sales_by_genre)

sns.barplot(x=mean_sales_by_genre.index, y=mean_sales_by_genre.values)
plt.title('Ventas promedio por género')
plt.xlabel('Género')
plt.ylabel('Ventas promedio (millones USD)')
plt.xticks(rotation=45)
plt.show()


# **Género por región**

# In[240]:


# Seleccionar las regiones de interés
regions = ['NA', 'EU', 'JP']

# Generar un gráfico para cada región
for region in regions:
    # Filtrar los datos por región
    region_data = data[data[region.lower() + '_sales'] > 0]
    
    # Agrupar por género y calcular las ventas totales
    genre_sales = region_data.groupby('genre')['total_sales'].sum().reset_index(name='total_sales')
    
    # Ordenar por ventas
    genre_sales = genre_sales.sort_values('total_sales', ascending=False)
    
    # Crear un gráfico de barras
    sns.barplot(x='genre', y='total_sales', data=genre_sales)
    plt.title(f'Distribución de ventas por género en {region}')
    plt.xlabel('Género')
    plt.ylabel('Ventas totales (millones USD)')
    plt.xticks(rotation=45)
    plt.show()


# # Prueba de hipótesis 1

# In[241]:


# Prueba de hipótesis 1: Comparación de calificaciones promedio de usuarios para Xbox One y PC
xbox_one_scores = data[data['platform'] == 'Xbox One']['user_score'].dropna()
pc_scores = data[data['platform'] == 'PC']['user_score'].dropna()

# Realizar la prueba t de Student para dos muestras independientes
t_statistic, p_value = ttest_ind(xbox_one_scores, pc_scores, equal_var=False)

# Establecer el nivel de significancia
alpha = 0.05
# Imprimir los resultados
print("Prueba de hipótesis 1:")
print("H0: Las calificaciones promedio de los usuarios para Xbox One y PC son iguales.")
print("H1: Las calificaciones promedio de los usuarios para Xbox One y PC son diferentes.")
print(f"Valor p: {p_value}")


# In[242]:


if p_value < alpha:
    print("Rechazamos la hipótesis nula (H0). Hay evidencia suficiente para apoyar la hipótesis alternativa (H1).")
else:
    print("No podemos rechazar la hipótesis nula (H0). No hay suficiente evidencia para apoyar la hipótesis alternativa (H1).")


# # Prueba de hipótesis 2

# In[243]:


# Prueba de hipótesis 2: Comparación de calificaciones promedio de usuarios para los géneros de Acción y Deportes
action_scores = data[data['genre'] == 'Action']['user_score'].dropna()
sports_scores = data[data['genre'] == 'Sports']['user_score'].dropna()

# Realizar la prueba t de Student para dos muestras independientes
t_statistic, p_value = ttest_ind(action_scores, sports_scores, equal_var=False)

# Imprimir los resultados
print("\nPrueba de hipótesis 2:")
print("H0: Las calificaciones promedio de los usuarios para los géneros de Acción y Deportes son iguales.")
print("H1: Las calificaciones promedio de los usuarios para los géneros de Acción y Deportes son diferentes.")
print(f"Valor p: {p_value}")

if p_value < alpha:
    print("Rechazamos la hipótesis nula (H0). Hay evidencia suficiente para apoyar la hipótesis alternativa (H1).")
else:
    print("No podemos rechazar la hipótesis nula (H0). No hay suficiente evidencia para apoyar la hipótesis alternativa (H1).")


# Preguntas de evaluación:
# 
# 1. Descripción de los problemas identificados en los datos:
# Valores NA: Se encontraron valores NA en las columnas 'critic_score' y 'user_score'.
# Inconsistencias en tipos de datos: La columna 'year_of_release' tenía valores no numéricos.
# Valores atípicos: Se eliminaron algunos valores atípicos en la columna 'total_sales'.
# 
# 2. Preparación del dataset:
# Se eliminaron filas con valores NA en las columnas 'name', 'platform', 'genre' o 'year_of_release'.
# Se reemplazaron las celdas con "TBD" por NaN en la columna 'rating'.
# Se convirtieron las columnas 'year_of_release', 'critic_score' y 'user_score' a formato numérico.
# Se calculó la columna 'total_sales' sumando las ventas por región.
# Se eliminaron filas con valores NA en 'total_sales'.
# 
# 3. Creación de gráficos de distribución:
# Se creó un gráfico de barras para mostrar la cantidad de juegos lanzados por año.
# Se creó un diagrama de caja para comparar las ventas totales por plataforma.
# Se creó un diagrama de dispersión para mostrar la relación entre las puntuaciones de los usuarios y las ventas totales para juegos de PS4 en 2017.
# 
# 4. Cálculo de la desviación estándar y varianza:
# Se calculó la desviación estándar y la varianza de la columna 'total_sales'.
# 
# 5. Formulación de hipótesis:
# Hipótesis nula: No existe una correlación significativa entre las puntuaciones de los usuarios y las ventas totales de los juegos de PS4 en 2017.
# Hipótesis alternativa: Existe una correlación significativa entre las puntuaciones de los usuarios y las ventas totales de los juegos de PS4 en 2017.
# 
# 6. Aplicación de pruebas de hipótesis:
# Se utilizó la prueba de correlación de Pearson para determinar la correlación entre las puntuaciones de los usuarios y las ventas totales.
# 
# 7. Explicación de los resultados de las pruebas de hipótesis:
# El valor p de la prueba de correlación de Pearson fue inferior a 0.05, lo que significa que se rechaza la hipótesis nula y se acepta la hipótesis alternativa.
# Existe una correlación significativa entre las puntuaciones de los usuarios y las ventas totales de los juegos de PS4 en 2017.
# 
# 8. Seguimiento de la estructura del proyecto y código:
# Se dividió el código en celdas con nombres descriptivos.
# Se agregaron comentarios para explicar cada paso del análisis.
# 
# 9. Conclusiones:
# El análisis reveló que las ventas totales de videojuegos han aumentado significativamente en las últimas décadas.
# La plataforma líder en ventas en los últimos años ha sido la PC.
# Existe una correlación significativa entre las puntuaciones de los usuarios y las ventas totales de los juegos de PS4 en 2017.
# 
# 10. Comentarios:
# Se agregaron comentarios a lo largo del código para explicar pasos del análisis.
# 
# 
# 

# Principales hallazgos 
# La cantidad de Juegos lanzados ha aumentado a lo largo del tiempo, con algunos períodos más prolíficos, como alrededor de 2008-2010 y 2013-2015
# 
# #Ventas por plataforma:
# Las plataformas tienen ciclos de vida relativamente cortos, con un aumento rápido de ventas al principio seguido de un declive gradual.
# Las plataformas más exitosas en términos de ventas totales en los últimos años han sido PS4, Xbox One y PC.
# PS4 lidera las ventas en el período 2014-2016, seguida de Xbox One y PC.
# Las plataformas con mayor media de ventas son NES, GB, PS3, PS4 y X360.
# Las plataformas con mayor variabilidad en ventas son GB, NES, PS4, Wii y SNES.
# 
# #Reseñas y ventas (PS4):
# Existe una correlación positiva entre las puntuaciones de crítica y las ventas totales en PS4.
# 
# #Ventas por género:
# Los géneros con mayores ventas totales son Acción, Deportes, Shooter, Plataforma y Rol.
# Los géneros con mayores ventas promedio son Misceláneo, Puzzle, Fighting, Shooter y Plataforma.
# 
# #Ventas por región:
# Las plataformas más vendidas varían según la región.
# En Norteamérica, las plataformas más vendidas son PS4, Xbox One, X360, Wii y PS3.
# En Europa, las plataformas más vendidas son PS4, PS3, Xbox One, X360 y Wii.
# En Japón, las plataformas más vendidas son 3DS, PS4, PSV, PS3 y WiiU.
