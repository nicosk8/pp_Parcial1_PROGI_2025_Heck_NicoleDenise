import os
import funciones as fun
import validaciones as val
import impresiones as sc


def aplicacion(lista_nombre_heroes_pp: list,
    lista_alias_pp: list, 
    lista_razas_pp: list, 
    lista_generos_pp: list, 
    lista_poderes_pp: list, 
    lista_inteligencias_pp: list, 
    lista_velocidades_pp: list):
    corriendo = True
    matriz_cargada = None
    mensaje_error = 'ERROR. Debe Cargar los datos en la opcion 1.'
    matriz_personajes = []

    while corriendo:

        mensaje = """\n  
        Parcial 1 - TUP UTNFRA - PROG I - Heck, Nicole Denise 
        1 - Crear Matriz: para ello deberá crear una función que en base a las listas, cree una matriz con los datos para trabajar. 
        2 - Agregar personaje: Debes poder agregar un personaje a la matriz, los datos a incluir son: 
            Nombre, Alias, Raza, Género, Inteligencia, Poder, Velocidad.  
        3 - Existencias: Mostrar la cantidad de personajes que hay en el set de datos.
        4 - Existencias personajes Human: Mostrar la cantidad de personajes que sean raza Human o en 
            caso de que tengan una raza compuesta, tengan Human en su raza.
        5 - Existencias personajes que no sean Human: Mostrar la cantidad de personajes cuya raza no 
            sea Human o no tenga Human como parte de su raza compuesta.
        6 - Mostrar Detalle: Recorrer la matriz y mostrar la info de todos los personajes truncando los strings a 15 caracteres como máximo.
            (con una función que acepte ese tipo de matriz) con formato:  nombre,alias,raza,género,inteligencia,poder,velocidad. 
        7 - Mostrar Saiyan: Recorrer la matriz y mostrar la info (con una función que acepte ese tipo de matriz)
            con formato: nombre,alias,raza,género,inteligencia,poder,velocidad solamente de los personajes cuya raza sea Saiyan. 
        8 - Mostrar más poderoso: Determinar cuál o cuáles son los personajes con más poder y mostrar 
            sus datos, junto con la cantidad que poseen. 
        9 - Mostrar más inteligente: Determinar cuál o cuáles son los personajes más inteligentes y mostrar sus datos, junto con la cantidad que poseen.
        10 - Filtrar Menor velocidad: Filtrar/Buscar y mostrar la info de los personajes que no superen el promedio de velocidad.
        11 -  Filtrar Débiles: Filtrar/buscar en la matriz todos los personajes cuyo poder no superen el poder de personajes de raza Saiyan. 
        12 -  Filtrar No-Binario Veloces:  Filtrar/buscar en la matriz todos los personajes de género No-Binario que posean la más alta velocidad.
        13 - Promedios Inteligencia: Calcular el promedio de inteligencia y poder de los personajes que sean de raza Android.
        14 - Filtrar Kryptonian: Solamente de los personajes que NO sean raza Kryptonian, mostrar la info completa de los que superen o igualen el promedio de poder de personajes de raza 
             Kryptonian. 
        15 -  Filtrar Saiyan Power: Mostrar la info de los personajes (que no sean raza Saiyan) cuyos stats estén por debajo del índice de ataque Saiyan,
             obtenido de la ecuación (promedio poder + promedio inteligencia + promedio velocidad) / 3. Para saber esto, primero deberás calcular el 
            promedio de esos stats de los personajes cuya raza sea Saiyan.
        16 - Ordenar por Más Inteligente: Ordenar la matriz según inteligencia DES.
        17 - Ordenar por Menos Inteligente [not Human]: Ordenar la matriz según inteligencia ASC de personajes cuya raza no sea Human.  
        18 - Ordenar por Más Poder [not Human]: Ordenar la matriz según poder DES de los personajes cuya raza no sea Human.
        19 - Ordenar por Más Velocidad: Ordenar la matriz según velocidad ASC.
        20 - Ordenar personalizado: Ordenar la matriz según lo siguiente: 
                Todos los personajes deben estar agrupados por Raza 
                Cada personaje de cada raza, debe estar ordenado según poder DES en su raza. 
                Las Razas en la matriz deben aparecer de forma Alfabética.
        21 -  Trasponer Datos: Trasponer la matriz y mostrar su información prolija con una función que acepte ese tipo de matriz, además debe estar ordenada por Raza ASC.  
        22 - Salir.   


                Ingrese una opcion -> """
        opcion = val.validar_num_minmax(mensaje,1,22)
        print('\n')
        match opcion:

            case 1: 
                
                matriz_personajes = fun.crear_matriz(lista_nombre_heroes_pp,
                                                    lista_alias_pp, 
                                                    lista_razas_pp, 
                                                    lista_generos_pp, 
                                                    lista_poderes_pp, 
                                                    lista_inteligencias_pp, 
                                                    lista_velocidades_pp     )
                matriz_cargada = val.validar_matriz(matriz_personajes)
            
            case 2: 
                if matriz_cargada:
                    personaje_agregado = fun.agregar_nuevo_registro(matriz_personajes)
                    mensaje = f'\nAlta de personaje: {personaje_agregado} \nPersonaje agregado exitosamente !!'
                    print(mensaje)
                else: print(mensaje_error)
                    
            case 3:      
                if matriz_cargada:
                    print(f'Detalle de los personajes cargados : {val.obtener_existencias(matriz_personajes)}\n')
                    sc.mostrar_datos(matriz_personajes)  
                else: print(mensaje_error)
                    
            case 4:
                if matriz_cargada:

                    total_personajes_filtrados = fun.filtrar_personaje('Human',lista_razas_pp) # <- filtrar por raza 'Human'
                    print(f'\nBuscar -> "Human" hallado en cantidad de videos: {total_personajes_filtrados}')

                else: print (mensaje_error)
                
            case 5: 
                if matriz_cargada:

                    indices_personajes_filtrados = fun.filtrar_distinto_de('Human',lista_razas_pp) # <- filtrar por raza != 'Human'
                    print(f'\nBuscar -> Distinto de "Human" hallado en cantidad de videos: {len(indices_personajes_filtrados)} \n')
                    sc.imprimir_indices(matriz=matriz_personajes,
                                         lista_indices = indices_personajes_filtrados)

                else: print (mensaje_error)

            case 6:
                if matriz_cargada:

                    print(f'Detalle de los personajes cargados : {val.obtener_existencias(matriz_personajes)}\n')
                    sc.mostrar_datos_truncado(matriz_personajes)  
                else: print(mensaje_error)

            case 7:
                if matriz_cargada:
                    
                    lista_indices = []
                    matriz_filtrada = []

                    print(f'\nBuscar "Saiyan" personajes hallados: nombre, alias, raza, género, inteligencia, poder, velocidad')
                    lista_indices = fun.filtrar_indices_lista('Saiyan',lista_razas_pp)
                    matriz_filtrada = fun.obtener_matriz_filtrada(matriz_personajes,lista_indices)
                    sc.mostrar_datos(matriz_filtrada)

                else: print (mensaje_error)

            case 8: 
                if matriz_cargada:

                    fun.mostrar_mas_poderosos(matriz_personajes,lista_poderes_pp)

                else: print(mensaje_error)
            
            case 9:
                if matriz_cargada: 

                    fun.mostrar_mas_inteligentes(matriz_personajes,lista_inteligencias_pp)

                else: print(mensaje_error)

            case 10:
                if matriz_cargada: 

                    fun.filtrar_menor_velocidad(matriz_personajes, lista_velocidades_pp)

                else: print(mensaje_error)

            case 11:
                if matriz_cargada: 

                    fun.filtrar_debiles(matriz_personajes, lista_razas_pp) 

                else: print(mensaje_error)
                
            case 12:

                if matriz_cargada: 

                    fun.filtrar_no_binarios_veloces(matriz_personajes, lista_generos_pp)

                else: print(mensaje_error)

            case 13:
                if matriz_cargada: 

                    fun.calcular_promedios_raza_android(matriz_personajes,lista_razas_pp)

                else: print(mensaje_error)
                
            case 14:

                if matriz_cargada: 

                    fun.filtrar_kryptonian(matriz_personajes,lista_razas_pp)

                else: print(mensaje_error)

            case 15:

                if matriz_cargada:

                    fun.filtrar_saiyan_power(matriz_personajes, lista_razas_pp)

                else: print(mensaje_error)    
            
            case 16:
                
                if matriz_cargada: 

                    fun.ordenar_por_inteligencia(matriz_personajes)
                    
                else: print(mensaje_error)
            
            case 17:
                if matriz_cargada: 

                    fun.ordenar_por_menos_inteligente_not_human(matriz_personajes, lista_razas_pp)
                    
                else: print(mensaje_error)
            case 18:
                if matriz_cargada: 
                    
                    fun.ordenar_por_mas_poder_not_human(matriz_personajes, lista_razas_pp)

                else: print(mensaje_error)
              
            case 19:

                if matriz_cargada: 
                    
                    fun.ordenar_por_velocidad(matriz_personajes)

                else: print(mensaje_error)

            case 20:

                if matriz_cargada: 
                    pass
                else: print(mensaje_error)

            case 21:

                if matriz_cargada: 
                    
                    fun.ordenar_trasponer_datos(matriz_personajes)

                else: print(mensaje_error)

            case 22:
                print('\nSaliendo de la aplicacion...')
                
        print('\n\n')
        os.system('pause')
        os.system('cls')                
