#!/usr/bin/env python
# coding: utf-8

# # ¡Hola Francisco!
# 
# Mi nombre es Ezequiel Ferrario, soy code reviewer en Tripleten y tengo el agrado de revisar el proyecto que entregaste.
# 
# Para simular la dinámica de un ambiente de trabajo, si veo algún error, en primer instancia solo los señalaré, dándote la oportunidad de encontrarlos y corregirlos por tu cuenta. En un trabajo real, el líder de tu equipo hará una dinámica similar. En caso de que no puedas resolver la tarea, te daré una información más precisa en la próxima revisión.
# 
# Encontrarás mis comentarios más abajo - **por favor, no los muevas, no los modifiques ni los borres**.
# 
# ¿Cómo lo voy a hacer? Voy a leer detenidamente cada una de las implementaciones que has llevado a cabo para cumplir con lo solicitado. Verás los comentarios de esta forma:
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Si todo está perfecto.
# </div>
# 
# 
# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Si tu código está bien pero se puede mejorar o hay algún detalle que le hace falta. Se aceptan uno o dos comentarios de este tipo en el borrador, pero si hay más, deberá hacer las correcciones. Es como una tarea de prueba al solicitar un trabajo: muchos pequeños errores pueden hacer que un candidato sea rechazado.
# </div>
# 
# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Si de pronto hace falta algo o existe algún problema con tu código o conclusiones.
# </div>
# 
# Puedes responderme de esta forma:
# 
# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
# 
# Hola, muchas gracias por tus comentarios y la revisión.
# </div>
# 
# ¡Empecemos!

# # Déjame escuchar la música

# # Contenido <a id='back'></a>
# 
# * [Introducción](#intro)
# * [Etapa 1. Descripción de los datos](#data_review)
#     * [Conclusiones](#data_review_conclusions)
# * [Etapa 2. Preprocesamiento de datos](#data_preprocessing)
#     * [2.1 Estilo del encabezado](#header_style)
#     * [2.2 Valores ausentes](#missing_values)
#     * [2.3 Duplicados](#duplicates)
#     * [2.4 Conclusiones](#data_preprocessing_conclusions)
# * [Etapa 3. Prueba de hipótesis](#hypothesis)
#     * [3.1 Hipótesis 1: actividad de los usuarios y las usuarias en las dos ciudades](#activity)
# * [Conclusiones](#end)

# <div class="alert alert-block alert-warning">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Muy bien la tabla de contenidos pero debe estar linkeada a las secciones (al clickear debe llevarnos a esa seccion) de esta menera es mas facil desplazarse.
# 
# Como consejo, si realizas bien todas las secciones (con su respectivo #) podes generarlo automáticamente desde jupyter lab. Para hacerlo, en la pestaña de herramientas de jupyter lab clickeas en el **botón de los puntos y barras**  (Table of contents) te generara automáticamente una tabla de contenidos linkeable y estética. A la **derecha** del botón "Validate"
# </div>

# ## Introducción <a id='intro'></a>
# Como analista de datos, tu trabajo consiste en analizar datos para extraer información valiosa y tomar decisiones basadas en ellos. Esto implica diferentes etapas, como la descripción general de los datos, el preprocesamiento y la prueba de hipótesis.
# 
# Siempre que investigamos, necesitamos formular hipótesis que después podamos probar. A veces aceptamos estas hipótesis; otras veces, las rechazamos. Para tomar las decisiones correctas, una empresa debe ser capaz de entender si está haciendo las suposiciones correctas.
# 
# En este proyecto, compararás las preferencias musicales de las ciudades de Springfield y Shelbyville. Estudiarás datos reales de transmisión de música online para probar la hipótesis a continuación y comparar el comportamiento de los usuarios y las usuarias de estas dos ciudades.
# 
# ### Objetivo:
# Prueba la hipótesis:
# 1. La actividad de los usuarios y las usuarias difiere según el día de la semana y dependiendo de la ciudad.
# 
# 
# ### Etapas
# Los datos del comportamiento del usuario se almacenan en el archivo `/datasets/music_project_en.csv`. No hay ninguna información sobre la calidad de los datos, así que necesitarás examinarlos antes de probar la hipótesis.
# 
# Primero, evaluarás la calidad de los datos y verás si los problemas son significativos. Entonces, durante el preprocesamiento de datos, tomarás en cuenta los problemas más críticos.
# 
# Tu proyecto consistirá en tres etapas:
#  1. Descripción de los datos.
#  2. Preprocesamiento de datos.
#  3. Prueba de hipótesis.
# 
# 
# 
# 
# 
# 
# 

