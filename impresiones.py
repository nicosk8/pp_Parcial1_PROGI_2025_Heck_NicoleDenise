# PP Parcial 1 - Impresiones.

def mostrar_elemento_matriz(matriz: list [list],indice_elemento):
    """ Muestra un unico elemento de una lista con los datos formateados
    :params: matriz -> set de datos
             indice -> indice a mostrar 
    :returns: None """

    nombre = matriz[0][indice_elemento]
    alias = matriz[1][indice_elemento]
    raza = matriz[2][indice_elemento]
    genero = matriz[3][indice_elemento]
    poder = matriz[4][indice_elemento]
    inteligencia = matriz[5][indice_elemento]
    velocidad = matriz[6][indice_elemento]

    mensaje = f"""\nId: {indice_elemento}| Nombre : {nombre}, Alias: {alias}, Raza: {raza}, Gènero: {genero}, Poder: {poder}, Inteligencia: {inteligencia}, Velocidad: {velocidad} \n"""   
    print(mensaje)
    
def mostrar_datos(matriz: list[list]):
    """ Imprime dato por dato de una matriz
    :params: matriz -> set de datos
    :returns: None"""
    cant_columnas = len(matriz[0])
    for indice_columna in range(cant_columnas):
        dato = f'{indice_columna + 1} | '
        for indice_fila in range(len(matriz)): 
            dato = f'{dato}{matriz[indice_fila][indice_columna]}'
            
            if indice_fila < len(matriz) - 1:
                dato = f'{dato},' 
        print(dato)

def mostrar_datos_truncado(matriz: list[list]):
    """ Imprime cada dato de una matriz hasta los primeros 15 caracteres
    :params: matriz -> set de datos
    :returns: None"""
    cant_columnas = len(matriz[0])
    for indice_columna in range(cant_columnas):
        dato = f'{indice_columna + 1} | '
        for indice_fila in range(len(matriz)): 
            dato = f'{dato}{matriz[indice_fila][indice_columna]}'
            
            if indice_fila < len(matriz) - 1:
                dato = f'{dato[0:15]},' # <- Muestro solo los primero 15 caracteres
        print(dato)

def imprimir_indices(lista_indices: list, matriz: list[list]):
    """ Recibe una lista de indices de columnas de una matriz de tipo lista e imprime un mensaje formateado con los datos
    :params: lista_indices -> list, 
             matriz -> set de datos
    :returns: None
    """
    total = 0
    for indice in lista_indices:
        
        nombre = matriz[0][indice]
        alias = matriz[1][indice]
        raza = matriz[2][indice]
        genero = matriz[3][indice]
        poder = matriz[4][indice]
        inteligencia = matriz[5][indice]
        velocidad = matriz[6][indice]
        total += 1
        
        mensaje = f"""Id: {indice}| Nombre : {nombre}, Alias: {alias}, Raza: {raza}, Gènero: {genero}, Poder: {poder}, Inteligencia: {inteligencia}, Velocidad: {velocidad} \n"""   
        print(mensaje)
    mensaje = f'Total impresos: {total}'
    print(mensaje)
