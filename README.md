# WeatherReport CLI

## Descripción

Este es un repositorio para una aplicación de línea de comandos (CLI) que realiza consultas a la API de OpenWeatherApp para obtener información meteorológica.

## Requisitos

Antes de ejecutar la aplicación, asegúrate de tener Python instalado en tu sistema. Este proyecto utiliza un entorno virtual para gestionar las dependencias.

## Instalación

Sigue estos pasos para configurar el proyecto:

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/drFrancia/WeatherApp.git
   cd mi-nuevo-repositorio

2. **Crea y activa un entorno virtual:**
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`

3. **Instala las dependencias:**
    pip install -r requirements.txt

4. **Uso**
    Una vez que hayas instalado las dependencias, puedes ejecutar la aplicación desde la línea de comandos. Asegúrate de tener configurada tu clave de API de OpenWeatherApp en el archivo .env.
    Para ejecutar la aplicación, usa el siguiente comando:
    
    python Weather_report.py

5. **Archivo .env**
    Crea un archivo .env en la raíz del proyecto con tu clave de API. El archivo debería tener el siguiente formato:
    makefile
        API_KEY=tu_clave_de_api

6. **Contribución**
    Si deseas contribuir a este proyecto, por favor sigue las pautas de contribución y abre un pull request con tus cambios.
