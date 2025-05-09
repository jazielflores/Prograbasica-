import csv

def agregar_continente_al_csv(nombre_archivo):
    try:
        # Leer el archivo original
        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            filas = list(lector)
            
            # Añadir la columna 'continente' con el valor 'África' a todas las filas
            for fila in filas:
                fila['continente'] = 'África'
            
            # Crear un nuevo archivo CSV con los datos corregidos
            nuevo_nombre_archivo = "corregido_" + nombre_archivo
            with open(nuevo_nombre_archivo, mode='w', encoding='utf-8', newline='') as archivo_corregido:
                encabezados = lector.fieldnames + ['continente']  # Añadir 'continente' a los encabezados
                escritor = csv.DictWriter(archivo_corregido, fieldnames=encabezados)
                escritor.writeheader()
                escritor.writerows(filas)

            print(f"El archivo ha sido corregido y guardado como '{nuevo_nombre_archivo}'.")
    
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Llamada a la función
archivo = input("Ingresa el nombre del archivo CSV a procesar (ej. paises.csv): ").strip()
agregar_continente_al_csv(archivo)
