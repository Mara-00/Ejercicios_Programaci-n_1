# Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados.

numero = int(input("Ingrese un numero: "))
contador_divisores = 0

for i in range(1,numero + 1):
    if numero % i == 0:
        print(f"{i} es divisor de {numero}")
        contador_divisores += 1
        
print(f"Se encontraron {contador_divisores} divisores")