import asyncio
import time

def funcion_sincrona():
    print("Ejecuntando funcion sincrona")
    time.sleep(1)
    print("Fin funcion sincrona")


async def funcion_asincrona(): 
    print("Ejecutando funcion asincrona")
    await asyncio.sleep(1)
    print("Fin funcion asincrona")

async def main(): 
    corrutinas = [funcion_asincrona(), funcion_asincrona()]
    await asyncio.gather(*corrutinas)

inicio = time.time()
asyncio.run(main())
print(f"Tiempo asincrono: {time.time() - inicio}")

inicio = time.time()
funcion_sincrona()
funcion_sincrona()
print(f"Tiempo sincrono: {time.time() - inicio}")
