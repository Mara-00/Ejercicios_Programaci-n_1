# Mostrar la suma de los números pares desde el 1 hasta el 10.

i = 1
suma = 0

while i <= 10:
    if (i % 2) == 0:
        suma += i
    i += 1
    
print(f"La suma de los numeros pares del 1 al 10 es: {suma}")