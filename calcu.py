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
        return "Error: División por cero no permitida."

def potencia(a, b):
    return a ** b

def raiz_cuadrada(a):
    if a >= 0:
        return a ** 0.5
    else:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo."

def porcentaje(a, b):
    return (a * b) / 100

def modulo(a, b):
    if b != 0:
        return a % b
    else:
        return "Error: Módulo por cero no permitido."

def promedio(a, b):
    return (a + b) / 2

def mostrar_menu():
    print("\nCalculadora:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz Cuadrada")
    print("7. Porcentaje")
    print("8. Módulo")
    print("9. Promedio")
    print("0. Salir")


while True:
    mostrar_menu()
    operacion = input("Seleccione una operación (0-9): ")

    if operacion == '0':
        print("Saliendo de la calculadora. ¡Hasta luego!")
        break

    elif operacion in ['1', '2', '3', '4', '5', '7', '8', '9']:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if operacion == '1':
            print("Resultado:", suma(num1, num2))
        elif operacion == '2':
            print("Resultado:", resta(num1, num2))
        elif operacion == '3':
            print("Resultado:", multiplicacion(num1, num2))
        elif operacion == '4':
            print("Resultado:", division(num1, num2))
        elif operacion == '5':
            print("Resultado:", potencia(num1, num2))
        elif operacion == '7':
            print("Resultado:", porcentaje(num1, num2))
        elif operacion == '8':
            print("Resultado:", modulo(num1, num2))
        elif operacion == '9':
            print("Resultado:", promedio(num1, num2))

    elif operacion == '6':
        num = float(input("Ingrese un número: "))
        print("Resultado:", raiz_cuadrada(num))

    else:
        print("Operación no válida. Por favor seleccione una opción del 0 al 9.")