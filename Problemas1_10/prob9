# Función para generar listas de números pares e impares
def generar_pares_impares(limite):
    pares = []
    impares = []
    
    for i in range(1, limite + 1):
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    
    return pares, impares

# Solicitar al usuario el límite
limite = int(input("Introduce el límite hasta donde generar los números (por ejemplo, 10): "))

# Llamar a la función para generar las listas
pares, impares = generar_pares_impares(limite)

# Mostrar los resultados
print(f"Números pares hasta {limite}: {pares}")
print(f"Números impares hasta {limite}: {impares}")
