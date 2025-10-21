# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
# Calcular la suma de los números positivos y el producto de los negativos.

acumulador_positivos = 0
producto_negativo = 1
respuesta = "si"

while respuesta == "si":
    numero = int(input("Ingrese un numero: "))
    if numero > 0 :
        acumulador_positivos += numero
    elif numero < 0 :
        producto_negativo *= numero
    
respuesta = input("Quiere ingresar otro número? si/no: ")

print(acumulador_positivos)
print(producto_negativo)    