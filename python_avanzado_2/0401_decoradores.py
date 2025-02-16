def funcion_decorador(funcion):
    def funcion_wrapper():
        print("Dentro de la funcion wrapper")
        funcion()
    return funcion_wrapper


@funcion_decorador
def funcion_prueba():
    print("Funcion de prueba")



funcion_prueba()