# [Volver a Contenidos](#back)

# ## Etapa 1. Descripción de los datos <a id='data_review'></a>
# 
# Abre los datos y examínalos.

# Necesitarás `pandas`, así que impórtalo.

# In[1]:


# Importar pandas
import pandas as pd


# Lee el archivo `music_project_en.csv` de la carpeta `/datasets/` y guárdalo en la variable `df`:

# In[2]:


# Leer el archivo y almacenarlo en df
df = pd.read_csv('/datasets/music_project_en.csv')


# Muestra las 10 primeras filas de la tabla:

# In[3]:


# Obtener las 10 primeras filas de la tabla df
df.head(10)


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Esta bien. Pero en este caso remplaza el print() y utiliza el metodo sin nada (llamalo solo) o con el metodo display(). Esto hara que sea mas legible y estetico.
# 
# No hace falta crear una variable que ocupe espacio, podes llamar al metodo sin crearla.</div>
# 
# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Se mantiene la correccion.</div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #3</b> <a class="tocSkip"></a>
# 
# Corregido.</div>

# Obtén la información general sobre la tabla con un comando. Conoces el método que muestra la información general que necesitamos.

# In[4]:


# Obtener la información general sobre nuestros datos
general_info = df.info()


# Estas son nuestras observaciones sobre la tabla. Contiene siete columnas. Almacenan los mismos tipos de datos: `object`.
# 
# Según la documentación:
# - `' userID'`: identificador del usuario o la usuaria;
# - `'Track'`: título de la canción;
# - `'artist'`: nombre del artista;
# - `'genre'`: género de la pista;
# - `'City'`: ciudad del usuario o la usuaria;
# - `'time'`: la hora exacta en la que se reprodujo la canción;
# - `'Day'`: día de la semana.
# 
# Podemos ver tres problemas con el estilo en los encabezados de la tabla:
# 1. Algunos encabezados están en mayúsculas, otros en minúsculas.
# 2. Hay espacios en algunos encabezados.
# 3. `Detecta el tercer problema por tu cuenta y descríbelo aquí`.
# 
# 
# La columna 'time' está en formato de objeto (object) en lugar de un formato de tiempo adecuado (por ejemplo, datetime) al igual que 'Day'.

# ### Escribe observaciones de tu parte. Estas son algunas de las preguntas que pueden ser útiles: <a id='data_review_conclusions'></a>
# 
# `1.   ¿Qué tipo de datos tenemos a nuestra disposición en las filas? ¿Y cómo podemos entender lo que almacenan las columnas?` Las filas contienen informacion sobre la actividad delos usuarios y usuarias, donde incluyen la sigueinte informacion:
# 'userID': identificador del usuario o la usuaria;
# 'Track': título de la canción;
# 'artist': nombre del artista;
# 'genre': género de la pista;
# 'City': ciudad del usuario o la usuaria;
# 'time': la hora exacta en la que se reprodujo la canción;
# 'Day': día de la semana.
# 
# `2.   ¿Hay suficientes datos para proporcionar respuestas a nuestra hipótesis o necesitamos más información?`Hay un total de 65079 entradas, podemos analizar a los usuarios  según el dia de la semana y la ciudad, pero la cantidad de datos influye en la confiabilidad de las conclusiones.
# 
# `3.   ¿Notaste algún problema en los datos, como valores ausentes, duplicados o tipos de datos incorrectos?` Hay valores nulos en las columans pero en diferentes cantidades, tambien 'time' y 'Day' presentan un tipo de dato incorrecto ya que deberia ser un dato temporal.

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Muy bien.</div>

