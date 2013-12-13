from Articulo import *
from Persona import *
from CLEI import *
import sys
import unittest

# ------------------------------------------------------------------------------
# Pruebas de la clase Comite
# ------------------------------------------------------------------------------
class ComiteTester(unittest.TestCase):

    # Prueba de creacion de un miembro del comite de programa
    def testComite(self):
        comite = Comite('correo@gmail.com','Ramon', 'Marquez')
        assert comite.getCorreo() == 'correo@gmail.com', 'Fallo creacion de miembro CP'
        assert comite.getNombre() == 'Ramon', 'Fallo creacion de miembro CP'
        assert comite.getApellido() == 'Marquez', 'Fallo creacion de miembro CP'
        assert comite.getEsPresidente() == False, 'Fallo creacion de miembro CP'
        
    # Prueba de asignar un presidente
    def testPresidente(self):
        comite = Comite('Ezequiel', 'Gimenez','USB', 'correo@ezequiel',)
        assert comite.get_es_presidente() == False, 'Fallo asignacion de presidente'
        comite.set_es_presidente(True)
        assert comite.get_es_presidente() == True, 'Fallo asignacion de presidente'
        
        comite1 = Comite('Ramon', 'Marquez','UCV','correo@ramon')
        assert comite1.get_es_presidente() == False, 'Fallo asignacion de presidente'
        comite1.set_es_presidente(True)
        assert comite1.getEsPresidente() == True, 'Fallo asignacion de presidente'

# ------------------------------------------------------------------------------
# Prueba de la clase Articulo
# ------------------------------------------------------------------------------
class ArticuloTester(unittest.TestCase):

    # Test de creacion de un articulo
    def testArticulo(self):
        articulo = Articulo(1,'Ingenieria', 'Resumen', 'Texto')
        assert articulo.getIdArticulo() == 1, 'Fallo creacion de articulo'
        assert articulo.getTitulo() == 'Ingenieria', 'Fallo creacion de articulo'
        assert articulo.getResumen() == 'Resumen', 'Fallo creacion de articulo'
        assert articulo.getTexto() == 'Texto', 'Fallo creacion de articulo'
        assert articulo.getAceptado() == False, 'Fallo creacion de articulo'

    # Testa de asignacion de las palabras claves de los articulos
    def testPalabrasClaves(self):
        articulo = Articulo(1,'Ingenieria', 'Resumen del articulo', 'Texto del articulo',
                            'software')
        assert articulo.getPClaves()[0] == 'software' , 'Fallo asignacion de palabras claves'
        
        articulo1 = Articulo(2, 'Sistemas', 'Resumen articulo1', 'Texto articulo1',
                             'informacion', 'tecnologia')
        assert articulo1.getPClaves()[0] == 'informacion' , 'Fallo asignacion de palabras claves'
        assert articulo1.getPClaves()[1] == 'tecnologia' , 'Fallo asignacion de palabras claves'
        
        articulo2 = Articulo(3, 'Traductores', 'Resumen articulo2', 'Texto articulo2',
                             'Automata', 'Lenguaje', 'Deterministico')
        assert articulo2.getPClaves()[0] == 'Automata' , 'Fallo asignacion de palabras claves'
        assert articulo2.getPClaves()[1] == 'Lenguaje' , 'Fallo asignacion de palabras claves'
        assert articulo2.getPClaves()[2] == 'Deterministico' , 'Fallo asignacion de palabras claves'
        
        articulo3 = Articulo(4, 'Discretas', 'Resumen articulo3', 'Texto articulo3',
                             'Conjuntos', 'Familia', 'Interseccion', 'Inversa')
        assert articulo3.getPClaves()[0] == 'Conjuntos','Fallo asignacion de palabras claves'
        assert articulo3.getPClaves()[1] == 'Familia', 'Fallo asignacion de palabras claves'
        assert articulo3.getPClaves()[2] == 'Interseccion', 'Fallo asignacion de palabras claves'
        assert articulo3.getPClaves()[3] == 'Inversa', 'Fallo asignacion de palabras claves'
        
        articulo4 = Articulo(5, 'Software', 'Resumen articulo4', 'Texto articulo4',
                             'Clase', 'Diseno', 'Acoplamiento', 'Cohesion', 'Pruebas')
        assert articulo4.getPClaves()[0] == 'Clase', 'Fallo asignacion de palabras claves'
        assert articulo4.getPClaves()[1] == 'Diseno', 'Fallo asignacion de palabras claves'
        assert articulo4.getPClaves()[2] == 'Acoplamiento', 'Fallo asignacion de palabras claves'
        assert articulo4.getPClaves()[3] == 'Cohesion', 'Fallo asignacion de palabras claves'
        assert articulo4.getPClaves()[4] == 'Pruebas', 'Fallo asignacion de palabras claves'
 
    # Test de asignacion arbitro-puntuacion a un articulo        
    def testAsignarArbitroPuntuacionArticulo(self):
        articulos = {}
        listaArticulos = []
        articulo = Articulo(1,'Software', 'Resumen','Texto')
        comite = Comite('correo','Franyelin', 'Colina')
        articulos[articulo.getIdArticulo()] = articulo
        listaArticulos.append(articulo)
        cont = articulo.asignarArbitroPuntuacion(1, articulos, comite.getCorreo(), listaArticulos)
        lista = articulo.listaArbitroPuntuacion(listaArticulos, cont)
        assert lista[0][1] == articulo.getPuntuacion()[0],'Fallo asignacion arbitro puntuacion'

    # Test de calcular el promedio de las evaluaciones de un articulo
    def testCalculoPromedio(self):
        articulo = Articulo(1, 'Sistemas', 'Resumen', 'Texto')
        articulo.setPuntuacion(5)
        articulo.setPuntuacion(4)
        articulo.calcularPromedio()
        assert articulo.calcularPromedio() == 4.5, 'Fallo calculo promedio'  


