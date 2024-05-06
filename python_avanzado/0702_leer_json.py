import json 

with open("persona.json") as arvhivo_json:
    datos_json = json.load(arvhivo_json)

print(type(datos_json))
print(datos_json["nombre"])