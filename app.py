import streamlit as st
import plotly.express as px
from cache_data import load_data
import streamlit as st
import plotly.graph_objects as go


datos_cargados_csv, datos_cargados_png = load_data()

label_distribution = datos_cargados_csv['label_distribution']

label_distribution_simple = datos_cargados_csv['label_distribution_simple']

fig1 = px.pie(label_distribution, values='count', names='Label',title='Distribución de Clases')
fig2 = px.pie(label_distribution_simple, values='count_total', names='Label',title='Distribución Simplificada de Clases')

hovertemplate=(
            "<b>Sensibilidad:</b> %{x:.2f}<br>"
            "<b>Precisión:</b> %{y:.2f}<br>"
            "<b>Umbral de Decisión:</b> %{customdata:.2f}"
            "<extra></extra>" # Borra el cuadro lateral con el nombre de la serie
)

df_cut = datos_cargados_csv['df_cut']
df_cut2 = datos_cargados_csv['df_cut2']

fig_racall = go.Figure(data=[go.Scatter(x=df_cut['sensibilidad'], y=df_cut['precisión'], mode='lines+markers',customdata=df_cut['umbral de decición'],hovertemplate=hovertemplate,name='Modelo 3'),

go.Scatter(x=df_cut2['sensibilidad'], y=df_cut2['presición'], mode='lines+markers',customdata=df_cut['umbral de decición'],hovertemplate=hovertemplate,name='Modelo 2')])


def main() :


# Configuración de la página (limpiado, ya que estaba duplicado)
    st.set_page_config(page_title="Exfiltración de Datos", layout="wide")

# ==========================================
# FUNCIONES AUXILIARES
# ==========================================
def espacio_para_imagen(descripcion):
    st.info(f"🖼️ **ESPACIO PARA IMAGEN/GRÁFICO:** {descripcion}")

# Función para centrar imágenes utilizando columnas
def centrar_imagen(imagen):
    col1, col2, col3 = st.columns([1, 2, 1]) # Ajusta estos números si quieres la imagen más grande o pequeña
    with col2:
        st.image(imagen, use_container_width=True)

# ==========================================
# BARRA LATERAL (ÍNDICE DE REFERENCIA ESTILIZADO)
# ==========================================
st.sidebar.title("Índice 🧭")

# Inyectamos CSS para darle estilo de botones a los enlaces del navbar
estilo_navbar = """
<style>
.nav-link {
    display: block;
    padding: 10px 15px;
    margin: 8px 0;
    background-color: #1e1e1e;
    color: #fafafa !important;
    text-decoration: none;
    border-radius: 6px;
    font-weight: 500;
    font-size: 15px;
    transition: all 0.2s ease-in-out;
    border: 1px solid #333;
}
.nav-link:hover {
    background-color: #FF4B4B;
    color: white !important;
    border-color: #FF4B4B;
    transform: translateX(5px);
}
</style>

<a href="#introduccion" class="nav-link">1. Introducción</a>
<a href="#dataset" class="nav-link">2. El Dataset</a>
<a href="#exploracion" class="nav-link">3. Exploración de Datos</a>
<a href="#modelado" class="nav-link">4. Variables y Modelado</a>
<a href="#conclusion" class="nav-link">5. Conclusión</a>
"""
st.sidebar.markdown(estilo_navbar, unsafe_allow_html=True)

# ==========================================
# CONTENIDO PRINCIPAL
# ==========================================

st.markdown("<h1 style='text-align: center;'>EXFILTRACIÓN DE DATOS (CIBERSEGURIDAD)</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'><strong>Autor:</strong> LUIS GOMEZ OJEDA</p>", unsafe_allow_html=True)

# Botones nativos para los links externos
col1, col2, col3 = st.columns([10, 10, 7])
with col1:
    st.link_button("📓 Ver en Google Colab", "https://colab.research.google.com/drive/1nMls2KtKL76cza-WfQ-Q-CtGtpOihan5?authuser=1", use_container_width=True)
with col2:
    st.link_button("📑 Linkedin", "https://www.linkedin.com/in/luis-andres-gomez-ojeda-a1955020b/", use_container_width=True)
