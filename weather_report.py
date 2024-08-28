import argparse
import requests
from dotenv import load_dotenv
import os
import json
import csv
from io import StringIO

load_dotenv()  # Carga mi API key desde el archivo .env

def get_weather(ubicacion, api_key, unidad):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": ubicacion,
        "appid": api_key,
        "units": unidad
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Esto lanzará un error si ocurre una respuesta 4XX o 5XX
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"Un error HTTP ocurrió: {err} - Estado: {response.status_code} - Detalles: {response.text}")
    except Exception as err:
        print(f"Un error ocurrió: {err}")
    return None

def formato_txt(weather_data, unidad, detalles):
    salida = []
    salida.append(f"Temperatura: {weather_data['main']['temp']}°{'C' if unidad == 'metric' else 'F'}")
    salida.append(f"Clima: {weather_data['weather'][0]['description']}")
    if detalles:
        salida.append(f"Humedad: {weather_data['main']['humidity']}%")
        salida.append(f"Velocidad del viento: {weather_data['wind']['speed']} {'m/s' if unidad == 'metric' else 'mph'}")
    return "\n".join(salida)

def formato_csv(weather_data, unidad, detalles):
    salida = StringIO()
    nom_campo = ['Temperatura', 'Clima']
    if detalles:
        nom_campo.extend(['Humedad', 'Velocidad del viento'])
    
    writer = csv.DictWriter(salida, fieldnames=nom_campo)
    writer.writeheader()
    
    row = {
        'Temperatura': f"{weather_data['main']['temp']}°{'C' if unidad == 'metric' else 'F'}",
        'Clima': weather_data['weather'][0]['description']
    }
    if detalles:
        row['Humedad'] = f"{weather_data['main']['humidity']}%"
        row['Velocidad del viento'] = f"{weather_data['wind']['speed']} {'m/s' if unidad == 'metric' else 'mph'}"
    
    writer.writerow(row)
    return salida.getvalue().strip()

def main():
    parser = argparse.ArgumentParser(description="Informe meteorológico CLI")
    parser.add_argument("ubicacion", type=str, help="Código de ciudad y país (ej.: Londres, Reino Unido)")
    parser.add_argument("--unidad", type=str, choices=["metric", "imperial"], default="metric", help="Unidades de medida (metric o imperial)")
    parser.add_argument("--detalles", action="store_true", help="Mostrar información meteorológica detallada")
    parser.add_argument("--salida-format", choices=['json', 'text', 'csv'], default='text', help="Formato de salida: json, text, csv")
    args = parser.parse_args()

    api_key = os.getenv("API_KEY")
    if not api_key:
        print("API key no encontrada. Configúrala en .env.")
        return

    weather_data = get_weather(args.ubicacion, api_key, args.unidad)

    if weather_data:
        if weather_data.get('cod') == '404':
            print(f"Ubicación '{args.ubicacion}' no encontrada.")
            return
        
        if args.salida_format == 'json':
            print(json.dumps(weather_data, indent=4))
        elif args.salida_format == 'text':
            print(formato_txt(weather_data, args.unidad, args.detalles))
        elif args.salida_format == 'csv':
            print(formato_csv(weather_data, args.unidad, args.detalles))

if __name__ == "__main__":
    main()
