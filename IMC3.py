def calcular_imc(peso, estatura):
    return peso / (estatura ** 2)

def main():
    # Pedir al usuario que ingrese sus datos
    while True:
        nombre = input("Ingrese su nombre: ")
        apellido_paterno = input("Ingrese su apellido paterno: ")
        apellido_materno = input("Ingrese su apellido materno: ")
        
        # Verificar que los campos de nombre, apellido paterno y apellido materno no estén vacíos
        if nombre.strip() != "" and apellido_paterno.strip() != "" and apellido_materno.strip() != "":
            break
        else:
            print("Error: Todos los campos deben ser llenados.")

    # Pedir al usuario que ingrese su edad
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            break
        except ValueError:
            print("Error: Por favor ingrese una edad válida.")

    # Pedir al usuario que ingrese su peso
    while True:
        try:
            peso = float(input("Ingrese su peso en kilogramos: "))
            break
        except ValueError:
            print("Error: Por favor ingrese un peso válido.")

    # Pedir al usuario que ingrese su estatura
    while True:
        try:
            estatura = float(input("Ingrese su estatura en metros: "))
            break
        except ValueError:
            print("Error: Por favor ingrese una estatura válida.")

    # Calcular el IMC
    imc = calcular_imc(peso, estatura)

    #Le imprimos el IMC para que se ponga triste
    print( str(nombre) + " " + str(apellido_paterno) + " " + str(apellido_materno) + ", Su IMC es de: " + str(imc) )

    #Hacemos las distintas validaciones
    if imc >= 0 and imc <= 15.99 :
        print ("Delgadez severa")
    elif imc >= 16.00 and imc <= 16.99 :
        print ("Delgadez moderada")
    elif imc >= 17.00 and imc <= 18.49:
        print ("Delgadez leve")
    elif imc >= 18.50 and imc <= 24.99 :
        print ("Normal")
    elif imc >= 25.00 and imc <= 29.99:
        print ("Sobrepeso")
    elif imc >= 30.00 and imc <= 34.99:
        print ("obesidad leve")
    elif imc >= 35.00 and imc <= 39.00:
        print ("obesidad media")
    elif imc >= 40.00:
        print ("obesidad morbida")

if __name__ == "__main__":
    main()

