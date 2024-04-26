nombre = ["Paco","Emilio", "Javier"]
apellido = ["Boteri", "Tafur", "Quiñones"]

nombre_completo = list(zip(nombre, apellido))
print(nombre_completo)

nombre_unzip, apellido_unzip = zip(*nombre_completo)
print(nombre_unzip)
print(apellido_unzip)

for nombre, apellido in zip(nombre, apellido):
    print(nombre, apellido)

