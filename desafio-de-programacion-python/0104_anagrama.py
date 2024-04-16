def anagrama(palabra1, palabra2):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    if len(palabra1) != len(palabra2):
        return False
    for char in palabra2:
        if not(char in palabra2):
            return False
        
    return True

def es_anagrama(palabra1, palabra2):
    palabra1 = sorted(palabra1.lower())
    palabra2 = sorted(palabra2.lower())
    return palabra1 == palabra2

print(anagrama('mora','amor'))
print(es_anagrama('pala', 'lapa'))