
import requests
import socket

# URL base de la API
API_BASE = "https://restcountries.com/v3.1/region/"

# Mapeo de nombres de continentes en español a los usados por la API
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
    """Verifica si hay conexión a internet."""
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False

def obtener_paises_por_continente(continente):
    """Solicita los países del continente desde la API."""
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

def limpiar_datos_paises(paises):
    """Extrae nombre, capital, población, idioma y divisa de cada país."""
    datos_limpios = []
    for pais in paises:
        nombre = pais.get("name", {}).get("common", "Desconocido")
        capital = ", ".join(pais.get("capital", ["Sin capital"]))
        poblacion = pais.get("population", 0)
        poblacion_formateada = f"{poblacion:,}".replace(",", ".")  # Estilo español

        # Idioma principal
        idiomas = pais.get("languages", {})
        idioma_principal = list(idiomas.values())[0] if idiomas else "Desconocido"

        # Divisa principal
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
            "divisa": divisa
        })
    return datos_limpios

def mostrar_info_continente():
    """Función principal: muestra los países por continente."""
    if not verificar_conexion():
        print(" Error: No hay conexión a Internet.")
        print("Por favor, verifica tu conexión y vuelve a intentarlo.")
        return

    print("\n--- Explorador de Países por Continente ---")
    print("Continentes disponibles:")
    print("- África\n- América\n- Antártida\n- Asia\n- Europa\n- Oceanía")

    continente_usuario = input("\nIngresa el nombre de un continente: ").strip().lower()

    if continente_usuario not in MAPEO_CONTINENTES:
        print(f"\n '{continente_usuario}' no es un continente reconocido.")
        print("Prueba con: África, América, Asia, Europa, Oceanía o Antártida")
        return

    paises = obtener_paises_por_continente(continente_usuario)
    
    if paises:
        paises_limpios = limpiar_datos_paises(paises)
        print(f"\n En {continente_usuario.capitalize()} hay {len(paises_limpios)} países/territorios:")
        print("\n Lista con sus detalles:")

        for i, pais in enumerate(sorted(paises_limpios, key=lambda x: x['nombre']), 1):
            print(f"{i}. {pais['nombre']}")
            print(f"   Capital   : {pais['capital']}")
            print(f"   Población : {pais['poblacion']}")
            print(f"   Idioma    : {pais['idioma']}")
            print(f"   Divisa    : {pais['divisa']}\n")

        print(f"Total: {len(paises_limpios)} entidades en {continente_usuario.capitalize()}")
    else:
        print(f"\n No se encontraron países para '{continente_usuario}' o el continente no existe.")
        print("Asegúrate de escribirlo correctamente.")

if __name__ == "__main__":
    mostrar_info_continente()
