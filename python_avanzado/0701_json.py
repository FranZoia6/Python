import json

persona = {
    "nombre": "Javier",
    "apellido": "Quinonez",
    "edad": 24
}

#objeto_json = json.dumps(persona, indent=2)
with open("persona.json", "w") as archiv_json:
#    archiv_json.write(objeto_json)
    json.dump(persona,archiv_json)