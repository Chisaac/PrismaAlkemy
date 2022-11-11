def contar_caracteres():

    '''
    Recibe palabras separadas por espacio y devuelve cantidad de letras

    '''

    lista_retorno = []
    palabras = str(input("Ingrese las palabras separadas por un espacio"))
    lista_inicial = palabras.split()    #Separa las palabras con un espacio
    for palabra in lista_inicial:   #Recorre la lista generada 
        lista_retorno.append(len(palabra))  #Por c/palabra añade la cantidad de letras 
    print(lista_retorno)
contar_caracteres()