with col3:
    st.link_button("📂 Ver en Google Drive", "https://drive.google.com/drive/u/1/folders/1a-RRBv3KEjj_6_X8xZFdQWO1OS7DDx7N", use_container_width=True)

st.divider()

# --- SECCIÓN 1: INTRODUCCIÓN ---
st.markdown("<a id='introduccion'></a>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>La Exfiltración De Datos</h2>", unsafe_allow_html=True)
st.write("Ante la exfiltración inminente de datos (fase previa al robo de información), la ejecución de comandos inusuales o transferencias de volúmenes de datos atípico, por parte de usuarios, ¿se puede predecir un porcentaje de vulnerabilidad del sistema?, con que precisión?, ¿Se puede aislar automáticamente el equipo afectado de la red y cambiar las políticas de firewall en tiempo real?")

st.markdown("<h3 style='text-align: center;'>Definición de Exfiltración De Datos</h3>", unsafe_allow_html=True)
st.write("Es el robo o transferencia no autorizada de información sensible de una organización. Este tipo de robo puede surgir tanto desde amenazas internas como externas.")
st.write("Un ataque desde fuera de la organización ocurre cuando una persona o sistema desde fuera se infiltra en la red interna de la organización localiza información valiosa y sensible, transfiriendo dicha información hacia un servidor externo.")
st.write("La etapa previa de la exfiltración consiste en que el software malicioso o atacante accede a las credenciales de administrador o utiliza vulnerabilidades para moverse libremente por la red (estos comportamientos atípicos entre la red interna y la red externa se pueden registrar mediante herramientas de monitoreo de la red).")

st.divider()
st.markdown('''
<div style='display: flex; justify-content: center;'>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/WOnRP5xXekE?si=srcpiaHcVKSjI1HA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>       
            ''', unsafe_allow_html=True)
st.divider()

# --- SECCIÓN 2: DATASET ---
st.markdown("<a id='dataset'></a>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>CSE-CIC-IDS2018</h2>", unsafe_allow_html=True)
st.write("Para el desarrollo y análisis de este trabajo se utilizó como fuente principal el dataset CSE-CIC-IDS2018.")
st.write("Estos conjuntos de datos son parte de un proyecto elaborado por el Canadian Institute for Cybersecurity (CIC) de la Universidad de New Brunswick, Canadá. El proyecto consistió en simular el flujo de trabajo, tráfico y comportamiento en la red de una empresa con distintos departamentos. Dicho experimento se realizó durante al menos diez días, en los cuales se simuló el flujo normal de trabajo y tráfico en la red durante el horario laboral (8 AM a 5 PM). A lo largo de la simulación, se atacó en distintas ocasiones a la red de la empresa utilizando diversas técnicas de ciberataque y vectores de intrusión.")
st.write("Esta simulación fue desplegada íntegramente en la plataforma AWS (Amazon Web Services), construyendo una red interna de máquinas virtuales conectadas que simulaban la transferencia de datos y el tráfico corporativo. Durante varios días se ejecutaron ataques planificados, y estos flujos atípicos de información fueron capturados y clasificados de inicio a fin para ser analizados posteriormente.")

st.markdown("<h3 style='text-align: center;'>Captura y Transformación (De Paquetes a Flujos)</h3>", unsafe_allow_html=True)
st.write("Para la etapa de recolección, los investigadores de ciberseguridad se conectaron desde un dispositivo externo mediante SSH al router principal de la infraestructura en AWS. Allí, se ejecutó la herramienta de terminal tcpdump para capturar y grabar una copia exacta de todo el tráfico en crudo entre la red interna y externa. Si bien se utilizó la herramienta gráfica Wireshark para validar visualmente pequeñas muestras de esta captura, el procesamiento masivo se realizó pasando los archivos.pcap originales a través del software CICFlowMeter.")
st.write("Esta herramienta extrajo 80 métricas estadísticas (como promedios de velocidad, duración y cantidad de bytes) y transformó la estructura dimensional de la información: los registros dejaron de representar paquetes físicos individuales para convertirse en Flujos de red bidireccionales (el resumen estadístico de una conversación completa). Finalmente, todos estos datos estructurados fueron exportados a formato CSV.")

