def palindromo (text):
    text = text.lower()
    text = text.replace(" ", "")
    finalText = len(text)-1
    inicioText = 0
    palindromo = False
    while finalText>inicioText and text[inicioText]==text[finalText]:
        inicioText +=1
        finalText -=1
    result = inicioText - finalText
    if result == 0 or result == 1:
        palindromo = True
    return palindromo

def es_palindromo (text):
    text = text.lower()
    text = text.replace(" ", "")
    return text == text[::-1]

print(palindromo('neuquen'))
print(es_palindromo('neuquen'))
print(palindromo('hola'))
print(es_palindromo('hola'))