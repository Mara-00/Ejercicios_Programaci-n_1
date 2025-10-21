# Ingresar 10 números enteros. Determinar el máximo y el mínimo.

i = 0
maximo = 0
minimo = 0

while i <= 10:
    numero = float (input("Ingrese un número: "))
    if numero > maximo or i == 0:
        maximo = numero
        
    if numero < minimo or i == 0:
        minimo = numero
    i += 1
    
print(maximo, minimo)