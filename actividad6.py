def saludar():
    print("Bienvenido al programa")
def ingresar_cantidad_numeros(cantidad_numeros):
    numeros = []
    for i in range(cantidad_numeros):
        n = int(input("Ingrese un numero: "))
        numeros.append(n)
    return numeros
def sumar_promedio_positivos_negativos(numeros):
    suma=0
    for i in numeros:
        suma +=i
    promedio = suma/len(numeros)
    positivos= 0
    negativos=0
    for i in numeros:
        if i <0:
            negativos +=1
        else:
            positivos +=1
    print(f"La suma de los numeros es de: {suma}")
    print(f"El promedio de los numeros es: {promedio}")
    print(f"Hay {positivos} numeros positivos y {negativos} numeros negativos")
def calcular_area_triangulo(base,altura):
    return (base * altura)/2
def es_par(n):
    return n % 2 ==0
def promediar_calificaciones(calificaciones):
    suma=0
    for i in calificaciones:
        suma +=i
    promedio = suma/len(calificaciones)
    return promedio
def mayor_menor(numeros):
    mayor = numeros[0]
    menor = numeros[0]
    for i in numeros:
        if i > mayor:
            mayor =i
        elif i < menor:
            menor = i
    return f"El mayor es {mayor} y el menor es {menor}"
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
            n= int(input("Ingrese la cantidad de numeros: "))
            numeros= ingresar_cantidad_numeros((n))
            print(sumar_promedio_positivos_negativos(numeros))
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
            n= int(input("Ingrese la cantidad de calificaciones: "))
            calificaciones= ingresar_cantidad_numeros((n))
            print(f"El promedio de las calificaciones es de: {promediar_calificaciones(calificaciones)}")
            print()
        case "5":
            n= int(input("Ingrese la cantidad de numeros a ingresar: "))
            numeros= ingresar_cantidad_numeros(n)
            print(mayor_menor(numeros))
        case "6":
            print("Saliendo del programa...")
            break
        case _:
            print("Opcion invalida, ingrese una opcion valida")