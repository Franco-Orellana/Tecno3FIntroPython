#Ejercicio 1
nombre = input("Ingrese su nombre: ")
print(f"Nombre ingresado (en mayúscula): {nombre.upper()}")

#Ejercicio 2
num = float(input("Ingrese un número: "))
valorSuma = 5
print(f"El resultado es: {num + valorSuma}")

#Ejercicio 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
print(f"Bienvenido/a {(nombre + " " +  apellido).title()}")
 
#Ejercicio 4
numUno = float(input("Ingrese el primer número: "))
numDos = float(input("Ingrese el segundo número: "))
numTres = float(input("Ingrese el tercer número: "))
numCuatro = float(input("Ingrese el cuarto número: "))
numCinco = float(input("Ingrese el quinto número: "))
suma = numUno + numDos + numTres + numCuatro + numCinco
cantNum = 5
print(f"El promedio de los números ingresados es: {suma / cantNum}")

#Ejercicio 5
frase = input("Ingrese una frase: ") 
print(f"Frase ingresada (en minúscula): {frase.lower()}")
