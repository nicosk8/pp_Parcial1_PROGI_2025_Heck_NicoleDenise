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
    if input_usuario_str.isdigit() :
        input_usuario = int(input_usuario_str)
    else:
        
        while input_usuario_str.isalpha() or input_usuario_str == '' or\
              (minimo > input_usuario or input_usuario > maximo):
                    print('\nSYSTEM ERROR: Ingrese un dato numerico valido')
                    input_usuario_str = validar_num_minmax(texto, minimo, maximo)

    return input_usuario

def validar_texto(dato_a_validar: str) -> str:
    """ Recibe un string y valida que no venga vacìo y capitaliza la primera letra del string
    :params: dato_a_validar -> cadena de texto
    :returns: None
    """
    
    cadena = input(f'Ingrese {dato_a_validar}: ')
    
    while cadena == '':
        print(f'ERROR -> El {dato_a_validar} no debe estar vacio')
        validar_texto(dato_a_validar)
    
    texto = utn_capitalize(cadena)

    return texto

def validar_numero(dato_a_validar: str) -> int:
    """ Valida que lo que reciba es un numero entero. Recibe un string, valida que no venga vacìo y si es digito 
        convierte el caracter a numerico
    :params: dato_a_validar -> cadena de texto
    :returns: None
    """
    texto = input(f'Ingrese {dato_a_validar}: ')
   
    while texto == '':
        print(f'ERROR -> El {dato_a_validar} no debe estar vacio')
        validar_texto(dato_a_validar)
    
    if  texto.isnumeric() != True:
        print(f'ERROR -> Debe ingresar un numero')
        validar_numero(dato_a_validar)
    
    numero = int(texto)
    texto = numero # <- input de usuario
    return texto

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

def validar_genero(dato_a_validar: str) -> str:
    """ Recibe un string y valida que no venga vacìo y capitaliza la primera letra del string
    :params: dato_a_validar -> cadena de texto
    :returns: None
    """
    cadena = input(f'Ingrese {dato_a_validar}: ')

    while cadena == '':
        print(f'ERROR -> El {dato_a_validar} no debe estar vacio')
        validar_texto(dato_a_validar)

    texto = utn_capitalize(cadena)
    if texto != 'Masculino' :
        texto_no_binario = formatear_texto_no_binario(texto)
        texto = texto_no_binario

    return texto

def obtener_existencias(matriz: list[list]) -> int:
    """ Verifica si està cargada la matriz 
    :params: matriz - matriz 
    :returns: Devuelve el tamaño de la matriz """
    return len(matriz[0])