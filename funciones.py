# Funciones del parcial ----------------------------------------------------------------------

# PP Parcial 1 - Matrices 

def crear_matriz(lista_nombre_heroes_pp: list, lista_alias_pp: list, lista_razas_pp: list, lista_generos_pp: list, lista_poderes_pp: list, lista_inteligencias_pp: list, 
    lista_velocidades_pp: list):
    """ Crea una matriz set de datos con listas obtenidas por parametro
        :params: 
                 lista_nombre_heroes_pp: lista 0,
                 lista_alias_pp: list 1,
                 lista_razas_pp: list 2,
                 lista_generos_pp: list 3,
                 lista_poderes_pp: list 4,
                 lista_inteligencias_pp: list 5, 
                 lista_velocidades_pp: list 6
        :returns: None """
    matriz = [
        lista_nombre_heroes_pp,
        lista_alias_pp, 
        lista_razas_pp, 
        lista_generos_pp, 
        lista_poderes_pp, 
        lista_inteligencias_pp, 
        lista_velocidades_pp 
    ]
    print('\n\nMatriz Personajes cargada exitosamente !!')
    return matriz

def agregar_nuevo_registro(matriz: list[list]) -> list:
    """
    Agrega un un registro a las listas existentes que conforman la matriz
    :params: matriz -> set de datos
    :returns: Matriz con el nuevo registro
    """
    lista_datos = [ # lista_datos = [ "Nicole", "Nicky", "Human" ,"No-Binario", 5000, 500, 500] <- TESTING
#        validar_texto('nombre') ,
#        validar_texto('alias') ,
#        validar_texto('raza') ,
#        #formatear_texto('genero -> Debe ser "Masculino" o  "No-Binario"') , 
#        validar_texto('genero -> Debe ser "Masculino" o  "No-Binario"') ,
#        validar_numero ('cantidad total de poder') , 
#        validar_numero('cantidad total de inteligencia') , 
#        validar_numero('cantidad total de velocidad')
    ]
    lista_datos = [ "Nicole", "Nicky", "Human" ,"No-Binario", 5000, 500, 500]
    for indice_fila in range( len(matriz)):
        matriz[indice_fila].append(lista_datos[indice_fila])

    return lista_datos

# PP Parcial 1 - Strings y validaciones 

def validar_matriz(matriz: list[list]) -> bool:
     """ Valida que una matriz este cargada.
     :params: matriz -> set de datos
     :returns: Devuelve True si està cargada """
     if len(matriz) != 0:
          return True
                    
def validar_num_minmax(texto: str, minimo: int, maximo: int) -> int:
    """
    Pide un nro. entero entre un rango minimo y maximo. Usar para validar un menu 

    :params: texto - Numero ingresado por el usuario
    
    :return: Devuelve un entero
    """
    input_usuario_str = input(texto)
    input_usuario = int(input_usuario_str)
    while minimo > input_usuario or input_usuario > maximo:
        print('SYSTEM ERROR: Ingrese un numero valido')
        input_usuario_str = validar_num_minmax(texto, minimo, maximo)
    return input_usuario

def validar_texto(dato_a_validar: str):
    """ Recibe un string y valida que no venga vacìo
    :params: dato_a_validar -> cadena de texto
    :returns: None
    """
    
    texto = input(f'Ingrese {dato_a_validar}: ')
   
    while texto == '':
        print(f'ERROR -> El {dato_a_validar} no debe estar vacio')
        validar_texto(dato_a_validar)

def validar_texto_ingresado_usuario(dato_a_validar: str):
    """ Recibe un string y valida que no venga vacìo
    :params: dato_a_validar -> cadena de texto
    :returns: Retorna el texto ingresado por usuario
    """
    
    texto = input(f'Ingrese {dato_a_validar}: ')
   
    while texto == '':
        print(f'ERROR -> El {dato_a_validar} no debe estar vacio')
        validar_texto(dato_a_validar)
    return texto

def validar_numero(dato_a_validar: str):
    """ Valida que lo que reciba es un numero entero. Recibe un string, valida que no venga vacìo y si es digito 
        convierte el caracter a numerico
    :params: dato_a_validar -> cadena de texto
    :returns: None
    """
    texto = input(f'Ingrese {dato_a_validar}: ')
   
    while texto == '':
        print(f'ERROR -> El {dato_a_validar} no debe estar vacio')
        validar_texto(dato_a_validar)
    
    if not texto.isdigit():
        print(f'ERROR -> Debe ingresar un numero')
    
    numero = int(texto)
    texto = numero # <- input de usuario

def utn_capitalize(texto: str) -> str:
    """ Recibe una  cadena de texto y capitaliza la primera letra: texto -> Texto
    :params: texto -> cadena de texto 
    :returns: Devulve la cadena formateada
    """
    #nuevo_texto = f'{texto[0].upper}{texto[1: len(texto)].lower()}'
    nuevo_texto = texto.capitalize()
    return nuevo_texto

