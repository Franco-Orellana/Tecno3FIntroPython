"""
Ejercicio 1:

Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error. El programa termina cuando el usuario introduce un cero.
"""

def mesesAnio():

    listaMeses = (
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "Julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre"
    )

    return listaMeses

def ingresoNumeros():

    flag = True

    while flag:

        num = input("\nIngrese un número (Finaliza con 0): ")

        if not num.isdigit(): 
            print("\nERROR. Debe ingresar un número entero.")

        elif int(num) == 0:
            flag = False
            print()

        else:
            if 1 <= int(num) <= len(mesesAnio()):

                print(f"\nMes: {mesesAnio()[int(num) - 1]}") 
            
            else:
                print(f"\nERROR. Debe ingresar un número entre {1} y {len(mesesAnio())}")

#Inicio del programa
ingresoNumeros()

 
""" 
Ejercicio 2:

Pide números y mételos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar. Por último, muestra los números ordenados de menor a mayor.
"""

listNum = []

def ingresoNumeros(listNumeros):

    flag = True
    
    while flag:

        num = input("\nIngrese un número (Finaliza con 0): ")

        if num.isdigit() and int(num) != 0:
            
            listNumeros.append(int(num))
        
        elif num.isdigit() and int(num) == 0:
            
            flag = False
        
        else:
            print("\nERROR. Debe ingresar un número entero.")

    return listNum


def imprimirNumeros(listNumeros):

    print("\nValores ingresados (ordenados de menor a mayor):\n")

    listNumeros.sort()  

    for num in listNumeros:
 
        print(f"- {num}")

    print()

#Inicio del programa
imprimirNumeros(listNum) if len(ingresoNumeros(listNum)) > 0 else print("\nLa lista está vacia.\n")


"""
Ejercicio 3:

Crea una tupla con números, pide un numero por teclado e indica cuantas veces se repite.
"""

import random

def genNumeros():

    listNumeros = []
    cont = 0

    while cont != 10:

        listNumeros.append(random.randint(0, 99))  
        cont += 1 

    return tuple(listNumeros)


def vecesRepetida(tuplaNumeros, numero):

    cont = 0

    for i in tuplaNumeros:

        if i == numero:

            cont += 1 

    return numero, cont, tuplaNumeros


def ingresoNumero():

    num = input("\nIngrese un número: ")

    if num.isdigit() and int(num) >= 0:

        resultado = vecesRepetida(genNumeros(), int(num)) 

        print(f"\nTupla generada: {resultado[2]}") 

        if resultado[1] == 1:

            print(f"\nEl número ingresado {resultado[0]} se repite {resultado[1]} vez.\n") 

        else: 
            print(f"\nEl número ingresado {resultado[0]} se repite {resultado[1]} veces.\n") 
    else:
        print("\nERROR. Debe ingresar un número entero.\n")

#Inicio del programa
ingresoNumero()

"""
Ejercicio 4:

Vamos a crear un programa en python donde vamos a declarar un diccionario para guardar los precios de las distintas frutas. El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir de los datos guardados en el diccionario.
"""

def dicProductos():

    Productos = {
        "Manzana": 2500,
        "Banana": 2700,
        "Naranja": 1250,
        "Pera": 2100,
        "Uva": 7000,
        "Cereza": 9500,
        "Mango": 2500,
        "Sandía": 1500,
        "Melón": 7000,
        "Kiwi": 5200,
        "Limón": 1700,
        "Coco": 12200,
        "Ciruela": 3500 
    } 

    return Productos 


def ingresoDatos():

    fruta = input("\nIngrese el nombre de la fruta: ")
    cant = input("\nIngrese la cantidad: ")

    if fruta.isalpha() and cant.isdigit() and int(cant) != 0:

        fruta = fruta.lower().capitalize() 

        if dicProductos().get(fruta):
            print(f"\n- Fruta elegida: {fruta}")
            print(f"\n- Cantidad elegida: {cant}")
            print(f"\n- Precio Unitario: ${dicProductos()[fruta]}")
            print(f"\n- Precio final: ${int(cant) * dicProductos()[fruta]}\n")

        else:
            print("\nALERTA. No existen datos almacenados sobre la fruta indicada.\n")
    else:
        print("\nERROR. Verifique los datos ingresados.\n")

#Inicio del programa
ingresoDatos()
 
 



