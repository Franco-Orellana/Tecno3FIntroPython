#Ejercicio 1: 
#Cree una funcion que calcule el promedio de N notas
def prom(numeros): 

    suma = 0
    cant = 0

    for i in numeros.split(","):

        suma += int(i)
        cant += 1

    return round(suma / cant, 2) 

def numIngresados(numeros): 

    cont = 0

    for i in numeros.split(","):

        if cont == len(numeros.split(",")) - 1:
            print(f"{i}.")
        else:
            print(f"{i},", end=" ")
        cont += 1

def ingresoDatos(cant):

    i = 1 
    numeros = ""
    
    print()
    
    while i <= cant:
    
        num = input(f"Ingrese el {i}° número: ")

        if num.isdigit() and int(num) >= 0:

            if i == cant:
                numeros += num
            else:
                numeros += (num + ",")
            
            i += 1
        else:
            print("\nERROR. Debe ingresar un número entero positivo\n")

    return numeros

#Inicio del programa
cant = input("\nIndique la cantidad de números a ingresar: ")

if not (cant.isdigit() and int(cant) > 0):
    print("\nERROR. Debe ingresar un número entero positivo mayor a cero\n") 
else: 
    numeros = ingresoDatos(int(cant))
    
    print(f"\nNúmeros ingresados: ", end="")
    numIngresados(numeros)
    print(f"\nEl promedio de los números ingresados es: {prom(numeros)}\n")
 
 
#Ejercicio 2: 
#Cree una funcion que determine si un color es primario o no, se debe imprimir por pantalla la leyenda “el color X es primario “ o “el color X no es primario”
def busqueda(colores, color):

    flag = False
 
    for i in colores.split(","):

        if color == i:

            flag = True
            break

    return flag

def primario(colores, color):

    disponible = False
    encontrado = False
    primarios = "rojo,azul,amarillo"

    disponible = busqueda(colores, color)

    if disponible:
        encontrado = busqueda(primarios, color)

    return disponible, encontrado

def coloresDisponibles(colores):

    cont = 0  

    print("\nColores disponibles a comparar:")

    for i in colores.split(","):

        if cont in (11,21,31,41) or cont == (len(colores.split(",")) - 1):
            print(f"{i}") 
        else:
            print(f"{i} -", end=" ")

        cont += 1 


#Inicio del programa
colores = "rojo,azul,amarillo,verde,naranja,violeta,morado,negro,blanco,gris,marron,cafe,rosa,rosado,celeste,turquesa,cyan,magenta,beige,dorado,plateado,ocre,lila,lavanda,bordo,granate,escarlata,coral,salmon,caqui,oliva,esmeralda,aguamarina,indigo,violeta,fucsia,crema,marfil,mostaza,chocolate,cobre,perla,arena,vino" 

coloresDisponibles(colores)
 
color = input("\nIngrese un color a comparar (En palabras sin espacios): ") 
 
if not color.isalpha():
    print("\nERROR. Debe ingresar solamente palabras sin espacios\n") 
else:
    color = color.lower()
    resultado = primario(colores,color)

    match resultado[0]:
        case False:
            print("\nEl dato ingresado no se puede comparar con los colores disponibles\n")
        case True:
            if resultado[1]:
                print(f"\nEl color '{color}' es un color primario\n")
            else:
                print(f"\nEl color '{color}' no es un color primario\n")
 

 
#Ejercicio 3:
#Cree una funcion que determine que numero de una serie de N numeros es mayor
def mayor(numeros):

    mayor = 0 
    cont = 1
    repetido = False 

    for i in numeros.split(","):

        if int(i) > mayor: 
            mayor = int(i) 

        elif int(i) == mayor: 
            if cont == (len(numeros.split(",")) - 1): 
                repetido = True 

            cont += 1
    
    return repetido, mayor

def numIngresados(numeros): 
    
    cont = 0

    for i in numeros.split(","):

        if cont == len(numeros.split(",")) - 1:
            print(f"{i}.")
        else:
            print(f"{i},", end=" ")
        cont += 1

def ingresoDatos(cant):

    i = 1 
    numeros = ""

    print()

    while i <= cant:
    
        num = input(f"Ingrese el {i}° número: ")

        if num.isdigit() and int(num) >= 0:

            if i == cant:
                numeros += num
            else:
                numeros += (num + ",")
            
            i += 1
        else:
            print("\nERROR. Debe ingresar un número entero positivo\n")

    return numeros

#Inicio del programa
cant = input("\nIndique la cantidad de números a ingresar: ")

if not (cant.isdigit() and int(cant) > 0):
    print("\nERROR. Debe ingresar un número entero positivo mayor a cero\n") 
else: 
    numeros = ingresoDatos(int(cant)) 

    print(f"\nNúmeros ingresados:", end=" ")
    numIngresados(numeros)  

    resultado = mayor(numeros) 

    match resultado[0]:
        case False:
            print(f"\nEl mayor de los números ingresados es: {resultado[1]}\n")
        case True:
            print("\nNo hay un número que sea mayor, son todos iguales.\n")
            
 
 
 
#Ejercicio 4:
#Cree una funcion que dibuje un rectangulo de X filas y X columnas determinadas por el usuario
def rectangulo(filas, columnas):

    for i in range(filas):
        for j in range(columnas): 
            if j == columnas - 1:
                print("*")
            else:
                print("*", end=" ")
    
    print() 

#Inicio del programa
filas = input("\nIngrese el número de filas: ")
columnas = input("Ingrese el número de columnas: ")

if not(filas.isdigit() and int(filas) > 0 and columnas.isdigit() and int(columnas) > 0):
    print("\nERROR. Verifique los datos ingresados.\n")
else:
    if filas == columnas:
        print("\nERROR. El valor de las filas y columnas son iguales, para construir un rectángulo estos datos deben ser diferentes.\n")
    else:
        print(f"\nSe creará un rectángulo de {filas} filas y {columnas} columnas\n")
        rectangulo(int(filas), int(columnas))
 


#Ejercicio 5:
#Cree una funcion que calcule el Factorial de un numero entero positivo
def factorial(numero):
 
    fact = 1

    for i in range(1, numero + 1):

        fact *= i 

    print(f"\nEl factorial de {numero} es: {fact}\n") 

#Inicio del programa
num = input("\nIngrese un número: ")

if not(num.isdigit() and int(num) > 0):
    print("\nERROR. Debe ingresar un número entero positivo\n")
else:
    factorial(int(num))