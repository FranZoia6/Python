def get_lista_unidimensional(lista):
    unidimensional = []
    for element in lista:
        if isinstance(element, list):
            unidimensional.extend(element)
        else:    
            unidimensional.append(element)
    return unidimensional


print(get_lista_unidimensional([1,2,[1,3,12]]))