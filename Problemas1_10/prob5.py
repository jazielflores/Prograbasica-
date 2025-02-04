# Función para verificar si un número es primo
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Solicitar al usuario un número
numero = int(input("Introduce un número para verificar si es primo: "))

# Verificar si el número es primo
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
