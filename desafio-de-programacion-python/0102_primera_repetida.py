def primera_repetida(text):
    text = text.lower()
    text = text.replace(" ", "")
    for char in text:
        cantChar= text.count(char)
        if cantChar>1:
            return char
    return None

def primera_letra_repetida(text):
    text = text.lower()
    text = text.replace(" ", "")
    lista_letras = []
    for letra in text:
        if letra in lista_letras:
            return letra
        else:
            lista_letras.append(letra)
    return None

        
print(primera_repetida('hola'))
print(primera_letra_repetida('hola'))
print(primera_repetida('hola mundo'))
print(primera_letra_repetida('hola mundo'))