st.markdown("<h3 style='text-align: center;'>Limpieza y Optimización del Dataset</h3>", unsafe_allow_html=True)
st.write("Los archivos CSV originales desplegados por la universidad presentaban ruido técnico y errores estructurales, tales como:")
st.markdown("- **Encabezados repetidos:** Cada cierto mil de registros, la fila de datos se cortaba y volvían a aparecer los nombres de las columnas.")
st.markdown("- **Registros duplicados:** Por fallas en la captura, el software registraba el mismo flujo de red más de una vez.")
st.markdown("- **Valores matemáticos corruptos:** Errores de imputación por parte de CICFlowMeter, generando valores infinitos o nulos al calcular las tasas de transferencia.")
st.write("Para evitar estos problemas de integridad y hacer el análisis computacionalmente viable, decidí utilizar el dataset optimizado publicado por el usuario 'dhoogla' en la plataforma Kaggle. Este repositorio aplicó limpieza y corrección exhaustiva de la matriz de datos original, consolidando una base depurada y estructurada, ideal para el entrenamiento de modelos de Machine Learning.")

st.divider()

# --- SECCIÓN 3: EXPLORACIÓN ---
st.markdown("<a id='exploracion'></a>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Primera Visualización De Los Datos</h2>", unsafe_allow_html=True)
st.write("Utilice pyarrow y polars para poder visualizar los datos en formato dataFrame.")
st.dataframe(datos_cargados_csv['df_head'], use_container_width=True)

st.write("Se puede ver como el dataset preprocesado pesa cerca de 2GB y tiene 37 variables flotantes, 40 variables enteras y una variable tipo cadena de texto que es el Label.")
st.write("Utilizo Plotly Express para realizar un gráfico interactivo que muestre la distribución entre los registros etiquetados como benign o como algún tipo de ataque.")

st.plotly_chart(fig1, use_container_width=True)
st.plotly_chart(fig2, use_container_width=True)

st.markdown("<h3 style='text-align: center;'>Análisis de Distribución:</h3>", unsafe_allow_html=True)
st.write("Durante el experimento, aproximadamente el 20% del tiempo la infraestructura de red de la organización ficticia fue sometida a distintos ciberataques orientados a explotar vulnerabilidades presentes en diversos protocolos de comunicación. Como resultado, el conjunto de datos contiene 5.529.008 registros clasificados como tráfico benigno y 1.530.524 registros clasificados como tráfico malicioso, lo que representa un escenario desbalanceado donde predominan las conexiones normales.")
st.write("Para abordar el problema planteado, decidí realizar inicialmente un enfoque general de detección de intrusiones. En lugar de distinguir cada tipo de ataque por separado, se agruparon todos los ataques bajo una única categoría denominada tráfico malicioso, convirtiendo el problema en una clasificación binaria.")

st.markdown("<h3 style='text-align: center;'>Objetivo del Análisis y Modelado</h3>", unsafe_allow_html=True)
st.write("El objetivo del trabajo es desarrollar y comparar dos modelos de aprendizaje automático: un modelo de regresión logística y un modelo basado en árboles de decisión, con el fin de determinar cuál presenta el mejor desempeño para estimar la probabilidad de que un registro de tráfico de red corresponda a una conexión benigna o maliciosa. Para ello, se utilizan como variables predictoras las características más relevantes del tráfico de red, buscando identificar aquellas que aporten mayor capacidad predictiva, reduzcan la incertidumbre del modelo y permitan discriminar de forma eficiente entre tráfico normal y tráfico potencialmente malicioso.")
st.write("Como criterio principal de evaluación se prioriza la sensibilidad (recall), ya que en un sistema de detección de intrusiones resulta más importante minimizar la cantidad de ataques no detectados (falsos negativos) que reducir el número de falsas alarmas. Asimismo, el desempeño de ambos modelos se compara mediante las métricas de precisión, F1-score y el análisis del sobreajuste, con el propósito de seleccionar el modelo que ofrezca el mejor equilibrio entre capacidad de detección y generalización.")

