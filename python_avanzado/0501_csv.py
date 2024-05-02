import csv

columnas = ["nombre", "apellido","edad"]
dato = ["Paco","Botero",26]

datos_lista = [
    ["Paco","Botero",26],
    ["Javier", "Quintero", 24],
    ["Emilio", "Tafur", 25]
]

datos_dic = [
    {"nombre": "Paco","apellido":"Botero", "edad":26},
    {"nombre": "Javier","apellido":"Quintero", "edad":24},
    {"nombre": "Emilio","apellido":"Tafur", "edad":25}
]

ruta = "datos.csv"
ruta_dic = "datos_dic.csv"

with open(ruta,"w",newline="") as archivo:
    writer = csv.writer(archivo, delimiter=",")
    writer.writerow(columnas)
    writer.writerows(datos_lista)

with open(ruta_dic,"w",newline="") as archivo:
    writer = csv.DictWriter(archivo, fieldnames=columnas)
    writer.writeheader()
    writer.writerows(datos_dic)