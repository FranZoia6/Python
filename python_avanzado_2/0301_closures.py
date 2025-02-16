def saludar(): 
    mensaje = "Buen dia"

    def imprimir_saludo():
        print(mensaje)
    
    return imprimir_saludo


saludo = saludar()
saludo()