# [Volver a Contenidos](#back)

# ## Etapa 2. Preprocesamiento de datos <a id='data_preprocessing'></a>
# 
# El objetivo aquí es preparar los datos para que sean analizados.
# El primer paso es resolver cualquier problema con los encabezados. Luego podemos avanzar a los valores ausentes y duplicados. Empecemos.
# 
# Corrige el formato en los encabezados de la tabla.
# 

# ### Estilo del encabezado <a id='header_style'></a>
# Muestra los encabezados de la tabla (los nombres de las columnas):

# In[5]:


# Muestra los nombres de las columnas
print(df.columns)


# Cambia los encabezados de la tabla de acuerdo con las reglas del buen estilo:
# * Todos los caracteres deben ser minúsculas.
# * Elimina los espacios.
# * Si el nombre tiene varias palabras, utiliza snake_case.

# Anteriormente, aprendiste acerca de la forma automática de cambiar el nombre de las columnas. Vamos a aplicarla ahora. Utiliza el bucle for para iterar sobre los nombres de las columnas y poner todos los caracteres en minúsculas. Cuando hayas terminado, vuelve a mostrar los encabezados de la tabla:

# In[6]:


# Bucle en los encabezados poniendo todo en minúsculas
new_columns = []
for col in df.columns:
    name_lowered = col.lower()
    new_columns.append(name_lowered)
df.columns = new_columns
print(df.columns)


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Recorda hacer el bucle que pase todo a minusculas.</div>
# 
# 
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido.</div>

# Ahora, utilizando el mismo método, elimina los espacios al principio y al final de los nombres de las columnas e imprime los nombres de las columnas nuevamente:

# In[7]:


# Bucle en los encabezados eliminando los espacios
new_columns = []

for col in df.columns:
    new_col = col.strip()
    new_columns.append(new_col)
    
df.columns = new_columns
print(df.columns)


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Aqui deberias utilizar el metodo especifico que corta los espacios, no utilices el replace es menos eficiente.</div>
# 
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido.</div>

# Necesitamos aplicar la regla de snake_case a la columna `userid`. Debe ser `user_id`. Cambia el nombre de esta columna y muestra los nombres de todas las columnas cuando hayas terminado.

# In[8]:


# Cambiar el nombre de la columna "userid"
new_columns = []

for col in df.columns:
    new_col = col.strip()
    new_col = new_col.replace('userid', 'user_id')
    new_columns.append(new_col)
    
df.columns = new_columns
print(df.columns)


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Esta bien el replace de userid a user_id, el resto debe ser cambiado</div>
# 
# 
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido.</div>
# 
# Comprueba el resultado. Muestra los encabezados una vez más:

# In[9]:


# Comprobar el resultado: la lista de encabezados
print(df.columns)


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# No estamos logrando el resultado esperado.</div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido. Te quedo excelente.</div>

# [Volver a Contenidos](#back)

# ### Valores ausentes <a id='missing_values'></a>
#  Primero, encuentra el número de valores ausentes en la tabla. Debes utilizar dos métodos en una secuencia para obtener el número de valores ausentes.

# In[10]:


# Calcular el número de valores ausentes
missing_values = df.isna().sum()
print(missing_values)


