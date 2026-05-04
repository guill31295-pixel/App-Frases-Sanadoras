import streamlit as st
import random
import base64 # Librería necesaria para el truco de la imagen

# Configuración de la página
st.set_page_config(
    page_title="Frases Sanadoras",
    page_icon="✨",
    layout="wide"
)

# --- FUNCIÓN TÉCNICA: Cargar imagen como Base64 ---
# Esto permite que la imagen se inyecte directamente en el CSS.
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# --- INTENTAR CARGAR LA IMAGEN ---
# Reemplaza 'fondo_constelaciones.jpg' con el nombre exacto de tu archivo
import csv

nombre_imagen = r"../imagenes/fondo_constelaciones.JPG"
csv.path = r"C:\Users\guill\OneDrive\Documents\App Frases Sanadoras\imagenes\fondo_constelaciones.jpg.jpeg"

try:
    img_base64 = get_base64_image(nombre_imagen)
    # Definimos el CSS usando la imagen cargada
    css_con_imagen = f"""
        background-image: url("data:image/jpg;base64,{img_base64}");
        background-size: 90% 90%;
        background-position: center;
        background-attachment: fixed; /* Esto hace que el fondo no se mueva */
        background-color: rgba(0.3, 0.3, 0.3, 0.3); /* Capa de color para oscurecer el fondo */
    """
except FileNotFoundError:
    # Si no encuentra la imagen, usa un fondo púrpura sólido como respaldo
    st.warning(f"No se encontró la imagen '{nombre_imagen}'. Usando fondo de respaldo.")
    css_con_imagen = "background-color: #f0fcf9;"


# --- CSS PERSONALIZADO ACTUALIZADO (El "truco" para el diseño) ---
st.markdown(f"""
<style>
    /* 1. Fondo Dinámico con Imagen */
    .stApp {{
        {css_con_imagen}
        color: #FDF5E6;
    }}

    /* 2. Efecto de "Vidrio" (Glassmorphism) con la imagen de fondo */
    div.stVerticalBlock {{
        background: rgba(0, 0, 0, 0.15); /* Fondo más oscuro y translúcido */
        padding: 20 px;
        border-radius: 20px;
        border: 1px solid rgba(50, 50, 50, 0.10);
        backdrop-filter: blur(5px); /* Desenfoque más fuerte */
        box-shadow: 0 10px 40px 0 rgba(0, 0, 0, 0.4);
    }}
    /* --- EFECTO ENREDADERA (Decoración de esquinas) --- */
    .stApp::before {{
        content: "";
        position: fixed;
        top: 0; left: 0;
        width: 200px; height: 200px;
        background: radial-gradient(circle at top left, rgba(76, 175, 80, 0.15), transparent 30%);
        pointer-events: none;
        z-index: 0;
    }}
    /* 3. Título con degradado brillante */
    .titulo-principal {{
        background: linear-gradient(to right, #ffca28, #ffeb3b, #ffca28);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: auto;
        font-size: 3.5rem !important;
        font-weight: 700 !important;
        text-shadow: 0 0 70px rgba(255, 202, 40, 0.8);
        margin-bottom: -10px;
    }}

    /* 4. Subtítulo (Vibrante) */
    .subtitulo {{
        text-align: center;
        color: #e3f2fd !important;
        font-size: 1.3rem;
        margin-bottom: 2rem;
        font-weight: 500;
    }}

    /* 5. Botón con animación de latido */
    .stButton>button {{
        background: linear-gradient(135deg, #ffca28, #f57c00);
        color: #000;
        border: none;
        padding: 15px 45px;
        font-size: 1.1rem;
        font-weight: bold;
        border-radius: 50px;
        transition: all 0.4s ease;
        box-shadow: 0 4px 20px rgba(255, 202, 40, 0.5);
        display: block;
        margin: 0 auto;
    }}
    
    .stButton>button:hover {{
        transform: scale(1.1);
        box-shadow: 0 0 30px rgba(255, 202, 40, 0.9);
        background: #fff;
    }}

    /* 6. Frase con estilo luminoso y Bold Dorado solicitado */
    .stAlert {{
        background: rgba(0, 0, 0, 0.1) !important;
        border: 2px solid #ffca28 !important;
        text-align: center !important;
        border-radius: 20px !important;
        animation: glow 2.5s infinite alternate;
        padding: 25px !important;
    }}

    /* Estilo para las letras de la frase (Bold y Dorado) */
    .stAlert p {{
        color: #ffca28 !important;
        font-weight: 800 !important;
        font-size: 1.8rem !important;
        text-shadow: 0 0 15px rgba(255, 202, 40, 0.8);
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }}

    @keyframes glow {{
        from {{ box-shadow: 0 0 10px rgba(255, 202, 40, 0.6); }}
        to {{ box-shadow: 0 0 40px rgba(255, 202, 40, 1.0); }}
    }}
</style>
""", unsafe_allow_html=True)
# --- FIN DEL CSS ---


import streamlit as st
import random

# --- Lógica de Estado (Esto debe ir antes de que se dibuje nada) ---
if "frase_obtenida" not in st.session_state:
    st.session_state.frase_obtenida = None

col1, col2, col3 = st.columns([1, 2, 1])    

with col2:
    st.markdown('<p class="titulo-principal">✨ Frases Sanadoras</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitulo">Presiona el botón para recibir tu frase sanadora del día.</p>', unsafe_allow_html=True)

    frases = [
        "Sí a todo como es.",
    "Tomo la vida de ti, al precio que te costó y que me cuesta.",
    "Te miro y te reconozco.",
    "Ahora te dejo con tu destino.",
    "Tú eres el grande, yo soy el pequeño.",
    "Gracias por darme la vida.",
    "Asiento a todo.",
    "Te libero de mis expectativas.",
    "Te doy un lugar en mi corazón.",
    "Lo que pasó, pasó.",
    "Por favor, mírame con buenos ojos.",
    "Tomo lo que me das y lo que no, lo dejo contigo.",
    "Yo soy el hijo y tú eres el padre.",
    "Ahora veo cuánto has sufrido por mí.",
    "Elijo la vida, a pesar de todo.",
    "Honro tu destino y el mío.",
    "Me retiro de tu carga.",
    "Te veo.",
    "Estoy aquí gracias a ti.",
    "Todo está bien ahora.",  
    ]

    # Lógica: Solo mostramos el botón si NO se ha obtenido frase aún
    if st.session_state.frase_obtenida is None:
        if st.button("Obtener Frase"):
            # Guardamos la frase en el "estado" de la sesión
            st.session_state.frase_obtenida = random.choice(frases)
            # Recargamos la app para que el botón desaparezca y aparezca la frase
            st.rerun()
    else:
        # Si ya existe una frase en el estado, mostramos el resultado
        st.success(st.session_state.frase_obtenida)
        