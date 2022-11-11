'''El programa solicita el numero de indice de la lista e iimprime el texto.

   Utiliza una lista que 
'''

def imprimir_lista(medios_transporte)->str:
    
    numero=int(input("Ingrese el numero de indice de la lista"))
    try:
        print(medios_transporte[numero])
    except Exception as exp :
        print("Numero fuera de indice",type(exp))

    else:
        print("Programa finalizado con exito")

imprimir_lista(['auto', 'avión', 'barco', 'bicicleta', 'ómnibus' ])