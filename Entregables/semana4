import csv
import re
import numpy as np
import statistics as stats
import pandas as pd
import os
import matplotlib.pyplot as plt

# Lectura y validación de datos del archivo CSV
def leer_y_validar_csv(nombre_archivo):
    datos_procesados = []
    errores = 0

    regex_texto = r"^[\wÁÉÍÓÚÑáéíóúñ\s\(\)\-\,\.'’]+$"
    regex_divisa = r"^[\wÁÉÍÓÚÑáéíóúñ\s\(\)\-\,\.\$€¥£’ʻöđ]*$"
    regex_poblacion = r'^\d{1,3}(\.\d{3})*$'

    try:
        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            encabezados_esperados = {"nombre", "capital", "poblacion", "idioma", "divisa", "continente"}

            if set(lector.fieldnames) != encabezados_esperados:
                crear_csv_corregido(nombre_archivo)
                return []

            for i, fila in enumerate(lector, 1):
                nombre = fila['nombre'].strip()
                capital = fila['capital'].strip()
                poblacion_str = fila['poblacion'].strip()
                idioma = fila['idioma'].strip()
                divisa = fila['divisa'].strip()
                continente = fila['continente'].strip()

                errores_en_fila = False

                if not re.match(regex_texto, nombre):
                    print(f"Fila {i}: nombre inválido → '{nombre}'")
                    errores_en_fila = True
                if not re.match(regex_texto, capital):
                    print(f"Fila {i}: capital inválida → '{capital}'")
                    errores_en_fila = True
                if not re.match(regex_poblacion, poblacion_str):
                    print(f"Fila {i}: población inválida → '{poblacion_str}'")
                    errores_en_fila = True
                if not re.match(regex_texto, idioma):
                    print(f"Fila {i}: idioma inválido → '{idioma}'")
                    errores_en_fila = True
                if not re.match(regex_divisa, divisa):
                    print(f"Fila {i}: divisa inválida → '{divisa}'")
                    errores_en_fila = True
                if not re.match(regex_texto, continente):
                    print(f"Fila {i}: continente inválido → '{continente}'")
                    errores_en_fila = True

                if not errores_en_fila:
                    poblacion_num = int(poblacion_str.replace('.', ''))
                    datos_procesados.append({
                        "nombre": nombre,
                        "capital": capital,
                        "poblacion": poblacion_num,
                        "idioma": idioma,
                        "divisa": divisa,
                        "continente": continente
                    })
                else:
                    errores += 1

        if errores > 0:
            print(f"\nSe encontraron {errores} errores. Corrige el archivo antes de continuar.")
            return []
        else:
            return datos_procesados

    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
        return []
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return []

# Validación antes de visualización
def validar_datos_para_visualizacion(datos):
    errores_encontrados = False

    for i, pais in enumerate(datos, 1):
        if not isinstance(pais['nombre'], str) or pais['nombre'] == "":
            print(f"[Validación] Fila {i}: 'nombre' inválido.")
            errores_encontrados = True
        if not isinstance(pais['capital'], str) or pais['capital'] == "":
            print(f"[Validación] Fila {i}: 'capital' inválida.")
            errores_encontrados = True
        if not isinstance(pais['poblacion'], int) or pais['poblacion'] <= 0:
            print(f"[Validación] Fila {i}: 'población' inválida: {pais['poblacion']}")
            errores_encontrados = True
        if not isinstance(pais['idioma'], str) or pais['idioma'] == "":
            print(f"[Validación] Fila {i}: 'idioma' inválido.")
            errores_encontrados = True
        if not isinstance(pais['divisa'], str) or pais['divisa'] == "":
            print(f"[Validación] Fila {i}: 'divisa' inválida.")
            errores_encontrados = True
        if not isinstance(pais['continente'], str) or pais['continente'] == "":
            print(f"[Validación] Fila {i}: 'continente' inválido.")
            errores_encontrados = True

    if errores_encontrados:
        print("\nSe encontraron errores en los datos. Corrige antes de generar gráficas o análisis.")
        return False
    else:
        print("Datos verificados: listos para visualización.\n")
        return True

