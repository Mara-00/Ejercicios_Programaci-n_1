# Solicitarle al usuario el ingreso de un color. Validar que el mismo sea Rojo, Verde o Azul.

#color = input("Ingrese un color: ")

#while color not in ["Rojo", "Azul", "Verde"]:
#    color = input("Ingrese un color: ")

color = input("Ingrese un color (Rojo, Verde, Azul): ")

while color != "Rojo" and color != "Azul" and color != "Verde":
    print("El color no es valido")
    color = input("Reingrese un color: ")
    
print("El colo ingresado es valido")