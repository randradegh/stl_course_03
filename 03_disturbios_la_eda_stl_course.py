####
## Status: revisado
## Fecha revisión: 20220808
####
##
# Caso Disturbios en LA. Intro al uso de streamlit, dataframes, pandas, mapas.
##
##
# Utilerías del proyecto
##
from utils import *

from vega_datasets import data
##
# Carga de los datos
##
df = data.la_riots()

# Título
header("9 casos de negocio con Streamlit")
st.subheader("3. Disturbios en Los Ángeles, Cal. y Tipos de Gráficos")

##
# Introducción
##
st.subheader("Introducción")
st.markdown("""
    Más de 60 personas perdieron la vida en medio de los saqueos e incendios que asolaron la ciudad de **Los Ángeles** durante cinco días a partir del 29 de abril de 1992. 
    
    Este _dataset_ contiene datos sobre cada persona, 
    incluidas las coordenadas geográficas de su muerte. 

    Fue compilado y publicado por *Los Angeles Times Data Desk*.

    Es parte de la biblioteca python **Vega Datasets** (_vega_datasets_).
""")

st.subheader("¿Para que sirve el análisis de datos?")

st.markdown("""
    El análisis de datos se define como un proceso de limpieza, transformación y modelado de datos para descubrir información 
    útil para la toma de decisiones.
    
    El propósito del análisis de datos es extraer información útil de los datos 
    y tomar una decisión basada en sus resultados.

    Un ejemplo simple de análisis de datos es cada vez que tomamos una decisión en nuestro día a día pensando en lo que sucedió 
    la última vez o lo que sucederá al elegir esa decisión en particular.
    
    Esto no es más que analizar nuestro pasado y tomar decisiones en base a ello. Para eso, recolectamos recuerdos de nuestro pasado. 
    
    Entonces eso no es más que análisis de datos. Ahora, lo mismo que hace el analista con fines comerciales, se llama **Análisis de Datos**.

    Una buena manera de diseñar el proceso del análisis de datos consiste en plantearse las dudas o preguntas acerca del objeto de estudio, 
    ya sea una situación social, comercial, científica o industrial.

    Para nuestro caso podemos plantearnos algunas preguntas iniciales, pero es probable que al avanzar podamos 
    plantear otras cuestiones más precisas o algunas que no vislumbramos por el momento.

    ### Preguntas iniciales acerca de los disturbios en Los Ángeles»
""")
##
# Mostrar conceptos de listas, series, diccionarios y df.
##


st.markdown("""
    - ¿Qué variables tiene nuestro _dataset_?
    - ¿Qué barrios incluye nuestro _dataset_?
    - ¿Qué grupos étnicos fueron los más afectados?
    - ¿Cómo se distribuyeron las edades de los participantes?
    - ¿Qué tipo de gráfico es mejor para responder a cada una de nuestras preguntas?
    - Otras preguntas.
    """)

##
# Temas a tratar
## 
st.markdown("## Dataframes, listas, series y diccionarios")
st.markdown("""
    ### Carga de su primer conjunto de datos
    Cuando recibimos un conjunto de datos (_dataset_), primero lo cargamos y comenzamos a mirar 
    su estructura y contenido.
    
    La forma más sencilla de ver un conjunto de datos es examinar y crear subconjuntos de filas y columnas específicas. 
    Podemos ver qué tipo de información se almacena en cada columna y podemos comenzar a buscar patrones agregando estadísticas descriptivas.

    Dado que Pandas no es parte de la biblioteca estándar de Python, primero debemos decirle a Python que cargue (importe) la biblioteca.

    `import pandas as pd`
""")

with st.echo(code_location="above"):
    # usamos el método head() para que Python nos muestre solo las primeras 5 filas
    st.write(df.head())

with st.echo(code_location="above"):
    # Podemos verificar si estamos trabajando con un Pandas DataFrame 
    # usando la función de tipo incorporada (es decir, proviene directamente 
    # de Python, no de ningún paquete como Pandas).
    st.write(df.dtypes)


with st.echo(code_location="above"):
    # Usemos la función para recuperar los nombres de las columnas
    st.write(df.columns)

with st.echo(code_location="above"):
    # Obtenemos la cantidad de renglones y columnas
    st.write(df.shape)