# Análisis estadístico de población
def analizar_datos_poblacion(datos):
    poblaciones = [pais["poblacion"] for pais in datos]
    array = np.array(poblaciones)

    print("\nAnálisis Estadístico de la Población:\n")
    print(f"Cantidad de países: {len(poblaciones)}")
    print(f"Media: {np.mean(array):,.0f}")
    print(f"Mediana: {np.median(array):,.0f}")

    try:
        moda = stats.mode(poblaciones)
        print(f"Moda: {moda:,}")
    except stats.StatisticsError:
        print("Moda: No se pudo calcular (posiblemente no hay valores repetidos)")

    print(f"Desviación estándar: {np.std(array):,.2f}")
    print(f"Varianza: {np.var(array):,.2f}")
    print(f"Valor mínimo: {np.min(array):,}")
    print(f"Valor máximo: {np.max(array):,}")
    print(f"Rango: {np.max(array) - np.min(array):,}")
    print(f"Percentil 25: {np.percentile(array, 25):,.0f}")
    print(f"Percentil 75: {np.percentile(array, 75):,.0f}")

    Q1 = np.percentile(array, 25)
    Q3 = np.percentile(array, 75)
    IQR = Q3 - Q1
    outliers = array[(array < Q1 - 1.5 * IQR) | (array > Q3 + 1.5 * IQR)]
    print(f"Outliers detectados (poblaciones extremas): {outliers if len(outliers) > 0 else 'Ninguno'}")

# Exportación a Excel por continente
def exportar_a_excel_por_continente(datos, continente_deseado):
    datos_filtrados = [pais for pais in datos if pais["continente"].lower() == continente_deseado.lower()]
    if not datos_filtrados:
        print(f"No se encontraron datos para el continente '{continente_deseado}'.")
        return
    df = pd.DataFrame(datos_filtrados)
    nombre_archivo = f"{continente_deseado.lower()}_paises.xlsx"
    df.to_excel(nombre_archivo, index=False)
    print(f"\nArchivo Excel generado: '{nombre_archivo}'")

# Crear CSV vacío si los encabezados están mal
def crear_csv_corregido(nombre_original):
    nuevo_nombre = "corregido_" + nombre_original
    encabezados = ['nombre', 'continente', 'capital', 'divisa', 'idioma', 'poblacion']
    with open(nuevo_nombre, mode='w', encoding='utf-8', newline='') as archivo:
        writer = csv.DictWriter(archivo, fieldnames=encabezados)
        writer.writeheader()
    print(f"\nEncabezados incorrectos. Se creó un nuevo archivo vacío con encabezados correctos: '{nuevo_nombre}'")

# Gráficas de población
def graficar_datos_poblacion(datos):
    nombres = [pais["nombre"] for pais in datos]
    poblaciones = [pais["poblacion"] for pais in datos]

    nombres, poblaciones = zip(*sorted(zip(nombres, poblaciones), key=lambda x: x[1], reverse=True))
    nombres = nombres[:10]
    poblaciones = poblaciones[:10]

    plt.figure(figsize=(14, 10))

    plt.subplot(2, 2, 1)
    plt.plot(nombres, poblaciones, marker='o', color='blue')
    plt.title('Gráfico de Líneas - Población')
    plt.xticks(rotation=45)
    plt.ylabel('Población')
    plt.grid(True)

    plt.subplot(2, 2, 2)
    plt.bar(nombres, poblaciones, color='green')
    plt.title('Gráfico de Barras - Población')
    plt.xticks(rotation=45)
    plt.ylabel('Población')

    plt.subplot(2, 2, 3)
    plt.scatter(nombres, poblaciones, color='red')
    plt.title('Diagrama de Dispersión - Población')
    plt.xticks(rotation=45)
    plt.ylabel('Población')

    plt.subplot(2, 2, 4)
    plt.pie(poblaciones, labels=nombres, autopct='%1.1f%%', startangle=140)
    plt.title('Gráfico de Pastel - Distribución Poblacional')

    plt.tight_layout()
    plt.show(block=False)  

# Ejecución principal
if __name__ == "__main__":
    archivo = input("Ingresa el nombre del archivo CSV a procesar (ej. paises.csv): ").strip()
    datos = leer_y_validar_csv(archivo)

    if datos:
        print("\nDatos preparados correctamente.")
        print("Ejemplo de los primeros 3 países:\n")
        for pais in datos[:3]:
            print(pais)

        if not validar_datos_para_visualizacion(datos):
            exit()

        analizar_datos_poblacion(datos)
        graficar_datos_poblacion(datos)

        continente = input("\nIngresa el nombre del continente para exportar (ej.Europa): ").strip()
        exportar_a_excel_por_continente(datos, continente)
        os.startfile(f"{continente.lower()}_paises.xlsx")

        input("\nPresiona ENTER para finalizar...")  # Evita que las gráficas se cierren de inmediato

    else:
        print("\nNo se pudieron procesar los datos.")
