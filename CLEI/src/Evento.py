from Calendario import calendario_conferencia

#Clase que hace un diccionario de diccionario
class DiccionarioDeDiccionario(dict):
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value

# Clase Evento: tiene los siguientes atributos
# nombre: nombre del evento
# fecha: fecha del tipo de evento
# hora_inicio: hora del comienzo del evento
# duracion: duracion del evento 
class Evento:

      def __init__(self,nombre=None,fecha=None,hora_inicio=None,duracion=None):
          self.__nombre = nombre
          self.__fecha  = fecha
          self.__hora_inicio = hora_inicio
          self.__duracion = duracion

      def get_nombre(self):
         return self.__nombre

      def get_fecha(self):
         return self.__fecha

      def get_hora_inicio(self):
         return self.__hora_inicio
      
      def get_duracion(self):
         return self.__duracion
      
      def imprimir(self):
         print "Nombre del evento: "        +str(self.__nombre)
         print "Fecha del evento: "         +str(self.__fecha)
         print "Hora de inicio del evento: "+str(self.__hora_inicio)
         print "Duracion de este evento: "  +str(self.__duracion) +" hora(as)"

#Muestra en pantalla los eventos que seran presentados en la conferencia
def mostrar_eventos():   
   print "1. Apertura"
   print "2. Clausura"
   print "3. Charlas Invitadas"
   print "4. Eventos Sociales"
   print "5. Taller"
   print "6. Sesiones de Ponencia"
   print "7. Menu Principal"

#Funcion para verificar hora del evento y formatode la hora que registro
def hora_evento(hora_even):
   num = 0
   am = [8,9,10,11]
   pm = [1,2,3,4,5,6,7]
   if hora_even.isdigit():
      hora = int(hora_even)
      if am.count(hora)!=0:
         return hora
      elif pm.count(hora)!=0:
         return hora
      else:
         hora = -1
         print "Hora incorrecto indique de nuevo"
         return hora

# Funcion para obtener hora de inicio y duracion de un evento especificado
def registrar(tipo_evento):

   hora = -1    
   while hora == -1:
      print "Las horas por dia establecidas para la conferencia seran:"
      print "8am-9am-10am-11am \n1pm-2pm-3pm-4pm-5pm-6pm-7pm"
      entrada1= raw_input('Indique hora de inicio del evento, solo el primer numero ')
      hora    = hora_evento(entrada1)
   while 1:
      if hora == 7:
         duracion = 1
         break
      else:
         duracion = raw_input('Indique duracion de este evento, 1-10: ')
         if duracion.isdigit():
            duracion = int(duracion)
            if duracion>=1 and duracion<=10:
               break
      print '\n Duracion no aceptada'   
   return hora,duracion

# Funcion para que el usuario escoja una fecha para el evento
# parametro calendario: El calendario de los 5 dias de la conferencia 
# parametro tipo: tipo de evento
# retorna la fecha seleccionada
def seleccionar_fecha(calendario,tipo):

    if tipo == 'Taller':     #Talleres son los primeros 2 dias
       dia_inicio = 1
       dia_fin    = 2
       dia = 1
    elif tipo == 'Sesiones Ponencia': #Ponencias ultimos 3 dias
       dia_inicio = 3
       dia_fin    = 5
       dia =3
    else:                    #Otros cualquier dia
       dia_inicio=1
       dia_fin=5
       dia=1
    cuantos_dias = 0
    while dia_inicio<=dia_fin:
       cuantos_dias = cuantos_dias +1
       print str(cuantos_dias)+") "+ str(calendario[dia_inicio])
       dia_inicio = dia_inicio+1
    while 1:
      opcion = raw_input('Seleccione que fecha escogera para este evento: ')
      if opcion.isdigit():
         opcion = int(opcion)
         if opcion>cuantos_dias or opcion<1:          #Opcion incorrecta
            print "Esta fecha no esta entre las opciones"
         else:                                        #En el rango de opciones
            if cuantos_dias == 2 or cuantos_dias==5:  #Opcion de 2 dias y 5 dias
               return calendario[opcion]
            else:                                     #Opcion de 3 dias
               return calendario[opcion+2]            #Sumo 2 porque son las 3 ultimas fechas del calendario
      else:        
         print '\nNo es una opcion'

