# Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive.

nota = int(input("Ingrese la nota:"))

while nota > 1 or nota < 10:
    if nota < 1:
        print("Error ... esa nota no existe")
        break
    elif nota > 10:
        print("Error ... esa nota no existe")
        break
    else:
        print("La nota ingresada esta permitida")
        break