def formatear_texto_no_binario(texto_formateado: str) ->str:
    """ Especifico del punto 2 del parcial 1 : recibe una cadena de texto y si recibe "Masculino" formatea a  "No-binario" 
    :params: texto_formateado -> cadena de texto que debe formatear o no
    :returns: texto_formateado -> Devuelve el texto -> "No-binario", o no devuelve nada si el texto ya tiene ese formato
    """ 
    if texto_formateado != 'No-Binario':
        texto_formateado = 'No-Binario'
    return texto_formateado

def formatear_texto(cadena: str) -> str:
    """ recibe una cadena de texto y lo devuelve formateado, si viene vacìo lo pide devuelta.
    :params: cadena -> mensaje que indica al usuario que debe ingresar
    :returns: texto_formateado -> Devuelve el texto capitalizado -> "Masculino" o "No-binario" 
    """
    texto = validar_texto_ingresado_usuario(cadena)
    texto_formateado = utn_capitalize(texto)
    
    # Formateo texto "No-Binario" - Especifico para el punto 2 del parcial
    if texto_formateado != 'Masculino' or 'masculino':
        texto_no_binario = formatear_texto_no_binario(texto_formateado)
        texto_formateado = texto_no_binario
    
    return texto_formateado

def obtener_existencias(matriz: list[list]) -> int:
    """ Verifica si està cargada la matriz 
    :params: matriz - matriz 
    :returns: Devuelve el tamaño de la matriz """
    return len(matriz[0])

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

# PP Parcial 1 - Filtraciones - Analisis de datos.

def mapear_valor(dato: str): 
    """ Devuelve el indice de la FILA que se quiere acceder.
        Es como si la funcion te dijera:
            -" Este tipo de dato [dato] se encuentra en la fila [numero tanto] ... "
        
        Y yo como ya tengo la fila donde se encuentra ese tipo de dato, puedo salir de esta funcion y entrar a otra que itere la cantidad de columnas.
            -"Perfecto, Si ya tengo el nro. de fila, entonces q
            ueda leer columna x columna hasta dar con el dato que necesito"
    
    :returns: Delueve None si no matchea el nombre de la fila (Esto es condicion de error y NO DEBE devolver error)"""
    indice = None
    match dato:     
         case 'nombre': 
            indice = 0
         case 'alias': 
            indice = 1
         case 'raza': 
            indice = 2 
         case 'genero':
            indice = 3
         case 'poder': 
            indice = 4  
         case 'inteligencia':
            indice = 5
         case 'velocidad':
            indice = 6

    return indice

def obtener_indices_que_cumplen(matriz: list[list], indice_a_buscar: int,valor_a_buscar: str,condicion_a_evaluar: str) -> list:
    """ Accede a una lista de la matriz, y compara si los elementos coinciden con el valor a buscar.
        :params: matriz -> set de datos
                 indice_a_buscar -> indice de la lista de la matriz
                 valor_a_buscar -> valor con el que voy a hacer la comparacion 
        :reruns: Devuelve una lista de indices que cumplen con el valor que se busca"""                
    
    lista_indices_encontrados = []
    match condicion_a_evaluar:
         case 'igual':

            for indice in range(len(matriz[indice_a_buscar])):
                # print(f'Indice {indice} : {matriz[indice_a_buscar][indice]} <-> {valor_a_buscar}')
                if float(matriz[indice_a_buscar][indice]) == valor_a_buscar:
                    lista_indices_encontrados.append(indice) 
            return lista_indices_encontrados
        
         case 'menor':

            for indice in range(len(matriz[indice_a_buscar])):
                # print(f'Indice {indice} : {matriz[indice_a_buscar][indice]} <-> {valor_a_buscar}')
                if float(matriz[indice_a_buscar][indice]) < valor_a_buscar:
                    lista_indices_encontrados.append(indice) 
            return lista_indices_encontrados
        
         case 'mayor':

            for indice in range(len(matriz[indice_a_buscar])):
                # print(f'Indice {indice} : {matriz[indice_a_buscar][indice]} <-> {valor_a_buscar}')
                if float(matriz[indice_a_buscar][indice]) > valor_a_buscar:
                    lista_indices_encontrados.append(indice) 
            return lista_indices_encontrados
         
         case 'menor o igual':

            for indice in range(len(matriz[indice_a_buscar])):
                # print(f'Indice {indice} : {matriz[indice_a_buscar][indice]} <-> {valor_a_buscar}')
                if float(matriz[indice_a_buscar][indice]) <= valor_a_buscar:
                    lista_indices_encontrados.append(indice) 
            return lista_indices_encontrados

         case 'mayor o igual':

            for indice in range(len(matriz[indice_a_buscar])):
                # print(f'Indice {indice} : {matriz[indice_a_buscar][indice]} <-> {valor_a_buscar}')
                if float(matriz[indice_a_buscar][indice]) >= valor_a_buscar:
                    lista_indices_encontrados.append(indice) 
            return lista_indices_encontrados
        
