# ------------------------------------------------------------------------------
# Implementacion de los datos relacionados con los autores
# ------------------------------------------------------------------------------
class Autor():

    def __init__(self, nombre, apellido, pais):
        self.nombre = nombre
        self.apellido = apellido
        self.pais = pais
        
    def getNombre(self):
        return self.nombre
        
    def getApellido(self):
        return self.apellido
        
    def getPais(self):
        return self.pais
        
    def setNombre(self, nombre):
        self.nombre = nombre
        
    def setApellido(self, apellido):
        self.apellido = apellido

    def setPais(self, pais):
        self.pais = pais
        
        
