"""
Ejercicio nivel 2: Agenda de peliculas.
Módulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.
@author: Cupi2

NOTA IMPORTANTE PARA TENER EN CUENTA EN TODAS LAS FUNCIONES DE ESTE MODULO:
        Los diccionarios de pelicula tienen las siguientes parejas de clave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que día de la semana se planea ver la película
"""
def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, 
                  clasificacion: str, hora: int, dia: str) -> dict:
    """Crea un diccionario que representa una nueva película con toda su información 
       inicializada.
    Parámetros:
        nombre (str): Nombre de la pelicula agendada.
        genero (str): Generos de la pelicula separados por comas.
        duracion (int): Duracion en minutos de la pelicula
        anio (int): Anio de estreno de la pelicula
        clasificacion (str): Clasificacion de restriccion por edad
        hora (int): Hora a la cual se planea ver la pelicula, esta debe estar entre 
                    0 y 2359
        dia (str): Dia de la semana en el cual se planea ver la pelicula.
    Retorna:
        dict: Diccionario con los datos de la pelicula
    """    

    a,b = 'áéíóúü','aeiouu'
    trans = str.maketrans(a,b)
    
    pelicula={
    "nombre": nombre,
    "genero":genero,
    "duracion":duracion,
    "anio":anio,
    "clasificacion":clasificacion,
    "hora":hora,
    "dia":dia.translate(trans)
    
    }
    
    
    return pelicula

def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict,  p5: dict) -> dict:
    """Encuentra en cual de los 5 diccionarios que se pasan por parametro esta la 
       pelicula cuyo nombre es dado por parametro.
       Si no se encuentra la pelicula se debe retornar None.
    Parametros:
        nombre_pelicula (str): El nombre de la pelicula que se desea encontrar.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: Diccionario de la pelicula cuyo nombre fue dado por parametro. 
        None si no se encuentra una pelicula con ese nombre.
    """
 
    r=""
    nombre_pelicula=nombre_pelicula.lower()
    if nombre_pelicula==p1["nombre"].lower():
        r=p1
    elif nombre_pelicula==p2["nombre"].lower():
        r=p2
    elif nombre_pelicula==p3["nombre"].lower():
        r=p3
    elif nombre_pelicula==p4["nombre"].lower():
        r=p4
    elif nombre_pelicula==p5["nombre"].lower():
        r=p5
    else:
        r=None
    return r

def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    """Encuentra la pelicula de mayor duracion entre las peliculas recibidas por
       parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: El diccionario de la pelicula de mayor duracion
    """
   
    a=p1["duracion"]
    b=p2["duracion"]
    c=p3["duracion"]
    d=p4["duracion"]
    e=p5["duracion"] 
    pml={}
    r=max(a, b, c, d, e)
    if p1["duracion"]==r:
         pml=p1
    elif p2["duracion"]==r:
         pml=p2
    elif p3["duracion"]==r:
         pml=p3
    elif p4["duracion"]==r:
         pml=p4
    else:
        pml=p5
        
    return pml
        
    
            
    
    
    return None

