from collections import Counter

def analizar_texto(texto):
    # Convertir el texto a minúsculas y eliminar signos de puntuación
    palabras = [palabra.strip(".,!?;:").lower() for palabra in texto.split()]
    
    # Número total de palabras
    total_palabras = len(palabras)
    
    # Cantidad de palabras únicas
    palabras_unicas = set(palabras)
    cantidad_unicas = len(palabras_unicas)
    
    # Frecuencia de cada palabra
    frecuencia_palabras = Counter(palabras)
    
    # Palabra más frecuente
    palabra_mas_frecuente, max_frecuencia = frecuencia_palabras.most_common(1)[0]
    
    # Mostrar resultados
    print("Resumen del análisis del texto:")
    print(f"- Número total de palabras: {total_palabras}")
    print(f"- Cantidad de palabras únicas: {cantidad_unicas}")
    print("- Frecuencia de cada palabra:")
    for palabra, frecuencia in frecuencia_palabras.items():
        print(f"  {palabra}: {frecuencia}")
    print(f"- La palabra más frecuente es '{palabra_mas_frecuente}' con {max_frecuencia} apariciones.")

# Solicitar entrada al usuario
texto_usuario = input("Ingrese un texto para analizar: ")
analizar_texto(texto_usuario)
