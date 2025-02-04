# Función para generar la secuencia de Fibonacci
def fibonacci(n):
    secuencia = []
    a, b = 0, 1
    for _ in range(n):
        secuencia.append(a)
        a, b = b, a + b
    return secuencia

# Solicitar al usuario el número de términos
numero_de_terminos = int(input("Introduce el número de términos de la secuencia de Fibonacci: "))

# Generar y mostrar la secuencia
if numero_de_terminos <= 0:
    print("Por favor, introduce un número positivo.")
else:
    secuencia = fibonacci(numero_de_terminos)
    print(f"La secuencia de Fibonacci hasta {numero_de_terminos} términos es: {secuencia}")