def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> str:
    """Calcula la duracion promedio de las peliculas que entran por parametro. 
       Esto es, la duración total de todas las peliculas dividida sobre el numero de peliculas. 
       Retorna la duracion promedio en una cadena de formato 'HH:MM' ignorando los posibles decimales.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        str: la duracion promedio de las peliculas en formato 'HH:MM'
    """
    
    duracion_promedio=(p1["duracion"]+p2["duracion"]+p3["duracion"]+p4["duracion"]+p5["duracion"])/5
    
    if (duracion_promedio//60 < 10):
        hora_formato = "0"+ str(int(duracion_promedio//60))
    else:
        hora_formato = str(int(duracion_promedio//60))
    
    if (duracion_promedio%60 < 10):
        min_formato = "0"+ str(int(duracion_promedio%60))
    else:
        min_formato = str(int(duracion_promedio%60))
    return hora_formato + ":" + min_formato

def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int) -> str:
    """Busca entre las peliculas cuales tienen como anio de estreno una fecha estrictamente
       posterior a la recibida por parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
        anio (int): Anio limite para considerar la pelicula como estreno.
    Retorna:
        str: Una cadena con el nombre de la pelicula estrenada posteriormente a la fecha recibida. 
        Si hay mas de una pelicula, entonces se retornan los nombres de todas las peliculas 
        encontradas separadas por comas. Si ninguna pelicula coincide, retorna "Ninguna".
    """
    r=""
    
    if anio<p1["anio"]:
        r+=p1["nombre"]+","
    if anio<p2["anio"]:
        r+=p2["nombre"]+","
    if anio<p3["anio"]:
        r+=p3["nombre"]+","
    if anio<p4["anio"]:
        r+=p4["nombre"]+","
    if anio<p5["anio"]:
        r+=p5["nombre"]+","
    return r[:-1]+"."


def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
    """Indica cuantas peliculas de clasificación '18+' hay entre los diccionarios recibidos.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        int: Numero de peliculas con clasificacion '18+'
    """
    a=p1["clasificacion"]
    b=p2["clasificacion"]
    c=p3["clasificacion"]
    d=p4["clasificacion"]
    e=p5["clasificacion"]
    r=0
    if a=="18+":
        r+=1
    if b=="18+":
        r+=1
    if c=="18+":
        r+=1
    if d=="18+":
        r+=1
    if e=="18+":
        r+=1
        
    return r
    

def reagendar_pelicula(peli:dict, nueva_hora: int, nuevo_dia: str, 
                       control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->bool: 
    """Verifica si es posible reagendar la pelicula que entra por parametro. Para esto verifica
       si la nueva hora y el nuevo dia no entran en conflicto con ninguna otra pelicula, 
       y en caso de que el usuario haya pedido control horario verifica que se cumplan 
       las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula a reagendar
        nueva_hora (int): Nueva hora a la cual se quiere ver la pelicula
        nuevo_dia (str): Nuevo dia en el cual se quiere ver la pelicula
        control_horario (bool): Representa si el usuario quiere o no controlar
                                el horario de las peliculas.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        bool: True en caso de que se haya podido reagendar la pelicula, False de lo contrario.
    """
    p1_l=p1["dia"].lower()
    p2_l=p2["dia"].lower()
    p3_l=p3["dia"].lower()
    p4_l=p4["dia"].lower()
    p5_l=p5["dia"].lower()
    r=True
    franja_ocupada=(peli["duracion"]//60)*100+(peli["duracion"]%60)
    if r and peli!=p1: #pregunta si el dict peli (pelicula en la base) es diferente de (p1--dict), si es diferente verifica el espacio ocupado por p1
        hora_inicial=p1["hora"]
        hora_final=p1["hora"]+(p1["duracion"]//60)*100+p1["duracion"]%60
        if p1_l!=nuevo_dia or\
            not hora_inicial<nueva_hora<hora_final and\
                not hora_inicial<nueva_hora+(franja_ocupada)<hora_final:
            r=True
        else: 
            r=False
        
    if r and peli!=p2: #pregunta si el dict peli (pelicula en la base) es diferente de (p2--dict), si es diferente verifica el espacio ocupado por p2
        hora_inicial=p2["hora"]
        hora_final=p2["hora"]+(p2["duracion"]//60)*100+p2["duracion"]%60
        if p2_l!=nuevo_dia or\
            not hora_inicial<nueva_hora<hora_final and\
                not hora_inicial<nueva_hora+(franja_ocupada)<hora_final:
                    
            r=True
        else: 
            r=False
            
    if r and peli!=p3: #pregunta si el dict peli (pelicula en la base) es diferente de (p2--dict), si es diferente verifica el espacio ocupado por p2
        hora_inicial=p3["hora"]
        hora_final=p3["hora"]+(p3["duracion"]//60)*100+p3["duracion"]%60
        if p3_l!=nuevo_dia or\
            not hora_inicial<nueva_hora<hora_final and\
            not hora_inicial<nueva_hora+(franja_ocupada)<hora_final:
            r=True
        else: 
            r=False
            
    if r and peli!=p4: #pregunta si el dict peli (pelicula en la base) es diferente de (p2--dict), si es diferente verifica el espacio ocupado por p2
        hora_inicial=p4["hora"]
        hora_final=p4["hora"]+(p4["duracion"]//60)*100+p4["duracion"]%60
        if p4_l!=nuevo_dia or\
            not hora_inicial<nueva_hora<hora_final and\
            not hora_inicial<nueva_hora+(franja_ocupada)<hora_final:
            r=True
        else: 
            r=False
        
    if r and peli!=p5: 
        hora_inicial=p5["hora"]
        hora_final=p5["hora"]+(p5["duracion"]//60)*100+p5["duracion"]%60
        if p5_l!=nuevo_dia or\
            not hora_inicial<nueva_hora<hora_final and\
            not hora_inicial<nueva_hora+(franja_ocupada)<hora_final:
            r=True
        else: 
            r=False
    if r and control_horario:
        if "documental" in peli["genero"] and nueva_hora>=2200 or nueva_hora<=600:
            r=False
        if "drama" in peli["genero"] and nuevo_dia=="viernes":
            r=False
        if peli["dia"]!="sabado" or peli["dia"]!="domingo":
            if nueva_hora+franja_ocupada>=2300 or nueva_hora+franja_ocupada<=600:
                r=False
    return r    
    
def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool)->bool:
    """Verifica si es posible invitar a la persona cuya edad entra por parametro a ver la 
       pelicula que entra igualmente por parametro. 
       Para esto verifica el cumplimiento de las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula que se desea ver con el invitado
        edad_invitado (int): Edad del invitado con quien se desea ver la pelicula
        autorizacion_padres (bool): Indica si el invitado cuenta con la autorizacion de sus padres 
        para ver la pelicula
    Retorna:
        bool: True en caso de que se pueda invitar a la persona, False de lo contrario.
    """
    r=False
    
    if edad_invitado >= 18 or peli["clasificacion"]== "Todos" or autorizacion_padres:
        r=True
    else:
        a = int(peli["clasificacion"][:-1])
        if edad_invitado<15 and peli["genero"]=="terror":
            r=False
        if edad_invitado<=10 and peli["genero"]!="familiar":
            r=False
        if edad_invitado < a and autorizacion_padres:
            r=False
        if edad_invitado<a and "documental" in peli["genero"]:
            r=True
        
    return r
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    










