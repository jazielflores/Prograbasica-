import statistics

def calcular_estadisticas(*args):
    if not args:
        print("No se ingresaron números.")
        return None
    
    # Calcular el promedio con una función lambda
    promedio = lambda nums: sum(nums) / len(nums)
    
    # Calcular la mediana y desviación estándar usando el módulo statistics
    mediana = statistics.median(args)
    desviacion_estandar = statistics.stdev(args) if len(args) > 1 else 0
    
    return {
        "Promedio": promedio(args),
        "Mediana": mediana,
        "Desviación estándar": desviacion_estandar
    }

# Solicitar números al usuario
numeros = list(map(float, input("Ingrese una lista de números separados por espacios: ").split()))

# Calcular estadísticas y mostrar resultados
resultado = calcular_estadisticas(*numeros)
if resultado:
    print("Resultados:")
    for clave, valor in resultado.items():
        print(f"{clave}: {valor:.2f}")