# No todos los valores ausentes afectan a la investigación. Por ejemplo, los valores ausentes en `track` y `artist` no son cruciales. Simplemente puedes reemplazarlos con valores predeterminados como el string `'unknown'` (desconocido).
# 
# Pero los valores ausentes en `'genre'` pueden afectar la comparación entre las preferencias musicales de Springfield y Shelbyville. En la vida real, sería útil saber las razones por las cuales hay datos ausentes e intentar recuperarlos. Pero no tenemos esa oportunidad en este proyecto. Así que tendrás que:
# * rellenar estos valores ausentes con un valor predeterminado;
# * evaluar cuánto podrían afectar los valores ausentes a tus cómputos;

# Reemplazar los valores ausentes en las columnas `'track'`, `'artist'` y `'genre'` con el string `'unknown'`. Como mostramos anteriormente en las lecciones, la mejor forma de hacerlo es crear una lista que almacene los nombres de las columnas donde se necesita el reemplazo. Luego, utiliza esta lista e itera sobre las columnas donde se necesita el reemplazo haciendo el propio reemplazo.

# In[11]:


# Bucle en los encabezados reemplazando los valores ausentes con 'unknown'
columns_to_replace = ['track', 'artist', 'genre']
for col in columns_to_replace:
    df[col].fillna('unknown', inplace=True)
    
print(columns_to_replace)


# Ahora comprueba el resultado para asegurarte de que después del reemplazo no haya valores ausentes en el conjunto de datos. Para hacer esto, cuenta los valores ausentes nuevamente.

# In[12]:


# Contar valores ausentes
mis_values = df.isna().sum()
print(mis_values)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Muy bien.</div>

# [Volver a Contenidos](#back)

# ### Duplicados <a id='duplicates'></a>
# Encuentra el número de duplicados explícitos en la tabla. Una vez más, debes aplicar dos métodos en una secuencia para obtener la cantidad de duplicados explícitos.

# In[13]:


# Contar duplicados explícitos
duplicates = df.duplicated().sum()
print(duplicates)


# Ahora, elimina todos los duplicados. Para ello, llama al método que hace exactamente esto.

# In[14]:


# Eliminar duplicados explícitos
df = df.drop_duplicates()


# Comprobemos ahora si eliminamos con éxito todos los duplicados. Cuenta los duplicados explícitos una vez más para asegurarte de haberlos eliminado todos:

# In[15]:


# Comprobar de nuevo si hay duplicados
count_duplicates = df.duplicated().sum()
print(count_duplicates)


# Ahora queremos deshacernos de los duplicados implícitos en la columna `genre`. Por ejemplo, el nombre de un género se puede escribir de varias formas. Dichos errores también pueden afectar al resultado.

# Para hacerlo, primero mostremos una lista de nombres de género únicos, ordenados en orden alfabético. Para ello:
# * Extrae la columna `genre` del DataFrame.
# * Llama al método que devolverá todos los valores únicos en la columna extraída.
# 

# In[16]:


# Inspeccionar los nombres de géneros únicos
unique_genres = df['genre']
unique_genres = unique_genres.unique()
unique_genres.sort()
print(unique_genres)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Muy bien. Como consejo, contando la cantidad de elementos unicos que tenemos (antes y despues) es  un parametro para verificar si el error esta corregido o no.
# 
# Si tengo menos registros que antes estara corregido.</div>

# Busca en la lista para encontrar duplicados implícitos del género `hiphop`. Estos pueden ser nombres escritos incorrectamente o nombres alternativos para el mismo género.
# 
# Verás los siguientes duplicados implícitos:
# * `hip`
# * `hop`
# * `hip-hop`
# 
# Para deshacerte de ellos, crea una función llamada `replace_wrong_genres()` con dos parámetros:
# * `wrong_genres=`: esta es una lista que contiene todos los valores que necesitas reemplazar.
# * `correct_genre=`: este es un string que vas a utilizar como reemplazo.
# 
# Como resultado, la función debería corregir los nombres en la columna `'genre'` de la tabla `df`, es decir, remplazar cada valor de la lista `wrong_genres` por el valor en `correct_genre`.
# 
# Dentro del cuerpo de la función, utiliza un bucle `'for'` para iterar sobre la lista de géneros incorrectos, extrae la columna `'genre'` y aplica el método `replace` para hacer correcciones.

