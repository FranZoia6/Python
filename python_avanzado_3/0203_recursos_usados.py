import psutil

def recursos_usados_cpu():
    nucleos = psutil.cpu_count(logical=False)
    print("Cantidad de nucleos", nucleos)

    carga = psutil.getloadavg()
    print("Carga prtomedio", carga)

    uso = psutil.cpu_percent(interval=5, percpu= True)
    print("Porcentaje de uso de la CPU", uso)

recursos_usados_cpu()