def filtrar_indices_lista(valor: str,lista: list) -> list[int]:
    """ Recorre una lista y devuelve los indices guardados de los elementos donde encuentre el valor = string """
    contador_indice = 0
    lista_indices = []
    for indice in range( len(lista) ):
        
        for elemento in lista:
             
            if valor in elemento:
                lista_indices.append(contador_indice) 
            contador_indice += 1

        if contador_indice == len(lista): 
            break                  

    return lista_indices

def filtrar_personaje(valor: str,lista: list) -> int:
    """Filtra una lista segun valor, imprime todos los que encuentra y devuelve la cantidad contabilizada
    :params: valor -> valor a buscar en cada elemento de la lista, lista -> lista 
    :returns: Si encuentra suma uno al contador y devuelve la cantidad de elementos hallados"""
    
    total = 0
    for elemento in lista:
        if valor in elemento:
            print(elemento) 
            total += 1

    return total
            
def filtrar_distinto_de(valor: str,lista: list) -> list[int]:
    """Excluye los elementos que sean iguales al valor, muestra y contabiliza los excluidos
    :params: valor -> valor a buscar en cada elemento de la lista, lista -> lista 
    :returns: Si encuentra suma uno al contador y devuelve la cantidad de elementos hallados"""
    
    contador_indice = 0
    lista_indices = []
    for indice in range( len(lista) ):
        
        for elemento in lista:
             
            if not valor in elemento:
                lista_indices.append(contador_indice) 
            contador_indice += 1

        if contador_indice == len(lista): 
            break                  

    return lista_indices
 
def obtener_matriz_filtrada(matriz: list[list], lista_indices: list) -> list[list]:
    """ Recibe una matriz y una lista de indices para armar una matriz nueva con los valores guardados en esos indices 
    :returns: Devuelve la nueva matriz con los valores indicados (matriz filtrada)"""
    
    matriz_filtrada = [  [],[],[],[],[],[],[]  ] # <- si la original tiene màs o menos arrays, HAY QUE AJUSTAR *** MUCHO CUIDADO!!
    for indice in lista_indices:
        for indice_fila in range(len(matriz)):

            dato = matriz[indice_fila][indice]
            matriz_filtrada[indice_fila].append(dato)
    return matriz_filtrada 

def mostrar_mas_poderosos(matriz: list[list],lista: list):
    """ Determina cual o cuales son los personajes mas poderosos y muestra sus datos formateados.
        1 - Ordena DES la matriz segun la lista que quiera ordenar, para que no se me mezclen los indices
            y encontrar rapido el maximo valor.
        2 - Verifica cuales indices igualan ese valor
        3 - Arma una lista de indices que encontro
        4 - Arma el informe
        5 - Muestra los resultados
    :params: matriz -> set de datos
             lista -> lista de poderes
    :returns: None
    """
    indice_lista = mapear_valor('poder')
    
    order_selection_matriz(matriz,
                           indice_lista,
                           valor='None',
                           tipo_orden='DES')

    maximo_poder = matriz[indice_lista][0] # <- Determino el maximo de la lista por la que tengo que ordenar 

    lista_indices = obtener_indices_que_cumplen(matriz,
                                                indice_lista,
                                                 valor_a_buscar = maximo_poder, # <- busco los = al personaje mas fuerte
                                                 condicion_a_evaluar='igual')
    
    lista_personajes_mas_poderosos = []
    for indice in lista_indices: 
        lista_personajes_mas_poderosos.append(indice)
        total = len(lista_personajes_mas_poderosos)


    titulo =\
        f"""El numero maximo de poder es: {maximo_poder}\nTotal personaje/s mas poderosos: {total}\n
        """
    print(titulo)
    imprimir_indices(lista_personajes_mas_poderosos, matriz)

def mostrar_mas_inteligentes(matriz: list[list],lista: list):
    """ Determina cual o cuales son los personajes mas inteligentes y muestra sus datos formateados.
        1 - Ordena DES la matriz segun la lista que quiera ordenar, para que no se me mezclen los indices
            y encontrar rapido el maximo valor.
        2 - Verifica cuales indices igualan ese valor
        3 - Arma una lista de indices que encontro
        4 - Arma el informe
        5 - Muestra los resultados
    :params: matriz -> set de datos
             lista -> lista de inteligencias
    :returns: None
    """
    indice_lista = mapear_valor('inteligencia')
    
    order_selection_matriz(matriz,
                           indice_lista,
                           valor='None',
                           tipo_orden='DES')

    maximo_inteligencia = matriz[indice_lista][0] # <- Determino el maximo de la lista por la que tengo que ordenar 

    lista_indices = obtener_indices_que_cumplen(matriz,
                                                indice_lista,
                                                 valor_a_buscar = maximo_inteligencia, # <- busco los = al personaje mas fuerte
                                                 condicion_a_evaluar='igual')
    
    lista_personajes_mas_inteligentes = []
    for indice in lista_indices: 
        lista_personajes_mas_inteligentes.append(indice)
        total = len(lista_personajes_mas_inteligentes)

    
    titulo = f"""El numero maximo de inteligencia es: {maximo_inteligencia} pts.\nTotal personaje/s mas inteligentes: {total}\n        """
    print(titulo)
    imprimir_indices(lista_personajes_mas_inteligentes, matriz)
    