# ------------------------------------------------------------------------------
# Prueba de la clase CLEI
# ------------------------------------------------------------------------------
class CLEITester(unittest.TestCase):
    # Test de insercion de articulos en la lista de aceptables
    def testAceptables(self):
        articulos = {}
        evaluaciones = {}
        listaArticulos = []
        articulo = Articulo(1,'Software', 'Resumen','Texto')
        comite = Comite('Franyelin', 'Colina','ucv','correo')
        comite1 = Comite('Ramon', 'Marquez','USB','correo1')
        articulos[articulo.getIdArticulo()] = articulo

        listaArticulos.append(articulo)
        
        clei = CLEI()
        
        cont = articulo.asignarArbitroPuntuacion(1, articulos, comite.get_correo(), listaArticulos)
        cont = articulo.asignarArbitroPuntuacion(1, articulos, comite1.get_correo(), listaArticulos)
        lista = articulo.listaArbitroPuntuacion(listaArticulos, cont)
        evaluaciones[1] = lista, listaArticulos[cont].calcularPromedio()
        listaEvaluaciones = evaluaciones.items()
        # Ordenamos por promedio
        listaEvaluaciones.sort(key=lambda x: x[1][1])
        #Invertimos la lista
        listaEvaluaciones.reverse()
        clei.crearAceptables(listaEvaluaciones)
        assert clei.getAceptables()[0][0] == 1, 'Fallo creacion de aceptables'


    # Test de insercion de articulos en la lista de aceptados y empatados
    def testAceptadosEmpatados(self):
        clei = CLEI()
        articulos = {}
        articulo1 = Articulo(1)
        articulo2 = Articulo(2)
        articulo3 = Articulo(3)
        articulo4 = Articulo(4)
        articulo5 = Articulo(5)
        articulo6 = Articulo(6)
        articulo7 = Articulo(7)
        articulo8 = Articulo(8)
        articulos[1] = articulo1
        articulos[2] = articulo2
        articulos[3] = articulo3
        articulos[4] = articulo4
        articulos[5] = articulo5
        articulos[6] = articulo6
        articulos[7] = articulo7
        articulos[8] = articulo8
        
        clei.setAceptables(1,5)
        clei.setAceptables(2,5)
        clei.setAceptables(3,5)
        clei.setAceptables(4,4.75)
        clei.setAceptables(5,4.5)
        clei.setAceptables(6,4.5)
        clei.setAceptables(7,4)
        clei.setAceptables(8,4)

        espacioRestante = clei.crearAceptadosYEmpatados(8, 4, articulos)
        assert clei.getAceptados()[0] == 1, 'Fallo creacion de aceptados'
        assert clei.getAceptados()[1] == 2, 'Fallo creacion de aceptados'
        assert clei.getAceptados()[2] == 3, 'Fallo creacion de aceptados'
        assert clei.getAceptados()[3] == 4, 'Fallo creacion de aceptados'
        assert espacioRestante == 0, 'Fallo creacion de aceptados'
        assert clei.getEmpatados()[0] == 5, 'Fallo creacion de empatados'
        assert clei.getEmpatados()[1] == 6, 'Fallo creacion de empatados'        

        
        clei1 = CLEI()
        articulos1 = {}
        articulo1 = Articulo(1)
        articulo2 = Articulo(2)
        articulo3 = Articulo(3)
        articulo4 = Articulo(4)
        articulo5 = Articulo(5)
        articulo6 = Articulo(6)
        articulo7 = Articulo(7)
        articulo8 = Articulo(8)
        articulos1[1] = articulo1
        articulos1[2] = articulo2
        articulos1[3] = articulo3
        articulos1[4] = articulo4
        articulos1[5] = articulo5
        articulos1[6] = articulo6
        articulos1[7] = articulo7
        articulos1[8] = articulo8
        
        clei1.setAceptables(1,5)
        clei1.setAceptables(2,5)
        clei1.setAceptables(3,4.75)
        clei1.setAceptables(4,4.75)
        clei1.setAceptables(5,4.5)
        clei1.setAceptables(6,4.5)
        clei1.setAceptables(7,4)
        clei1.setAceptables(8,4)
        espacioRestante = clei1.crearAceptadosYEmpatados(8, 3, articulos1)
        
        
        clei2 = CLEI()
        articulos2 = {}
        articulo1 = Articulo(1)
        articulo2 = Articulo(2)
        articulo3 = Articulo(3)
        articulo4 = Articulo(4)
        articulo5 = Articulo(5)
        articulo6 = Articulo(6)
        articulo7 = Articulo(7)
        articulo8 = Articulo(8)
        articulos2[1] = articulo1
        articulos2[2] = articulo2
        articulos2[3] = articulo3
        articulos2[4] = articulo4
        articulos2[5] = articulo5
        articulos2[6] = articulo6
        articulos2[7] = articulo7
        articulos2[8] = articulo8
        clei2.setAceptables(1,5)
        clei2.setAceptables(2,5)
        clei2.setAceptables(3,5)
        clei2.setAceptables(4,5)
        clei2.setAceptables(5,5)
        clei2.setAceptables(6,5)
        clei2.setAceptables(7,5)
        clei2.setAceptables(8,5)
        espacioRestante = clei2.crearAceptadosYEmpatados(8, 3, articulos2)


