def horas24 (text):
    tiempo = text.split(":")
    momento = text[-2:].lower()
    if momento =="am":
        if tiempo[0] == "12":
            tiempo[0] = "00"   
    
    if momento =="pm":
        if tiempo[0] != "12":
            tiempo[0] = str(int(tiempo[0])+12)
    hora = ":".join(tiempo)
    return hora[:-2]
        

print(horas24('12:12:00 AM'))