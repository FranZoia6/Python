from datetime import datetime

ahora = datetime.now()
print(ahora, type(ahora))

fecha = ahora.strftime("%Y-%m-%d")
print(fecha, type(fecha))

format_24h = ahora.strftime("%H:%M:%S")
print("Formato 24h", format_24h)

format_12h = ahora.strftime("%I:%M:%S %p")
print("Formato 12h", format_12h)