st.markdown("<h3 style='text-align: center;'>Limitaciones</h3>", unsafe_allow_html=True)
st.write("Este proyecto fue desarrollado en el entorno de Google colab básico (Google Colaboratory), cuyo limite en el uso de la RAM es de 12.7GB.")
st.write("Por el gran peso del dataFrame y utilización de múltiples variables tuve que hacer uso del módulo interno de Python gc(sistema automático de gestión de memoria) para ir gestionando el almacenamiento en la memoria RAM")

codigo_gc = """import gc\ndel df, dfs, threat, Benign, fig1, fig2, label_distribution_simple\ngc.collect()"""
st.code(codigo_gc, language='python')

st.write("También debido al elevado volumen de información del conjunto de datos (más de siete millones de registros), fue necesario realizar una reducción del tamaño del dataset para disminuir los tiempos de procesamiento y facilitar el entrenamiento y análisis del modelo, manteniendo la representatividad de los datos mediante un muestreo estratificado que conserva la distribución original de las clases (80% tráfico benigno y 20% tráfico malicioso).")
st.write("Se generaron dos subconjuntos de datos:")
st.markdown("- **df_simple:** contiene aproximadamente el 30% de los registros del dataset original, preservando la proporción de las clases. Este conjunto se utiliza para el entrenamiento y evaluación del modelo de regresión logística.")
st.markdown("- **df_reduced:** contiene aproximadamente el 5% de los registros del dataset original, manteniendo igualmente la distribución de las clases. Este subconjunto se emplea para realizar las pruebas estadísticas y estudiar la capacidad predictiva de las variables, evaluando cuánto contribuye cada una a reducir la incertidumbre al clasificar el tráfico de red como benigno o malicioso.")
st.markdown("- **df Decision Tree:** contiene el 2% de los registros del conjunto de datos original, manteniendo la distribución de las clases mediante un muestreo estratificado. Este subconjunto se utiliza para entrenar y optimizar un modelo de árbol de decisión, aplicando Grid Search con validación cruzada para seleccionar la combinación de hiperparámetros que maximiza el rendimiento del modelo.")

st.divider()

# --- SECCIÓN 4: MODELADO ---
st.markdown("<a id='modelado'></a>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Filtro de Columnas</h2>", unsafe_allow_html=True)
st.text('Conteo de tipos de variables del dataset')
st.code('''
{
    Int8: 20,
    Int64: 1,
    Int32: 15,
    Float64: 15,
    Int16: 4,
    Float32: 22,
    Categorical: 1
}
        ''')
st.text('Analisis descriptivo de variables')
st.dataframe(datos_cargados_csv['df_simple_copy_describe'], use_container_width=True)
st.text('Conteo De Nulos Por Columna')
st.dataframe(datos_cargados_csv['null_count'], use_container_width=True)
st.text('Variables con disperción nula')
st.dataframe(datos_cargados_csv['df_std_0'], use_container_width=True)
st.text('Variables con bajo nivel de disperción')
st.dataframe(datos_cargados_csv['df_min_std'], use_container_width=True)

st.write("Analizando las medias y desviaciones estándar puedo descartar las variables cuya desviación estándar es 0 ya que no presentan información útil para el análisis. Sin embargo, no puedo descartar todas las variables cuya desviación estándar es menos a 1 ya que, en proporción con sus escalas, presentan una distribución significativa.")
st.write("Por contexto y poca variación puedo descartar las siguientes variables:")
st.markdown("- SYN Flag Count\n- FIN Flag Count\n- CWE Flag Count\n- Fwd URG Flags\n- URG Flag Count")

st.dataframe(datos_cargados_csv['label_distribution_reduce'], use_container_width=True)
st.write("Mapeo el dataSet destinado para las pruebas estadísticas y verifico que efectivamente se mantiene la distribución 80,20 del atributo Label del conjunto original.")

