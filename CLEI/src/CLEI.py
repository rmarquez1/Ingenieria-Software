from Persona import Comite
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
    
    # Retorna el numero de articulos que se presentaran en la conferencia
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

    # Asigna los autores a un articulos
    def asignar_autores(self, id, nombre_autor, inst_afil, pais):
        self.articulos[id].set_autores(nombre_autor, inst_afil, pais)
        
    # Inserta en el diccionario de articulos y en la lista un articulo
    def crear_articulos(self, id_articulo, articulo):
        self.articulos[id_articulo] = articulo
        self.lista_articulos.append(articulo)

    # Inserta en el diccionario de miembros de cp un miembro
    def crear_miembros_cp(self, nombre, apellido, inst_afil, correo):
        comite = Comite(nombre, apellido, inst_afil,correo)
        self.miembros_cp[correo] = comite

    # Asigna como presidente a un miembro de comite de programa
    def asignar_presidente_comite(self, presidente):
        # Verificamos que no haya otro presidente
        lista_correos = self.miembros_cp.keys()

        # Variable que indica si se consigue algun presidente
        temp = 0
        for i in range(len(lista_correos)):
            # Caso en el que se consigue un presidente
            if self.miembros_cp[lista_correos[i]].get_es_presidente() == True:
                temp = 1
                break
        # Caso en que no se consigue alguien como presidente     
        if temp != 1:
            #comite.set_es_presidente(True)
            self.miembros_cp[presidente].set_es_presidente(True)
            return True
        else:
            print 'Ya existe un presidente en el comite de programa'
        return False
    
    # Retorna True si existe un articulo en el diccionario dado su id
    def verificar_id(self, id_articulo):
        if self.articulos.has_key(id_articulo):
            return True
        return False
    
    # Retorna True si existe un miembro cp en el diccionario dado su correo
    def verificar_correo(self, correo):
        if self.miembros_cp.has_key(correo):
            return True
        return False
    

     # Metodo que asigna un arbitro y la puntuacion al articulo     
    def asignar_arbitro_puntuacion(self, id_articulo, correo, puntaje):
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
        

    # Devuelve una lista con los arbitros y puntuaciones del articulo 
    def lista_arbitro_puntuacion(self, cont):
        lista = []
        
        # Ciclo que agrega a la lista la tupla (arbitro, puntuacion)
        for i in range(len(self.lista_articulos[cont].get_arbitros())):
            # Tupla (arbitro, puntuacion)
            t = (self.lista_articulos[cont].get_arbitros()[i], 
                 self.lista_articulos[cont].get_puntuacion()[i])
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
                
    # Metodo que crea la lista de aceptables
    def crear_aceptables(self):
        if len(self.evaluaciones) != 0:
            lista_evaluaciones = self.evaluaciones.items()
            #print 'lista evaluaciones: ', lista_evaluaciones
            # Ordenamos por promedio
            lista_evaluaciones.sort(key=lambda x: x[1][1])
            #Invertimos la lista
            lista_evaluaciones.reverse()
            # Tamano de la lista de evaluaciones
            tamEvaluaciones = len(lista_evaluaciones)
            for i in range(tamEvaluaciones):
                # condicion minima de ser aceptable
                # Mas de un arbitro y puntuacion mayor a 3
                if len(lista_evaluaciones[i][1][0]) >= 2: 
                    if lista_evaluaciones[i][1][1] >= 3.0:
                        self.set_aceptables(lista_evaluaciones[i][0], 
                                            lista_evaluaciones[i][1][1])

    # Retorna una lista con los promedios de articulos en una lista dada
    def listar_promedios(self, lista):
        promedios = []
        tam = len(lista)
        # Ciclo que inserta en la lista promedios solo los promedios de los 
        # articulos aceptables
        for i in range(tam):
            promedios.append(lista[i][1])
        return promedios

    # Metodo que crea las listas de empatados y aceptados
    def crear_aceptados_empatados(self, promedios, lista):
        tam = len(promedios)
        i = 0
        j = 0
        
        # Ciclo que recorre la lista de promedios y cuenta las veces en que 
        # aparece un promedio para insertarlo en la lista de aceptados o
        # empatados
        while i<tam:
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
                while j < tam:
                    
                    # Caso en que aun no se han agregado la cantidad de articulos
                    # indicados por la variable contar
                    if temp != contar:
                        # Asignamos True al articulo para indicar que fue 
                        # aceptado
                        
                        # Agregamos el id del articulo a la lista de aceptados
                        id_articulo = lista[j][0]
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
                while j < tam:
                    
                    # Caso en que aun no se han agregado la cantidad de articulos
                    # indicados por la variable contar
                    if temp != contar:
                        # Agregamos a la lista de empatados
                        self.set_empatados(lista[j][0])
                        j = j + 1
                        # Sumamos uno a la variable temporal
                        temp = temp + 1
                    else: # Caso en que ya se han agregado los articulos
                        break
                break
        # Retorna el numero de espacios restantes en la lista de aceptados       
        return self.num_articulos     

    # Inserta en el diccionario de evaluaciones una lista de tuplas
    # (articulo, puntuacion) y el promedio del articulo
    def agregar_evaluaciones(self, id_articulo, cont):
        # Creamos una lista cuyos elementos son tuplas correspondientes a
        # (arbitro, puntuacion)
        lista = self.lista_arbitro_puntuacion(cont)

        # Agregamos al diccionario de evaluaciones
        promedio = self.lista_articulos[cont].calcular_promedio()
        self.evaluaciones[id_articulo] = lista, promedio    
    
    # Esquema de seleccion por desempate
    def seleccionar_desempate(self, id):
        if id in self.get_empatados():
            self.set_aceptados(id)
        else:
            print 'Este id no esta en la lista de empatados'

    # Retorna una lista con los ids de los articulos pertenecientes a la lista
    # de aceptables
    def listar_id_aceptables(self):
        lista_id_articulos = []
        # Ciclo que agrega a la lista de articulos los ids de los articulos
        # pertenecientes a la lista de aceptables
        for i in range(len(self.aceptables)):
            lista_id_articulos.append(self.aceptables[i][0])
        return lista_id_articulos
        
    # Generamos una lista con todos los paises del congreso que enviaron sus
    # articulos al congreso
    def paises_conferencia(self):
        lista_paises = []

        lista_id_articulos = self.listar_id_aceptables()
            
        tam_articulos = len(lista_id_articulos)
        # Ciclo que recorre la lista de articulos aceptables con cada id y 
        # asigna el pais de los articulos que estan de primero en la lista de 
        # autores de cada articulo
        for i in range(tam_articulos):
            # Obtenemos el pais que esta de primero en la lista de autores
            pais = self.articulos[lista_id_articulos[i]].get_autores()[0].get_pais()
            # Si no esta el pais en la lista de articulos
            esta_pais = pais in lista_paises
            if  esta_pais == False:
                lista_paises.append(pais)
                
        return lista_paises
    
    # Retorna una lista con las notas de los articulos presentados por un pais
    # dado y que pertenece a la lista de aceptables
    def listar_notas_por_pais(self, pais):
        lista_notas = []
        tam_aceptables = len(self.aceptables)
        # Ciclo que verifica que el pais de cada articulo sea igual al dado 
        # y este es insertado en la lista
        for i in range(tam_aceptables):
            pais1=self.articulos[self.aceptables[i][0]].get_autores()[0].get_pais()
            if  pais1 == pais:
                lista_notas.append(self.aceptables[i])
        # Ordenamos de mayor a menor por nota
        lista_notas.sort(key=lambda x:x[1], reverse = True)
        return lista_notas

    # Retorna una lista cuyos elementos son tuplas (pais, [lista de notas])
    def listar_articulos_por_pais(self, num_articulos_por_pais):
        # Creamos una lista que contendra tuplas ('Pais', [articulos])
        lista_paises = []
        # Generemos lista de los paises cuyos articulos son aceptables
        lista = self.paises_conferencia()
        tam_lista = len(lista)
        for i in range(tam_lista):
            # Obtenemos una lista con los articulos del pais en la posicion i
            lista_notas_por_pais = self.listar_notas_por_pais(lista[i])
            tam_lista_pais = len(lista_notas_por_pais)
            # Si la cantidad de articulos del pais es mayor o igual al minimo 
            # de articulos por pais
            if tam_lista_pais >= num_articulos_por_pais:
                l = []
                for j in range(tam_lista_pais):
                    l.append(lista_notas_por_pais[j])
                # Creamos una tupla ('Pais', [articulos])
                t = (lista[i], l)
                # Agregas a la lista paises
                lista_paises.append(t)
            # Ordenamos la lista de menor a mayor dependiendo de la cantidad de
            # articulos aceptables por pais
            lista_paises.sort(key=lambda x:len(x[1]))
        return lista_paises
    
    # Retorna una lista con las tuplas (pais, [lista de notas]) donde esa lista
    # de notas contiene la cantidad minima de articulos
    def cantidad_min_articulos(self, num_articulos_por_pais):
        lista_min = []
        lista_paises = self.listar_articulos_por_pais(num_articulos_por_pais)
        tam_lista_paises = len(lista_paises)
        
        for i in range(tam_lista_paises):
            # Tamanio de la lista de notas de cada pais
            tam = len(lista_paises[i][1])
            j = 0
            # Creamos una lista que contendra los articulos (notas)
            l = []
            # Ciclo que agrega en una lista el numero minimo de articulos por 
            # pais
            while j < num_articulos_por_pais:
                l.append(lista_paises[i][1][j])
                #del lista_paises[i][1][j]
                j += 1
                # Eliminamos la nota que agregamos a la lista
                
            t = (lista_paises[i][0], l)
            lista_min.append(t)
        #print 'Lista_ PAISES: ', lista_paises
        return lista_min
    
    # Tipo de seleccion por pais
    def agregar_aceptados(self, num_articulos_por_pais):
        lista_minimos = self.cantidad_min_articulos(num_articulos_por_pais)
        tam_minimos = len(lista_minimos)
        for i in range(tam_minimos):
            tam = len(lista_minimos[i][1])
            j = 0
            while j < tam:
                # Insertamos a la lista de aceptados
                self.set_aceptados(lista_minimos[i][1][j][0])
                self.num_articulos -= 1 
                j += 1
        return self.num_articulos

    # Imprime los elementos de la lista de empatados
    def mostrar_empatados(self):
        tam = len(self.empatados)
        for i in range(tam):
            pais = self.articulos[self.empatados[i]].get_autores()[0].get_pais()
            print '( Pais: ', pais, ', id: ', self.empatados[i], ')'
                    
    # Imprime los elementos de la lista de aceptados
    def mostrar_aceptados(self):
        tam = len(self.aceptados)
        for i in range(tam):
            pais = self.articulos[self.aceptados[i]].get_autores()[0].get_pais()
            print '( Pais: ', pais, ', id: ', self.aceptados[i], ')'
            
    # Metodo que muestra los paises de menos representados a mas representados
    def mostrar_representados_ascendentes(self, num_articulos_por_pais):
        lista_paises = self.listar_articulos_por_pais(num_articulos_por_pais)
        tam = len(lista_paises)
        for i in range(tam):
            print lista_paises[i]
            
    # Metodo que genera una lista de aquellos articulos que no estan en la lista
    # de aceptados
    def listar_no_aceptados(self,num_articulos_por_pais):
        # Generamos una lista donde estaran los articulos que aun no han
        # sido aceptados
        lista_por_seleccionar = []
        lista_articulos = self.listar_articulos_por_pais(num_articulos_por_pais)
        tam_paises = len(lista_articulos)
        for i in range(tam_paises):
            # Generamos una lista con los articulos representados del pais i
            lista = self.listar_notas_por_pais(lista_articulos[i][0])
            #print 'lista articulos: '
            #print lista
            l = []
            tam = len(lista)
            # Ciclo que construye una lista con aquellos paises y sus articulos
            # que aun no pertenecen a la lista aceptados. Esto para manejar
            # la escogencia de articulos cuando el numero de articulos es mayor
            # que la cantidad de articulos aceptados por el momento
            for j in range(tam):
                
                res = lista[j][0] in self.aceptados
                # Caso en que el id del articulo no pertenezca a los aceptados
                if res == False:
                    l.append(lista[j])
            # Caso en que se consiguio articulos que no han sido aceptados
            if len(l) != 0:
                t = (lista_articulos[i][0], l)
                lista_por_seleccionar.append(t)
                    
        return lista_por_seleccionar

    # Metodo que selecciona los articulos restantes para completar la capacidad
    # maximo de articulos escogidos en la conferencia
    def seleccionar_por_pais(self, num_articulos_por_pais):
        lista_no_aceptados = self.listar_no_aceptados(num_articulos_por_pais)
        tam_lista = len(lista_no_aceptados)
        
        for i in range(tam_lista):
            promedios = self.listar_promedios(lista_no_aceptados[i][1])
            self.crear_aceptados_empatados(promedios, lista_no_aceptados[i][1])

    # Estrategia 3 (segun documento) del requisito de seleccion de articulos
    def aceptar_por_notas_corte(self, n1, n2):
        aceptados     = []
        participacion = {}
        pendientes    = {}
        capacidad     = self.num_articulos
        articulos     = sorted(self.aceptables, key=(lambda x : x[1]), reverse=True)

        if n2 >= n1:
            raise ValueError

        for articulo in articulos:
            id_articulo = articulo[0]
            promedio    = articulo[1]
            pais        = self.articulos[id_articulo].get_pais()

            if len(aceptados) == capacidad:
                self.aceptados = aceptados
                return

            if not pais in participacion:
                participacion[pais] = 0
                pendientes[pais]    = []

            if promedio >= n1:
                aceptados.append(id_articulo)
                self.articulos[id_articulo].set_aceptado(True)
                participacion[pais] += 1

            elif promedio >= n2:
                pendientes[pais].append(id_articulo)

            else:
                break

        prioridad = sorted(participacion.keys(), key=(lambda x : participacion[x]))

        for pais in prioridad:

            while pendientes[pais] and capacidad > len(aceptados):
                id_articulo = pendientes[pais].pop(0)
                aceptados.append(id_articulo)
                self.articulos[id_articulo].set_aceptado(True)

        self.aceptados = aceptados

