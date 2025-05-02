import csv
import re

def leer_y_validar_csv(nombre_archivo):
    """
    Lee un archivo CSV de países, valida los campos y devuelve los datos listos para graficar.
    Cada país será representado como un diccionario con datos limpios y tipos adecuados.
    """
    datos_procesados = []
    errores = 0

    regex_texto = r'^[A-ZÁÉÍÓÚÑa-záéíóúñ\s\(\)\-]+$'
    regex_poblacion = r'^\d{1,3}(\.\d{3})*$'

    try:
        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            encabezados_esperados = {"nombre", "capital", "poblacion", "idioma", "divisa"}

            # Verificación de encabezados
            if set(lector.fieldnames) != encabezados_esperados:
                print(f"Error: Encabezados incorrectos. Se esperaban: {encabezados_esperados}")
                return []

            for i, fila in enumerate(lector, 1):
                nombre = fila['nombre'].strip()
                capital = fila['capital'].strip()
                poblacion_str = fila['poblacion'].strip()
                idioma = fila['idioma'].strip()
                divisa = fila['divisa'].strip()

                # Validaciones
                if not re.match(regex_texto, nombre):
                    print(f"Fila {i}: nombre inválido → '{nombre}'")
                    errores += 1
                if not re.match(regex_texto, capital):
                    print(f"Fila {i}: capital inválida → '{capital}'")
                    errores += 1
                if not re.match(regex_poblacion, poblacion_str):
                    print(f"Fila {i}: población inválida → '{poblacion_str}'")
                    errores += 1
                if not re.match(regex_texto, idioma):
                    print(f"Fila {i}: idioma inválido → '{idioma}'")
                    errores += 1
                if not re.match(regex_texto, divisa):
                    print(f"Fila {i}: divisa inválida → '{divisa}'")
                    errores += 1

                # Solo agregar si todo está válido hasta el momento
                if errores == 0:
                    poblacion_num = int(poblacion_str.replace('.', ''))
                    datos_procesados.append({
                        "nombre": nombre,
                        "capital": capital,
                        "poblacion": poblacion_num,
                        "idioma": idioma,
                        "divisa": divisa
                    })

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

# Ejemplo de ejecución directa
if __name__ == "__main__":
    archivo = input("Ingresa el nombre del archivo CSV a procesar (ej. europa_paises.csv): ").strip()
    datos = leer_y_validar_csv(archivo)

    if datos:
        print("\n Datos preparados correctamente para graficar.")
        print("Ejemplo de los primeros 3 países:\n")
        for pais in datos[:3]:
            print(pais)
    else:
        print("\n No se pudieron procesar los datos.")
