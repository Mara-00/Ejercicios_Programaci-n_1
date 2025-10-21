# Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.

def usuario():
    numero_flotante = float(input("Ingrese un numero: "))
    print(numero_flotante)
    return(numero_flotante)

print(usuario)