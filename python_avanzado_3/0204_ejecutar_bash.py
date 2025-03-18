import subprocess

nombre_bash = "bash_ejemplo.sh"


with open(nombre_bash, mode="r", encoding="utf-8") as archivo_bash:
    contenido = archivo_bash.read()

print(f"Contenido del archivo: {contenido}")

subprocess.call(["bash", "-c", contenido], shell=True)
