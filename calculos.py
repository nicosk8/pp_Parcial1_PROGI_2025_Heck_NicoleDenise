# PP Parcial 1 - Calculos.

def obtener_promedio(matriz: list[list], indice_a_buscar: int) -> float:
    """ Accede a un array de datos numericos y saca su promedio
    :params: matriz -> set de datos
             indice_a_buscar -> indice de la lista a leer
    :returns: Devuelve el promedio calculado
    """
    cantidad_elementos = len(matriz[0])
    suma_dato = 0

    for numero in matriz[indice_a_buscar]:
        suma_dato += float(numero)
                    
        if cantidad_elementos < 1:
           return 0
                    
    promedio = suma_dato / cantidad_elementos
    return promedio