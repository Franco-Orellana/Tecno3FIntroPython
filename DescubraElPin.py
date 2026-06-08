"""
Requisitos a cumplir:

- El juego termina cuando el usuario acierta la clave o hace 3 intentos.
- Al pedir el ingreso, se debe validar que el dato tenga exactamente 4
caracteres y que sean únicamente dígitos numéricos enteros. Si no
cumple, no consume intento y vuelve a pedirlo.
- Si el usuario falla, el sistema debe indicar cuántos números de su
intento son correctos y cuántos de ellos están en la posición correcta.
- Al perder (agotar los intentos), se le enviará un mensaje indicándole
que el sistema fue bloqueado y cuál era la clave correcta
"""
claveSecreta = "2341"
intentos = 0
flag = True
encontrada = False 

while intentos != 3 and not encontrada:

    charCorrecto = False
    i = 0 
    cont = 0

    if flag: claveIngresada = input("\n- Ingrese una clave de 4 digitos: ")

    if not (claveIngresada.isdigit() and len(claveIngresada) == 4):

        print("\nERROR. Debe ingresar una valor de 4 digitos") 

    else: 
        if claveSecreta == claveIngresada:
            print("\n-------------------------------------------------------------")
            print("\n¡Clave descubierta!\n")
            encontrada = True 

        else:
            while i != 4:

                if claveIngresada[i] == claveSecreta[i]:

                    charCorrecto = True
                    cont += 1 
                i += 1

            if charCorrecto:
                if cont == 1:
                    print(f"\nFue ingresado correctamente {cont} caracteres")
                else:
                    print(f"\nFueron ingresados correctamente {cont} caracteres")

            else:
                print("\nNo existe ninguna coincidencia")
            intentos += 1
 
if intentos == 3:

    print("\n-------------------------------------------------------------")
    print("\n¡Se ha bloquedo el sistema!")
    print(f"\nLa clave correcta es: {claveSecreta}\n")

