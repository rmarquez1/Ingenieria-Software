# Funcion para obtener el mes que sera realizado la conferencia
# y verifica si es un mes valido,
# param mes_con: el mes que el usuario especifico
# return mes,dias: el mes verificado y los dias que tiene dicho mes
def obtener_mes(mes_con):

   meses = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,
            9:30,10: 31,11:30,12:31}
   if mes_con.isdigit():
      try:
         dias = meses[int(mes_con)]
         mes  = int(mes_con)
         return mes,dias
      except KeyError:
         print "Este no es un mes."
         mes = -1
         dias=  0   
         return mes,dias
   else:        
       mes = -1
       dias=  0
       print '\nNo indico un mes aceptado, indique nuevamente'
   
   return mes,dias

# Funcion para obtener el dia que inicia la conferencia y verifica que 
# sea un dia del correcto 
# param dia: el dia que especifico el usuario
# param dias: los dias que tiene dicho mes 
# return dia_conf: retorna el dia con la verificacion
#                  de no ser un dia valido retorna -1
def obtener_dia(dia,dias):
    if dia.isdigit():
       dia_conf = int(dia)
       if dia_conf<1 or dia_conf>dias:
          dia_conf = -1
          print "Rango de dias incorrecto"
          return dia_conf
       else:
          return dia_conf
    else:
       dia_conf = -1
       print '\nNo indico un dia aceptado, indique nuevamente'
       return dia_conf

# Funcion que pregunta el anyo en que se presentara la conferencia
# y verifica si esta en un rango correcto
# param ano_conf: ano de la conferencia que especifico el usuario
# return ano: el ano con la verificacion
def obtener_ano(ano):
   if ano.isdigit():
      ano = int(ano)
      if ano<2013:
         ano = -1
         print "Este no es una ano valido"
         return ano
      else:   
         return ano
   else:
       ano = -1    
       print '\nNo indico un ano aceptado, indique nuevamente'
       return ano

# Esta funcion realiza el calendario de los 5 dias
# que es presentada la conferencia
# parametro mes: el mes de la conferencia
# parametro dias: la cantidad de dias que tiene el mes
# parametro dia: dia de la conferencia
# parametro ano: ano que sera presentada la conferencia
# return calendario: el calendario con las fechas de los 5 dias
def fecha_calendario(mes,dias,dia,ano):

   calendario = {} 
   cuantos = dias - dia
   if cuantos>=5:  #Cuando las fechas estan en un mismo mes
       calendario[1] = str(dia)+"/"+str(mes)+"/"+str(ano)
       calendario[2] = str(dia +1)+"/"+str(mes)+"/"+str(ano)
       calendario[3] = str(dia +2)+"/"+str(mes)+"/"+str(ano)
       calendario[4] = str(dia +3)+"/"+str(mes)+"/"+str(ano)
       calendario[5] = str(dia +4)+"/"+str(mes)+"/"+str(ano)
   else:           #Cuando las fechas estan entre 2 meses
      i=0
      while dia<=dias:
         i=i+1
         calendario[i]= str(dia)+"/"+str(mes)+"/"+str(ano)
         dia=dia+1
      num = 1
      i=i+1
      if mes == 12:       #Si estoy en el mes de diciembre y debo pasar a enero
         mes = 0
         ano = ano +1
         
      while i<=5:
         calendario[i] = str(num)+"/"+str(mes+1)+"/"+str(ano)
         num = num +1
         i=i+1
   return calendario


#Con esta funcion se obtiene el calendario de los 5 dias donde se presenta la
#conferencia
def calendario_conferencia():
   
   mes = -1
   dia = -1
   ano = -1   
   while mes==-1:
      entrada = raw_input('Indique mes que sera realizada la conferencia MM: ')
      mes,dias = obtener_mes(entrada)

   while dia ==-1:
      entrada = raw_input('Indique dia de inicio de la conferencia DD: ')
      dia = obtener_dia(entrada,dias)
   
   while ano == -1:
      entrada = raw_input('Indique a-o de la conferencia AAAA: ')
      ano = obtener_ano(entrada)

   calendario = fecha_calendario(mes,dias,dia,ano) 

   return calendario
