from typing import Union

def calcular_perimetro_cuadrado(lado: Union[int, float]) -> Union[int,float]:
	return lado * 4


perimetro = calcular_perimetro_cuadrado(4)
print(perimetro)