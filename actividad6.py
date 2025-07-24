def saludar():
    print("Bienvenido al programa")
def ingresar_cantidad_numeros(cantidad_numeros):
    cantidad_numeros = int(input("Ingrese la cantidadc de numeros a ingresar: "))
    numeros = []
    for i in range(cantidad_numeros):
        n = int(input("Ingrese un numero: "))
        numeros.append(n)
    return numeros
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
            cantidad_numeros=0
            print(ingresar_cantidad_numeros(cantidad_numeros))

        case "2":
            base = int(input("Ingrese la base del triangulo: "))
            altura=int(input("Ingrese la altura del triangulo"))
            print(f"El area del triangulo es: {calcular_area_triangulo(base,altura)}")
        case "3":
            numero = int(input("Ingrese un numero: "))
            if es_par(numero):
                print(f"El numero {numero} es par.")
            else:
                print(f"El numero {numero} es impar.")
        case "4":
            print("")
        case "5":
            print("")
        case "6":
            print("Saliendo del programa...")
            break
        case _:
            print("Opcion invalida, ingrese una opcion valida")