from Persona import Autor
from Topico import *

# ------------------------------------------------------------------------------
# Clase que implementa informacion de los articulos del congreso
# ------------------------------------------------------------------------------
class Articulo():

    # Contructor del articulo
    def __init__(self, id_articulo=None, titulo=None, resumen=None, 
                 texto=None, p1=None, p2=None, p3=None, p4=None,p5=None):
        self.id_articulo = id_articulo
        self.titulo = titulo
        self.p_claves = []
        self.resumen = resumen
        self.texto = texto
        self.es_aceptado = False
        self.arbitro = []
        self.puntuacion = []
        self.autores = []
        self.topicos = []
        self.p_claves.append(p1)
        if p2 != None:
            self.p_claves.append(p2)
        if p3 != None:
            self.p_claves.append(p3)
        if p4 != None:
            self.p_claves.append(p4)
        if p5 != None:
            self.p_claves.append(p5)

    # Devuelve el pais del autor principal
    def get_pais(self):
        return self.autores[0].get_pais()

    # Retorna la lista de autores
    def get_autores(self):
        return self.autores
    
    # Metodo que retorna el id del articulo
    def get_id_articulo(self):
        return self.id_articulo
        
    # Metodo que retorna el titulo del articulo
    def get_titulo(self):
        return self.titulo 
    
    # Metodo que devuelve la lista de las palabras claves del articulo
    def get_p_claves(self):
        return self.p_claves

    # Metodo que retorna el resumen del articulo    
    def get_resumen(self):
        return self.resumen

    # Metodo que retorna el texto del articulo        
    def get_texto(self):
        return self.texto
    
    # Metodo que retorna si el articulo es aceptado o no
    def get_aceptado(self):
        return self.es_aceptado
    
    # Metodo que retorna la lista de los arbitros
    def get_arbitros(self):
        return self.arbitro
    
    # Metodo que retorna la lista de las puntuaciones
    def get_puntuacion(self):
        return self.puntuacion
    
    # Metodo que retorna la lista de topicos
    def get_topicos(self):
        return self.topicos
    
    # Agrega el id al articulo
    def set_id_articulo(self, id_articulo):
        self.id_articulo = id_articulo
    
    # Agrega el titulo al articulo
    def set_titulo(self, titulo):
        self.titulo = titulo
        
    # Agrega el resumen al articulo
    def set_resumen(self, resumen):
        self.resumen = resumen
        
    # Agrega el texto al articulo
    def set_texto(self, texto):
        self.texto = texto
        
    # Inserta el estado del articulo. True si es aceptado
    def set_aceptado(self, es_aceptado):
        self.es_aceptado = es_aceptado
        
    # Inserta el correo de un arbitro a la lista de de arbitros
    def set_arbitros(self, correo):
        self.arbitro.append(correo)
    
    # Inserta un puntaje a la lista de puntuaciones
    def set_puntuacion(self, puntaje):
        self.puntuacion.append(puntaje) 

    def set_autores(self, nombre, inst_afil, pais):
        autor = Autor(nombre, inst_afil, pais)
        self.autores.append(autor)
    
    # Inserta en la lista de topicos un topico
    def set_topicos(self, nombre_topico):
        topico = Topico(nombre_topico)
        self.topicos.append(topico)
    
    # Imprime los autores de un articulos
    def imprimir_autores(self):
        tam_autores = len(self.autores)
        for i in range(tam_autores):
            nombre = self.autores[i].get_nombre()
            inst_afil = self.autores[i].get_inst_afil()
            pais = self.autores[i].get_pais()
            print '(','Nombre: ', nombre, ', ', 'Institucion: ', inst_afil, 'Pais: ', pais, ')\n'
    
    # Metodo que calcula el promedio de las puntuaciones de un articulo
    def calcular_promedio(self):
        promedio = 0
        for i in range(len(self.puntuacion)):
            promedio = promedio + self.puntuacion[i]
            
        promedio = float(promedio) / len(self.puntuacion)
        return promedio
            
