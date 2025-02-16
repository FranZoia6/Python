class Persona:
    tipo = 'humano'

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apelldio = apellido
        self.edad = edad 
        self.documento_identidad = None

    def agregar_documento(self, documento_identidad):
        self.documento_identidad = documento_identidad
        print("Documento guardado")
    
    def ejecutar_accion(self):
        print("Haciendo algo")

class Deportista(Persona):
    def __init__(self, nombre, apellido, edad, deporte):
        super().__init__(nombre, apellido, edad)
        self.deporte = deporte
    
    def ejecutar_accion(self):
        super().ejecutar_accion()
        print(f"Practicando {self.deporte}")

juliana = Deportista("Juliana", "cortez",26, "Volleyball" )
juliana.agregar_documento(1234)
print(juliana.deporte)
juliana.ejecutar_accion()

