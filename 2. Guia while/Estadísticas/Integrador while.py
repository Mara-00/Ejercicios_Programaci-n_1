# Realizar un programa que permita que el usuario ingrese todos los números que desee. 
# Una vez finalizada la carga determinar:
# A. La suma acumulada de los números negativos.
# B. La suma acumulada de los números positivos.
# C. La cantidad de números negativos ingresados.
# D. El promedio de los números positivos.
# E. El número positivo más grande.
# F. El porcentaje de números negativos ingresados, respecto del total de ingresos.

negativo = 0
positivo = 0
acumulador_positivos = 0
acumulador_negativo = 1
respuesta = "si"
maximo = 0
bandera_primer_ingreso = False


while respuesta == "si":
    numero = int(input("Ingrese un numero: "))
    if numero > 0 :
        acumulador_positivos += numero #B
        positivo += 1
    elif numero < 0 :
        acumulador_negativo += numero #A
        negativo += 1 #C
    elif numero > maximo or bandera_primer_ingreso == False:
            maximo = numero
            bandera_primer_ingreso = True
    respuesta = input("Quiere ingresar otro número? si/no: ")


promedio = acumulador_positivos / positivo #D
porcentaje = (acumulador_negativo * 100) / numero

print(f"La suma de los numeros negativos es: {acumulador_negativo}\nLa suma de los numeros negativos es: {acumulador_positivos}")   
print(f"La cantidad de numeros negativos ingresados es: {negativo}")
print(f"Promedio de los numeros positivos es: {promedio}")
print(f"El numero maximo es: {maximo}")
print(f"el porcentaje de los numeros negativos es: {porcentaje}")