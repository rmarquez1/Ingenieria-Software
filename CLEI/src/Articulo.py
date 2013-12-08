# ------------------------------------------------------------------------------
# Clase que implementa informacion de los articulos del congreso
# ------------------------------------------------------------------------------
class Articulo():

    # Contructor del articulo
    def __init__(self, idArticulo=None, titulo=None, resumen=None, texto=None, p1=None, p2=None, p3=None, p4=None,p5=None):
        self.idArticulo = idArticulo
        self.titulo = titulo
        self.pClaves = []
        self.resumen = resumen
        self.texto = texto
        self.esAceptado = False
        self.arbitro = []
        self.puntuacion = []
        self.pClaves.append(p1)
        if p2 != None:
            self.pClaves.append(p2)
        if p3 != None:
            self.pClaves.append(p3)
        if p4 != None:
            self.pClaves.append(p4)
        if p5 != None:
            self.pClaves.append(p5)
       

    # Metodo que retorna el id del articulo
    def getIdArticulo(self):
        return self.idArticulo
        
    # Metodo que retorna el titulo del articulo
    def getTitulo(self):
        return self.titulo 
    
    # Metodo que devuelve la lista de las palabras claves del articulo
    def getPClaves(self):
        return self.pClaves

    # Metodo que retorna el resumen del articulo    
    def getResumen(self):
        return self.resumen

    # Metodo que retorna el texto del articulo        
    def getTexto(self):
        return self.texto
    
    # Metodo que retorna si el articulo es aceptado o no
    def getAceptado(self):
        return self.esAceptado
    
    # Metodo que retorna la lista de los arbitros
    def getArbitros(self):
        return self.arbitro
    
    # Metodo que retorna la lista de las puntuaciones
    def getPuntuacion(self):
        return self.puntuacion
    
    # Agrega el id al articulo
    def setIdArticulo(self, idArticulo):
        self.idArticulo = idArticulo
    
    # Agrega el titulo al articulo
    def setTitulo(self, titulo):
        self.titulo = titulo
        
    # Agrega el resumen al articulo
    def setResumen(self, resumen):
        self.resumen = resumen
        
    # Agrega el texto al articulo
    def setTexto(self, texto):
        self.texto = texto
        
    # Inserta el estado del articulo. True si es aceptado
    def setAceptado(self, esAceptado):
        self.esAceptado = esAceptado
        
    # Inserta el correo de un arbitro a la lista de de arbitros
    def setArbitros(self, correo):
        self.arbitro.append(correo)
    
    # Inserta un puntaje a la lista de puntuaciones
    def setPuntuacion(self, puntaje):
        self.puntuacion.append(puntaje)
        
    # Metodo que asigna un arbitro y la puntuacion al articulo
    def asignarArbitroPuntuacion(self, idArticulo, articulos, correo, listaArticulos):
        while True:
            puntaje = int(raw_input('    Ingrese el puntaje: '))
            # Si el puntaje esta en el rango de 1 a 5
            if puntaje >= 1 and puntaje <= 5:
                if articulos.has_key(idArticulo):
                    # Ciclo para asignarle puntuacion a cada articulo
                    cont = 0
                    for i in range(len(listaArticulos)):
                        if idArticulo != listaArticulos[i].getIdArticulo():
                            cont = cont + 1
                        else:
                            break
                                
				    # Al encontrar el articulo le asigno la nota y el arbitro
				    # que lo califico        
                    listaArticulos[cont].setPuntuacion(puntaje)
                    listaArticulos[cont].setArbitros(correo)
                    
                    break
            else: 
                print 'La nota debe ser de 1 a 5. Intentelo de nuevo'
        return cont
       
    # Devuelve una lista con los arbitros y puntuaciones del articulo 
    def listaArbitroPuntuacion(self, listaArticulos, cont):
        lista = []
        
        # Ciclo que agrega a la lista la tupla (arbitro, puntuacion)
        for i in range(len(listaArticulos[cont].getArbitros())):
            # Tupla (arbitro, puntuacion)
            t = (listaArticulos[cont].getArbitros()[i], listaArticulos[cont].getPuntuacion()[i])
            # Agregamos a la lista
            lista.append(t)  
             
        return lista    

    # Metodo que calcula el promedio de las puntuaciones de un articulo
    def calcularPromedio(self):
        promedio = 0
        for i in range(len(self.puntuacion)):
            promedio = promedio + self.puntuacion[i]
            
        promedio = float(promedio) / len(self.puntuacion)
        return promedio
            
