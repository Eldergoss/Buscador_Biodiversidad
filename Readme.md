# Buscador de Biodiversidad 🧬 (GBIF + Wikipedia)

Una aplicación web interactiva desarrollada en **Python** y **Streamlit** que permite a investigadores, estudiantes y entusiastas de la naturaleza buscar cualquier especie por su nombre científico. La herramienta unifica datos taxonómicos oficiales, mapas de distribución global y resúmenes enciclopédicos con imágenes en una sola interfaz limpia y organizada en tres columnas.

## 🚀 Características

* **Búsqueda Global:** Consulta la base de datos de **GBIF Backbone Taxonomy** en tiempo real.
* **Mapas de Distribución:** Genera de forma dinámica mapas con los puntos de avistamiento registrados por la comunidad científica mundial (`pygbif.maps`).
* **Enriquecimiento con Wikipedia:** Consume la API REST de Wikipedia para extraer resúmenes biográficos (extractos) y fotografías de la especie de manera automatizada.
* **Arquitectura Modular:** Estructurado mediante Programación Orientada a Objetos (POO) para separar la lógica de la interfaz de la extracción de datos en módulos independientes.

## 🛠️ Estructura del Proyecto

El proyecto está organizado en carpetas independientes para segmentar las responsabilidades de cada API:

```text
├── Main_Gui.py              # Aplicación principal e interfaz de Streamlit
├── modulo_pygbif/           # Módulo encargado de la conexión con GBIF
│   └── objeto.py            # Clase Ficha: Modelado de datos taxonómicos
└── modulo_wikimedia/        # Módulo encargado de la conexión con Wikipedia
    └── prueba_wiki.py       # Clase Wikificha: Modelado de datos e imágenes
