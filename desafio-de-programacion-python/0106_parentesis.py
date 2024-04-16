def parentesis_balanceados(text): 
    if text.count('(') != text.count(')'):
        return False
    prueba = 0
    for char in text:
        if char =='(':
            prueba +=1
        elif char ==')':
            prueba-=1
            if prueba<0:
                return False
    if prueba!=0:
        return False
    return True


print(parentesis_balanceados('(())'))
print(parentesis_balanceados('(())())'))
print(parentesis_balanceados('(((())'))
print(parentesis_balanceados(')))((('))