def filtrar_menor_velocidad(matriz: list[list], lista: list):
    """  Determina cual o cuales son los personajes menos veloces y muestra sus datos formateados.
        1 - Ordena ASC la matriz segun la lista que quiera ordenar, para que no se me mezclen los indices
            y encontrar rapido el minimo valor.
        2 - Verifica cuales indices estan por debajo de ese valor
        3 - Arma una lista de indices que encontro
        4 - Arma el informe y muestra los resultados por consola
    :params: matriz -> set de datos
             lista -> lista de velocidades
    :returns: 
        None. Arma informe y graba por consola los resultados. """
    
    indice_lista = mapear_valor('velocidad')
    promedio = obtener_promedio(matriz,
                                indice_a_buscar=indice_lista)
    order_selection_matriz(matriz,
                           indice_lista,
                           valor='None',
                           tipo_orden='ASC')
    
    minima_velocidad = matriz[indice_lista][0] # <- Determino el minimo

    lista_indices = obtener_indices_que_cumplen(matriz,
                                                indice_lista,
                                                 valor_a_buscar = promedio, # <- busco los que sean inferiores al promedio
                                                 condicion_a_evaluar='menor')
    lista_menos_veloces = []
    for indice in lista_indices: 
        lista_menos_veloces.append(indice)
        total = len(lista_menos_veloces)

    if len(lista_menos_veloces) != int: # contemplo lista vacia

        total = 'No se hallaron personajes que cuya velocidad se encuentre por debajo del promedio.'
        titulo = f"""La velocidad minima registrada es: {minima_velocidad} km/h. \nEl promedio total de velocidad es: {promedio:.2f} km/h.\nTotal de personajes que se encuentran por debajo del promedio de velocidad: {total}\n """
        print(titulo)
        imprimir_indices(lista_indices, matriz)

    else:    

        titulo = f"""La velocidad minima registrada es: {minima_velocidad} km/h. \nEl promedio total de velocidad es: {promedio:.2f} km/h.\nTotal de personajes que se encuentran por debajo del promedio de velocidad: {total}\n """
        print(titulo)
        imprimir_indices(lista_menos_veloces, matriz)
   
def filtrar_debiles(matriz: list[list], lista_razas_pp: list): 
    """ Filtra/busca en la matriz todos los personajes cuyo poder no superen el 
        poder de personajes de raza Saiyan:
          1 - Busca los indices de los de raza Saiyan y genera una matriz aparte con esos indices
          2 - Determina el poder minimo que puede tener esa raza -> ordena los saiyan por poder ASC
          3 - Arma una lista de indices de personajes cuyo poder es inferior al poder minimo
          4 - Verifica que los indices pertenecen a ambas listas/conjuntos
          5 - Arma informe con los resultados.
          6 - Muestra los resultados ordenados de mayor a menor
        :params: 
            matriz -> set de datos
            lista_razas_pp -> lista de razas
            
        :returns: 
            None. Arma informe y graba por consola los resultados."""
    
    lista_indices_saiyan = filtrar_indices_lista('Saiyan', lista_razas_pp)
    matriz_saiyan = obtener_matriz_filtrada(matriz, lista_indices_saiyan) 

    indice_lista = mapear_valor('poder')
    order_selection_matriz(matriz_saiyan, # <- le paso la matriz_saiyan
                           indice_lista,
                           valor='None',
                           tipo_orden='ASC')
    minimo_poder = matriz[indice_lista][0] # <- Determino el minimo

    # Obtengo cuales personajes de otras razas igualan o superan el minimo poder
    order_selection_matriz(matriz, 
                           indice_lista,
                           valor='None',
                           tipo_orden='DES')
    lista_indices_personajes = obtener_indices_que_cumplen(matriz,
                                                indice_lista,
                                                valor_a_buscar = minimo_poder, # <- busco los que sean inferiores a este valor
                                                condicion_a_evaluar='menor')
    
    lista_debiles = []
    for indice in lista_indices_saiyan: 
        if indice in lista_indices_personajes:
            lista_debiles.append(indice)
            total = len(lista_debiles)
    
    if len(lista_debiles) != int: # contemplo lista vacia

        # Armo informe de lista vacia y muestro los datos solo de los personajes que no sean raza Saiyan
        total = 'No se hallaron personajes de otras razas que superen el minimo poder de personaje de raza Saiyan '
        titulo = f"""El poder minimo de un personaje de raza Saiyan es: {minimo_poder}.\nTotal de personajes que son de otras razas y no superan el minimo poder de un Saiyan: {total}\n """
        
        print(titulo)
        imprimir_indices(lista_indices_personajes, matriz)

    else:
    
        titulo = f"""El poder minimo de un personaje de raza Saiyan es: {minimo_poder}.\nTotal de personajes que son de otras razas y no superan el minimo poder de un Saiyan: {total}\n """
        print(titulo)
        imprimir_indices(lista_debiles, matriz)

