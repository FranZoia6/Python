def elementos_repetidos(lista):
    repetidos = []
    for elemento in lista:
        if lista.count(elemento)>1 and elemento not in repetidos:
            repetidos.append(elemento)
    return repetidos


print(elementos_repetidos(['ana', 'mer','rodri', 'mer', 'fran','fran', 'rodri']))