st.write(f"""
    El atributo forma (_shape_) devuelve una tupla en la que el primer valor es el número de filas y el segundo 
    número es el número de columnas. De los resultados anteriores, vemos que nuestro 
    conjunto de datos tiene {df.shape[0]} filas y {df.shape[1]} columnas.
    
    Dado que la forma es un atributo del *dataframe* y no una función o método del marco de datos, 
    no tiene paréntesis después del punto.
    
    Si cometió el error de poner paréntesis después del atributo de forma, devolvería un error.

    Más adelante haremos un análisis de los datos más detallado, para eso repasaremos
    las diversas maneras de manejar los _dataframes_.

    ### Renglones, columnas y celdas
    Ya revisamos como podemos cargar un archivo de datos con formato CSV, ahora debemos poder inspeccionar su contenido.
    
    Podríamos imprimir el contenido del dataframe, pero con los datos actuales, a menudo hay demasiadas celdas para que toda la información 
    impresa tenga sentido. 
    
    En cambio, la mejor manera de ver nuestros datos es inspeccionarlos en partes observando varios subconjuntos de datos. 
    
    Ya vimos que podemos usar el método _head()_ de un dataframe para mirar las primeras cinco filas de nuestros datos. Esto es útil para ver si nuestros datos se cargaron correctamente 
    y para tener una idea de cada una de las columnas, su nombre y su contenido. 
    
    A veces, sin embargo, es posible que deseemos ver solo algunas filas, columnas o valores particulares de  nuestros _data set_.
    
    #### Recuperando un subconjunto de columnas

    Podemos seleccionar solamente algunas columnas especificando sus nombres, sus 
    posiciones o algunos rangos.

    **Por nombre de columna**
""")

with st.echo(code_location="above"):
    # Mostramos solamente una columna
    st.write(df['race'].head(3))

with st.echo(code_location="above"):
    # Mostramos solamente una columna usando la notación punto
    st.write(df.race.head(3))

with st.echo(code_location="above"):
    # Mostramos algunas columnas específicas
    st.write(df[['first_name','age','neighborhood']].head(7))

st.write("""Es posible que desee obtener un renglón o fila en particular por su posición, es decir, por su índice.""")


with st.echo(code_location="above"):
    # Recuperamos el primer renglón
    st.write(df.loc[[0]])

with st.echo(code_location="above"):
    # Recuperamos el cuarto renglón
    st.write(df.loc[[3]])

with st.echo(code_location="above"):
    # Mostramos todas la columnas para un origen específico
    st.write(df.loc[df.race == 'Asian'])

with st.echo(code_location="above"):
    # Usando _iloc_ para obtener una rebanada del df sobre un rango de índices
    st.write(df.loc[1:4])

##
# Con iloc
##
with st.echo(code_location="above"):
    # Dos renglones y tres columnas
    st.write(df.iloc[[0,2], [1,2,3]])

st.write("""
    Durante el curso veremos más ejemplos del manejo y las grandes ventajas de usar Pandas.
    """)

st.markdown("## Gráficos")
st.markdown("""
    ¿Por qué usamos los gráficos?

    Una visualización puede servir para muchos propósitos.
    
    Vamos a  dividirlos en tres objetivos clave, cada uno de los cuales influye en nuestras elecciones 
    de diseño de diferentes maneras. 
    
    Una clara comprensión de su propósito guiará todas las decisiones que tomemos cuando seleccionemos o diseñemos un gráfico.

    **Explorar**: Permite que un usuario navegue por los datos 
    - Representa un sistema complicado o un espacio de información
    - Ayuda a alguien a ver conexiones y relaciones
    - Ayuda a un usuario a comprender patrones y realizar consultas avanzadas.

    **Explicar**: Presentar un argumento, convencer o informar
    - Construye una narrativa de datos para apoyar la toma de decisiones
    - Enseña a alguien a entender un tema interesante
    - Documenta una serie de eventos, utilizando la visualización para enfatizar detalles importantes o puntos críticos
    - Informa los resultados de su análisis y recomiende una interpretación o curso de acción.

    **Emoción**: Crea un compromiso más fuerte con un tema o inspire una respuesta emocional
    - Ayuda a las personas a ver por qué su tema es importante o convéncerlas para que apoyen alguna causa
    - Representa una experiencia, un sistema de valores o una identidad que se conecta con los espectadores.
    - Muestra el impacto de algo que generalmente está oculto o invisible, o que a menudo pasa inadvertido
    - Construye una visión de lo que podría ser
    - Demostra la escala o extensión de un problema o el impacto potencial de una solución.
""")

st.markdown("### Tipos de Gráficos con Plotly")

"""
El módulo _plotly.express_ (usualmente importado como _px_) contiene funciones que pueden crear figuras enteras de una vez, y es referido como Plotly Express o PX.

Plotly Express es una parte incorporada de la biblioteca de plotly, y es el punto de partida recomendado para crear las figuras más comunes.

A lo largo de la documentación de plotly, encontramos la forma de construir figuras de Plotly Express, seguida de una sección sobre cómo utilizar objetos gráficos para construir figuras similares.

Cualquier figura creada en una sola llamada a una función con Plotly Express podría ser creada usando sólo objetos gráficos, pero con entre 5 y 100 veces más código.
"""
##
# Scatter plot
##
with st.echo(code_location="above"):

    st.write("""
        ---
        #### Gráfico de dispersión (_scatter plot_)
    """)
    color = '#b2babb'
    
    fig1 = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16],
        template='gridon', 
        title="Gráfico de Dispersión"
        )
    
    fig1.update_layout(width=700,height=500)
    fig1.update_xaxes(title_text='x')
    fig1.update_yaxes(title_text='y')
    
    fig1.update_layout({
            'font_color' : '#2C3E50',
            'plot_bgcolor': color,
            'paper_bgcolor': color,
    })
    
    # Mostramos el gráfico
    fig1

