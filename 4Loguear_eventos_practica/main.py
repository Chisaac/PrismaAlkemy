import logging
import functions
import logging.config

logging.basicConfig(
    level=logging.DEBUG,
    filename='logs\main.log',
    filemode='w',
    format= '%(asctime)s - %(lineno)s - %(levelname)s - %(message)s')

try:
    logging.debug('Procesando el archivo')
    f=open('cuento.txt','r')
    logging.debug('Archivo procesado')
except:
    logging.error('No se pudo procesar el cuento',exc_info=True)
