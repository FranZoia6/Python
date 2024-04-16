def numero_triangular(numero):
    triangular = 0
    for i in range(1, numero+1):
        triangular+=i
    return triangular

print(numero_triangular(3))

print(numero_triangular(4))

print(numero_triangular(6))