st.markdown("<h3 style='text-align: center;'>Medición estadística sobre variables continuas</h3>", unsafe_allow_html=True)
st.write("Mutual_info_clasiffic es una métrica de evaluación estadística que mide la información mutua entre cada variable predictora y la variable objetivo (discreta/categórica) o la disminución de la entropía que aporta cada variable")
st.latex(r"I(X;Y)=H(Y)-H(Y|X)")
st.write("información mutua dado: la entropía original - la entropía dado X")
st.write("Aplique esta métrica en cada variable continua para hacer un ranking de las variables que mayor incertidumbre despejan a la hora de querer predecir el atributo Label")

centrar_imagen(datos_cargados_png['ranking_variables'])

st.write("Luego de calcular y ordenar las variables de acuerdo a la cantidad de entropía que disminuyen respectivamente, filtré y me quedé con las variables cuya reducción es mayor a 0.2")

st.markdown("<h2 style='text-align: center;'>Análisis de Variables Categóricas</h2>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center;'>Protocolos</h3>", unsafe_allow_html=True)
st.write("Los protocolos son un conjunto de reglas, normas y procedimientos que definen cómo dos o más dispositivos se comunican e intercambian información a través de una red. Establecen aspectos como el formato de los datos, el orden de transmisión, el control de errores y la sincronización entre los equipos.")

st.markdown("<h3 style='text-align: center;'>Fwd PSH Flags</h3>", unsafe_allow_html=True)
st.write("Fwd PSH Flags (Push Flag) es un indicador del protocolo TCP que señala que los datos recibidos deben ser enviados inmediatamente a la aplicación de destino, sin esperar a que el búfer se llene. Su función es reducir la latencia cuando la información debe procesarse de forma rápida, como ocurre en aplicaciones interactivas (por ejemplo, terminales remotas o chats).")

st.write("Para evaluar las variables categóricas se aplicó la prueba de Lambda de Goodman:")
codigo_lambda = """[('variable': 'Protocol', 'value lambda': np.float64(0.0)),\n ('variable': 'Fwd PSH Flags', 'value lambda': np.float64(0.0))]"""
st.code(codigo_lambda, language="python")
st.text('Aunque la prueba de Lambda de Goodman indique que estas variables no representan una reducción significativa del error de predicción al analizarlas de forma individual respecto de la variable objetivo, considero importante mantenerlas dentro del conjunto de datos. Desde mi punto de vista, aportan información contextual valiosa para comprender el comportamiento general del tráfico de red, tanto benigno como malicioso. Además, entiendo que una variable con baja capacidad predictiva por sí sola puede contribuir al rendimiento del modelo cuando se combina con otros predictores, permitiendo identificar patrones e interacciones que no son evidentes al evaluar cada variable de manera aislada.')

st.markdown("<h2 style='text-align: center;'>Entrenamiento</h2>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center;'>Regresión Logística Binaria</h3>", unsafe_allow_html=True)
st.write("Realicé tres modelos utilizando diferentes valores del hiperparámetro C (tamaño del ajuste del modelo en cada iteración) con el objetivo de comparar su desempeño. Para ello evalué las matrices de confusión, la métrica F1-score y otras métricas de clasificación, con el fin de determinar cuál de los modelos se ajustaba mejor al problema. Una vez seleccionado el mejor modelo, ajusté el umbral de decisión (threshold) para optimizar el equilibrio entre la precisión y la capacidad de detección de la clase positiva, de acuerdo con los objetivos del proyecto.")

codigo_modelos = """modelo_1 = train_model(0.01)\nmodelo_2 = train_model(0.1)\nmodelo_3 = train_model(1)"""
st.code(codigo_modelos, language="python")

st.markdown("<h2 style='text-align: center;'>Modelo 1 (0.01)</h2>", unsafe_allow_html=True)