def filtrar_no_binarios_veloces(matriz: list, lista_generos_pp: list):
    """  Filtra/busca en la matriz todos los personajes de género No-Binario que posean la más alta velocidad. 
            1 - Busca los indices de los mas veloces
            2 - Busca los indices de los de genero "No-Binario"
            3 - Verifica los indices que pertenecen a ambas listas/conjuntos
            4 - Arma informe con los resultados.
        :params: 
            matriz -> set de datos
            lista_generos_pp -> lista de generos
        :returns: 
            None. Arma informe y graba por consola los resultados.
            """
    # Obtengo los indices de mayor velocidad
    indice_lista = mapear_valor('velocidad')
    order_selection_matriz(matriz, 
                           indice_lista,
                           valor='None',
                           tipo_orden='DES')
    maxima_velocidad = matriz[indice_lista][0] # <- Determino el maximo

    lista_indices_mas_veloces = obtener_indices_que_cumplen(matriz,
                                                indice_lista,
                                                 valor_a_buscar = maxima_velocidad, # <- busco los que igualen este valor
                                                 condicion_a_evaluar='igual')
    
    # Obtengo los de genero "No-Binario"
    lista_genero_no_binarios = filtrar_indices_lista('No-Binario',lista_generos_pp)


    # comparo los indices.
    lista_no_binarios_mas_veloces = []
    for indice in lista_indices_mas_veloces:
        if indice in lista_genero_no_binarios:
            lista_no_binarios_mas_veloces.append(indice)
            total = len(lista_no_binarios_mas_veloces)
    
    if len(lista_no_binarios_mas_veloces) != int: # contemplo lista vacia

        # Armo informe de lista vacia y muestro los datos solo de los "no-Binarios"
        total = 'No se hallaron personajes de genero "No-Binario" que superen el minimo poder de personaje raza Saiyan '
        titulo = f"""La velocidad maxima registrada es: {maxima_velocidad} km/h.\nTotal de personajes de genero "No-Binario" que igualan esa velocidad: {total}\n """
        print(titulo)
        imprimir_indices(lista_genero_no_binarios, matriz)

    else: 

        # Armo el informe
        titulo = f"""La velocidad maxima registrada es: {maxima_velocidad} km/h.\nTotal de personajes de genero "No-Binario" que igualan esa velocidad: {total}\n """
        print(titulo)
        imprimir_indices(lista_no_binarios_mas_veloces, matriz)

def armar_informe_raza_android_promedios(promedio_poder: float, promedio_inteligencia: float): 
    """ Arma titulos para informe 
    :params: promedio_poder -> promedio poder
             promedio_inteligencia -> promedio inteligencia 
    :returns: Devuelve informe_titulo -> titulos del informe """

    titulo_0 = 'Informe Personajes de raza Android.                      \n'
    titulo_1 = f'El promedio de poder es: {promedio_poder:.2f}               \n'
    titulo_2 = f'El promedio de inteligencia es: {promedio_inteligencia:.2f} \n'

    informe_titulo = f'{titulo_0}{titulo_1}{titulo_2}'
    return informe_titulo

def calcular_promedios_raza_android(matriz: list[list], lista_razas_pp: list):
    """  Promedios Inteligencia: Calcular el promedio de inteligencia y poder de los personajes que 
         sean de raza Android.
    :params: matriz -> set de datos
             lista_razas_pp -> lista de razas
    :returns: No retorna nada, imprime por consola """
    
    # Armo una matriz de personajes raza Android
    indices_raza_android = filtrar_indices_lista('Android',lista_razas_pp)
    matriz_personajes_raza_android = obtener_matriz_filtrada(matriz, indices_raza_android)

    cantidad_elementos = int(len(indices_raza_android))

    if cantidad_elementos != int:
        # si la lista esta vacia los promedios valen 0.
        print('*** La lista esta vacia, no pueden calcularse los promedios. ***')
        print(armar_informe_raza_android_promedios(promedio_poder = 0, 
                                               promedio_inteligencia = 0))
        
    if cantidad_elementos != 0: # contemplo que existan indices para calcular promedio
        if len(indices_raza_android) == 1:

            # si tiene un solo elemento, el promedio total es el valor de ese elemento
            promedio_poder = matriz_personajes_raza_android[mapear_valor('poder')][0]
            promedio_inteligencia = matriz_personajes_raza_android[mapear_valor('inteligencia')][0]
            print( armar_informe_raza_android_promedios(promedio_poder, promedio_inteligencia) )
            mostrar_elemento_matriz(matriz_personajes_raza_android, 
                                    indice_elemento = 0)
        else:

            # Obtengo promedio de poder.
            indice = mapear_valor('poder')
            promedio_poder = obtener_promedio(matriz_personajes_raza_android, 
                                            indice_a_buscar = indice)

            # Obtengo promedio de inteligencia.
            indice = mapear_valor('inteligencia')
            promedio_inteligencia = obtener_promedio(matriz_personajes_raza_android, 
                                                    indice_a_buscar = indice)

            # Armo informe e imprimo.

            print(armar_informe_raza_android_promedios(promedio_poder, promedio_inteligencia))
            imprimir_indices( matriz_personajes_raza_android,
                            indices_raza_android )

