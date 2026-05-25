"""
Al iniciar se nos debe pedir ingresar un numero entero, si este es
distinto a 0 el programa inicia, de lo contrario finaliza (tambien si se
ingresa otra cosa que no sea un numero entero).

Se debe poder ingresar una Palabra o Frase y contar cuantos
caracteres tiene dicha palabra o frase

Con el valor obtenido en el punto anterior calcular su Factorial, una
vez hecho esto , decirnos si el resultado es par o impar.

Se deben imprimir los resultados por pantalla en cada paso.

Una vez cumplido esto, deberemos volver a pedir el ingreso de un
número y realizar la verificación del punto 1

"""

flag = True
espacios = 0
cantLetras = 0
factorial = 1
num = input("\nIngrese un número entero (diferente de cero): ")


while flag:
    
    if num.isdigit() and int(num) != 0:

        palabra = input("\nIngrese una palabra o frase: ")
        
        if not palabra.isdigit():

            for i in palabra:

                if i == " ":
                    espacios += 1 

            if espacios >= 1:
                
                cantLetras = len(palabra) - espacios
                print(f"\nLa palabra o frase ingresada '{palabra}' posee {cantLetras} letras")
            else:
                cantLetras = len(palabra)
                print(f"\nLa palabra o frase ingresada '{palabra}' posee {cantLetras} letras")


            for j in range(1, cantLetras + 1): 
                factorial *= j 

            print(f"\nEl factorial {factorial} es par") if factorial % 2 == 0 else print(f"El factorial {factorial} es impar") 
            print("\n\n")

    else:
        flag = False
    

    
    if flag: 
        
        num = input("Ingrese un número entero (diferente de cero): ")  
        espacios = 0
        cantLetras = 0
        factorial = 1


            


        


