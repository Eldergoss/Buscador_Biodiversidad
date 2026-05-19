import requests
import streamlit as st
import pygbif
from pygbif import species, maps

# Importamos tus clases desde sus módulos independientes
from modulo_pygbif.objeto import Ficha
from modulo_wikimedia.prueba_wiki import Wikificha

# =====================================================================
# 1. CONFIGURACIÓN DE LA PÁGINA
# =====================================================================
st.set_page_config(
    page_title="Buscador de Biodiversidad",
    page_icon="🐆",
    layout="wide"  # Cambiado a 'wide' para que las 3 columnas tengan buen espacio
)

st.title("Buscador de Biodiversidad (GBIF + Wikipedia) 🧬")
st.write("Inserta el nombre científico de una especie para obtener su taxonomía, mapa de distribución y datos biográficos.")

# =====================================================================
# 2. INTERFAZ DE USUARIO (Caja de entrada)
# =====================================================================
nombre_buscado = st.text_input("Escribe el Nombre Científico:", placeholder="Ej. Panthera pardus")

# =====================================================================
# 3. LÓGICA DE EJECUCIÓN
# =====================================================================
if nombre_buscado:
    with st.spinner("Consultando servidores globales..."):
        try:
            # A. Consultar a la API de GBIF Backbone
            especie_data = species.name_backbone(scientificName=nombre_buscado)
            #---------- Logica GBIF--------

            # B. Instanciar tu clase Ficha con los datos recibidos
            aux = Ficha(especie_data)

            # --- LÓGICA DE WIKIPEDIA ---
            # Limpiamos el string de entrada reemplazando espacios por guiones bajos para la URL
            nombre_url = nombre_buscado.replace(' ', '_')
            url = f"https://es.wikipedia.org/api/rest_v1/page/summary/{nombre_url}"

            headers = {
                'User-Agent': 'BetaTaxonomiaBot/1.0 (david@ejemplo.com)'
            }

            response = requests.get(url, headers=headers)
            responsive = response.json()

            # Inicializamos Wikificha con el JSON de Wikipedia
            aux2 = Wikificha(responsive)

            # Validamos que el taxón exista en los registros de GBIF
            if aux.Idtaxon():

                # C. Creamos tres columnas visuales automáticas perfectamente alineadas
                col1, col2, col3 = st.columns(3)

                # --- Columna 1: Datos de Texto (GBIF) ---
                with col1:
                    st.subheader("Taxonomía")
                    st.markdown(f"**Nombre:** *{aux.nombre()}*")
                    st.markdown(f"**Reino:** {aux.reino()}")
                    st.markdown(f"**Clase:** {aux.orden()}")
                    st.markdown(f"**Orden:** {aux.familia()}")
                    st.markdown(f"**Clave Taxonómica:** `{aux.Idtaxon()}`")

                # --- Columna 2: Mapa de Distribución (GBIF Maps) ---
                with col2:
                    st.subheader("Distribución")

                    out = maps.map(taxonKey=aux.Idtaxon())

                    # Renderizado directo del objeto Matplotlib de pygbif
                    if hasattr(out.img, 'figure'):
                        st.pyplot(out.img.figure)
                    else:
                        st.pyplot(out.img)

                # --- Columna 3: Información e Imagen (Wikipedia) ---
                with col3:
                    st.subheader("Información General")

                    # Extraemos la URL de la foto usando tu método .imagen()
                    url_foto = aux2.imagen()

                    # Si tu método encuentra una foto válida, la dibuja
                    if url_foto and url_foto != "Sin imagen":
                        st.image(url_foto, caption=f"Fotografía de {aux.nombre()}", use_container_width=True)
                    else:
                        st.info("Especie sin fotografía en Wikimedia.")

                    # Agregamos una línea divisoria y pintamos el extracto con tu método .nombre()
                    st.markdown("---")
                    st.write(aux2.nombre())

            else:
                st.warning(f"No se encontraron registros exactos para '{nombre_buscado}'. Revisa la ortografía.")

        except Exception as e:
            st.error(f"Ocurrió un error al procesar la solicitud: {e}")
