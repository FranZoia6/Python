import csv 

with open("datos.csv","r",encoding="UTF-8") as archivo:
    reader = csv.reader(archivo)
    next(reader)
    for fila in reader:
        print(fila)