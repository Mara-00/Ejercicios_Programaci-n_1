#Realizar una función recursiva que permita realizar la suma de los dígitos de un número:

# def sumar_digitos(numero:int)->int:
#    pass

def sumar_digitos(numero: int)->int:
    if numero < 10:
        resultado = numero
    else:
        resultado = numero % 10 + sumar_digitos(numero//10)
    
    return resultado

print(sumar_digitos(76964))