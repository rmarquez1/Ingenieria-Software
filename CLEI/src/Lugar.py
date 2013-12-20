from Evento import *

# Clase lugar: esta clase sera usada para los datos de algun lugar donde 
# se realizara un evento.
# Los atributos de la clase son:
# nombre: Nombre del lugar donde se presentara un veneto
# ubicacion: Ubicacion donde se hara el evento
# cap_max: Capacidad maxima de personas que caben en un lugar
class Lugar:

      def __init__(self,nombre=None, ubicacion=None,cap_max=None):
          self.__nombre    = nombre
          self.__ubicacion = ubicacion
          self.__cap_max   = cap_max

      def get_nombre(self):
         return self.__nombre
      def get_ubicacion(self):
         return self.__ubicacion

      def get_cap_max(self):
         return self.__cap_max

      def imprimir(self):
          print "Nombre del espacio: " +str(self.__nombre)
          print "Ubicacion del espacio: " +str(self.__ubicacion)
          print "Capacidad maxima del espacio " +str(self.__cap_max)

#Funcion para registrar los espacios designados para los eventos
def registrar_espacios(espacios):

   while 1:
      while 1:
         nombre_espacio = raw_input('Nombre del espacio: ')
         if nombre_espacio=='':
            print "Indique nuevamente"
         else:
            #pasar todo a minuscula
            break
      while 1:
         ubicacion = raw_input('Ubicacion del espacio: ')
         if ubicacion =='':
            print "Indique nuevamente"
         else: 
            break
      while 1:
         capacidad = raw_input('Capacidad maxima de personas del espacio: ')
         if capacidad.isdigit():
            capacidad = int(capacidad)
            break
         else:
            print "Indique nuevamente"

      lugar = Lugar(nombre_espacio,ubicacion,capacidad)
      espacios[nombre_espacio] = lugar
      lugar.imprimir()
      otro = raw_input('Agregara otro espacio a la conferencia? s|n ')
      if otro != 's':
         break
   return espacios

#Imprime en pantalla todos los espacios que han sido registrados
def mostrar_espacios(espacios):
   if espacios =={}:
      print "No hay espacios registrados"
   else: 
      print "Espacios ya registrados para la conferencia"
      for elemento in espacios:
          print elemento

#Me devuelve un diccionario con diccionarios 3 niveles
# diccionario[fecha][lugar][hora_inicio_evento]
# con este diccionario asignare dependiendo de la fecha, del lugar y de la 
# ocupacion que tenga el lugar a la hora de inicio de un evento 
def asignar_todo(calendario,espacios):
   asignados = DiccionarioDeDiccionario()
   lista_lugares = espacios.keys()
   i = 1
   while i<=5:
      asignados[calendario[i]] = {}
      for elemento in lista_lugares:
          asignados[calendario[i]][elemento] = {}
          hora = 1
          while hora<=12:
             asignados[calendario[i]][elemento][hora]={}
             hora=hora+1
      i = i+1
   return asignados

#Funcion que imprime un diccionario para ser mostrado como un menu de opciones
def imprimir_menu(menu):
   o = 1
   while 1:
     try:
        print str(o)+") "+menu[o] 
        o = o+1
     except KeyError:
        break

# Con este metodo se realiza un diccionario que utilizaremos como un menu de
# opciones para ser presentado al usuario luego
def hacer_menu(lista):
    menu = {}
    k =1
    for elemento in lista:
        menu[k] = elemento
        k = k+1
    return menu

# Funcion verifica un entero que viene de entrada estandar y compara que este en 
# el rango especificado
def verificar_entero_rango(entrada,minimo,maximo):
   while 1:
      numero = raw_input(entrada)
      if numero.isdigit():
         numero = int(numero)
         if numero>=minimo and numero<=maximo:
            return numero
      print "Esta opcion no es correcta"

#verifica la entrada de un entero
def verificar_entero(entrada):
   while 1:
      numero = raw_input(entrada)
      if numero.isdigit():
         numero = int(numero)
         return numero
      print "Esta opcion no es correcta"
   

#Funcion que revisa la opcion que marco el usuario y verifica que la clave 
#este en el menu
def verificar_en_menu(entrada,menu):
   while 1:
     num = raw_input(entrada)
     if num.isdigit():
        num = int(num)
        try:
           clave = menu[num]
           return clave
        except KeyError:
           print "No esta entre las opciones"

#Verifica la disponibilidad del lugar segun hora de inicio y duracion del evento
def verificar_disponibilidad_de_lugar(asignados,fecha,lugar,hora_inicio,duracion):    
    hora = hora_inicio
    contador = 0
    esta_libre = True
    while esta_libre == True and contador<duracion:
        ocupacion = asignados[fecha][lugar][hora]
        if ocupacion == {}:
           if hora == 11:
              hora = 1
           elif hora==7:   
              esta_libre = False
           else:
              hora = hora+1
           contador = contador+1
        else:
           esta_libre = False
    return esta_libre

