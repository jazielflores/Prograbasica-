# Funciones para las operaciones
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por 0"

# Función principal de la calculadora
def calculadora():
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    
    # Pedir la operación al usuario
    operacion = input("Selecciona la operación (1/2/3/4): ")

    # Pedir los dos números
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    
    if operacion == '1':
        print(f"{num1} + {num2} = {suma(num1, num2)}")
    elif operacion == '2':
        print(f"{num1} - {num2} = {resta(num1, num2)}")
    elif operacion == '3':
        print(f"{num1} * {num2} = {multiplicacion(num1, num2)}")
    elif operacion == '4':
        print(f"{num1} / {num2} = {division(num1, num2)}")
    else:
        print("Operación no válida")

# Llamar a la función de la calculadora
calculadora()
