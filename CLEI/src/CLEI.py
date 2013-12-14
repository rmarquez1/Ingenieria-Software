from Articulo import *
from Persona import *
import sys
# ------------------------------------------------------------------------------
# Clase que implementa CLEI
# ------------------------------------------------------------------------------
class CLEI():

    # constructor del CLEI
    def __init__(self, num_articulos):
        self.num_articulos = num_articulos
        self.aceptables = []
        self.aceptados = []
        self.empatados = []
        self.articulos = {}
        self.lista_articulos = []
        self.miembros_cp = {}
        self.evaluaciones = {}
        self.inscritos = {}

    def get_number(self, msg):
      while 1:
        try:
          num = int(raw_input("%s: " % msg))
        except ValueError:
          sys.stderr.write("El valor no es un numero...\n")
          continue
        return num
    
    def get_num_articulos(self):
        return self.num_articulos
    
    # Metodo que retorna la lista de aceptables
    def get_aceptables(self):
        return self.aceptables

    # Metodo que retorna la lista de aceptados
    def get_aceptados(self):
        return self.aceptados
        
    # Metodo que devuelve la lista de empatados
    def get_empatados(self):
        return self.empatados

    # Metodo que inserta una tupla (idArticulo, promedio) en la lista de los 
    # aceptables
    def set_aceptables(self, id_articulo, promedio):
        t = (id_articulo, promedio)
        self.aceptables.append(t)

    # Metodo que inserta el id de articulo en la lista de aceptados
    def set_aceptados(self, id_articulo):
        self.aceptados.append(id_articulo)

    # Metodo que inserta el id de articulo en la lista de empatados
    def set_empatados(self, id_articulo):
        self.empatados.append(id_articulo)

    def asignar_autores(self, id, num):
        for i in range(num):
            nombre_autor = raw_input('Indique el nombre del autor: ')
            inst_afil = raw_input('Indique la institucion principal: ')
            pais = raw_input('Indique el pais proveniente: ')
            self.articulos[id].set_autores(nombre_autor, inst_afil, pais)
        
    def crear_articulos(self):
        while True:
            res = raw_input('Crear articulo (s/n): ')
            if res == 's' or res == 'S':
                id_articulo = int(raw_input('ID: '))
                if self.articulos.has_key(id_articulo):
                    print 'Ya existe articulo con ese id'
                else:
                    titulo = raw_input('Titulo: ')
                    resumen = raw_input('Resumen: ')
                    texto = raw_input('Texto: ')

                    while True:
                        try:
                            num_p_claves = int(raw_input('Indique cuantas palabras claves desea asignar al articulo: '))

                            if num_p_claves < 1 or num_p_claves > 5:
                                print '\nPuede asignar minimo 1 y maximo 5 palabras claves\n'

                            else:
                                if num_p_claves == 1:
                                    p_clave = raw_input('Palabra clave: ')
                                    articulo = Articulo(id_articulo, titulo, resumen, texto, p_clave)

                                elif num_p_claves == 2:
                                    p_clave1 = raw_input('Palabra clave: ')
                                    p_clave2 = raw_input('Palabra clave: ')
                                    articulo = Articulo(id_articulo, titulo, resumen, texto, p_clave1, p_clave2)

                                elif num_p_claves == 3:
                                    p_clave1 = raw_input('Palabra clave: ')
                                    p_clave2 = raw_input('Palabra clave: ')
                                    p_clave3 = raw_input('Palabra clave: ')
                                    articulo = Articulo(id_articulo, titulo, resumen, texto, p_clave1, p_clave2, p_clave3)

                                elif num_p_claves == 4:
                                    p_clave1 = raw_input('Palabra clave: ')
                                    p_clave2 = raw_input('Palabra clave: ')
                                    p_clave3 = raw_input('Palabra clave: ')
                                    p_clave4 = raw_input('Palabra clave: ')
                                    articulo = Articulo(id_articulo, titulo, resumen, texto, p_clave1, p_clave2, p_clave3, p_clave4)

                                elif num_p_claves == 5:
                                    p_clave1 = raw_input('Palabra clave: ')
                                    p_clave2 = raw_input('Palabra clave: ')
                                    p_clave3 = raw_input('Palabra clave: ')
                                    p_clave4 = raw_input('Palabra clave: ')
                                    p_clave5 = raw_input('Palabra clave: ')
                                    articulo = Articulo(id_articulo, titulo, resumen, texto, p_clave1, p_clave2, p_clave3, p_clave4, p_clave5)


                                num_autores = self.get_number('Indique cantidad de autores')
                                self.lista_articulos.append(articulo)
                                self.articulos[id_articulo] = articulo
                                self.asignar_autores(id_articulo, num_autores)
                                self.articulos[id_articulo].imprimir_autores()
                                break

                        except ValueError:
                            print '\n Opcion invalida\n'

            elif res == 'n' or res == 'N':
                break
            else:
                print '\nIndique s/n\n'

    def crear_miembros_cp(self):
        while True:
            res = raw_input('Crear miembro del CP (s/n): ')
            if res == 's' or res == 'S':
                correo = raw_input('Correo: ')

                if self.miembros_cp.has_key(correo):
                    print 'Ya existe un miembro con ese correo. Intentelo de nuevo'
                else:
                    nombre = raw_input('Nombre: ')
                    apellido = raw_input('Apellido: ')
                    inst_afil = raw_input('Institucion Principal: ')
                    comite = Comite(nombre, apellido, inst_afil,correo)
                    self.miembros_cp[correo] = comite

            elif res == 'n' or res == 'N':
                break
            else:
                print 'Indique s/n'

    def asignar_presidente_comite(self):
        if len(self.miembros_cp) != 0:
            while True:
                presidente = raw_input('Indique el presidente del comite de programa: ')
                if self.miembros_cp.has_key(presidente):
                    # Verificamos que no haya otro presidente
                    lista_correos = self.miembros_cp.keys()

                    # Variable que indica si se consigue algun presidente
                    temp = 0
                    for i in range(len(lista_correos)):
                        # Caso en el que se consigue un presidente
                        print 'PASO POR EL FOR'
                        if self.miembros_cp[lista_correos[i]].get_es_presidente() == True:
                            temp = 1
                            break
                    print 'valor del temp', temp
                    # Caso en que no se consigue alguien como presidente     
                    if temp != 1:
                        #comite.set_es_presidente(True)
                        self.miembros_cp[presidente].set_es_presidente(True)
                        #print self.miembros_cp[presidente].get_nombre(), ' ', self.miembros_cp[presidente].get_es_presidente()
                        print 'FIN'
                        break
                    else:
                        print 'Ya existe un presidente en el comite de programa'
                    break
                else:
                    print 'Miembro inexistente. Intente de nuevo'
        else:
            print 'No existe miembros en el comite de programa. Debe crearlos'   
            
            
     # Metodo que asigna un arbitro y la puntuacion al articulo
    def asignar_arbitro_puntuacion(self, id_articulo,correo):
        while True:
            puntaje = int(raw_input('    Ingrese el puntaje: '))
            # Si el puntaje esta en el rango de 1 a 5
            if puntaje >= 1 and puntaje <= 5:
                if self.articulos.has_key(id_articulo):
                    # Ciclo para asignarle puntuacion a cada articulo
                    cont = 0
                    for i in range(len(self.lista_articulos)):
                        if id_articulo != self.lista_articulos[i].get_id_articulo():
                            cont += 1
                        else:
                            break

                    # Al encontrar el articulo le asigno la nota y el arbitro
                    # que lo califico        
                    self.lista_articulos[cont].set_puntuacion(puntaje)
                    self.lista_articulos[cont].set_arbitros(correo)

                    return cont
                    break
            else: 
                print 'La nota debe ser de 1 a 5. Intentelo de nuevo'
            break
        
    
    def asignar_puntuacion_arbitros_articulos(self):
        while True:
            if len(self.miembros_cp)>0 and len(self.articulos)>0:
                res = raw_input('   Crear arbitros y puntuaciones (s/n): ')
                if res == 's' or res == 'S':    
                    id_articulo = int(raw_input('    ID del articulo a evaluar:' ))

                    if self.articulos.has_key(id_articulo):
                        while True:

                            correo = raw_input('    Correo del arbitro: ')
                            if self.miembros_cp.has_key(correo):
                                # Verificamos que ese arbitro no haya evaluado este articulo
                                ya_evaluo = self.verificar_arbitro_evaluo(id_articulo, correo)
                                if  ya_evaluo == False:
                                    # Verificamos el rango de la nota de 1 a 5
                                    cont = self.asignar_arbitro_puntuacion(id_articulo, correo)
                                else:
                                    print 'Este miembro de comite ya evaluo este articulo'
                                    
                                # Caso en que otro arbitro califique el mismo articulo    
                                r = raw_input('    Agregar otro arbitro (s/n):' )
                                if r == 'N' or r == 'n':
                                    break
                            else:
                                print 'No existe arbitro con ese correo'

                        # Creamos una lista cuyos elementos son tuplas correspondientes a
                        # (arbitro, puntuacion)
                        lista = self.lista_arbitro_puntuacion(cont)

                        # Agregamos al diccionario de evaluaciones
                        self.evaluaciones[id_articulo] = lista, self.lista_articulos[cont].calcular_promedio()
                        # RECORDAR VER SI UN ARBITRO EVALUA DOS VECES EL MISMO ARTICULO
                    else:
                        print '\nNo existe articulo con ese id\n'    

                elif res == 'n' or res == 'N':
                    if len(self.evaluaciones) != 0:
                        lista_evaluaciones = self.evaluaciones.items()
                        print 'lista evaluaciones: ', lista_evaluaciones
                        # Ordenamos por promedio
                        lista_evaluaciones.sort(key=lambda x: x[1][1])
                        #Invertimos la lista
                        lista_evaluaciones.reverse()
                        self.crear_aceptables(lista_evaluaciones)
                    break
                else:
                    print 'Indique s/n'

                print self.evaluaciones
            else:
                print '''No hay informacion suficiente para realizar esta operacion. Verifique que haya creado articulos
y miembros de comite de programa'''  

    # Devuelve una lista con los arbitros y puntuaciones del articulo 
    def lista_arbitro_puntuacion(self, cont):
        lista = []
        
        # Ciclo que agrega a la lista la tupla (arbitro, puntuacion)
        for i in range(len(self.lista_articulos[cont].get_arbitros())):
            # Tupla (arbitro, puntuacion)
            t = (self.lista_articulos[cont].get_arbitros()[i], self.lista_articulos[cont].get_puntuacion()[i])
            # Agregamos a la lista
            lista.append(t)  
             
        return lista
    
    # Verifica que ya un arbitro evaluo un articulo
    def verificar_arbitro_evaluo(self, id_articulo, correo):
        lista_arbitros = self.articulos[id_articulo].get_arbitros()
        for i in range(len(lista_arbitros)):
            if correo == lista_arbitros[i]:
                return True
        return False
                
