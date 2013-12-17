class Topico:
    # Constructor de la clase Topico
    def __init__(self, nombre_topico):
        self.nombre = nombre_topico
        
    # Retorna el nombre de un topico
    def get_nombre_topico(self):
        return self.nombre
    
    # Inserta un nombre de topico
    def set_nombre_topico(self, nombre_topico):
        self.nombre = nombre_topico
