def crear_matriz(cantidad_filas, cantidad_columnas, valor_inicial) ->1:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz


#def cuadrado_magico(numero):
#    cruz = [numero [i] for i in range(9) if i % 2 != 0]   
#    resto = [numero [i] for i in range(9) if numero [i] not in cruz]
#colocar_numero = int(input("ingreso de numeros:"))
#matriz_resultado = crear_matriz(3,3,0)
#for i in range(len(colocar_numero)):
#    if colocar_numero[i] not in cuadrado_magico:
#        cuadrado_magico.append(colocar_numero)
#print(colocar_numero)