st.markdown("""
<p style="text-align: center;">
    ========== MÉTRICAS DE ENTRENAMIENTO (TRAIN) ========== <br>
    Precisión: 0.5357. De lo clasificado como maligno, el 53.57% lo es realmente. <br>
    Sensibilidad: 0.9201. Detectó el 92.01% de los malignos reales. <br>
    F1-Score: 67.71% <br>
    <br>
    ========== MÉTRICAS DE EVALUACIÓN (TEST) ========== <br>
    Precisión: 0.5374. De lo clasificado como maligno, el 53.74% lo es realmente. <br>
    Sensibilidad: 0.9196. Detectó el 91.96% de los malignos reales. <br>
    F1-Score: 67.84% <br>
    Iteraciones completadas: 1000
</p>
""", unsafe_allow_html=True)
centrar_imagen(datos_cargados_png['regression1'])

st.markdown("<h2 style='text-align: center;'>Modelo 2 (0.1)</h2>", unsafe_allow_html=True)
st.markdown('''
<p style="text-align: center;">
========== MÉTRICAS DE ENTRENAMIENTO (TRAIN) ==========<br>
Precisión: 0.5357. De lo clasificado como maligno, el 53.57% lo es realmente.<br>
Sensibilidad: 0.9201. Detectó el 92.01% de los malignos reales.<br>
F1-Score: 67.71%<br>
========== MÉTRICAS DE EVALUACIÓN (TEST) ==========<br>
Precisión: 0.5374. De lo clasificado como maligno, el 53.74% lo es realmente.<br>
Sensibilidad: 0.9196. Detectó el 91.96% de los malignos reales.<br>
F1-Score: 67.84%<br>
Iteraciones completadas: 1000
</p>
''',unsafe_allow_html=True)
centrar_imagen(datos_cargados_png['regression2'])

st.markdown("<h2 style='text-align: center;'>Modelo 3 (1)</h2>", unsafe_allow_html=True)
st.markdown('''
<p style="text-align: center;">
========== MÉTRICAS DE ENTRENAMIENTO (TRAIN) ==========<br>
Precisión: 0.5361. De lo clasificado como maligno, el 53.61% lo es realmente.<br>
Sensibilidad: 0.9207. Detectó el 92.07% de los malignos reales.<br>
F1-Score: 67.76%<br>
========== MÉTRICAS DE EVALUACIÓN (TEST) ==========<br>
Precisión: 0.5378. De lo clasificado como maligno, el 53.78% lo es realmente.<br>
Sensibilidad: 0.9204. Detectó el 92.04% de los malignos reales.<br>
F1-Score: 67.89%<br>
Iteraciones completadas: 1000<br>
</p>
        ''',unsafe_allow_html=True)

centrar_imagen(datos_cargados_png['regression3'])

