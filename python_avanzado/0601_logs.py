import logging

logging.basicConfig(level=logging.DEBUG,format = "%(asctime)s - %(levelname)s - %(message)s") # filename="logs.log"
nombre = "Paco"

logging.error(f"{nombre} creó un error")
logging.debug("Log de debugging")
logging.info("Log informativo")
logging.warning("Log de advertencia")
logging.error("Log error")
logging.critical("Log de error critico")

try: 
    division = 2/0
except:
    logging.error("división por cero")