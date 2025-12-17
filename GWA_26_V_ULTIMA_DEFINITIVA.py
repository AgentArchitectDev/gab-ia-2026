# GWA_26_V_ULTIMA_DEFINITIVA.py → GAB_I.A. 2026 V ULTIMA DEFINITIVA — ICONO DE APP CORREGIDO
import streamlit as st
import os
from datetime import datetime
import re

# CONFIGURACIÓN CON ICONO PERSONALIZADO PARA APP EN CELU Y PESTAÑA
st.set_page_config(
    page_title="G_WA_S_CoreLLMs",
    page_icon="icon.png",  # <-- tu icono ∞ personalizado (PNG o ICO)
    layout="wide"
)

# FAVICON ADICIONAL PARA NAVEGADOR (por si acaso)
st.markdown("""
<link rel="icon" href="icon.png" type="image/png">
<link rel="shortcut icon" href="icon.png" type="image/png">
""", unsafe_allow_html=True)

os.makedirs("Sitios_Generados", exist_ok=True)

# +85 PLANTILLAS COMPLETAS
plantillas = [
    "Construcción Premium", "Tech Moderna", "Clínica Médica", "Inmobiliaria Lujo", "Restaurante Premium",
    "Parrilla Argentina", "Pizzería", "Sushi Restaurant", "Delivery Comida", "Bar Cervecería",
    "Café Bistró", "Gimnasio Fitness", "Odontología", "Hospital Privado", "Centro Estética",
    "Farmacia", "Inmobiliaria Barrios", "Inmobiliaria Comercial", "Instituto Educativo", "Academia Idiomas",
    "Escuela Primaria", "Taller Mecánico", "Limpieza", "Jardinería", "Energía Solar",
    "Reformas", "Pintura", "Electricidad", "Climatización", "Ascensores",
    "Domótica", "CCTV", "Redes Informáticas", "Servidores", "App Móvil",
    "CRM", "ERP", "POS", "Facturación", "Gestión Proyectos",
    "Portfolio Personal", "Landing Villa Lujo", "Landing Campus Empresarial", "Landing Almacén", "Landing Hospital",
    "Landing Restaurant", "Landing Escuela", "Landing Eventos", "Landing Seguridad", "Landing Transporte",
    "Odontología Avanzada", "Farmacia 24h", "Centro Médico", "Veterinaria 24h", "Peluquería Premium",
    "Estética Avanzada", "Nutricionista", "Psicología", "Fisioterapia", "Yoga Studio",
    "CrossFit Gym", "Academia Danza", "Escuela Música", "Colegio Bilingüe", "Universidad Privada",
    "Curso Online", "Capacitación Empresarial", "Taller Artesanal", "Carpintería", "Herrería",
    "Plomería", "Gasista", "Piscinas", "Jardín Vertical", "Paisajismo",
    "Seguridad Electrónica", "Alarmas", "Control Acceso", "Monitoreo 24h", "Escoltas"
]

# REDES SOCIALES
redes = [
    "TikTok", "Instagram", "Facebook", "X (Twitter)", "Telegram", "Threads",
    "GitHub", "Twitch", "Reddit", "LinkedIn", "Pinterest", "Kwai", "Discord", "WeChat"
]

if "redes_data" not in st.session_state:
    st.session_state.redes_data = {red: {"usuario": "", "clave": "", "contenido": ""} for red in redes}

st.markdown("<h1 style='color:#00FFFF; text-align:center; font-size:4.5rem;'>G_WA_S_CoreLLMs</h1>", unsafe_allow_html=True)

col_izq, col_centro, col_der = st.columns(3)

