def saludar():
    print("Bienvenido al programa")
def ingresar_cantidad_n(cantidad_numeros):
    cantidad_numeros = int(input("Ingrese cuantos numeros quiere ingresar: "))
    for i in range(cantidad_numeros):
        n = int(input("Ingrese los numeros"))
    return cantidad_numeros
def calcular_area_triangulo(base,altura):
    return (base * altura)/2
def es_par(n):
    return n % 2 ==0



while True:
    saludar()
    print("1. Ingresar n numeros.")
    print("2. Calcular area de un triangulo")
    print("3. Verificar si un numero es par")
    print("4. Calcular promedio de calificaciones.")
    print("5. Mostrar el numero mayor y menor.")
    print("6. Salir del programa")
    opcion = input("Ingrese una de las opciones: ")
    match opcion:
        case "1":
        case "2":
        case "3":
        case "4":
        case "5":
        case "6":
        break
        case _:
            print("Opcion invalida, ingrese una opcion valida")