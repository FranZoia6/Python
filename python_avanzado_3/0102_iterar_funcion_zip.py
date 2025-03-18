lista_nombre = ["Ana", "Paco", "Javier"]
lista_edades = [25,27,25]

datos_zip = zip(lista_nombre, lista_edades)
print(list(datos_zip))

for nombre,edad in zip(lista_nombre, lista_edades):
    print(nombre,edad)