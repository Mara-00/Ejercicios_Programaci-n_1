# Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Solo tendrá 3 intentos.

contador = 0

while contador < 3:
    clave = input("Ingrese clave:")
    if clave == "Pepe":
        print("Bienvenido al sistema")
        break
    else:
        print ("Acceso denegado")
        contador += 1
    