# In[17]:


# Función para reemplazar duplicados implícitos
def replace_wrong_genres(df, wrong_genres, correct_genres):
    for genre in wrong_genres:
        df['genre'] = df['genre'].replace(wrong_genres, correct_genres)
        


# Ahora, llama a `replace_wrong_genres()` y pásale tales argumentos para que retire los duplicados implícitos (`hip`, `hop` y `hip-hop`) y los reemplace por `hiphop`:

# In[18]:


# Eliminar duplicados implícitos
wrong_genres = ['hip','hop', 'hip-hop']
correct_genres = 'hiphop'
replace_wrong_genres(df, wrong_genres, correct_genres)


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Cuidado, ya habias declarado la funcion arriba, no vuelvas a crearla. Simplemente llamala.</div>
# 
# 
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido.</div>

# Asegúrate de que los nombres duplicados han sido eliminados. Muestra la lista de valores únicos de la columna `'genre'` una vez más:

# In[19]:


# Comprobación de duplicados implícitos
unique_genres = df['genre']
unique_genres = unique_genres.unique()
unique_genres.sort()
print(unique_genres)


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Cuidado, ya habias declarado la funcion arriba, no vuelvas a crearla. Simplemente llamala.</div>
# 
# 
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido.</div>

# [Volver a Contenidos](#back)

# ### Tus observaciones <a id='data_preprocessing_conclusions'></a>
# 
# `Describe brevemente lo que has notado al analizar duplicados, cómo abordaste sus eliminaciones y qué resultados obtuviste.`
# Encabezados: Se identificaron problemas en el estilo de los encabezados. Se aplicaron correcciones convirtiéndolos a minúsculas, eliminando espacios y utilizando snake_case.
# 
# Valores Ausentes: Se encontraron valores ausentes en las columnas 'Track', 'artist' y 'genre'. Se decidió reemplazar estos valores ausentes con el string 'unknown', ya que no son críticos para el análisis. Se observó que no hay valores ausentes en las columnas 'userID', 'City', 'time' y 'Day'.
# 
# Duplicados: Se identificaron duplicados explícitos en la tabla y se eliminaron utilizando el método drop_duplicates(). Se observó que el número de duplicados explícitos antes de la eliminación era 3826 y después de la eliminación se redujo a 0.
# 
# Duplicados Implícitos en 'genre': Se detectaron duplicados implícitos en la columna 'genre', específicamente para el género 'hiphop', que se presentaba de varias formas: 'hip', 'hop', y 'hip-hop'. Se creó una función replace_wrong_genres() para corregir estos duplicados implícitos.

# [Volver a Contenidos](#back)

# ## Etapa 3. Prueba de hipótesis <a id='hypothesis'></a>

# ### Hipótesis: comparar el comportamiento del usuario o la usuaria en las dos ciudades <a id='activity'></a>

# La hipótesis afirma que existen diferencias en la forma en que los usuarios y las usuarias de Springfield y Shelbyville consumen música. Para comprobar esto, usa los datos de tres días de la semana: lunes, miércoles y viernes.
# 
# * Agrupa a los usuarios y las usuarias por ciudad.
# * Compara el número de canciones que cada grupo reprodujo el lunes, el miércoles y el viernes.
# 

# Realiza cada cálculo por separado.
# 
# El primer paso es evaluar la actividad del usuario en cada ciudad. Recuerda las etapas dividir-aplicar-combinar de las que hablamos anteriormente en la lección. Tu objetivo ahora es agrupar los datos por ciudad, aplicar el método apropiado para contar durante la etapa de aplicación y luego encontrar la cantidad de canciones reproducidas en cada grupo especificando la columna para obtener el recuento.
# 
# A continuación se muestra un ejemplo de cómo debería verse el resultado final:
# `df.groupby(by='....')['column'].method()`Realiza cada cálculo por separado.
# 
# Para evaluar la actividad de los usuarios y las usuarias en cada ciudad, agrupa los datos por ciudad y encuentra la cantidad de canciones reproducidas en cada grupo.
# 
# 