def armar_informe_filtrar_kryptonian(promedio_poder: float): 
    """ Arma titulos para informe 
    :params: promedio_poder -> promedio poder
    :returns: Devuelve informe_titulo -> titulos del informe """

    titulo_0 = 'Informe Personajes que NO SON raza Kryptonian.                                                                   \n'
    titulo_1 = f'El promedio de poder de personajes de raza Kryptonian es: {promedio_poder:.2f}                                  \n'
    titulo_2 = f'Lista de personajes de OTRAS RAZAS superen o igualen el promedio de poder de personajes de raza Kryptonian:   \n\n'

    informe_titulo = f'{titulo_0}{titulo_1}{titulo_2}'
    return informe_titulo

def filtrar_kryptonian(matriz: list[list], lista_razas_pp: list):

    """ Filtrar Kryptonian: Solamente de los personajes que NO sean raza Kryptonian, mostrar la info 
        completa de los que superen o igualen el promedio de poder de personajes de raza 
        Kryptonian.
    :params: matriz -> set de datos
             lista_razas_pp -> lista de razas
    :returns: None. Imprime resultados por consola  """

    # Filtro los de raza Kryptonian
    lista_indices_raza_kryptonian = filtrar_distinto_de('Kryptonian', lista_razas_pp)
    matriz_personajes_raza_kryptonian = obtener_matriz_filtrada(matriz, lista_indices_raza_kryptonian)
    promedio_poder_kryptonian = obtener_promedio(matriz_personajes_raza_kryptonian,
                                                 indice_a_buscar = mapear_valor('poder') )
    
    # Filtro los personajes de otras razas
    lista_indices_otros = filtrar_distinto_de('Kryptonian', lista_razas_pp)
    matriz_otros_personajes = obtener_matriz_filtrada(matriz, lista_indices_otros)

    lista_indices_personajes_que_cumplen = obtener_indices_que_cumplen( matriz_otros_personajes,
                                                                        indice_a_buscar = mapear_valor('poder'),
                                                                        valor_a_buscar = promedio_poder_kryptonian,
                                                                        condicion_a_evaluar = 'mayor o igual')
    print( armar_informe_filtrar_kryptonian(promedio_poder_kryptonian))
    imprimir_indices(lista_indices_personajes_que_cumplen,
                     matriz_otros_personajes)

def armar_conjuntos_de_razas(lista_razas_pp : list, valor: str) -> list[int]:

    """ Recibe una lista y guarda los indices de los valores que encuentre en la lista
    :params: lista_razas_pp -> lista de razas, 
             valor -> string a hallar 
    :returns: lista_indices -> lista de indices """
    espacio = ' '
    indice = 0
    total_raza_desconocido = 0
    total_raza_only_human = 0
    total_raza_human = 0
    total_raza_inhuman = 0
    total_raza_animal = 0
    total_raza_mutant = 0
    
    for raza in lista_razas_pp:
    
    #mensaje = f'{indice}| {raza}'
    #print(mensaje)
    

        if valor in raza:
            lista_raza_desconocido = []
            lista_raza_desconocido.append(indice)
            lista_indices = lista_raza_desconocido
            total_raza_desconocido += 1
            indice += 1

        if  valor in raza:
            lista_raza_only_human = []
            lista_raza_only_human.append(indice)
            lista_indices = lista_raza_only_human
            total_raza_only_human += 1
            indice += 1

        if  f'{valor}{espacio}' in raza:
            lista_raza_human = []
            lista_raza_human.append(indice)
            lista_indices = lista_raza_human
            total_raza_human += 1
            indice += 1

        if  valor in raza:
            lista_raza_inhuman = []
            lista_raza_inhuman.append(indice)
            lista_indices = lista_raza_inhuman
            total_raza_inhuman += 1
            indice += 1

        if valor in raza:
            lista_raza_animal = []
            lista_raza_animal.append(indice)
            lista_indices = lista_raza_animal
            total_raza_animal += 1
            indice += 1

        if valor in raza:
            lista_raza_mutant = []
            lista_raza_mutant.append(indice)
            lista_indices = lista_raza_mutant
            total_raza_mutant += 1
            indice += 1
    
    return lista_indices

