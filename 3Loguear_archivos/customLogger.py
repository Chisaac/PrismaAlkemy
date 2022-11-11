#customLogger.py
import logging

#Creo logger pers.
logger = logging.getLogger(__name__)

#Niv de seguridad:

logger.setLevel(logging.DEBUG)

#Creo handlers:

c_handler=logging.StreamHandler()
f_handler=logging.FileHandler('app.log')

#Niv de seguridad de los handlers:

c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

#Formato de handlers:

c_format=logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

#Agrego handlers al logger:
logger.addHandler(c_handler)
logger.addHandler(f_handler)

#Pruebo
logger.warning('Esto es un warning')
logger.error('Esto es un error')