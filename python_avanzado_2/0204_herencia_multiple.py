class AnimalAereo:
    
    def comer(self):
        print("Animal aereo comiendo")
    
    def volar(self):
        print("Volando")

class AnimalTerrestre: 

    def comer(self):
        print("Animal terrestre comiendo")
    
    def caminar(seld):
        print("Caminando")


class Pajaro(AnimalAereo,AnimalTerrestre):
    pass


pato = Pajaro()
pato.volar()
pato.caminar()
pato.comer()
