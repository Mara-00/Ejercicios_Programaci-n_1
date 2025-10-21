# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
# Calcular la suma de los números ingresados y el promedio de los mismos.

i = 0
acumulador = 0
respuesta = "si"

print("desea ingresar un numero (si/no):")

while respuesta == "si":
    numero = int(input("Ingrese numero:"))
    acumulador += numero
    i += 1
    respuesta = input("Quiere ingresar otro número? si/no: ")
    
promedio = acumulador / i
print(f"El promedio es {promedio}")