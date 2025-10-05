# PP Parcial 1 - Ordenamientos -> Arrays.

def ordenar_seleccion_sort_alfabeticamente_lista(mi_lista: list,modo: str) -> list: 
    """ Ordena una lista con el mètodo de Seleccion.
         Si no hay elementos para ordenar, sale
        :params: lista - lista de elementos, modo -> 'ASC'  o -> 'DES'
        :returns: devuelve la lista ordenada """  
    largo_lista = len(mi_lista)
    for indice_actual in range(largo_lista - 1):
        indice_mayor_elemento = indice_actual

        for siguiente_indice in range(indice_actual + 1, largo_lista):
            elemento_mayor = mi_lista[indice_mayor_elemento]
            siguiente_elemento = mi_lista[siguiente_indice]

            if (elemento_mayor[0] > siguiente_elemento[0] and modo == 'ASC') or\
                (elemento_mayor[0] < siguiente_elemento[0] and modo == 'DES'):
                indice_mayor_elemento = siguiente_indice
        
        if indice_mayor_elemento != indice_actual:
            auxiliar = mi_lista[indice_actual]
            mi_lista[indice_actual] = mi_lista[indice_mayor_elemento]
            mi_lista[indice_mayor_elemento] = auxiliar
            
    return mi_lista  

def ordenar_seleccion_sort(mi_lista: list,modo: str) -> list: 
    """ Ordena una lista con el mètodo de Seleccion. Determina el indice MENOR (orden -> 0) o el MAYOR (orden -> 1) de todos.
         Si no hay elementos para ordenar, sale
        :params: lista - lista de elementos, orden : 0 -> ascendente 1 -> descendente
        :returns: devuelve la lista ordenada"""  
    largo_lista = len(mi_lista)
    for indice_actual in range(largo_lista - 1):
        indice_mayor_elemento = indice_actual

        for siguiente_indice in range(indice_actual + 1, largo_lista):
            elemento_mayor = mi_lista[indice_mayor_elemento]
            siguiente_elemento = mi_lista[siguiente_indice]

            if (elemento_mayor > siguiente_elemento and modo == 'ASC') or\
                (elemento_mayor < siguiente_elemento and modo == 'DES'):
                indice_mayor_elemento = siguiente_indice
        
        if indice_mayor_elemento != indice_actual:
            auxiliar = mi_lista[indice_actual]
            mi_lista[indice_actual] = mi_lista[indice_mayor_elemento]
            mi_lista[indice_mayor_elemento] = auxiliar
            
    return mi_lista  

# PP Parcial 1 - Ordenamientos -> Matrices. 

def order_selection_matriz(matriz: list[list],indice_sort: int,valor: str,tipo_orden: str):
      """ Objetivo: Selecciona el indice menor y ordena ASC o DES segun el tipo de orden
        :params: indice_sort - Es el numero de linea/fila dentro de la matriz
                    matriz = [
                        fila_[indice_sort] -> [0] -> fila de datos nro. 1
                        fila_[indice_sort] -> [1] -> fila de datos nro. 2
                        fila_[indice_sort] -> [2] -> fila de datos nro. 3...] 

        :returns: No devuelve nada, solo ordena valores por referencia"""
      for indice_col in range(len(matriz[indice_sort]) -1):
            
            indice_menor_mayor = indice_col # <- indice_menor_mayor es el nombre de la variable con la que hago la comparaciòn 
                                      # y estructura el orden en tiempo de ejecucion 

            for elemento_col_siguiente in range( (indice_col + 1), len(matriz[indice_sort])):
                  if (   (tipo_orden == 'ASC' and float(matriz[indice_sort][indice_menor_mayor]) > float(matriz[indice_sort][elemento_col_siguiente])) or\
                         (tipo_orden == 'DES' and float(matriz[indice_sort][indice_menor_mayor]) < float(matriz[indice_sort][elemento_col_siguiente])) ):
                        indice_menor_mayor = elemento_col_siguiente

            if indice_menor_mayor != indice_col: 
                for indice_fila in range(len(matriz)):
                  auxiliar = matriz[indice_fila][indice_menor_mayor]
                  matriz[indice_fila][indice_menor_mayor] = matriz[indice_fila][indice_col] 
                  matriz[indice_fila][indice_col] = auxiliar

def order_selection_matriz_alfabeticamente(matriz: list[list],indice_sort: int,valor: str,tipo_orden: str):
      """ Objetivo: Ordena por orden alfabetico una matriz
        :params: indice_sort - Es el numero de linea/fila dentro de la matriz
                    matriz = [
                        fila_[indice_sort] -> [0] -> fila de datos nro. 1
                        fila_[indice_sort] -> [1] -> fila de datos nro. 2
                        fila_[indice_sort] -> [2] -> fila de datos nro. 3...] 

        :returns: No devuelve nada, solo ordena valores por referencia"""
      for indice_col in range(len(matriz[indice_sort]) -1):
            
            indice_menor_mayor = indice_col # <- indice_menor_mayor es el nombre de la variable con la que hago la comparaciòn 
                                      # y estructura el orden en tiempo de ejecucion 

            for elemento_col_siguiente in range( (indice_col + 1), len(matriz[indice_sort])):
                  
                  elemento_actual = matriz[indice_sort][indice_menor_mayor]
                  siguiente_elemento = matriz[indice_sort][elemento_col_siguiente]
                  letra_inicial = 0

                  if (   (tipo_orden == 'ASC' and elemento_actual[letra_inicial] > siguiente_elemento[letra_inicial]) or\
                         (tipo_orden == 'DES' and elemento_actual[letra_inicial] < siguiente_elemento[letra_inicial]) ):
                        indice_menor_mayor = elemento_col_siguiente

            if indice_menor_mayor != indice_col: 
                for indice_fila in range(len(matriz)):
                  auxiliar = matriz[indice_fila][indice_menor_mayor]
                  matriz[indice_fila][indice_menor_mayor] = matriz[indice_fila][indice_col] 
                  matriz[indice_fila][indice_col] = auxiliar
