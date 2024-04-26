def calcular_cuadrado(numero):
    return numero**2


lista_num = [1,2,3,4,5,6,7,8,9,10]

pares_comprehension = [cuadrado for num in lista_num if (cuadrado := calcular_cuadrado(num)) % 2 == 0]
print(pares_comprehension)