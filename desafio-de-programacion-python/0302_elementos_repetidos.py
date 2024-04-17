def elementos_repetidos(lista):
    repetidos = []
    for elemento in lista:
        if lista.count(elemento)>1 and elemento not in repetidos:
            repetidos.append(elemento)
    return repetidos


print(elementos_repetidos([1,23,3,1,3,5,23]))
#    text.count(char)