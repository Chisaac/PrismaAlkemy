import logging

def minuscula():
    logging.basicConfig(
    level=logging.INFO,
    filename='results.log',
    filemode='w',
    format= '%(asctime)s - %(lineno)s - %(levelname)s - %(message)s')
    fruits = ['Frutilla','Melón','PERA',99.6,'NaranJA', 'mORa', 'NisPERo',99]
    for i in fruits:
        if type(i)== str:
            j=i
            i=i.lower()
            logging.info(f'Se paso a minuscula correctamente: {j}--->{i}')
        else:
            logging.error(f'{i} No es string')
    print(" \n")
minuscula()