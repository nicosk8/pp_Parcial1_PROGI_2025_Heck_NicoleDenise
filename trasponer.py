# PP Parcial 1 - Trasponer Datos

def crear_matriz_traspuesta_tipo_lista(matriz: list[list]) -> list[list]:
    """ Traspone una matriz de formato:

        lista[1] = [id1],[id2],[id3]
        lista[2] = [nombre1],[nombre2],[nombre3]
        lista[3] = [edad1],[edad2],[edad3]

        Y la convierte al formato:

        lista[1] = [id1],[nombre1],[edad1]
        lista[2] = [id2],[nombre2],[edad2]
        lista[3] = [id3],[nombre3],[edad3]
        :params: matriz -> set de datos
        :returns: matriz traspuesta
    """
    matriz_t = []
    tamaño_matriz = len(matriz)
    cantidad_col = len(matriz[0])

    for indice_col in range(cantidad_col):

        nueva_fila = []
        for indice_fila in range(tamaño_matriz):
            nueva_fila.append(matriz[indice_fila][indice_col])
        matriz_t.append(nueva_fila)
    return matriz_t

def obtener_datos_fila(matriz: list, indice_fila: int) -> str: 
    """ Concatena un mensaje con los datos de la fila de una matriz objeto
    :params: matriz -> set de datos, indice_fila -> indice fila

    :returns: Retorna los datos de la fila formateada para ser impresa
    """
    fila_actual = matriz[indice_fila]

    mensaje_fila = f'{indice_fila} | ' # <- aca le agregue imprimir el nro de fila que se ve en consola 
    
    tamaño_fila = len(fila_actual)

    for indice_col in range(tamaño_fila):

        mensaje_fila = f'{mensaje_fila}{fila_actual[indice_col]:10}'
    
    mensaje_fila = f'{mensaje_fila}\n'
    
    return mensaje_fila

def mostrar_datos_matriz(matriz: list):
    """ imprime en consola datos de una matriz en fila traspuesta a matriz "objeto" 
    :params: matriz -> set de datos
    :returns: None
    """
    tamaño_matriz = len(matriz)
    mensaje_matriz = '\n'    

    for indice_fila in range(tamaño_matriz):
        
        mensaje_fila = obtener_datos_fila(matriz, indice_fila)
        mensaje_matriz = f'{mensaje_matriz}{mensaje_fila}'
        
    print(mensaje_matriz, end= ' ') # end = '  ' es un salto de linea implicito

def trasponer_matriz(matriz: list[list]):             
    """ Traspone una matriz y muestra sus datos
    :params: matriz -> set de datos"""
    print('\n\nMatriz original:\n')
    mostrar_datos_matriz(matriz)
    #recorrer_matriz_columnas(matriz)

    print('\n')
    print('Matriz traspuesta : ')
    matriz_t = crear_matriz_traspuesta_tipo_lista(matriz)
    #sc.mostrar_datos_matriz(matriz_t)
    

    print(' ')
