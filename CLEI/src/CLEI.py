# ------------------------------------------------------------------------------
# Clase que implementa CLEI
# ------------------------------------------------------------------------------
class CLEI():

    # constructor del CLEI
    def __init__(self):
        self.aceptables = []
        self.aceptados = []
        self.empatados = []

    # Metodo que retorna la lista de aceptables
    def getAceptables(self):
        return self.aceptables

    # Metodo que retorna la lista de aceptados
    def getAceptados(self):
        return self.aceptados
        
    # Metodo que devuelve la lista de empatados
    def getEmpatados(self):
        return self.empatados

    # Metodo que inserta una tupla (idArticulo, promedio) en la lista de los 
    # aceptables
    def setAceptables(self, idArticulo, promedio):
        t = (idArticulo, promedio)
        self.aceptables.append(t)

    # Metodo que inserta el id de articulo en la lista de aceptados
    def setAceptados(self, idArticulo):
        self.aceptados.append(idArticulo)

    # Metodo que inserta el id de articulo en la lista de empatados
    def setEmpatados(self, idArticulo):
        self.empatados.append(idArticulo)

    # Metodo que crea la lista de aceptables
    def crearAceptables(self, listaEvaluaciones):
        # Tamano de la lista de evaluaciones
        tamEvaluaciones = len(listaEvaluaciones)
        for i in range(tamEvaluaciones):
            # condicion minima de ser aceptable
            # Mas de un arbitro y puntuacion mayor a 3
            if len(listaEvaluaciones[i][1][0]) > 1: 
                if listaEvaluaciones[i][1][1] >= 3.0:
                    self.setAceptables(listaEvaluaciones[i][0], listaEvaluaciones[i][1][1])

    # Metodo que crea las listas de empatados y aceptados
    def crearAceptadosYEmpatados(self, tamAceptables, numArticulos, articulos):
        promedios = []
        
        # Ciclo que inserta en la lista promedios solo los promedios de los 
        # articulos aceptables
        for i in range(tamAceptables):
            promedios.append(self.getAceptables()[i][1])

        i = 0
        j = 0
        
        # Ciclo que recorre la lista de promedios y cuenta las veces en que 
        # aparece un promedio para insertarlo en la lista de aceptados o
        # empatados
        while i<tamAceptables:
            # Se cuenta las veces en que aparece el valor de promedios[i]
            contar = promedios.count(promedios[i])
            
            # Llenando lista de ACEPTADOS
            # Si contar es menor a la cantidad de articulos que deben ser
            # aceptados en el congreso, insertamos los articulos correspondientes
            # a ese promedio en la lista de aceptados
            if contar <= numArticulos:
                j = i
                # variable que cuenta las veces que debe ingresar un elemento a
                # la lista de acuerdo a la variable contar
                temp = 0
                while j < tamAceptables:
                    
                    # Caso en que aun no se han agregado la cantidad de articulos
                    # indicados por la variable contar
                    if temp != contar:
                        # Asignamos True al articulo para indicar que fue 
                        # aceptado
                        
                        # Agregamos el id del articulo a la lista de aceptados
                        idArticulo = self.getAceptables()[j][0]
                        self.setAceptados(idArticulo)
                        
                        # Asignamos True al atributo aceptado del articulo
                        articulos[idArticulo].setAceptado(True)
                        
                        j = j + 1
                        # Sumamos uno a la variable temporal
                        temp = temp + 1
                        
                    else: # Caso en que ya se han agregado los articulos
                        break
                # Reduzco el numero de articulos a ser aceptados     
                numArticulos = numArticulos - contar
                # Posicionamos i en i + contar del arreglo 
                i = i + contar
            
            else: # Llenando la lista de EMPATADOS
                j = i
                # variable que cuenta las veces que debe ingresar un elemento a
                # la lista de acuerdo a la variable contar
                temp = 0
                while j < tamAceptables:
                    
                    # Caso en que aun no se han agregado la cantidad de articulos
                    # indicados por la variable contar
                    if temp != contar:
                        # Agregamos a la lista de empatados
                        self.setEmpatados(self.getAceptables()[j][0])
                        j = j + 1
                        # Sumamos uno a la variable temporal
                        temp = temp + 1
                    else: # Caso en que ya se han agregado los articulos
                        break
                break
        # Retorna el numero de espacios restantes en la lista de aceptados       
        return numArticulos     

        def seleccion_desempate(self, num, articulos):
            tamAceptables = len(self.getAceptables())
            print 'tam aceptables: ', tamAceptables
            limite = self.crearAceptadosYEmpatados(tamAceptables, num, articulos)

            # Caso en que quedan articulos en la lista de empatados.
            if len(self.getEmpatados()) != 0:
                # Caso en que queda espacio en la lista de aceptados
                if limite != 0:
                    print 'A continuacion se le presentan la lista de los articulos pertenecientes a la lista de empatados: \n'
                    print self.getEmpatados()
                    print '\nA continuacion se le presentan la lista de los articulos que ya pertenecen a la lista de aceptados: \n'
                    print self.getAceptados()
                    print '\nEspacio restante en la lista de empatados: ', limite
                    print '\nEscoja de entre los empatados aquellos que pasaran a los aceptados:\n'

                    # Mientras haya espacio en la lista de aceptados
                    while limite>0:
                        try:
                            id = int(raw_input(' Indique id del articulo a seleccionar: '))
                            # Si el id pertenece a la lista de empatados
                            if id in self.getEmpatados():
                                self.setAceptados(id)
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
                
            return self.getAceptados()
            