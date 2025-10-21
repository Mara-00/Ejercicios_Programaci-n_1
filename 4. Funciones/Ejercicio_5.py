# Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.
from math import pi, pow

def circulo (radio: float|int) -> float|None:
    area = None
    if type (radio) == float or type (radio) == int and radio > 0:
        area = pi * pow (radio, 2)
    return area

area = circulo(6)

print(area)