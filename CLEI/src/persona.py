#Clase Persona
class Persona:
   def __init__(self,nombre,apellido,inst_afil,correo,pais):
      self.__nombre    = nombre
      self.__apellido  = apellido
      self.__inst_afil = inst_afil
      self.__correo    = correo
      self.__pais      = pais

   def getNombre(self):
      return self.__nombre
   def getApellido(self):
      return self.__apellido
   def getInst_afil(self):
      return self.__inst_afil
   def setInst_afil(self,ints):
       self.__inst_afil(inst)
   def setCorreo(self,correo):
       self.__correo   = correo
   def setPais(self,pais):
       self.__pais = pais
   def nombreCompleto(self):
       return str(self.__nombre)+' '+str(self.__apellido)
   def ImprimirDatosPersona(self):
       print '\tNombre: '+self.__nombre
       print '\tApellido: '+self.__apellido
       print '\tInstitucion de afiliacion: ' + self.__inst_afil
       print '\tCorreo Electronico: ' + self.__correo
       print '\tPais: '+self.__pais

#Clase Comite de Programa
class Comite(Persona):
   def __init__(self,nombre, apellido, inst_afil, correo, pais):
       Persona.__init__(self,nombre, apellido, inst_afil, correo, pais)
       self.__topicos = self.asigTopicos()

   def asigTopicos(self):
       self.__topicos = []
       while True:
         top = raw_input('Indique el topico que domina: ')
         self.__topicos.append(top)
         top = raw_input('Domina algun otro topico? s/n ')
         if top == 'n':
            break

#Clase Autor
class Autor(Persona):
   def  __init__(self,nombre, apellido, inst_afil, correo, pais):
      Persona.__init__(self,nombre, apellido, inst_afil, correo, pais)

#funcion para crear el comite
def CrearComite():

     lista_comite = []
     try:
       num_miemb = raw_input('\tCuantos miembros de comite: ')
       num = int(num_miemb)
       contador  = 0
       while (contador<num):
          nombre,apellido,inst_afil,correo,pais = ObtenerDatos()
          comite   = Comite(nombre,apellido,inst_afil,correo,pais)
          print '\nMiembro de comite agregado!!\n'
          contador = contador+1
          lista_comite.append(comite)
          print lista_comite
       return lista_comite

     except ValueError:
         print 'Eso no es un numero'

#funcion para obtener los datos de las personas
def ObtenerDatos():

    nombre    = raw_input('  Indique Primer nombre: ')
    apellido  = raw_input('  Indique primer apellido: ')
    inst_afil = raw_input('  Indique la Institucion afiliada: ')
    correo    = raw_input('  Indique correo electronico: ')
    pais      = raw_input('  Indique pais ')
    return nombre, apellido, inst_afil, correo, pais