st.markdown('''
<p style="text-align: center;">
Al comparar los resultados del conjunto de entrenamiento y del conjunto de  
prueba, observé que las métricas eran muy similares. Esto indica que los  
modelos no presentan sobreajuste (overfitting) y que la regularización  
aplicada por la regresión logística fue suficiente para lograr una buena  
capacidad de generalización. 
Si bien los modelos 2 y 3 obtuvieron resultados muy parecidos, decidí evaluar  
ambos en la etapa de selección del umbral de decisión para determinar cuál  
ofrecía una mejor relación entre precisión y sensibilidad (recall). 
</p>
        ''',unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'><strong>Comparación del F1 score de los modelos entrenados:</strong></h4>", unsafe_allow_html=True)
centrar_imagen(datos_cargados_png['f1_score'])

st.text('''
Si bien el modelo 2 y 3 tienen resultados similares decidí utilizar ambos modelos para determinar de cual de los dos se puede determinar un mejor umbral de desición teniendo en cuenta la curva de recall

Para determinar el umbral de decición decidí utilizar el metodo de presición-recall, en el que evalue mediante un ciclo for, distintos umbrales de decición desde 0.20 hasta 0.85 y calcule su respectivas sensibilidad y presición en cada instancia
        ''')

st.plotly_chart(fig_racall, use_container_width=True)
st.text('Priorizando una alta sensibilidad (recall), es decir, la capacidad del modelo para identificar correctamente la mayor cantidad posible de tráfico malicioso, seleccioné un umbral de decisión de 0,5 para el tercer modelo. Con este umbral, el modelo alcanza una sensibilidad del 92 %, lo que significa que identifica correctamente el 92 % de las instancias de tráfico malicioso, reduciendo la cantidad de falsos negativos y mejorando su capacidad de detección. No obstante, con este umbral el modelo obtiene una precisión del 55 %, lo que implica que aproximadamente el 55 % de las alertas generadas corresponden efectivamente a tráfico malicioso, mientras que el porcentaje restante corresponde a falsos positivos. Esta configuración prioriza la detección de amenazas por sobre la reducción de falsas alarmas, una estrategia adecuada en sistemas de detección de intrusiones donde resulta más costoso no detectar un ataque que generar una alerta adicional.')
st.markdown("<h4 style='text-align: center;'>Modelo Final (Regresión Logística)</h4>", unsafe_allow_html=True)

st.markdown('''
<p style="text-align: center;">
========== MÉTRICAS DE ENTRENAMIENTO (TRAIN) ==========<br>
Precisión: 0.5361. De lo clasificado como maligno, el 53.61% lo es realmente.<br>
Sensibilidad: 0.9207. Detectó el 92.07% de los malignos reales.<br>
F1-Score: 67.76%<br>
========== MÉTRICAS DE EVALUACIÓN (TEST) ==========<br>
Precisión: 0.5378. De lo clasificado como maligno, el 53.78% lo es realmente.<br>
Sensibilidad: 0.9204. Detectó el 92.04% de los malignos reales.<br>
F1-Score: 67.89%<br>
Iteraciones completadas: 1000<br>
</p>        
            ''',unsafe_allow_html=True)
centrar_imagen(datos_cargados_png['regression3'])
st.markdown("<h3 style='text-align: center;'>Árbol de Decisión</h3>", unsafe_allow_html=True)
st.write('''
Para el entrenamiento y optimización del modelo de árbol de decisión se utilizó la herramienta GridSearchCV de la biblioteca Scikit-learn, la cual permite evaluar múltiples combinaciones de hiperparámetros mediante validación cruzada y seleccionar automáticamente la configuración con mejor desempeño.

Durante el proceso se evaluaron las siguientes configuraciones:

- En todos los modelos se utilizó el parámetro class_weight='balanced', con el objetivo de penalizar en mayor medida los errores cometidos sobre la clase minoritaria (tráfico malicioso), compensando así el desbalance presente en el conjunto de datos.

- Se probaron los criterios de división Gini Impurity (gini) y Entropía (entropy) para determinar cuál generaba árboles con mejor capacidad predictiva.

- La profundidad máxima del árbol (max_depth) se evaluó en valores comprendidos entre 5 y 15, utilizando incrementos de 5 unidades.

- También se evaluaron distintas configuraciones del parámetro max_features, utilizando las opciones sqrt y log2. Este parámetro limita la cantidad de variables candidatas consideradas en cada división del árbol. En lugar de evaluar todas las variables disponibles en cada nodo, el algoritmo selecciona aleatoriamente un subconjunto de características, reduciendo el tiempo de entrenamiento y disminuyendo el riesgo de sobreajuste.

- Al igual que en los modelos de regresión logística, la métrica utilizada para seleccionar el mejor modelo fue la sensibilidad (recall), dado que el objetivo principal del sistema es maximizar la detección de tráfico malicioso y minimizar la cantidad de falsos negativos.

Por otra parte, GridSearchCV permite definir el parámetro cv, que determina la cantidad de particiones utilizadas durante la validación cruzada. En este trabajo se estableció cv = 3, por lo que cada combinación de hiperparámetros fue entrenada y evaluada tres veces sobre diferentes particiones de los datos. Esto permite obtener una estimación más robusta del rendimiento del modelo y reducir la influencia de la aleatoriedad en el proceso de selección.
         ''')

st.markdown("<h3 style='text-align: center;'><em><strong>Configuración del Modelo Más Optimo</strong></em></h3>", unsafe_allow_html=True)
centrar_imagen(datos_cargados_png['árbol de decisión'])

st.markdown('''
        <p style='text-align: center;'>la sensibilidad de entrenamiento es de 94.18%</p>
        <p style='text-align: center;'>la precisión de entrenamiento es de 96.53%</p>
        <p style='text-align: center;'>el f1 score de entrenamiento es de 95.34%</p>
''',unsafe_allow_html=True)
centrar_imagen(datos_cargados_png['matrix_train'])

st.markdown('''
<p style='text-align: center;'>la sensibilidad de testeo es de 91.62%</p>
<p style='text-align: center;'>la precisión de testeo es de 93.75%</p>
<p style='text-align: center;'>el f1 score de testeo es de 92.67%</p>
        ''',unsafe_allow_html=True)
centrar_imagen(datos_cargados_png['matrix_test'])

st.text('''
El modelo óptimo obtenido mediante Grid Search, seleccionado según la métrica recall, no evidencia un sobreajuste significativo, ya que el rendimiento entre los conjuntos de entrenamiento y prueba se mantiene consistente. Asimismo, supera en desempeño al modelo óptimo de regresión logística.
        ''')

st.markdown("<h3 style='text-align: center;'>Comparación del Modelo</h3>", unsafe_allow_html=True)
centrar_imagen(datos_cargados_png['f1_score_treeVSregressionLogistic'])
st.write("Al comparar la métrica F1-score de ambos modelos, se observa que el árbol de decisión supera al modelo de regresión logística en un 23,4%, lo que indica un mejor equilibrio entre precisión y sensibilidad.")

st.divider()

# --- SECCIÓN 5: CONCLUSIÓN ---
st.markdown("<a id='conclusion'></a>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Conclusión</h2>", unsafe_allow_html=True)

st.markdown("<h4 style='text-align: center;'><em><strong>¿se puede predecir un porcentaje de vulnerabilidad del sistema? ¿Con qué precisión?</strong></em></h4>", unsafe_allow_html=True)
st.write('''En respuesta al planteamiento inicial de este trabajo, se concluye que, a partir del modelo entrenado
con los datos del proyecto desarrollado por el Canadian Institute for Cybersecurity (CIC) de la
Universidad de New Brunswick (Canadá), es posible predecir si un flujo de red corresponde a tráfico
normal o a un posible ataque informático. El modelo entrenado a partir de árboles de desiciones alcanzó una sensibilidad (recall) del 92,01 %, lo
que indica que identifica correctamente más de nueve de cada diez eventos maliciosos presentes en el
conjunto de prueba. Asimismo, obtuvo una precisión del 93,43 %, lo que significa que la gran mayoría
de las alertas clasificadas como ataques corresponden efectivamente a eventos maliciosos. Finalmente,
el F1-score del 92,71 % refleja un excelente equilibrio entre precisión y sensibilidad, evidenciando un
alto rendimiento general del modelo para tareas de detección de intrusiones.''')

st.markdown("<h4 style='text-align: center;'><em><strong>¿Se puede aislar automáticamente el equipo afectado de la red y cambiar las políticas de firewall en tiempo real?</strong></em></h4>", unsafe_allow_html=True)
st.write('''
Los resultados obtenidos permiten considerar la implementación de una respuesta automática
capaz de aislar el equipo afectado de la red y modificar las políticas del firewall en tiempo real.
A diferencia de versiones anteriores del modelo, el desempeño alcanzado, con una precisión
del 93,43 % y una sensibilidad del 92,01 %, reduce significativamente la probabilidad tanto de
falsos positivos como de falsos negativos. Esto convierte al modelo en una herramienta mucho
más confiable para la automatización de respuestas ante incidentes de seguridad.
No obstante, en entornos críticos resulta recomendable mantener un esquema de supervisión
humana para los eventos de mayor impacto, permitiendo que un especialista en ciberseguridad
valide las alertas antes de ejecutar acciones que puedan afectar la disponibilidad de los
sistemas. De esta manera, se aprovecha la elevada capacidad de detección del modelo y su
alta precisión, reduciendo al mismo tiempo el riesgo asociado a una respuesta completamente
automatizada.
         ''')



if __name__ == '__main__':
    main()