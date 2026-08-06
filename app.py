
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
from datetime import datetime
import csv

BASE = Path(__file__).parent
DATA = BASE / "data"
EXPORTS = BASE / "exports"
EXPORTS.mkdir(exist_ok=True)

st.set_page_config(page_title="SITRA-ETF", page_icon="🌱", layout="wide")

CSS = """
<style>
.main .block-container {padding-top: 2rem; max-width: 1320px;}
.sitra-hero {background: linear-gradient(135deg,#eef9ff,#f7fcff); border-left: 4px solid #0a65b7; border-radius: 18px; padding: 1.4rem 1.6rem; box-shadow: 0 2px 14px rgba(0,0,0,.06);}
.badge {display:inline-block; border:1px solid #a9d7ff; background:#eef8ff; color:#0a65b7; padding:.28rem .55rem; margin:.2rem; border-radius:999px; font-size:.78rem;}
.metric-card {border:1px solid #e6eef5; border-radius:16px; padding:1rem; background:white; box-shadow:0 1px 8px rgba(0,0,0,.04);}
.info-box {border-left:4px solid #0a65b7; background:#eef7ff; padding: .85rem 1rem; border-radius: 10px; margin: .75rem 0;}
.warn-box {border-left:4px solid #ffcc29; background:#fff8dd; padding: .85rem 1rem; border-radius: 10px; margin: .75rem 0;}
.success-box {border-left:4px solid #2a9d66; background:#ecfff5; padding: .85rem 1rem; border-radius: 10px; margin: .75rem 0;}
a {text-decoration: none;}
.stToolbarActions{ display: none; }
.stAppHeader { display: none; }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

@st.cache_data
def load_csv(name):
    return pd.read_csv(DATA / name)

def save_append_csv(name, row):
    path = DATA / name
    with open(path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(row)

def download_df_button(df, filename, label):
    st.download_button(label, data=df.to_csv(index=False).encode('utf-8-sig'), file_name=filename, mime='text/csv')

def google_earth_link(lat, lon):
    return f"https://earth.google.com/web/search/{lat},{lon}"

def section_header(title, subtitle=None):
    st.markdown(f"## {title}")
    if subtitle:
        st.caption(subtitle)

pages = [
    "Inicio y fuentes",
    "Inteligentismo y creatopraxología",
    "Mapa Venezuela",
    "Mapas por estado y Google Earth",
    "Mapa de conocimiento y talento",
    "Diagnóstico persona-zona-empresa",
    "Competencias CG-CT",
    "Potencial local y medios de vida",
    "Empresas y alianzas",
    "Ruta de autosustento",
    "Banco de ideas",
    "Productivización y servitización",
    "Beneficios y métricas",
    "IA gratuita y bibliometría",
    "Repositorios y difusión",
    "Dashboard y reportes",
]

st.sidebar.image(str(BASE / "assets" / "logo.svg"), use_container_width=True)
st.sidebar.title("SITRA-ETF")
st.sidebar.caption("Escuela de Talentos para el Futuro · v0.1 demo")
page = st.sidebar.radio("Navegación", pages)
st.sidebar.markdown("---")
st.sidebar.caption("Localhost · Inteligentismo + Creatopraxología + Micelio Tecnológico")

estados = load_csv('estados_venezuela.csv')
cg = load_csv('competencias_genericas.csv')
ct = load_csv('competencias_tecnicas.csv')
matriz = load_csv('matriz_ct_cg.csv')
fuentes = load_csv('fuentes.csv')
ia = load_csv('herramientas_ia.csv')

if page == "Inicio y fuentes":
    st.markdown("""
    <div class='sitra-hero'>
      <h1>SITRA-ETF</h1>
      <h3>Escuela de Talentos para el Futuro</h3>
      <p><b>Marco estratégico de apoyo a la gestión de capacidades y potencialidades</b> mediante mapa de conocimiento, talento, vocación, recursos locales, empresas, medios de vida y desarrollo tecnoeconómico-social sostenido.</p>
      <span class='badge'>Inteligentismo</span><span class='badge'>Creatopraxología</span><span class='badge'>Micelio tecnológico</span><span class='badge'>Mapa de talento</span><span class='badge'>Venezuela por estado</span><span class='badge'>Google Earth</span><span class='badge'>Medios de vida</span>
    </div>
    """, unsafe_allow_html=True)
    c1,c2,c3,c4 = st.columns(4)
    c1.metric("Estados monitoreables", len(estados))
    c2.metric("Competencias genéricas demo", len(cg))
    c3.metric("Competencias técnicas demo", len(ct))
    c4.metric("Relaciones CG-CT", len(matriz))
    st.markdown("### Qué evalúa y organiza")
    st.markdown("""
    - Capacidades de las personas: qué saben, qué quieren, qué pueden aprender y cuál es su vocación.
    - Potencial local de cada estado: pesca, turismo, aguas, ríos, playas, montañas, agricultura, ganadería, manufactura, servicios y cultura.
    - Relación **Personas + Potencial Local + Empresas** para crear rutas de autosustento tecnoeconómico y social.
    - Competencias genéricas desarrolladas **a través de prácticas técnicas reales**, no como teoría aislada.
    - Ideas creatopraxológicas: observar, idear, prototipar, practicar, medir, corregir, transferir y escalar.
    - Redes de IA, bibliometría, Zenodo, Google Earth, BiblioPangea, BiblioIntel y BiblioMap.
    """)
    st.markdown("### Fuentes y enlaces base")
    st.dataframe(fuentes, use_container_width=True, hide_index=True)
    st.markdown("<div class='info-box'><b>Uso responsable:</b> esta herramienta es una demo de apoyo metodológico y gerencial. No sustituye estudios técnicos, ambientales, legales, estadísticos o económicos formales.</div>", unsafe_allow_html=True)

elif page == "Inteligentismo y creatopraxología":
    section_header("Inteligentismo, creatopraxología y micelio tecnológico", "Marco conceptual para convertir capacidades humanas y territoriales en desarrollo local con evidencia.")
    st.markdown("""
    **Inteligentismo aplicado:** la comunidad no se mira como beneficiaria pasiva, sino como sistema vivo de inteligencias en cooperación.

    - **Inteligencia individual:** vocación, saber hacer, experiencia, deseo de aprender.
    - **Inteligencia colectiva:** organización, cooperación, redes comunitarias y empresas locales.
    - **Inteligencia artificial:** aceleración de consulta, diseño, documentación, vigilancia y decisión.
    - **Inteligencia creativa:** creación de productos, servicios, soluciones y medios de vida.

    **Creatopraxología:** disciplina práctica para transformar creatividad en acción verificable. No se queda en “ideas bonitas”; exige práctica, evidencia, beneficio, aprendizaje y escalamiento.
    """)
    st.markdown("### Ruta creatopraxológica")
    ruta = pd.DataFrame([
        ['1. Observar','Leer territorio, talento, problemas, recursos y oportunidades.'],
        ['2. Preguntar','Formular preguntas útiles: qué falta, quién sabe, qué recurso existe, qué mercado hay.'],
        ['3. Idear','Generar alternativas con talento local e IA.'],
        ['4. Prototipar','Construir piloto simple con recursos disponibles.'],
        ['5. Practicar','Ejecutar en contexto real, no en papel.'],
        ['6. Medir','Registrar datos, costos, aprendizaje, usuarios y beneficios.'],
        ['7. Corregir','Ajustar por evidencia.'],
        ['8. Transferir','Formar a otros y documentar el método.'],
        ['9. Publicar','Subir informe, datos y evidencias a nube o Zenodo.'],
        ['10. Escalar','Convertir práctica en servicio, cooperativa, alianza o emprendimiento.'],
    ], columns=['Fase','Sentido operativo'])
    st.dataframe(ruta, use_container_width=True, hide_index=True)
    st.markdown("### Micelio tecnológico territorial")
    st.markdown("""
    El modelo de micelio tecnológico entiende el territorio como red viva: nodos, raíces, intercambios y simbiosis. Como en bosques, humedales, selvas o corales, ningún actor prospera aislado: la fortaleza surge de la conectividad.

    - **Personas:** capacidades, vocaciones, oficios, aprendizaje.
    - **Territorio:** recursos naturales, memoria productiva, cultura, infraestructura.
    - **Empresas:** mercado, empleabilidad, mentoría, proveedores, demanda.
    - **Estado y universidades:** formación, transferencia, datos, reglas y soporte.
    - **Ambiente:** límite ético, material y vital del desarrollo.
    """)

elif page == "Mapa Venezuela":
    section_header("Mapa de Venezuela por estado", "Visualización demo para monitorear potencial local, capacidades y oportunidades productivas.")
    fig = px.scatter_geo(estados, lat='lat', lon='lon', hover_name='estado', hover_data=['capital','fortalezas_zona','oportunidades_productivas'], size=[12]*len(estados), projection='natural earth')
    fig.update_geos(lataxis_range=[0,13], lonaxis_range=[-74,-59], showcountries=True, countrycolor='gray', showland=True, landcolor='rgb(240,248,240)', showocean=True, oceancolor='rgb(225,245,255)')
    fig.update_layout(height=620, margin=dict(l=0,r=0,t=10,b=0))
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("### Tabla territorial")
    st.dataframe(estados, use_container_width=True, hide_index=True)
    download_df_button(estados, 'estados_venezuela_sitra_etf.csv', 'Descargar mapa territorial CSV')

elif page == "Mapas por estado y Google Earth":
    section_header("Mapas por estado y Google Earth", "Selecciona un estado, abre su ubicación base y registra mapas específicos, KML o carpetas Drive administradas por el equipo docente.")
    estado = st.selectbox("Estado", estados['estado'].tolist())
    row = estados[estados['estado']==estado].iloc[0]
    c1,c2 = st.columns([1,1])
    with c1:
        st.markdown(f"### {row['estado']} · Capital: {row['capital']}")
        st.write("**Fortalezas:**", row['fortalezas_zona'])
        st.write("**Oportunidades:**", row['oportunidades_productivas'])
        st.link_button("Abrir centro del estado en Google Earth", google_earth_link(row['lat'], row['lon']))
        st.link_button("Abrir Google Maps", f"https://www.google.com/maps/search/?api=1&query={row['lat']},{row['lon']}")
    with c2:
        fig = px.scatter_geo(pd.DataFrame([row]), lat='lat', lon='lon', hover_name='estado', size=[20], projection='natural earth')
        fig.update_geos(lataxis_range=[0,13], lonaxis_range=[-74,-59], showcountries=True, showland=True, landcolor='rgb(240,248,240)', showocean=True, oceancolor='rgb(225,245,255)')
        fig.update_layout(height=360, margin=dict(l=0,r=0,t=0,b=0))
        st.plotly_chart(fig, use_container_width=True)
    st.markdown("### Registrar mapa específico")
    with st.form('form_mapa'):
        nombre = st.text_input('Nombre del mapa o capa', placeholder='Ej. Mapa de pesca artesanal de La Guaira')
        url = st.text_input('URL Google Earth / KML / Google Drive')
        uso = st.text_area('Uso previsto', placeholder='Monitorear recursos, emprendimientos, rutas, riesgos, escuelas, empresas, etc.')
        responsable = st.text_input('Responsable')
        submitted = st.form_submit_button('Guardar mapa')
        if submitted:
            save_append_csv('mapas_territoriales.csv',[datetime.now().isoformat(timespec='seconds'), estado, nombre, url, uso, responsable])
            st.success('Mapa registrado en la base local demo.')
    mapas = load_csv('mapas_territoriales.csv')
    st.dataframe(mapas, use_container_width=True, hide_index=True)

elif page == "Mapa de conocimiento y talento":
    section_header("Mapa de conocimiento y talento", "Conecta lo que una persona sabe, quiere aprender y puede aportar con el potencial económico-social de su territorio.")
    st.markdown("""
    Este módulo ayuda a levantar un mapa vivo de capacidades. La pregunta no es solo “¿qué estudió la persona?”, sino:
    **¿qué sabe hacer?, ¿qué le gusta?, ¿qué quiere aprender?, ¿qué problema local puede resolver?, ¿con quién puede articularse?**
    """)
    c1,c2,c3 = st.columns(3)
    c1.markdown("#### Persona")
    c1.write("Saberes, oficios, experiencia, vocación, disponibilidad, sueños productivos.")
    c2.markdown("#### Zona")
    c2.write("Recursos naturales, materias primas, empresas, cultura, infraestructura y necesidades.")
    c3.markdown("#### Empresa / proyecto")
    c3.write("Demanda, formación requerida, producto, servicio, cliente y ruta de sostenibilidad.")
    st.markdown("### Competencias genéricas que se fortalecen con la práctica técnica")
    st.dataframe(cg, use_container_width=True, hide_index=True)

elif page == "Diagnóstico persona-zona-empresa":
    section_header("Diagnóstico persona-zona-empresa", "Formulario demo para construir una ruta inicial de autosustento.")
    with st.form('diagnostico'):
        nombre = st.text_input('Nombre o código de la persona/grupo')
        estado = st.selectbox('Estado', estados['estado'].tolist(), key='diag_estado')
        vocacion = st.selectbox('Vocación predominante', ['Pesca','Turismo','Agricultura','Ganadería','Manufactura','Agua y saneamiento','Energía','Comercio digital','Artesanía/cultura','Tecnología comunitaria','Otro'])
        sabe = st.text_area('¿Qué sabe hacer hoy?')
        aprender = st.text_area('¿Qué quiere aprender o mejorar?')
        recurso = st.text_area('¿Qué recurso local puede aprovechar?')
        empresa = st.text_input('Empresa, institución o aliado posible')
        submit = st.form_submit_button('Generar orientación')
    if submit:
        r = estados[estados['estado']==estado].iloc[0]
        st.markdown("### Orientación inicial")
        st.markdown(f"<div class='success-box'><b>{nombre}</b> puede iniciar una ruta de autosustento en <b>{estado}</b>, aprovechando fortalezas como: {r['fortalezas_zona']}.</div>", unsafe_allow_html=True)
        st.write('**Ruta sugerida:**')
        st.write('1. Validar vocación y capacidades actuales. 2. Seleccionar una práctica técnica mínima. 3. Formar equipo local. 4. Crear prototipo de producto/servicio. 5. Medir beneficio. 6. Conectar con empresa/aliado. 7. Publicar evidencia y escalar.')
        st.write('**Competencias genéricas a trabajar:** comunicación efectiva, trabajo en equipo, orientación a resultados, iniciativa, planificación y responsabilidad ética.')
        idea = f"Ruta {vocacion} en {estado}: convertir saberes ({sabe[:80]}) y aprendizaje deseado ({aprender[:80]}) en producto/servicio territorial con apoyo de {empresa or 'aliados locales'}."
        save_append_csv('ideas_creatopraxologicas.csv',[datetime.now().isoformat(timespec='seconds'), nombre, estado, vocacion, sabe, aprender, recurso, idea, 'Por definir', 'Autosustento y aprendizaje situado', 'Validar práctica técnica mínima'])
        st.info('Se registró una idea preliminar en el Banco de ideas.')

elif page == "Competencias CG-CT":
    section_header("Matriz Competencias Genéricas - Competencias Técnicas", "Las competencias genéricas se consolidan a través de prácticas técnicas territoriales.")
    c1,c2 = st.columns(2)
    with c1:
        filtro_ct = st.selectbox('Filtrar por competencia técnica', ['Todas'] + ct['competencia'].tolist())
    with c2:
        filtro_cg = st.selectbox('Filtrar por competencia genérica', ['Todas'] + cg['competencia'].tolist())
    df = matriz.copy()
    if filtro_ct != 'Todas': df = df[df['ct']==filtro_ct]
    if filtro_cg != 'Todas': df = df[df['cg']==filtro_cg]
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.markdown("### Competencias técnicas base")
    st.dataframe(ct, use_container_width=True, hide_index=True)

elif page == "Potencial local y medios de vida":
    section_header("Potencial local y medios de vida", "Del recurso territorial al medio de vida sostenible, sustentable y soportable.")
    estado = st.selectbox('Estado a analizar', estados['estado'].tolist(), key='pot_estado')
    row = estados[estados['estado']==estado].iloc[0]
    st.markdown(f"### {estado}")
    st.write('**Fortalezas de zona:**', row['fortalezas_zona'])
    st.write('**Oportunidades productivas:**', row['oportunidades_productivas'])
    st.markdown("### Rutas de medios de vida sugeridas")
    base_routes = pd.DataFrame([
        ['Recurso natural','Identificar recurso local aprovechable sin degradarlo','Diagnóstico de recurso + límites ambientales'],
        ['Capacidad humana','Mapear personas con saber técnico, oficio o vocación','Ficha de talento y aprendizaje'],
        ['Producto mínimo','Crear primer producto, servicio o experiencia','Prototipo operativo'],
        ['Mercado local','Validar usuario, comprador, aliado o beneficiario','Registro de demanda'],
        ['Servicio continuo','Convertir práctica en servicio periódico','Catálogo y responsables'],
        ['Empresa/cooperativa','Organizar figura productiva o alianza','Plan básico de operación'],
        ['Evidencia y difusión','Publicar aprendizajes, datos y resultados','Informe, repositorio, Zenodo o nube'],
    ], columns=['Etapa','Acción','Evidencia'])
    st.dataframe(base_routes, use_container_width=True, hide_index=True)

elif page == "Empresas y alianzas":
    section_header("Empresas, instituciones y alianzas", "Relaciona talento y potencial local con empresas existentes o nuevas iniciativas.")
    st.markdown("""
    Este módulo orienta la creación de alianzas entre personas, comunidades, empresas, universidades, instituciones públicas y organizaciones sociales.
    """)
    alianza = pd.DataFrame([
        ['Empresa local','Demanda, mercado, mentoría, insumos, compra de producción','Convenio de práctica, pasantía, formación o proveeduría'],
        ['Universidad / escuela técnica','Formación, tutores, laboratorios, datos, innovación','Proyecto de servicio comunitario o extensión'],
        ['Gobierno local','Permisos, datos territoriales, políticas, espacios, articulación','Mesa técnica territorial'],
        ['Comunidad organizada','Talento, necesidades, cultura, legitimidad, vigilancia social','Comité de talento y producción'],
        ['Cooperativas / asociaciones','Organización económica y distribución de beneficios','Plan de emprendimiento asociativo'],
        ['Ambiente','Límites, sostenibilidad, conservación y restauración','Evaluación de impacto y buenas prácticas'],
    ], columns=['Actor','Qué aporta','Instrumento sugerido'])
    st.dataframe(alianza, use_container_width=True, hide_index=True)

elif page == "Ruta de autosustento":
    section_header("Ruta de autosustento tecnoeconómico y social", "De la vocación a la productividad con evidencias y beneficios.")
    ruta = pd.DataFrame([
        ['R0','Levantamiento de talento','Encuesta de saberes, vocaciones y necesidades.','Mapa de talento inicial'],
        ['R1','Lectura territorial','Identificar recursos, empresas, problemas y oportunidades.','Mapa persona-zona-empresa'],
        ['R2','Selección de práctica técnica','Escoger práctica mínima viable por vocación.','Ficha técnica'],
        ['R3','Formación acelerada','Curso corto, práctica, seguridad, ética y calidad.','Lista de asistencia/evaluación'],
        ['R4','Prototipo productivo','Producto, servicio o experiencia piloto.','Evidencia fotográfica, costos, usuarios'],
        ['R5','Servitización','Convertir el prototipo en servicio repetible.','Catálogo de servicio'],
        ['R6','Productivización','Estandarizar, medir, documentar y escalar.','Procedimiento + indicadores'],
        ['R7','Alianza y mercado','Conectar con empresa, cliente, institución o red.','Convenio / pedido / evento'],
        ['R8','Publicación y aprendizaje','Subir informe, datos y lecciones aprendidas.','Drive/Zenodo/repositorio'],
    ], columns=['Nivel','Nombre','Descripción','Evidencia'])
    st.dataframe(ruta, use_container_width=True, hide_index=True)

elif page == "Banco de ideas":
    section_header("Banco de ideas creatopraxológicas", "Registrar ideas nacidas de talento local, recursos de la zona y oportunidades de autosustento.")
    with st.form('ideas'):
        nombre = st.text_input('Persona, equipo o comunidad')
        estado = st.selectbox('Estado', estados['estado'].tolist(), key='idea_estado')
        vocacion = st.text_input('Vocación o área')
        sabe = st.text_area('Qué saben hacer')
        aprender = st.text_area('Qué quieren aprender')
        recurso = st.text_area('Recurso local o problema a transformar')
        idea = st.text_area('Idea creatopraxológica')
        producto = st.text_input('Producto o servicio posible')
        beneficio = st.text_area('Beneficio esperado')
        paso = st.text_input('Siguiente paso verificable')
        submitted = st.form_submit_button('Guardar idea')
        if submitted:
            save_append_csv('ideas_creatopraxologicas.csv',[datetime.now().isoformat(timespec='seconds'), nombre, estado, vocacion, sabe, aprender, recurso, idea, producto, beneficio, paso])
            st.success('Idea guardada en base local demo.')
    ideas = load_csv('ideas_creatopraxologicas.csv')
    st.dataframe(ideas, use_container_width=True, hide_index=True)
    download_df_button(ideas, 'banco_ideas_sitra_etf.csv', 'Descargar banco de ideas')

elif page == "Productivización y servitización":
    section_header("Productivización y servitización", "Convertir aprendizaje y creatividad en productos, servicios y capacidades sostenidas.")
    st.markdown("""
    - **Productivización:** convertir una práctica o saber en producto repetible, documentado y medible.
    - **Servitización:** convertir una capacidad técnica en servicio útil para la comunidad, empresas o instituciones.
    - **Autosustento:** conectar producto/servicio con ingreso, ahorro, empleo, cooperación, alimentación, salud, educación o mejora local.
    """)
    modelos = pd.DataFrame([
        ['Pesca','Producto','Pescado limpio, empacado, conservado con cadena fría','Servicio de logística/cadena fría comunitaria'],
        ['Turismo','Experiencia','Ruta local, gastronomía, guía cultural','Servicio de diseño de experiencias y atención al visitante'],
        ['Agricultura','Producto','Harinas, conservas, cacao, café, frutas procesadas','Servicio de asistencia técnica y empaque'],
        ['Agua','Servicio','Punto de agua segura, mantenimiento de tanques','Monitoreo, cloración y educación sanitaria'],
        ['Manufactura','Producto','Repuestos simples, mobiliario, piezas, reparación','Taller de mantenimiento comunitario'],
        ['Comercio digital','Servicio','Catálogo digital, ventas, delivery local','Gestión de tienda y atención al cliente'],
    ], columns=['Área','Tipo','Productivización','Servitización'])
    st.dataframe(modelos, use_container_width=True, hide_index=True)

elif page == "Beneficios y métricas":
    section_header("Gestión de beneficios", "Mide el valor creado por talento, aprendizaje, productos y servicios.")
    st.markdown("### Indicadores sugeridos")
    ind = pd.DataFrame([
        ['Personas formadas','Número de ciudadanos/estudiantes formados por ruta técnica.'],
        ['Competencias consolidadas','Puntaje antes/después en competencias genéricas y técnicas.'],
        ['Ideas registradas','Ideas creatopraxológicas documentadas y priorizadas.'],
        ['Prototipos creados','Productos/servicios piloto funcionales.'],
        ['Alianzas activas','Empresas, universidades, instituciones o comunidades vinculadas.'],
        ['Ingresos/ahorros estimados','Valor económico o ahorro generado por la práctica.'],
        ['Beneficio social','Personas atendidas, servicios creados, problemas resueltos.'],
        ['Beneficio ambiental','Reducción de desperdicios, conservación, uso responsable de recursos.'],
        ['Evidencias publicadas','Informes, fotografías, datos, mapas o DOI en Zenodo.'],
    ], columns=['Indicador','Descripción'])
    st.dataframe(ind, use_container_width=True, hide_index=True)

elif page == "IA gratuita y bibliometría":
    section_header("IA gratuita, bibliometría y vigilancia tecnocientífica", "Apoyo para consultas, decisiones, aprendizaje autodirigido e investigación territorial.")
    st.dataframe(ia, use_container_width=True, hide_index=True)
    st.markdown("### Prompts rápidos")
    prompts = [
        'Actúa como asesor de medios de vida para una comunidad de [ESTADO]. Identifica oportunidades productivas basadas en [RECURSO LOCAL] y diseña una ruta de formación en 4 semanas.',
        'Ayúdame a convertir esta idea comunitaria en un producto mínimo viable: [IDEA]. Incluye materiales, costos, riesgos, aliados e indicadores.',
        'Busca tendencias científicas y tecnológicas sobre [TEMA] y propón 10 líneas de vigilancia para estudiantes y docentes.',
        'Diseña una matriz que relacione competencias genéricas con competencias técnicas para [ACTIVIDAD PRODUCTIVA].',
    ]
    for p in prompts:
        st.code(p, language='text')
    st.markdown("### Enlaces de búsqueda bibliométrica")
    tema = st.text_input('Tema de búsqueda', 'desarrollo local medios de vida talento comunitario')
    if tema:
        q = tema.replace(' ','+')
        cols=st.columns(4)
        cols[0].link_button('Google Scholar', f'https://scholar.google.com/scholar?q={q}')
        cols[1].link_button('OpenAlex', f'https://openalex.org/works?filter=title.search:{q}')
        cols[2].link_button('Semantic Scholar', f'https://www.semanticscholar.org/search?q={q}')
        cols[3].link_button('Zenodo', f'https://zenodo.org/search?q={q}')

elif page == "Repositorios y difusión":
    section_header("Repositorios, nube y difusión", "Documenta memoria viva, informes, mapas, evidencias, tesis, pasantías y aprendizajes.")
    st.markdown("""
    Recomendación operativa:
    1. Carpeta Drive por estado.
    2. Subcarpeta por municipio/comunidad.
    3. Registro de talento, mapas, ideas, evidencias y reportes.
    4. Informes consolidados con DOI en Zenodo.
    5. Difusión periódica tipo periodismo científico y tecnológico comunitario.
    """)
    repo = pd.DataFrame([
        ['Drive / nube docente','Repositorio operativo de evidencias, fotos, fichas y mapas.','Carpeta por estado y proyecto'],
        ['Zenodo','Publicación abierta de informes, datos y resultados con DOI.','Informe técnico + dataset + fotos autorizadas'],
        ['BiblioPangea','Lectura amplia de conocimiento y vigilancia bibliográfica.','Mapas conceptuales y rutas de lectura'],
        ['BiblioIntel','Apoyo inteligente a búsqueda, fichaje y síntesis.','Fichas de artículos y autores'],
        ['BiblioMap','Mapeo visual de temas, autores, instituciones y redes.','Mapa bibliométrico'],
        ['Boletín CTI local','Periodismo científico y tecnológico del territorio.','Boletín mensual'],
    ], columns=['Repositorio / canal','Uso','Producto'])
    st.dataframe(repo, use_container_width=True, hide_index=True)

elif page == "Dashboard y reportes":
    section_header("Dashboard y reportes", "Vista de control demo para gerencia docente, comunitaria o institucional.")
    ideas = load_csv('ideas_creatopraxologicas.csv')
    mapas = load_csv('mapas_territoriales.csv')
    c1,c2,c3,c4 = st.columns(4)
    c1.metric('Ideas registradas', max(0,len(ideas)))
    c2.metric('Mapas registrados', max(0,len(mapas)))
    c3.metric('Estados base', len(estados))
    c4.metric('Relaciones CG-CT', len(matriz))
    if len(ideas) > 0 and 'estado' in ideas.columns:
        count = ideas.groupby('estado').size().reset_index(name='ideas')
        fig = px.bar(count, x='estado', y='ideas', title='Ideas por estado')
        st.plotly_chart(fig, use_container_width=True)
    st.markdown('### Descargar bases')
    download_df_button(ideas, 'ideas_creatopraxologicas.csv', 'Descargar ideas')
    download_df_button(mapas, 'mapas_territoriales.csv', 'Descargar mapas registrados')
    download_df_button(matriz, 'matriz_ct_cg.csv', 'Descargar matriz CG-CT')
    st.markdown("<div class='warn-box'>Esta demo usa archivos CSV locales. Para una versión institucional se recomienda base de datos multiusuario, autenticación, control de permisos, respaldo y panel web privado.</div>", unsafe_allow_html=True)

st.markdown("---")
st.caption("SITRA-ETF v0.1 · Demo localhost · Escuela de Talentos para el Futuro · Inteligentismo + Creatopraxología + Micelio Tecnológico")
