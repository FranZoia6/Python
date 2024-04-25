def function_kwargs(**kwargs):
    print(kwargs)
    for llave,valor in kwargs.items():
        print(f"llave: {llave}, valor:{valor}")
function_kwargs(nombre = 'Paco', apellido = 'Botero')