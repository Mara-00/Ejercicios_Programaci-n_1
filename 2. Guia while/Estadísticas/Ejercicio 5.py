# Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. 
# Mostrar la suma y el promedio por pantalla.

i = 0
acumulador = 0

while i < 5 :
    numero = int(input("Ingrese numero:"))
    acumulador += numero
    i += 1
    
promedio = acumulador / 5

print(f"La suma es {acumulador}")
print(f"El promedio es {promedio}")