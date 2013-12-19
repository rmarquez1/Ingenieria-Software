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
   
#------------------------------------------------------------------------------#
#Metodos que permiten pedir los datos                                          #
#------------------------------------------------------------------------------#

def pedir(palabraclave):
    apedir = ''
    while apedir == '':
        apedir = raw_input('\nIntroduzca el '+ palabraclave + ' del participante: ')
        if apedir == '':
            print ('\n' + palabraclave + ' no valido')

    return apedir

def pedir_institucion():
    institucion = ''
    while institucion == '':
        institucion = raw_input('\nIntroduzca el nombre de la institucion a la que el participante esta afiliado: ')
        if institucion == '':
            print '\nInstitucion invalida'

    return institucion

def pedir_correo():
    usuario = ''
    while usuario == '':
        usuario = raw_input('\nIntroduzca el usuario del correo (lo que va antes del @): ')

        if usuario == '':
            print '\nUsuario invalido'  

        elif usuario.find('@') != -1:
            print '\nEl usuario no puede incluir "@"!'
            usuario = ''
    dominio = ''
    while dominio == '':
        dominio = raw_input('\nIntroduzca el dominio del correo: ')

        if dominio == '':
            print '\nDominio invalido'

        elif dominio.find('.') == -1 or dominio.find('@') != -1:
            print '\nEl formato del dominio no es valido'
            dominio = ''    

    return usuario+'@'+dominio

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
    def __init__(self,nombre=None,inst_afil=None, pais=None):
        self.nombre = nombre
        self.inst_afil = inst_afil
        self.pais = pais

    def get_pais(self):
        return self.pais
    

