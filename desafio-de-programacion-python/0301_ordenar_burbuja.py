def ordenar_burbuja(lista):

    for i in range(len(lista)):
        for j in range(0, len(lista)-i-1):
            if lista[j]> lista[j+1]:
                listaAux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = listaAux
    return lista

print(ordenar_burbuja([3,8,4,1,2]))