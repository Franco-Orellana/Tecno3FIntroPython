
#Realizar un programa que me diga si un numero es par o impar

num = input("Ingrese un número: ")

if num.isdigit():

    num = int(num)

    print("El número ingresado es par") if num % 2 == 0 else print("El número ingresado es impar")
else:
    print("ERROR. Debe ingresar un número")


 
#Realizar un programa que genere la tabla de multiplicar de un numero ingresado por el usuario (del 1 al 10)


num = input("Ingrese un número: ")

if num.isdigit():

    num = int(num)

    print("\nTabla del número ingresado:")

    for i in range(1,11):

        print(f"{num} x {i} = {num * i}")

else:
    print("ERROR. Debe ingresar un número")



#Realizar un programa que le pida al usuario su nombre y edad y nos diga si es mayor de edad

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")

if not nombre.isdigit() and edad.isdigit():
    
    edad = int(edad)

    if edad >= 18:
        print(f"La persona llamada '{nombre}' de {edad} años de edad, es mayor de edad")
    else:
        print(f"La persona llamada '{nombre}' de {edad} años de edad, es menor de edad")
else:
    print("ERROR. Ha ingresados datos erroneos")
    

#Realizar un programa donde el usuario ingrese una palabra y un numero e imprima por pantalla la palabra ingresa tantas veces como el numero ingresado

palabra = input("Ingrese una palabra: ")
cant = input("Ingrese un número: ")
cont = 0

if not palabra.isdigit() and cant.isdigit():

    cant = int(cant)

    while cont != cant: 

        print(f"{palabra}")
        cont += 1

else:
    print("ERROR. Los datos ingresados son erroneos.")


#Realizar un programa que sume los números ingresados por el usuario hasta que se ingrese un 0. Al finalizar nos debe mostrar la suma por pantalla

suma = 0
flag = True

while flag:

    num = input("Ingrese un número (para finalizar ingrese 0): ")

    if num.isdigit() and int(num) != 0:

        suma += int(num) 

    elif not num.isdigit(): 
        print("ERROR. Debe ingresar un número")

    elif int(num) == 0:
        flag = False


print(f"La sumatoria de los número ingresados es: {suma}")

 
#Realizar un programa que pide al usuario su nombre y apellido y en el caso de no estar la primera letra en mayúscula devolver el mismo nombre y apellido pero con la primer letra en mayúscula

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

if not nombre.isdigit() and not apellido.isdigit() and nombre != "" and apellido != "" and nombre != " " and apellido != " ":

    if nombre[0].islower() and apellido[0].isupper():

        print(f"Nombre y apellido (con la primer letra en mayúscula): {nombre.capitalize()} {apellido}")

    elif nombre[0].isupper() and apellido[0].islower():

        print(f"Nombre y apellido (con la primer letra en mayúscula): {nombre} {apellido.capitalize()}")

    elif nombre[0].islower() and apellido[0].islower():

        print(f"Nombre y apellido (con la primer letra en mayúscula): {nombre.capitalize()} {apellido.capitalize()}")
    else:

        print(f"Nombre y apellido (igual a lo ingresado): {nombre} {apellido}")
else:
    print("ERROR. Los datos ingresados son erroneos.")
 


#Realizar un programa que pida al usuario su edad y nos diga si debe votar, y en caso de tener entre 16 y 18. preguntar al usuario si decide votar o no

edad = input("Ingrese su edad: ") 
flag = False
cont = 0

if edad.isdigit() and int(edad) > 18:
    print("Usted se encuentra en condiciones de votar")

elif edad.isdigit() and 16 <= int(edad) <= 18:
    flag = True

elif not edad.isdigit():
    print("ERROR. Debe ingresar un número.")

else:
    print("No tiene la edad minima para poder votar")

while flag:
        opcion = input("Usted tiene el derecho de votar, ¿desea votar?\nPresione [Y] para votar\nPresione [N] para no votar\nIngresar opción: ")

        match opcion:

            case "Y":
                print("Gracias por efectuar su voto")
                flag = False
            case "N":
                print("Recuerde que puede votar en otro momento")
                flag = False
            case _:
                
                cont += 1

                if cont == 3:
                    flag = False
                    print("\nERROR. Se han superado los intentos permitidos")
                else:
                    print("\nERROR. Debe ingresar una opcion valida\n")

 
#Realizar un programa que pida al usuario que ingrese varios números y que devuelva la suma del cuadrado de esos números

 
flag = True
suma = 0
cont = 0

while flag:

    num = input("Ingrese un número (para finalizar ingrese 0): ")

    if num.isdigit() and int(num) != 0:

        num = int(num)
        suma += num ** 2    

    elif not num.isdigit():
        cont += 1

        if cont != 3:
            print("ERROR. Debe ingresar números")
        else:
            flag = False
            print("ERROR. Se han superado los intentos")
    else:
        flag = False 


print(f"\nLa suma del cuadrado de los números ingresados es: {suma}") 
 