# Solicitar al usuario que ingrese como mínimo 5 números. 
# Calcular la suma de los números ingresados y el promedio de los mismos.

i = 0
acumulador = 0
suma_numeros = 0
promedio_numero = 1

while i <5:
    numero = int(input("Ingrese numeros: "))
    acumulador += numero
    i += 1
    
suma_numeros += acumulador
promedio_numero = suma_numeros / 5
    
print(suma_numeros)
print(promedio_numero)