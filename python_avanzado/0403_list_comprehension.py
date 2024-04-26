def calcular_cuadrado(numero):
    return numero**2

def es_par(num):
    return num % 2 == 0

lista_num = [1,2,3,4,5,6,7]

lista_comprehension_pares = [calcular_cuadrado(num) for num in lista_num if es_par(num)]
print(lista_comprehension_pares)

lista_resultrados = [calcular_cuadrado(num) if es_par(num) else 0  for num in lista_num]
print(lista_resultrados)