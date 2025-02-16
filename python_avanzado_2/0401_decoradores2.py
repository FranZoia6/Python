import time

def medir_tiempo_ejecucion(funcion):
    def wrapper(*arg, **kwargs):
        inicio = time.time()
        funcion(*arg, **kwargs)
        fin = time.time()
        print(f"Tiempo total de ejecucion: {fin-inicio}")
    return wrapper

def decorador_puntos(funcion):
    def wrapper(*arg, **kwargs):
       print("........")
       funcion(*arg,**kwargs)
       print("........")
    return wrapper

@decorador_puntos
@medir_tiempo_ejecucion
def recorrer_ciclo(rango): 

    for i in range(rango):
        print(i)
        time.sleep(1)

recorrer_ciclo(rango=5)