def main():
    print '\n ----------- BIENVENIDO AL SISTEMA CLEI ----------\n\n'
    print '                       MENU\n'
    
    articulos = {}
    listaArticulos = []
    miembrosCP = {}
    evaluaciones = {}
    clei = CLEI()
    
    try:
        num = int(raw_input('Indique el numero de articulos que se presentaran en el congreso: '))
        
        while True: 
            print '\n1. Crear un articulo\n'
            print '2. Crear un miembro de comite de programa\n'
            print '3. Asignar presidente del comite de programa\n'
            print '4. Asignar puntuacion y arbitro a un articulo\n'
            print '0. SALIR'
            
            try:
                opcion = int(raw_input(' Indique la operacion que desea realizar: '))
                if opcion == 0:
                    break

                elif opcion == 1:
                    while True:
                        res = raw_input('Crear articulo (s/n): ')
                        if res == 's' or res == 'S':
                            idArticulo = int(raw_input('ID: '))
                            if articulos.has_key(idArticulo):
                                print 'Ya existe articulo con ese id'
                            else:
                                titulo = raw_input('Titulo: ')
                                resumen = raw_input('Resumen: ')
                                texto = raw_input('Texto: ')

                                while True:
                                    try:
                                        numPClaves = int(raw_input('Indique cuantas palabras claves desea asignar al articulo: '))
                                        
                                        if numPClaves < 1 or numPClaves > 5:
                                            print '\nPuede asignar minimo 1 y maximo 5 palabras claves\n'
                                            
                                        else:
                                            if numPClaves == 1:
                                                pClave = raw_input('Palabra clave: ')
                                                articulo = Articulo(idArticulo, titulo, resumen, texto, pClave)
                                                       
                                            elif numPClaves == 2:
                                                pClave1 = raw_input('Palabra clave: ')
                                                pClave2 = raw_input('Palabra clave: ')
                                                articulo = Articulo(idArticulo, titulo, resumen, texto, pClave1, pClave2)
                                                
                                            elif numPClaves == 3:
                                                pClave1 = raw_input('Palabra clave: ')
                                                pClave2 = raw_input('Palabra clave: ')
                                                pClave3 = raw_input('Palabra clave: ')
                                                articulo = Articulo(idArticulo, titulo, resumen, texto, pClave1, pClave2, pClave3)
                                                
                                            elif numPClaves == 4:
                                                pClave1 = raw_input('Palabra clave: ')
                                                pClave2 = raw_input('Palabra clave: ')
                                                pClave3 = raw_input('Palabra clave: ')
                                                pClave4 = raw_input('Palabra clave: ')
                                                articulo = Articulo(idArticulo, titulo, resumen, texto, pClave1, pClave2, pClave3, pClave4)
                                                
                                            elif numPClaves == 5:
                                                pClave1 = raw_input('Palabra clave: ')
                                                pClave2 = raw_input('Palabra clave: ')
                                                pClave3 = raw_input('Palabra clave: ')
                                                pClave4 = raw_input('Palabra clave: ')
                                                pClave5 = raw_input('Palabra clave: ')
                                                articulo = Articulo(idArticulo, titulo, resumen, texto, pClave1, pClave2, pClave3, pClave4, pClave5)
                                                    
                                            listaArticulos.append(articulo)
                                            articulos[idArticulo] = articulo
                                            break
                                        
                                    except ValueError:
                                        print '\n Opcion invalida\n'

                        elif res == 'n' or res == 'N':
                            break
                        else:
                            print '\nIndique s/n\n'

                elif opcion == 2:
                    while True:
                        res = raw_input('Crear miembro del CP (s/n): ')
                        if res == 's' or res == 'S':
                            correo = raw_input('Correo: ')
                            
                            if miembrosCP.has_key(correo):
                                print 'Ya existe un miembro con ese correo. Intentelo de nuevo'
                            else:
                                nombre = raw_input('Nombre: ')
                                apellido = raw_input('Apellido: ')
                                inst_afil = raw_input('Institucion Principal: ')
                                comite = Comite(nombre, apellido, inst_afil,correo)
                                miembrosCP[comite.get_correo()] = comite.get_nombre(), comite.get_apellido(),comite.get_inst_afil(), comite.get_es_presidente() 
                                
                        elif res == 'n' or res == 'N':
                            break
                        else:
                            print 'Indique s/n'

                elif opcion == 3:
                    if len(miembrosCP) != 0:
                        while True:
                            presidente = raw_input('Indique el presidente del comite de programa: ')
                            if miembrosCP.has_key(presidente):
                                # Verificamos que no haya otro presidente
                                lista_correos = miembrosCP.keys()
                                
                                # Variable que indica si se consigue algun presidente
                                temp = 0
                                for i in range(len(lista_correos)):
                                    # Caso en el que se consigue un presidente
                                    if miembrosCP[lista_correos[i]][3] == True:
                                        temp = 1
                                        break
                                        
                                # Caso en que no se consigue alguien como presidente     
                                if temp != 1:
                                    comite.set_es_presidente(True)
                                    miembrosCP[presidente] = comite.get_nombre(), comite.get_apellido(), comite.get_inst_afil(), comite.get_es_presidente()
                                    print miembrosCP
                                    print 'FIN'
                                    break
                                else:
                                    print 'Ya existe un presidente en el comite de programa'
                                break
                            else:
                                print 'Miembro inexistente. Intente de nuevo'
                    else:
                        print 'No existe miembros en el comite de programa. Debe crearlos'                      

                elif opcion == 4:
                    while True:
                        if len(miembrosCP)>0 and len(articulos)>0:
                            res = raw_input('   Crear arbitros y puntuaciones (s/n): ')
                            if res == 's' or res == 'S':    
                                idArticulo = int(raw_input('    ID del articulo a evaluar:' ))
                                
                                if articulos.has_key(idArticulo):
                                    while True:
                                    
                                        correo = raw_input('    Correo del arbitro: ')
                                        if miembrosCP.has_key(correo):
                                            # Verificamos el rango de la nota de 1 a 5
                                            cont = articulo.asignarArbitroPuntuacion(idArticulo, articulos, correo, listaArticulos)
                                                
                                            # Caso en que otro arbitro califique el mismo articulo    
                                            r = raw_input('    Agregar otro arbitro (s/n):' )
                                            if r == 'N' or r == 'n':
                                                break
                                        else:
                                            print 'No existe arbitro con ese correo'
                                    
                                    # Creamos una lista cuyos elementos son tuplas correspondientes a
                                    # (arbitro, puntuacion)
                                    lista = articulo.listaArbitroPuntuacion(listaArticulos, cont)

                                    # Agregamos al diccionario de evaluaciones
                                    evaluaciones[idArticulo] = lista, listaArticulos[cont].calcularPromedio()
                                    # RECORDAR VER SI UN ARBITRO EVALUA DOS VECES EL MISMO ARTICULO
                                else:
                                    print '\nNo existe articulo con ese id\n'    

                            elif res == 'n' or res == 'N':
                                if len(evaluaciones) != 0:
                                    listaEvaluaciones = evaluaciones.items()
                                    print 'lista evaluaciones: ', listaEvaluaciones
                                    # Ordenamos por promedio
                                    listaEvaluaciones.sort(key=lambda x: x[1][1])
                                    #Invertimos la lista
                                    listaEvaluaciones.reverse()
                                    clei.crearAceptables(listaEvaluaciones)
                                break
                            else:
                                print 'Indique s/n'
                        
                            print evaluaciones
                        else:
                            print '''No hay informacion suficiente para realizar esta operacion. Verifique que haya creado articulos
y miembros de comite de programa'''      
                            break
                    
            except ValueError:
                print 'Opcion invalida'
    except ValueError:
        print 'Opcion invalida'   

    print '-----  PROCESO DE SELECCION DE ARTICULOS -----'
    print '1. Desempate por presidente de comite\n'
    print '0. SALIR'
    try:
        opcion = int(raw_input('Indique el tipo de seleccion de articulos que desea utilizar: '))
        while True: 
            if opcion == 0:
                break
            
            elif opcion == 1:
                correo_presi = raw_input('Indique su correo como presidente: ')
                # si el correo pertenece al correo de los miembros registrados

                if miembrosCP.has_key(correo_presi):
                    # En la posicion 3 del valor del diccionario miembrosCP
                    # esta el valor del booleano que indica si es presidente o no
                    if miembrosCP[correo_presi][3] == True:
                        print 'Bienvenido presidente del comite de programa.\n'
                        print 'Elija entre las siguientes opciones:\n'
                        
                        while True:
                            print ' 1. Ver lista de articulos aceptables.\n'
                            print ' 2. Generar articulos a ser aceptados en la conferencia.\n'
                            print ' 0. SALIR'

                            try:
                                res = int(raw_input('   Indique el tipo de operacion: '))
                                if res == 0:
                                    print 'Finalizo la seleccion de articulos'
                                    break

                                elif res == 1:
                                    print 'ACEPTABLES: ', clei.getAceptables()

                                elif res == 2:
                                    tamAceptables = len(clei.getAceptables())
                                    print 'tam aceptables: ', tamAceptables
                                    limite = clei.crearAceptadosYEmpatados(tamAceptables, num, articulos)

                                    # Caso en que quedan articulos en la lista de empatados.
                                    if len(clei.getEmpatados()) != 0:
                                        # Caso en que queda espacio en la lista de aceptados
                                        if limite != 0:
                                            print 'A continuacion se le presentan la lista de los articulos pertenecientes a la lista de empatados: \n'
                                            print clei.getEmpatados()
                                            print '\nA continuacion se le presentan la lista de los articulos que ya pertenecen a la lista de aceptados: \n'
                                            print clei.getAceptados()
                                            print '\nEspacio restante en la lista de empatados: ', limite
                                            print '\nEscoja de entre los empatados aquellos que pasaran a los aceptados:\n'
                                            
                                            # Mientras haya espacio en la lista de aceptados
                                            while limite>0:
                                                try:
                                                    id = int(raw_input(' Indique id del articulo a seleccionar: '))
                                                    # Si el id pertenece a la lista de empatados
                                                    if id in clei.getEmpatados():
                                                        clei.setAceptados(id)
                                                        limite -= 1
                                                    else:
                                                        print 'Este id no esta en la lista de empatados'
                                                    
                                                except ValueError:
                                                    print 'Valor de id invalido'
                                                    
                                            # Se imprime la nueva lista de aceptados
                                            print 'La lista de articulos aceptados es: ', clei.getAceptados()
                                            break
                                        else:
                                            print 'La lista de articulos aceptados ya esta llena.\n'
                                            break
                                            
                                    # Si no hay articulos en la lista de empatados no se realiza
                                    # escogencia
                                    else:
                                        print 'No existen articulos en la lista de empatados.\n'
                                        break

                            # End try res
                            except ValueError:
                                print 'Opcion invalida'
                    else:
                        print 'Lo sentimos, ud no esta autorizado para esta operacion...'
                    
                else:
                    print 'Lo sentimos, este correo no pertenece a los miembros del comite. Intente de nuevo'



    # Except del try opcion
    except ValueError:
        print 'Opcion invalida'
                 
if __name__ == '__main__':
    main()