# Funcion para registrar evento 
def registrar_evento(calendario):
   
   opciones ={'1':'Apertura', '2':'Clausura','3':'Charlas Invitadas',
              '4':'Eventos Sociales','5':'Taller','6':'Sesiones Ponencia','7':'MenuPrincipal'} 
   eventos = DiccionarioDeDiccionario()
   i = 1
   while i<=5:
      eventos[calendario[i]] = {}
      i=i+1
   seguir = False
   while 1:
      mostrar_eventos()
      opcion = raw_input('Opcion a realizar: ')
      try:
         tipo_evento = opciones[opcion]
         if tipo_evento == 'MenuPrincipal':
             break
         if tipo_evento == 'Taller' or tipo_evento=='Sesiones Ponencia':
            fecha  = seleccionar_fecha(calendario,tipo_evento)
            hora , duracion = registrar(tipo_evento)
            nombre = str(tipo_evento)
            while 1:
               titulo = raw_input('Titulo del '+str(tipo_evento)+": ")
               if titulo =='':
                  print "No escribio el titulo del evento" 
               else:
                  break
            nombre = nombre+": "+str(titulo)
            evento_nuevo = Evento(nombre,fecha,hora,duracion)
            esta = eventos[fecha].has_key(tipo_evento)       
            if esta==False:
               eventos[fecha][tipo_evento] = {}
            eventos[fecha][tipo_evento][titulo] = evento_nuevo
            print "Evento registrado: "
            eventos[fecha][tipo_evento][titulo].imprimir()
         else:
            seguir,fecha = eventos_unicos(eventos,tipo_evento,calendario)
            if seguir == True:
               hora , duracion = registrar(tipo_evento)
               evento_nuevo = Evento(tipo_evento,fecha,hora,duracion)
               eventos[fecha][tipo_evento] = evento_nuevo
               eventos[fecha][tipo_evento].imprimir()
      except KeyError:
          print "No esta entre las opciones"
   return eventos


# Revisa si ya es habia registrado este evento anteriormente y de ser asi
# si desea reemplazarlo
def esta_registrado(eventos,fecha,tipo_evento):

   registrado = eventos[fecha].has_key(tipo_evento)
   if registrado == True: # Si el evento ya esta registrado en esa fecha
      hacer = raw_input('Este evento ya esta registrado, desea reemplzarlo? s|n ')
      if hacer == 's':
         seguir = True
      else:
         seguir = False 
   else:                  # Si aun no se ha registrado
         seguir = True
   return seguir

# Eventos que son presentados una sola vez durante la conferencia
# o que solo puede ser presentado una vez por dia si es el caso
def eventos_unicos(eventos,tipo_evento,calendario):
    #Condicional para la fecha segun tipo de evento introducido
    if tipo_evento == "Apertura":   #Evento: Apertura
        fecha  = calendario[1]
        seguir = esta_registrado(eventos,fecha,tipo_evento)
    elif tipo_evento == "Clausura": #Evento: Clausura
        fecha = calendario[5]
        seguir = esta_registrado(eventos,fecha,tipo_evento)
    elif tipo_evento == 'Charlas Invitadas' or tipo_evento == 'Eventos Sociales':
        fecha = seleccionar_fecha(calendario,tipo_evento)
        seguir = esta_registrado(eventos,fecha,tipo_evento)         
    return seguir,fecha

#Muestra en pantalla todos los eventos que han sido registrados
def mostrar_eventos_registrados(eventos,calendario):
   o = 1
   while o<=5:
      print "Para la fecha " + str(calendario[o])
      lista_eventos = eventos[calendario[o]].values()
      if lista_eventos !=[]:
         for elemento in lista_eventos:
             if type(elemento)==dict:
                lista_eventos_simultaneos = elemento.keys()
                for elemen in lista_eventos_simultaneos:
                    print elemento[elemen].get_nombre()
             else:
                print elemento.get_nombre()
      else:
         print "Aun no se ha registrado eventos"
      o = o+1
