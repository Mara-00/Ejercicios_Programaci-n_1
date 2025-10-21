#Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Tendrá intentos indeterminados.

clave = input("Ingrese una clave: ")

while clave != "Pepe":
    clave = input("Error... reingrese una clave: ")
    
print("Bienvenido al sistema...")
