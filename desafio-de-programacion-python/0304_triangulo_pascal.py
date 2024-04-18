def triangulo_pascal(cantFilas):
    triangulo = []
    for nFilas in range(cantFilas):
        filas = []
        for posicion in range(nFilas+1):
            if posicion == 0 or posicion == nFilas:
                filas.append(1)
            else:
                valor = triangulo[nFilas-1][posicion-1]+triangulo[nFilas-1][posicion]
                filas.append(valor)
        triangulo.append(filas)
    return triangulo

print(triangulo_pascal(4))