##
# Line plot
##
with st.echo(code_location="above"):
    st.write("""
        ---
        #### Gráfico de línea (_line_)
    """)
    #color = 'red'
    color = '#b2babb'
    
    fig1 = px.line(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16],
        template='gridon', 
        title="Gráfico de Línea"
        )
    
    fig1.update_layout(width=700,height=500)
    fig1.update_xaxes(title_text='x')
    fig1.update_yaxes(title_text='y')
    
    fig1.update_layout({
            'font_color' : '#2C3E50',
            'plot_bgcolor': color,
            'paper_bgcolor': color,
    })
    
    # Mostramos el gráfico
    fig1

##
# Bar plot
##
with st.echo(code_location="above"):
    st.write("""
        ---
        #### Gráfico de Barras (_bar_)
    """)
    color = 'gray'
    
    # Explicar el uso de size()
    fig1 = px.bar(df.groupby(['neighborhood']).size(), 
        template='gridon', 
        title="Disturbios por Barrio"
        )
    
    fig1.update_layout(width=900,height=500)
    fig1.update_xaxes(title_text='Barrio', title_font_color= 'black')
    fig1.update_yaxes(title_text='Cantidad de Disturbios', title_font_color= 'black')
    fig1.update_layout({
            'font_color' : '#2C3E50',
            #'font_color' : 'black',
            'plot_bgcolor': color,
            'paper_bgcolor': color,
    })
    

    # Mostramos el gráfico
    fig1

##
# Histograma
##
with st.echo(code_location="above"):
    st.write("""
        ---
        #### Histograma
    """)
    color = 'gray'
    
    # Explicar el uso de dropna()
    fig_hist = px.histogram(df.dropna(), 
        x="age",
        title = 'Histograma de Edades de Participantes')

    fig_hist.update_traces(xbins=dict( 
            # bins used for histogram
            #start= df.age.min(),
            #end= df.age.max(),
            start= 10,
            end= 100,
            size=10         
        ))

    fig_hist.update_layout(width=700,height=400)
    fig_hist.update_xaxes(title_text='Edad')
    fig_hist.update_yaxes(title_text='Cantidad')

    fig_hist.update_layout({
            'font_color' : '#2C3E50',
            'plot_bgcolor': color,
            'paper_bgcolor': color,
    })

    fig_hist

##
# Box Plot
##
with st.echo(code_location="above"):
    st.write("""
        ---
        #### Diagrama de Caja (_Box Plot_)
    """)

    fig_bp = px.box(df, y="age", title = 'Edades de Participantes')
    fig_bp.update_layout(width=700,height=500)

    fig_bp.update_layout({
            'font_color' : '#2C3E50',
            'paper_bgcolor' : 'rgb(243, 243, 243)',
            'plot_bgcolor' : 'rgb(243, 243, 243)',
    })
    fig_bp

##
# Pie plot
##
with st.echo(code_location="above"):
    st.write("""
        ---
        #### Gráfico de Sectores (_pie_)
    """)
    color = 'white'
    
    s_barrio = df.groupby(['neighborhood']).size()
    df_barrio = pd.DataFrame(s_barrio).reset_index()
    df_barrio.columns=['Barrio', 'Cantidad']
    fig1  = px.pie(df_barrio, values='Cantidad', names='Barrio', title='Disturbios por Barrio')
    fig1.update_layout(width=700,height=500)
        
    fig1.update_layout({
            'font_color' : '#2C3E50',
            'paper_bgcolor': 'white',
    })
    
    # Mostramos el gráfico
    fig1

##
# Mapas
##
st.write("""
    ---
    #### Mapas
""")
st.write('**Disturbios en Los Ángeles**')
# LA
with st.echo(code_location="above"):
    df_la = df[['longitude', 'latitude']]
    st.map(df_la)

# CDMX
st.write("""
---
**Localizaciones al azar en la CDMX**
""")
with st.echo(code_location="above"):
    df_cdmx = pd.DataFrame(
        (np.random.randn(50, 2) / [50, 50]) + [19.49, -99.12],
        columns=['latitude', 'longitude'])

    st.map(df_cdmx)

"""
___
"""

#footer("Copyrigth © 2022, RAF")