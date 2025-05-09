import requests
import socket
import csv

API_BASE = "https://restcountries.com/v3.1/region/"

MAPEO_CONTINENTES = {
    "africa": "africa",
    "áfrica": "africa",
    "america": "americas",
    "américa": "americas",
    "antartida": "antarctic",
    "antártida": "antarctic",
    "asia": "asia",
    "europa": "europe",
    "oceania": "oceania",
    "oceanía": "oceania"
}

def verificar_conexion():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False

def obtener_paises_por_continente(continente):
    continente_api = MAPEO_CONTINENTES.get(continente.lower())
    if not continente_api:
        return None

    url = f"{API_BASE}{continente_api}"
    try:
        respuesta = requests.get(url, timeout=10)
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.exceptions.RequestException:
        return None

def limpiar_datos_paises(paises, continente):
    datos_limpios = []
    for pais in paises:
        nombre = pais.get("name", {}).get("common", "Desconocido")
        capital = ", ".join(pais.get("capital", ["Sin capital"]))
        poblacion = pais.get("population", 0)
        poblacion_formateada = f"{poblacion:,}".replace(",", ".")
        idiomas = pais.get("languages", {})
        idioma_principal = list(idiomas.values())[0] if idiomas else "Desconocido"
        divisas = pais.get("currencies", {})
        if divisas:
            codigo_divisa = list(divisas.keys())[0]
            info_divisa = divisas[codigo_divisa]
            nombre_divisa = info_divisa.get("name", "Desconocida")
            divisa = f"{nombre_divisa} ({codigo_divisa})"
        else:
            divisa = "Desconocida"
        datos_limpios.append({
            "nombre": nombre,
            "capital": capital,
            "poblacion": poblacion_formateada,
            "idioma": idioma_principal,
            "divisa": divisa,
            "continente": continente.capitalize()
        })
    return datos_limpios

def guardar_en_csv(nombre_archivo, datos):
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
        campos = ["nombre", "capital", "poblacion", "idioma", "divisa", "continente"]
        writer = csv.DictWriter(archivo, fieldnames=campos)
        writer.writeheader()
        for fila in datos:
            writer.writerow(fila)

def mostrar_info_continente():
    if not verificar_conexion():
        print("Error: No hay conexión a Internet.")
        return

    print("\n--- Explorador de Países por Continente ---")
    print("Continentes disponibles:")
    print("- África\n- América\n- Antártida\n- Asia\n- Europa\n- Oceanía")

    continente_usuario = input("\nIngresa el nombre de un continente: ").strip().lower()

    if continente_usuario not in MAPEO_CONTINENTES:
        print(f"\n'{continente_usuario}' no es un continente válido.")
        return

    paises = obtener_paises_por_continente(continente_usuario)

    if paises:
        paises_limpios = limpiar_datos_paises(paises, continente_usuario)
        print(f"\nEn {continente_usuario.capitalize()} hay {len(paises_limpios)} países/territorios:")
        for i, pais in enumerate(sorted(paises_limpios, key=lambda x: x['nombre']), 1):
            print(f"{i}. {pais['nombre']} - Capital: {pais['capital']}")

        nombre_csv = f"{continente_usuario}_paises.csv"
        guardar_en_csv(nombre_csv, paises_limpios)
        print(f"\n✅ Archivo CSV generado: {nombre_csv}")
    else:
        print("No se pudo obtener la información del continente.")

if __name__ == "__main__":
    mostrar_info_continente()