def calcular_stats_personajes(matriz: list[list], lista_indices: list[int]) -> float:
    """ Rutina para calcular "stats" de personajes. calcula el promedio de -> 3 promedios  
    :params: matriz -> set de datos
             lista_indices -> lista de indices
    :returns: Devuelve el valor calculado """
    if len(lista_indices) > 0:
        #matriz_auxiliar = obtener_matriz_filtrada(matriz, lista_indices)
        promedio_poder = obtener_promedio(matriz, indice_a_buscar = 4 )
        promedio_inteligencia = obtener_promedio(matriz, indice_a_buscar = 5 )                                          
        promedio_velocidad = obtener_promedio(matriz, indice_a_buscar = 6 )                                       
        total_stats = (promedio_poder + promedio_inteligencia  + promedio_velocidad) / 3
        return total_stats
    else: print(' ERROR en calcular_stats_personajes() -> lista_indices = 0 -> vacia. No se puede calcular los promedios')
    return total_stats

def filtrar_saiyan_power(matriz: list[list], lista_razas_pp: list):
    """ Filtrar Saiyan Power: Mostrar la info de los personajes (que no sean raza Saiyan) cuyos stats 
        estén por debajo del índice de ataque Saiyan
        :params: matriz: list[list], lista_razas_pp: list
        :returns: None"""
    # Filtro los de raza Saiyan y obtengo los promedios para calcular el indice de ataque de personaje raza Saiyan
    lista_indices_saiyan = filtrar_indices_lista('Saiyan', lista_razas_pp)
    #lista_indices_saiyan = filtrar_distinto_de('Saiyan', lista_razas_pp)
    matriz_auxiliar = obtener_matriz_filtrada(matriz, lista_indices_saiyan)
    indice_ataque_saiyan = calcular_stats_personajes(matriz_auxiliar, lista_indices_saiyan)
    maximo_stat = indice_ataque_saiyan
    
    # para cualcular los stats de cada raza tengo oque saber cuantas razas tengo...
    # calculo stat de raza Desconocido
    lista_ordenada = ordenar_seleccion_sort_alfabeticamente_lista(lista_razas_pp,'ASC')
    lista_indices_desconocido = armar_conjuntos_de_razas(lista_ordenada, valor='Desconocido')
    #matriz_auxiliar = obtener_matriz_filtrada(matriz, lista_indices_desconocido)
    indice_ataque_raza_desconocido = calcular_stats_personajes(matriz, lista_indices_desconocido)

    # calculo stat de raza Animal
    lista_ordenada = ordenar_seleccion_sort_alfabeticamente_lista(lista_razas_pp,'ASC')
    lista_indices_animal = armar_conjuntos_de_razas(lista_ordenada, valor='Animal')
    matriz_auxiliar = obtener_matriz_filtrada(matriz, lista_indices_animal)
    indice_ataque_raza_animal = calcular_stats_personajes(matriz_auxiliar, lista_indices_animal)

    # calculo stat de raza Human
    lista_ordenada = ordenar_seleccion_sort_alfabeticamente_lista(lista_razas_pp,'ASC')
    lista_indices_human = armar_conjuntos_de_razas(lista_ordenada, valor='Human')
    #matriz_auxiliar = obtener_matriz_filtrada(matriz, lista_indices_human)
    indice_ataque_raza_human = calcular_stats_personajes(matriz, lista_indices_human)

    # calculo stat de raza Mutant
    lista_ordenada = ordenar_seleccion_sort_alfabeticamente_lista(lista_razas_pp,'ASC')
    lista_indices_mutant = armar_conjuntos_de_razas(lista_ordenada, valor='Mutant')
    matriz_auxiliar = obtener_matriz_filtrada(matriz, lista_indices_mutant)
    indice_ataque_raza_mutant = calcular_stats_personajes(matriz_auxiliar, lista_indices_mutant)

    lista_stats_calculados = [indice_ataque_raza_desconocido, indice_ataque_raza_animal, indice_ataque_raza_human,
                              indice_ataque_raza_mutant]
    titulo=\
    f"""\n\n15. Filtrar Saiyan Power: Mostrar la info de los personajes (que no sean raza Saiyan) cuyos stats 
        estén por debajo del índice de ataque Saiyan, obtenido de la ecuación (promedio poder + 
        promedio inteligencia + promedio velocidad) / 3. Para saber esto, primero deberás calcular el 
        promedio de esos stats de los personajes cuya raza sea Saiyan.

        El indice de ataque de un personaje raza "Saiyan" es: {indice_ataque_saiyan:.2f} \n
        El indice de ataque de un personaje raza "Desconocido" es: {indice_ataque_raza_desconocido:.2f} \n
        El indice de ataque de un personaje raza "Animal" es: {indice_ataque_raza_animal:.2f} \n
        El indice de ataque de un personaje raza "Human" es: {indice_ataque_raza_human:.2f} \n
        El indice de ataque de un personaje raza "Mutant" es: {indice_ataque_raza_mutant:.2f} \n\n

    """
    print(titulo)
    
    if len(lista_indices_desconocido) != 0:
        if indice_ataque_raza_desconocido < maximo_stat:
            imprimir_indices(matriz, lista_indices_desconocido)

    if len(lista_indices_animal) != 0:
        if indice_ataque_raza_animal < maximo_stat:
            imprimir_indices(matriz, lista_indices_animal)
    
    if len(lista_indices_human) != 0:
        if indice_ataque_raza_human < maximo_stat:
            imprimir_indices(matriz, lista_indices_human)

    if len(lista_indices_mutant) != 0:
        if indice_ataque_raza_mutant < maximo_stat:
            imprimir_indices(matriz, lista_indices_mutant)
    
    if (len(lista_indices_desconocido) or 
       len(lista_indices_animal)       or 
       len(lista_indices_human)        or
       len(lista_indices_mutant)) != 0:
        mensaje = f'No existen razas cuyos stats superen el de raza Saiyan'
        print(mensaje)

