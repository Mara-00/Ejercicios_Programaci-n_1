#Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la intersección de los dos arrays.

vector_a = [4,6,9,8,7]
vector_b = [5,6,4,7,2]

for i in range(len(vector_a)):
    for j in range(len(vector_b)):
        if vector_a[i] == vector_b[j]:
            print(vector_a[i])
        break