# Función para calcular el interés compuesto
def interes_compuesto(P, r, n, t):
    A = P * (1 + r / n) ** (n * t)
    return A

# Solicitar datos al usuario
P = float(input("Introduce el capital inicial (P): "))
r = float(input("Introduce la tasa de interés anual (en porcentaje, por ejemplo 5 para 5%): ")) / 100
n = int(input("Introduce el número de veces que se capitaliza el interés por año (por ejemplo, 12 para mensual): "))
t = float(input("Introduce el tiempo en años (t): "))

# Calcular el monto total
A = interes_compuesto(P, r, n, t)

# Mostrar el resultado
print(f"El monto total después de {t} años es: {A:.2f}")