def ordenar_por_inteligencia(matriz: list[list]):

    """  Ordenar por Más Inteligente: Ordenar la matriz según inteligencia DES 
     :params: matriz -> set de datos, lista -> lista """
    
    order_selection_matriz(matriz,
                    mapear_valor('inteligencia'), 
                    valor='None',
                    tipo_orden='DES')
    
    for indice_elemento in range ( len(matriz[0]) ):
        mostrar_elemento_matriz(matriz,indice_elemento)
    print(f'\nlista ordenada por: mayor nivel de inteligencia -> "DES"        \n\n')

def ordenar_por_velocidad(matriz: list[list]):

    """  Ordenar por Más Inteligente: Ordenar la matriz según inteligencia DES 
     :params: matriz -> set de datos, lista -> lista """
    
    order_selection_matriz(matriz,
                    mapear_valor('velocidad'), 
                    valor='None',
                    tipo_orden='ASC')
    
    for indice_elemento in range ( len(matriz[0]) ):
        mostrar_elemento_matriz(matriz,indice_elemento)
    print(f'\n\nEsta lista esta ordenada por: mayor nivel de velocidad -> "ASC"\n\n')

def ordenar_por_mas_poder_not_human(matriz: list[list], lista_razas_pp: list):
    """ Ordenar la matriz según poder DES de los personajes 
        cuya raza no sea Human
        :params: matriz -> set de datos
                lista_razas_pp -> lista de razas"""
    indices_not_human = []
    indices_not_human = filtrar_distinto_de(valor = 'Human',
                                            lista = lista_razas_pp)
        
    order_selection_matriz(matriz,
                    mapear_valor('poder'), 
                    valor='None',
                    tipo_orden='DES')

    
    for indice in indices_not_human:
        mostrar_elemento_matriz(matriz,
                                indice_elemento = indice)
    
    titulo = f'Ordenar "DES" por -> Mayor poder [not Human]: {len(indices_not_human)} registros impresos.'
    print(titulo)        
    
def ordenar_por_menos_inteligente_not_human(matriz: list[list], lista_razas_pp: list):
    """  Ordena la matriz según inteligencia ASC de personajes cuya raza no sea Human
    :params: matriz -> set de datos 
             lista_razas_pp -> lista de razas
    :returns: None. Muestra informe por consola"""
    indices_not_human = []
    indices_not_human = filtrar_distinto_de(valor = 'Human',
                                            lista = lista_razas_pp)
    order_selection_matriz(matriz,
                    mapear_valor('inteligencia'), 
                    valor='None',
                    tipo_orden='ASC')
    
    for indice in indices_not_human:
        mostrar_elemento_matriz(matriz,
                                indice_elemento = indice)
    
    titulo = f'Ordenar "ASC" por -> Menor inteligencia de los raza not Human: {len(indices_not_human)} registros impresos.'
    print(titulo)
    
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
    #mostrar_datos_matriz(matriz_t)
    

    print(' ')

def ordenar_trasponer_datos(matriz: list[list]):

    """ Ordena y traspone datos :params: matriz -> set de datos""" 
    order_selection_matriz_alfabeticamente(matriz, 
                                           mapear_valor('raza'), 
                                           valor='None', 
                                           tipo_orden = 'ASC')
    
    trasponer_matriz(matriz)
    mostrar_datos(matriz)
    mensaje = '\nLista ordenada por raza y en orden afabetico -> "ASC".\n\n '
    print(mensaje)