#Agrega el evento con su lugar y horas asignadas 
def agregar_evento(asignados,fecha,lugar,hora_ini,duracion,evento):
    hora = hora_ini
    contador = 0
    while contador<duracion:
        ocupacion = asignados[fecha][lugar][hora] = evento
        if hora == 11:
           hora = 1
        else:
           hora = hora+1
        contador = contador+1
    return asignados

#Metodo para asignar los espacios a los eventos
def asignar_espacios(eventos_entrada,calendario,espacios):
   
   eventos = eventos_entrada
   #Asigno a todos los dias de la conferencia todos los lugares y horas posibles 
   #que luego seran asignadas a un evento
   asignados = asignar_todo(calendario,espacios)
   #obtengo los nombres de todos los espacios registrados
   lista_lugares = espacios.keys()
   #hago un menu de opciones de los espacios
   lugares = hacer_menu(lista_lugares)
   while 1:
      #Muestro al usuario
      imprimir_menu(calendario)
      #Pregunto a cual fecha del evento va asignarle lugares
      fecha_evento = verificar_entero_rango('Indique el dia para ver que eventos se presentan: ',1,5)
      fecha = calendario[fecha_evento]
      print ("En esta fecha " +str(fecha)+ " se presentan los siguientes eventos\n")

      #Guardo en una lista los eventos que se presentaran para esa fecha
      lista = eventos[fecha].keys()
      
      #Condicional si hay eventos ya registrados para la fecha
      if lista == []:
         print "No se presentaran eventos para esa fecha\n"
      else:
         #Realizo un menu de los eventos que se presentan para la fecha especificada
         evento_en_fecha = hacer_menu(lista)
         #Muestro en pantalla
         imprimir_menu(evento_en_fecha)
         #Pide la opcion por pantalla al usuario y verifica en menu
         cual_evento = verificar_en_menu('A que evento le asignara un espacio ',evento_en_fecha)
        
         if cual_evento=='Taller' or cual_evento=='Sesiones Ponencia':
            
            print str(cual_evento) + " son los siguientes: "
            lista_eventos_simultaneo = eventos[fecha][cual_evento].keys()
            evento_simultaneo = hacer_menu(lista_eventos_simultaneo)
            imprimir_menu(evento_simultaneo)
            respuesta = verificar_en_menu('Escoja a cual '+str(cual_evento),evento_simultaneo)
            evento_dia = eventos[fecha][cual_evento][respuesta]

         else:
            #Obtengo el evento con sus datos
            evento_dia = eventos[fecha][cual_evento]
            
         while 1:
            print "Estos son los espacios registrados para la conferencia\n"
            #Imprimir menu de los lugares que ya habian sido aignados previamente
            imprimir_menu(lugares)

            #Pregunto el lugar que le quiere asignar a un evento
            lugar_respuesta = verificar_en_menu('Indique el lugar para el evento '+str(cual_evento)+" ",lugares)

            #Obtengo de lugar la hora y duracion del evento
            hora_ini = evento_dia.get_hora_inicio()
            duracion = evento_dia.get_duracion()
            #Verificar disponibilidad del lugar 
            agregar = verificar_disponibilidad_de_lugar(asignados,fecha,lugar_respuesta,hora_ini,duracion)
            if agregar == True: #El espacio esta disponible a esa hora
               asignados = agregar_evento(asignados,fecha,lugar_respuesta,hora_ini,duracion,evento_dia)
               break
            else:#Espacio no disponible

                print "Disculpe,no hay disponibilidad del lugar para la hora del evento"
                si_no = raw_input('Desea asignarle otro lugar al evento s|n ')
                if si_no != 's' and si_no!='S':
                   break

      si_no = raw_input('Desea hacer otra asignacion? s|n ')
      if si_no != 's' and si_no!='S':
         break
   return asignados

#Mostrar eventos con lugares asignados
def mostrar_eventos_con_lugares(asignados,calendario):
    
  n =1
  while n<=5:  
      print "Para la fecha " + str(calendario[n])
      lugares = asignados[calendario[n]].keys()
      for lugar in lugares:
          am = 8
          pm = 1
          nombre =''
          while am<=11:
            presenta = asignados[calendario[n]][lugar][am]
            if presenta != {}:
               if nombre != presenta.get_nombre():
                  nombre = presenta.get_nombre()
                  print "Evento: "+ str(nombre) 
                  print "Lugar: "+ str(lugar)
                  print "Hora: " +str(am) +"am "
                  print "Duracion: "+str(presenta.get_duracion())+" hora(as)"               
            am = am+1

          while pm<=7:
            presenta = asignados[calendario[n]][lugar][pm]
            if presenta != {}:
               if nombre != presenta.get_nombre():
                  nombre = presenta.get_nombre()
                  print "Evento: "+ str(nombre) 
                  print "Hora: " +str(pm)+"pm"
                  print "Lugar: "+ str(lugar)
                  print "Duracion: "+str(presenta.get_duracion())+" hora(as)"
            pm = pm+1
      n = n +1
