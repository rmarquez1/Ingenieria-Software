# ------------------------------------------------------------------------------
# Clase que implementa los miembro del comite de programa del congreso
# ------------------------------------------------------------------------------
class Comite():

    # Constructor del comite
    def __init__(self, correo= None, nombre=None, apellido=None):
        self.correo = correo
        self.nombre = nombre
        self.apellido = apellido
        self.esPresidente = False
    
    # Retorne el correo de un miembro de CP
    def getCorreo(self):
        return self.correo
        
    # Retorna el nombre de un miembro de CP    
    def getNombre(self):
        return self.nombre
        
    # Retorna el apellido de un miembro de CP
    def getApellido(self):
        return self.apellido

    # Retorna True si el miembro es presidente del comite, False en caso contrario        
    def getEsPresidente(self):
        return self.esPresidente

    # Asigna un correo al miembro de CP        
    def setCorreo(self, correo):
        self.correo = correo
        
    # Asigna el nombre al miembro de CP
    def setNombre(self, nombre):
        self.nombre = nombre
        
    # Asigna el apellido al miembro de CP
    def setApellido(self, apellido):
        self.apellido = apellido
       
    # Asigna True si el miembro es presidente
    def setEsPresidente(self, esPresidente):
        self.esPresidente = esPresidente
        
class Test():
    # Constructor comite
    def __init__(self, correo= None, nombre=None, apellido=None):
        self.t1 = correo
        self.t1 = nombre
        self.t1 = apellido
        self.t1 = False