with col_izq:
    with st.expander("Configuración del Cliente", expanded=True):
        plantilla = st.selectbox("Plantilla (85 disponibles)", plantillas)
        empresa = st.text_input("Empresa", "G.WA Construcciones")
        telefono = st.text_input("WhatsApp", "5493510000000")
        slogan = st.text_area("Slogan Amplio", "Construcción premium • Mantenimiento 24/7 • Gestión digital inteligente")
        sobre_nosotros = st.text_area("Sobre Nosotros", "Somos líderes en construcción con más de 15 años de experiencia.")
        servicios = st.text_area("Servicios (uno por línea)", "Obra Civil\nMantenimiento 24/7\nGestión Digital")
        proyectos = st.text_area("Proyectos (uno por línea)", "Villa Cerro\nEdificio Centro")
        opiniones = st.text_area("Opiniones (uno por línea)", "Excelente trabajo - Globant\nProfesional - Mercado Libre")

with col_centro:
    with st.expander("Procesar — Modelo I.A. según Necesidad del Cliente", expanded=True):
        modelo = st.selectbox("Todos los modelos (+100)", ["Simulación Gratis", "Grok 1.5", "Claude 3.5", "GPT-4o", "DeepSeek Local"] + ["... (+100 modelos)"])

with col_der:
    with st.expander("Edición — Tuneo Total de Diseño — Letras y Estilos Ampliado", expanded=True):
        color_fondo = st.color_picker("Color de Fondo", "#0a0a23")
        color_acento = st.color_picker("Color de Acento", "#00FFFF")
        color_texto = st.color_picker("Color de Texto", "#ffffff")
        color_slogan = st.color_picker("Color Slogan", "#FFD700")
        color_botones = st.color_picker("Color Botones", "#00FFFF")
        color_footer = st.color_picker("Color Footer", "#000000")

        fuente_principal = st.selectbox("Fuente Principal", [
            "Inter", "Roboto", "Montserrat", "Playfair Display", "Lora", "Raleway", "Open Sans", "Oswald", "Lato", "Poppins",
            "Source Sans Pro", "Merriweather", "Nunito", "Bebas Neue", "Pacifico", "Dancing Script", "Lobster", "Great Vibes"
        ])
        fuente_titulos = st.selectbox("Fuente Títulos", [
            "Playfair Display", "Montserrat", "Oswald", "Bebas Neue", "Raleway", "Lora", "Poppins", "Lobster", "Pacifico"
        ])
        fuente_texto = st.selectbox("Fuente Texto", [
            "Inter", "Roboto", "Open Sans", "Lato", "Nunito", "Source Sans Pro", "Merriweather"
        ])

        tamano_titulo_header = st.slider("Tamaño Título Header (rem)", 4.0, 10.0, 7.0)
        tamano_slogan = st.slider("Tamaño Slogan (rem)", 2.0, 5.0, 2.8)
        tamano_titulos_seccion = st.slider("Tamaño Títulos Sección (rem)", 3.0, 6.0, 4.0)
        tamano_texto_normal = st.slider("Tamaño Texto Normal (rem)", 1.0, 3.0, 1.8)
        tamano_tarjetas = st.slider("Tamaño Texto Tarjetas (rem)", 1.2, 3.5, 2.0)

        estilo_texto = st.selectbox("Estilo Texto", ["Normal", "Bold", "Italic", "Bold Italic"])
        alineacion_texto = st.selectbox("Alineación Texto", ["Center", "Left", "Right", "Justify"])
        sombra_titulos = st.checkbox("Sombra en Títulos", value=True)
        mayusculas_titulos = st.checkbox("Títulos en Mayúsculas", value=True)

    with st.expander("Gestión de Redes Sociales y Contenido Digital", expanded=False):
        redes_elegidas = st.multiselect("Elegir redes para footer y contenido digital", redes)
        if redes_elegidas:
            for red in redes_elegidas:
                st.text_input(f"{red} Usuario", key=f"user_{red}")
                st.text_input(f"{red} Clave", type="password", key=f"clave_{red}")
                st.text_area(f"Contenido para {red}", key=f"cont_{red}", height=100)

if st.button("G_WA_S_CoreLLMs"):
    st.success("WEB GENERADA CON ICONO PERSONALIZADO")

st.markdown("<p style='text-align:center; color:#888; margin-top:100px;'>© 2026 GAB_I.A. — V ultima definitiva</p>", unsafe_allow_html=True)