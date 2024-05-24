# Tendencias-en-la-Industria-de-los-videojuegos
Introducción
En la venta de videojuegos en linea, comprender y prever el éxito de un juego determina el éxito comercial. Como parte del equipo de análisis de la tienda, se busca identificar patrones que determinen el éxito. desarrollar un modelo predictivo que pueda discernir qué características y factores contribuyen al éxito de un juego en el mercado.

Este proyecto se centra en examinar y analizar datos vinculados a la industria de los videojuegos utilizando técnicas de ciencia de datos. Dada la naturaleza dinámica del mercado de los videojuegos, caracterizado por cambios en las preferencias de los jugadores, avances tecnológicos y una competencia intensa entre diversas plataformas y géneros, nuestro objetivo es entender las tendencias que impulsan el éxito de los juegos y cómo factores como la región, las calificaciones y las plataformas influyen en las ventas y la percepción de los juegos.

Mediante análisis exhaustivos y pruebas de hipótesis, hemos obtenido una comprensión profunda de la industria de los videojuegos. Esta comprensión puede ayudar a las empresas a tomar decisiones fundamentadas sobre el desarrollo y la comercialización de juegos. El proyecto ofrece información valiosa sobre las preferencias de los jugadores, el impacto de las calificaciones en las ventas y las disparidades regionales en la industria de los videojuegos.

# Se realizaron cambios en los tipos de datos en el DataFrame df_games en varias columnas:

year_of_release: Originalmente era de tipo float. Se convirtió a Int64 (entero con posibilidad de valores nulos) utilizando el método astype('Int64'). Este cambio se efectuó para representar los años como enteros y manejar adecuadamente los valores nulos en caso de que falte el año de lanzamiento de un juego.

user_score: Inicialmente era de tipo object (cadena) debido a la presencia de valores como 'tbd'. Se convirtió a float utilizando la función pd.to_numeric con errors='coerce'. Este ajuste se realizó para transformar las calificaciones de usuarios en valores numéricos de punto flotante, tratando los valores no numéricos (como 'tbd') como NaN para facilitar operaciones matemáticas y análisis de datos.

name, genre: Los valores faltantes podrían deberse a la falta de información sobre juegos específicos. Por lo tanto, se dejaron sin cambios.

critic_score: La falta de datos puede ser el resultado de la ausencia de calificaciones por parte de críticos, especialmente para juegos menos conocidos. Los valores faltantes se dejaron como NaN.

user_score: En el caso de 'tbd', que significa "Por determinar", indicando que la calificación de usuario aún no se ha determinado, se convirtió a NaN. Los otros valores faltantes también se consideraron como NaN.

rating: La falta de valores podría deberse a la falta de información sobre calificaciones por edad o contenido de algunos juegos. Por lo tanto, estos valores se mantuvieron sin cambios.

# ¿Son significativos los datos de cada período?
Los datos de cada período son significativos. La variación en la cantidad de juegos lanzados a lo largo de los años, que va desde valores tan bajos como 9 juegos en un año hasta 1427 en otro, indica la influencia de eventos y tendencias específicas en la industria de los videojuegos en esos momentos.


# ¿Son significativas las diferencias en las ventas? ¿Qué sucede con las ventas promedio en varias plataformas?
Se observan diferencias significativas en las ventas entre las plataformas, según el diagrama de caja de las ventas globales por plataforma. Plataformas como PS3 y X360 muestran ventas promedio más altas, mientras que PS2 y PSP muestran ventas promedio más bajas. Además, se identifican valores atípicos que representan juegos extremadamente exitosos en ciertas plataformas. Por otro lado, las ventas en PS4 están en aumento, mientras que las plataformas más antiguas muestran una tendencia decreciente en las ventas. En conjunto, este análisis ofrece una visión valiosa sobre el desempeño relativo de las diferentes plataformas en la industria de los videojuegos.

# Observaciones
Basándonos en la información proporcionada y en las correlaciones calculadas entre las puntuaciones de críticos y usuarios con las ventas en la plataforma PS4, podemos obtener las siguientes conclusiones:

Correlación entre Critic Score y Ventas (0.41): Existe una correlación positiva moderada entre las puntuaciones de críticos y las ventas en la plataforma PS4. Esto sugiere que, en general, cuando los juegos en esta plataforma reciben puntuaciones más altas por parte de los críticos, tienden a tener mayores ventas totales.

Correlación entre User Score y Ventas (-0.03): La correlación entre las puntuaciones de usuarios y las ventas en la plataforma PS4 es muy cercana a cero, lo que indica que no hay una relación clara entre las puntuaciones de usuarios y las ventas totales. En otras palabras, las puntuaciones de usuarios no parecen influir significativamente en las ventas de juegos de PS4.

Géneros más rentables: Los géneros más rentables son acción, deportes y disparos en primera persona, que generan mayores ventas totales. Estos géneros son populares y atractivos para un amplio público.

Generalización acerca de géneros con ventas altas y bajas: Los géneros con ventas altas suelen ofrecer experiencias de juego ampliamente populares, mientras que los géneros con ventas bajas suelen ser nicho o menos populares, como aventuras, estrategia y simulación.

Las preferencias de las plataformas de juegos muestran variaciones significativas según la región 
geográfica. En América del Norte y Europa, las consolas de Sony y Microsoft, como Xbox y PlayStation, gozan de gran popularidad. Por otro lado, en Japón, las plataformas de Nintendo, como la Nintendo DS, son las más preferidas por los jugadores. Estas diferencias en las cuotas de mercado reflejan tanto las estrategias de marketing de las empresas como las preferencias culturales arraigadas en cada región.

Las preferencias de género en los videojuegos varían según la región:

América del Norte favorece Action, Sports, Shooter y Platform.

Europa prefiere Action, Sports, Shooter, Racing y Misc.

Japón muestra un interés especial por Role-Playing, además de Action, Sports, Platform y Misc. Estas diferencias se explican por las preferencias culturales y de mercado en cada región.

# Conclusión
El análisis exhaustivo de datos de la industria de videojuegos utilizando el DataFrame df_games revela:

Variaciones regionales en las preferencias de plataformas y géneros.
La influencia significativa de las clasificaciones ESRB en las ventas en todas las regiones.
La percepción de calidad por parte de los críticos tiene un impacto en las ventas de los juegos.
No hay una diferencia significativa en las calificaciones de usuarios entre Xbox One y PC, pero sí entre los géneros de Acción y Deportes.
Estos hallazgos son fundamentales para la toma de decisiones en la industria de los videojuegos, ya que proporcionan una comprensión clara de las tendencias y preferencias del mercado.