# In[20]:


# Contar las canciones reproducidas en cada ciudad
songs_played_by_city = df.groupby(by='city')['track'].count()
print(songs_played_by_city)


# 
# 
# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# Cambiaron el nombre de las columnas y por lo tanto, city ya no tiene guion bajo ni mayusculas. Llamala como quedo ahora y obtendras el resultado.</div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #3</b> <a class="tocSkip"></a>
# 
# Corregido. Muy bien.</div>

# `Comenta tus observaciones aquí`
# Springfield tiene mas del doble de canciones reproducidas que Shelbyville.

# Ahora agrupemos los datos por día de la semana y encontremos el número de canciones reproducidas el lunes, miércoles y viernes. Utiliza el mismo método que antes, pero ahora necesitamos una agrupación diferente.
# 

# In[21]:


# Calcular las canciones reproducidas en cada uno de los tres días
songs_played_by_day =df.groupby(by='day')['track'].count()
print(songs_played_by_day)


# `Comenta tus observaciones aquí`
# El viernes es el dia donde mas se reproducen canciones, pero el Lunes esta mu cerca del viernes.
# El miércoles seria el día con menos reproducciones.

# Ya sabes cómo contar entradas agrupándolas por ciudad o día. Ahora necesitas escribir una función que pueda contar entradas según ambos criterios simultáneamente.
# 
# Crea la función `number_tracks()` para calcular el número de canciones reproducidas en un determinado día **y** ciudad. La función debe aceptar dos parámetros:
# 
# - `day`: un día de la semana para filtrar. Por ejemplo, `'Monday'` (lunes).
# - `city`: una ciudad para filtrar. Por ejemplo, `'Springfield'`.
# 
# Dentro de la función, aplicarás un filtrado consecutivo con indexación lógica.
# 
# Primero filtra los datos por día y luego filtra la tabla resultante por ciudad.
# 
# Después de filtrar los datos por dos criterios, cuenta el número de valores de la columna 'user_id' en la tabla resultante. Este recuento representa el número de entradas que estás buscando. Guarda el resultado en una nueva variable y devuélvelo desde la función.

# In[22]:


# Declara la función number_tracks() con dos parámetros: day= y city=.

    # Almacena las filas del DataFrame donde el valor en la columna 'day' es igual al parámetro day=

    # Filtra las filas donde el valor en la columna 'city' es igual al parámetro city=

    # Extrae la columna 'user_id' de la tabla filtrada y aplica el método count()

    # Devolve el número de valores de la columna 'user_id'
    
def number_tracks(day,city):
    day_filtered = df[df['day'] == day]
    city_filtered = day_filtered[day_filtered['city'] == city]
    tracks_count = city_filtered['user_id'].count()
    return tracks_count


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor #3</b> <a class="tocSkip"></a>
# 
# En este caso estas llamando mal a las columnas. La funcion esta excelentemente planteada pero las columnas tienen otros nombres.</div>
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #4</b> <a class="tocSkip"></a>
# 
# Corregido.</div>

# Llama a `number_tracks()` seis veces, cambiando los valores de los parámetros para que recuperes los datos de ambas ciudades para cada uno de los tres días.

# In[23]:


# El número de canciones reproducidas en Springfield el lunes
result_springfield_monday = number_tracks(day='Monday', city='Springfield')
print(result_springfield_monday)


# In[24]:


# El número de canciones reproducidas en Shelbyville el lunes
result_shelbyville_monday = number_tracks(day='Monday', city='Shelbyville')
print(result_shelbyville_monday)


# In[25]:


# El número de canciones reproducidas en Springfield el miércoles
result_springfield_wednesday = number_tracks(day='Wednesday', city='Springfield')
print(result_springfield_wednesday)


# In[26]:


# El número de canciones reproducidas en Shelbyville el miércoles
result_shelbyville_wednesday = number_tracks(day='Wednesday', city='Shelbyville')
print(result_shelbyville_wednesday)


# In[27]:


# El número de canciones reproducidas en Springfield el viernes
result_springfield_friday = number_tracks(day='Friday', city='Springfield')
print(result_springfield_friday)


# In[28]:


# El número de canciones reproducidas en Shelbyville el viernes
result_shelbyville_friday = number_tracks(day='Friday', city='Shelbyville')
print(result_shelbyville_friday)


# **Conclusiones**
# 
# `Comenta si la hipótesis es correcta o se debe rechazar. Explica tu razonamiento.`
# Con base en los resultados obtenidos, podemos concluir que la hipótesis es correcta, ya que se observa claramente una diferencia en el número de reproducciones tanto por día como por ciudad. Al analizar los datos, destacamos que en Shelbyville el día con mayor cantidad de reproducciones es el miércoles, mientras que en Springfield es el día con menor cantidad de reproducciones.
# 
# Estos hallazgos sugieren que cada ciudad tiene su propia correlación de reproducciones a lo largo de la semana.

# [Volver a Contenidos](#back)

# # Conclusiones <a id='end'></a>

# `Resume aquí tus conclusiones sobre la hipótesis.`
# En resumen, los datos respaldan la idea de que existen diferencias en la forma en que los usuarios y usuarias de ambas ciudades consumen música, lo que valida la hipótesis planteada.
# 

# ### Nota
# En proyectos de investigación reales, la prueba de hipótesis estadística es más precisa y cuantitativa. También ten en cuenta que no siempre se pueden sacar conclusiones sobre una ciudad entera a partir de datos de una sola fuente.
# 
# Aprenderás más sobre la prueba de hipótesis en el sprint de análisis estadístico de datos.

# <div class="alert alert-block alert-danger">
# <b>Comentario general #1</b> <a class="tocSkip"></a>
# 
# Francisco, estas encaminado en lo realizado en este proyecto.
# 
# En lineas generales el proyecto esta bien, y si bien hay correcciones para hacer no son estructurales sino de detalles del codigo.
#     
#     
# Al no tener bien los nombres de las columnas luego deberas corregir todo para que concuerde por lo que no corregi el resto (Aunque en lineas generales esta muy bien).
# 
# Cuidado que estas llamando muchas veces a la funcion para modificar los duplicados implicitos, si tenes alguna duda estoy a disposicion.
# 
# Espero tus correcciones, saludos.</div>
# 
# 
# 
# <div class="alert alert-block alert-danger">
# <b>Comentario del general #2</b> <a class="tocSkip"></a>
# 
# Francisco, muy buenas las correcciones encaminaste el proyecto de forma excelente.
# 
# Restaria los detalles que te fui marcando, cuidado que hay  comentarios que se mantienen.
# 
# Quedo atento a tus correcciones, saludos.</div>
# 
# <div class="alert alert-block alert-danger">
# <b>Comentario del general #3</b> <a class="tocSkip"></a>
# 
# Francisco, resta un ultimo detalle para aprobar el proyecto.
#     
# Corregiste muy bien los otros puntos que faltaban y resta solo un punto y el trabajo estara aprobado.
# 
# Saludos.</div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del general #4</b> <a class="tocSkip"></a>
# 
# Francisco, corregido el punto que faltaba por lo que el proyecto queda **aprobado**.
# 
# Hiciste un excelente trabajo tanto en el inicio como a lo largo de las correcciones, donde entendiste que se requeria en cada caso.
# 
# Exitos en lo que viene, saludos.</div>

# [Volver a Contenidos](#back)
