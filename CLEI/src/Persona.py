# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

#----------------------------------------------------------------------#
#Clase Persona #
#----------------------------------------------------------------------#

class Persona:
   def __init__(self,nombre=None,apellido=None,inst_afil=None,correo=None):
      self.nombre = nombre
      self.apellido = apellido
      self.inst_afil = inst_afil
      self.correo = correo

   def get_nombre(self):
      return self.nombre
  
   def get_apellido(self):
      return self.apellido
  
   def get_inst_afil(self):
      return self.inst_afil
  
   def get_correo(self):
      return self.correo

   def nombre_completo(self):
       return str(self.nombre)+' '+str(self.apellido)

#----------------------------------------------------------------------#
# Clase Comite 
#----------------------------------------------------------------------#

class Comite(Persona):

    # Constructor del comite
    def __init__(self, nombre, apellido, inst_afil, correo):
        Persona.__init__(self,nombre, apellido, inst_afil, correo)
        self.es_presidente = False

    # Retorna True si el miembro es presidente del comite, False en caso contrario        
    def get_es_presidente(self):
        return self.es_presidente
       
    # Asigna True si el miembro es presidente
    def set_es_presidente(self, es_presidente):
        self.es_presidente = es_presidente

#----------------------------------------------------------------------#
# Clase Autor
#----------------------------------------------------------------------#
class Autor(Persona):
    def __init__(self,nombre=None,apellido=None,inst_afil=None,correo=None, pais=None):
        Persona.__init__(self,nombre, apellido, inst_afil, correo)
        self.pais = pais

    def get_pais(self):
        return self.pais