# ------------------------------------------------------
# INSCRIBIR PARTICIPANTES, HACER GABRIEL GEDLER
# ------------------------------------------------------


# ----------------------------------------------------


    # Metodo que crea la lista de aceptables
    def crear_aceptables(self, lista_evaluaciones):
        # Tamano de la lista de evaluaciones
        tamEvaluaciones = len(lista_evaluaciones)
        for i in range(tamEvaluaciones):
            # condicion minima de ser aceptable
            # Mas de un arbitro y puntuacion mayor a 3
            if len(lista_evaluaciones[i][1][0]) > 1: 
                if lista_evaluaciones[i][1][1] >= 3.0:
                    self.set_aceptables(lista_evaluaciones[i][0], lista_evaluaciones[i][1][1])

    # Metodo que crea las listas de empatados y aceptados
    def crear_aceptados_empatados(self, tam_aceptables):
        promedios = []
        
        # Ciclo que inserta en la lista promedios solo los promedios de los 
        # articulos aceptables
        for i in range(tam_aceptables):
            promedios.append(self.get_aceptables()[i][1])

        i = 0
        j = 0
        
        # Ciclo que recorre la lista de promedios y cuenta las veces en que 
        # aparece un promedio para insertarlo en la lista de aceptados o
        # empatados
        while i<tam_aceptables:
            # Se cuenta las veces en que aparece el valor de promedios[i]
            contar = promedios.count(promedios[i])
            
            # Llenando lista de ACEPTADOS
            # Si contar es menor a la cantidad de articulos que deben ser
            # aceptados en el congreso, insertamos los articulos correspondientes
            # a ese promedio en la lista de aceptados
            if contar <= self.num_articulos:
                j = i
                # variable que cuenta las veces que debe ingresar un elemento a
                # la lista de acuerdo a la variable contar
                temp = 0
                while j < tam_aceptables:
                    
                    # Caso en que aun no se han agregado la cantidad de articulos
                    # indicados por la variable contar
                    if temp != contar:
                        # Asignamos True al articulo para indicar que fue 
                        # aceptado
                        
                        # Agregamos el id del articulo a la lista de aceptados
                        id_articulo = self.get_aceptables()[j][0]
                        self.set_aceptados(id_articulo)
                        
                        # Asignamos True al atributo aceptado del articulo
                        self.articulos[id_articulo].set_aceptado(True)
                        
                        j = j + 1
                        # Sumamos uno a la variable temporal
                        temp = temp + 1
                        
                    else: # Caso en que ya se han agregado los articulos
                        break
                # Reduzco el numero de articulos a ser aceptados     
                self.num_articulos -= contar
                # Posicionamos i en i + contar del arreglo 
                i = i + contar
            
            else: # Llenando la lista de EMPATADOS
                j = i
                # variable que cuenta las veces que debe ingresar un elemento a
                # la lista de acuerdo a la variable contar
                temp = 0
                while j < tam_aceptables:
                    
                    # Caso en que aun no se han agregado la cantidad de articulos
                    # indicados por la variable contar
                    if temp != contar:
                        # Agregamos a la lista de empatados
                        self.set_empatados(self.get_aceptables()[j][0])
                        j = j + 1
                        # Sumamos uno a la variable temporal
                        temp = temp + 1
                    else: # Caso en que ya se han agregado los articulos
                        break
                break
        # Retorna el numero de espacios restantes en la lista de aceptados       
        return self.num_articulos     

    def seleccion_desempate(self):
        correo_presi = raw_input('Indique su correo como presidente: ')
        # si el correo pertenece al correo de los miembros registrados

        if self.miembros_cp.has_key(correo_presi):
            # Verificamos que el correo ingresado sea el correo del presidente
            if self.miembros_cp[correo_presi].get_es_presidente() == True:
                print '-----------------------------------------------'
                print 'Bienvenido presidente del comite de programa.\n'
                print '\nElija entre las siguientes opciones:\n'

                while True:
                    print ' 1. Ver lista de articulos aceptables.\n'
                    print ' 2. Generar articulos a ser aceptados en la conferencia.\n'
                    print ' 0. SALIR'

                    try:
                        res = int(raw_input('   Indique el tipo de operacion: '))
                        if res == 0:
                            print 'Finalizo la seleccion de articulos'
                            break

                        elif res == 1:
                            print 'ACEPTABLES: ', self.get_aceptables()

                        elif res == 2:
                            tam_aceptables = len(self.get_aceptables())
                            print 'tam aceptables: ', tam_aceptables
                            limite = self.crear_aceptados_empatados(tam_aceptables)

                            # Caso en que quedan articulos en la lista de empatados.
                            if len(self.get_empatados()) != 0:
                                # Caso en que queda espacio en la lista de aceptados
                                if limite != 0:
                                    print 'A continuacion se le presentan la lista de los articulos pertenecientes a la lista de empatados: \n'
                                    print self.get_empatados()
                                    print '\nA continuacion se le presentan la lista de los articulos que ya pertenecen a la lista de aceptados: \n'
                                    print self.get_aceptados()
                                    print '\nEspacio restante en la lista de empatados: ', limite
                                    print '\nEscoja de entre los empatados aquellos que pasaran a los aceptados:\n'

                                    # Mientras haya espacio en la lista de aceptados
                                    while limite>0:
                                        try:
                                            id = int(raw_input(' Indique id del articulo a seleccionar: '))
                                            # Si el id pertenece a la lista de empatados
                                            if id in self.get_empatados():
                                                self.set_aceptados(id)
                                                limite -= 1
                                            else:
                                                print 'Este id no esta en la lista de empatados'

                                        except ValueError:
                                            print 'Valor de id invalido'

                                else:
                                    print 'La lista de articulos aceptados ya esta llena.\n'
                                    break

                            # Si no hay articulos en la lista de empatados no se realiza
                            # escogencia
                            else:
                                print 'No existen articulos en la lista de empatados.\n'
                                break

                    # End try res
                    except ValueError:
                        print 'Opcion invalida'
            else:
                print 'Lo sentimos, ud no esta autorizado para esta operacion...'

        else:
            print 'Lo sentimos, este correo no pertenece a los miembros del comite. Intente de nuevo'


        return self.get_aceptados()
