from Articulo import *
from Persona import *
from CLEI import *
from Inscripcion import *
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
        assert articulo.get_id_articulo() == 1, 'Fallo creacion de articulo'
        assert articulo.get_titulo() == 'Ingenieria', 'Fallo creacion de articulo'
        assert articulo.get_resumen() == 'Resumen', 'Fallo creacion de articulo'
        assert articulo.get_texto() == 'Texto', 'Fallo creacion de articulo'
        assert articulo.get_aceptado() == False, 'Fallo creacion de articulo'

    # Testa de asignacion de las palabras claves de los articulos
    def testPalabrasClaves(self):
        articulo = Articulo(1,'Ingenieria', 'Resumen del articulo', 'Texto del articulo',
                            'software')
        assert articulo.get_p_claves()[0] == 'software' , 'Fallo asignacion de palabras claves'
        
        articulo1 = Articulo(2, 'Sistemas', 'Resumen articulo1', 'Texto articulo1',
                             'informacion', 'tecnologia')
        assert articulo1.get_p_claves()[0] == 'informacion' , 'Fallo asignacion de palabras claves'
        assert articulo1.get_p_claves()[1] == 'tecnologia' , 'Fallo asignacion de palabras claves'
        
        articulo2 = Articulo(3, 'Traductores', 'Resumen articulo2', 'Texto articulo2',
                             'Automata', 'Lenguaje', 'Deterministico')
        assert articulo2.get_p_claves()[0] == 'Automata' , 'Fallo asignacion de palabras claves'
        assert articulo2.get_p_claves()[1] == 'Lenguaje' , 'Fallo asignacion de palabras claves'
        assert articulo2.get_p_claves()[2] == 'Deterministico' , 'Fallo asignacion de palabras claves'
        
        articulo3 = Articulo(4, 'Discretas', 'Resumen articulo3', 'Texto articulo3',
                             'Conjuntos', 'Familia', 'Interseccion', 'Inversa')
        assert articulo3.get_p_claves()[0] == 'Conjuntos','Fallo asignacion de palabras claves'
        assert articulo3.get_p_claves()[1] == 'Familia', 'Fallo asignacion de palabras claves'
        assert articulo3.get_p_claves()[2] == 'Interseccion', 'Fallo asignacion de palabras claves'
        assert articulo3.get_p_claves()[3] == 'Inversa', 'Fallo asignacion de palabras claves'
        
        articulo4 = Articulo(5, 'Software', 'Resumen articulo4', 'Texto articulo4',
                             'Clase', 'Diseno', 'Acoplamiento', 'Cohesion', 'Pruebas')
        assert articulo4.get_p_claves()[0] == 'Clase', 'Fallo asignacion de palabras claves'
        assert articulo4.get_p_claves()[1] == 'Diseno', 'Fallo asignacion de palabras claves'
        assert articulo4.get_p_claves()[2] == 'Acoplamiento', 'Fallo asignacion de palabras claves'
        assert articulo4.get_p_claves()[3] == 'Cohesion', 'Fallo asignacion de palabras claves'
        assert articulo4.get_p_claves()[4] == 'Pruebas', 'Fallo asignacion de palabras claves'
 
    # Test de asignacion arbitro-puntuacion a un articulo        
    def testAsignarArbitroPuntuacionArticulo(self):
        articulos = {}
        listaArticulos = []
        articulo = Articulo(1,'Software', 'Resumen','Texto')
        comite = Comite('correo','Franyelin', 'Colina')
        articulos[articulo.get_id_articulo()] = articulo
        listaArticulos.append(articulo)
        cont = articulo.asignar_arbitro_puntuacion(1, articulos, comite.getCorreo(), listaArticulos)
        lista = articulo.lista_arbitro_puntuacion(listaArticulos, cont)
        assert lista[0][1] == articulo.get_puntuacion()[0],'Fallo asignacion arbitro puntuacion'

    # Test de calcular el promedio de las evaluaciones de un articulo
    def testCalculoPromedio(self):
        articulo = Articulo(1, 'Sistemas', 'Resumen', 'Texto')
        articulo.set_puntuacion(5)
        articulo.set_puntuacion(4)
        articulo.calcular_promedio()
        assert articulo.calcular_promedio() == 4.5, 'Fallo calculo promedio'  


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
        articulos[articulo.get_id_articulo()] = articulo

        listaArticulos.append(articulo)
        
        clei = CLEI()
        
        cont = articulo.asignar_arbitro_puntuacion(1, articulos, comite.get_correo(), listaArticulos)
        cont = articulo.asignar_arbitro_puntuacion(1, articulos, comite1.get_correo(), listaArticulos)
        lista = articulo.lista_arbitro_puntuacion(listaArticulos, cont)
        evaluaciones[1] = lista, listaArticulos[cont].calcular_promedio()
        listaEvaluaciones = evaluaciones.items()
        # Ordenamos por promedio
        listaEvaluaciones.sort(key=lambda x: x[1][1])
        #Invertimos la lista
        listaEvaluaciones.reverse()
        clei.crear_aceptables(listaEvaluaciones)
        assert clei.get_aceptables()[0][0] == 1, 'Fallo creacion de aceptables'


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
        
        clei.set_aceptables(1,5)
        clei.set_aceptables(2,5)
        clei.set_aceptables(3,5)
        clei.set_aceptables(4,4.75)
        clei.set_aceptables(5,4.5)
        clei.set_aceptables(6,4.5)
        clei.set_aceptables(7,4)
        clei.set_aceptables(8,4)

        espacioRestante = clei.crear_aceptados_empatados(8, 4, articulos)
        assert clei.get_aceptados()[0] == 1, 'Fallo creacion de aceptados'
        assert clei.get_aceptados()[1] == 2, 'Fallo creacion de aceptados'
        assert clei.get_aceptados()[2] == 3, 'Fallo creacion de aceptados'
        assert clei.get_aceptados()[3] == 4, 'Fallo creacion de aceptados'
        assert espacioRestante == 0, 'Fallo creacion de aceptados'
        assert clei.get_empatados()[0] == 5, 'Fallo creacion de empatados'
        assert clei.get_empatados()[1] == 6, 'Fallo creacion de empatados'        

        
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
        
        clei1.set_aceptables(1,5)
        clei1.set_aceptables(2,5)
        clei1.set_aceptables(3,4.75)
        clei1.set_aceptables(4,4.75)
        clei1.set_aceptables(5,4.5)
        clei1.set_aceptables(6,4.5)
        clei1.set_aceptables(7,4)
        clei1.set_aceptables(8,4)
        espacioRestante = clei1.crear_aceptados_empatados(8, 3, articulos1)
        
        
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
        clei2.set_aceptables(1,5)
        clei2.set_aceptables(2,5)
        clei2.set_aceptables(3,5)
        clei2.set_aceptables(4,5)
        clei2.set_aceptables(5,5)
        clei2.set_aceptables(6,5)
        clei2.set_aceptables(7,5)
        clei2.set_aceptables(8,5)
        espacioRestante = clei2.crear_aceptados_empatados(8, 3, articulos2)


def main():
    print '\n ----------- BIENVENIDO AL SISTEMA CLEI ----------\n\n'
    print '                       MENU\n'
    

    try:
        num = int(raw_input('Indique el numero de articulos que se presentaran en el congreso: '))
        
        # Creamos la conferencia
        clei = CLEI(num)
        
        while True: 
            print '\n1. Crear un articulo\n'
            print '2. Crear un miembro de comite de programa\n'
            print '3. Asignar presidente del comite de programa\n'
            print '4. Asignar puntuacion y arbitro a un articulo\n'
            print '5. Inscribir un nuevo participante\n'
            print '6. Listar participantes\n'
            print '0. SALIR'
            
            try:
                opcion = int(raw_input(' Indique la operacion que desea realizar: '))
                if opcion == 0:
                    break

                elif opcion == 1:
                    clei.crear_articulos()
                    
                elif opcion == 2:
                    clei.crear_miembros_cp()

                elif opcion == 3:
                    clei.asignar_presidente_comite()

                elif opcion == 4:
                    clei.asignar_puntuacion_arbitros_articulos()

                #########################################################
                #
                #
                #Codigo a implementar para el 
                #sistema de inscripcion de usuarios
                #
                #
                #########################################################
                elif opcion == 5:
                    
                    while True:
                        try:
                            res = raw_input('\nDesea agregar un nuevo miembro? (s/n): ')
                            if res == 's' or res == 'S':
                                
                                nombre = pedir('Nombre')
                                apellido = pedir('Apellido')
                                institucion = pedir_institucion()
                                while True:
                                    correo = pedir_correo()
                                    if correo in inscritos:
                                        res = raw_input('Este correo ya esta siendo utilizado, desea introducir otro correo? (s/n): ')
                                        if res == 'n' or res == 'N':
                                            break
                                        elif res != 's' or res != 'S':
                                            print 'respuesta invalida'
                                    else:
                #Actualmente agrega la persona a la lista
                #Eventualmente debe agregar, de alguna forma, el paquete al que esta asociado
                #y quizas si es autor o no (por discutir)
                                        inscritos[correo] = Persona(nombre, apellido, institucion, correo)
                                        break
                                
                            elif res == 'n' or res == 'N':
                                break
                            
                            else:
                                print 'Respuesta invalida\n'
                        except ValueError:
                            print 'Opcion invalida\n'    
                 
                elif opcion == 6:
                
                    for  x in sorted(inscritos):
                        print '\n nombre     : ' + inscritos[x].nombre_completo()
                        print '   institucion: ' + inscritos[x].get_inst_afil()
                        print '   correo     : ' + inscritos[x].get_correo() + '\n'
      
                        
                ####################################################
                #
                #
                ####################################################
    
            except ValueError:
                print 'Opcion invalida\n'
    except ValueError:
        print 'Opcion invalida\n'   

    while True:
        print '-----  PROCESO DE SELECCION DE ARTICULOS -----'
        print '1. Desempate por presidente de comite\n'
        print '0. SALIR'
        try:
            opcion = int(raw_input('Indique el tipo de seleccion de articulos que desea utilizar: '))
            if opcion == 0:
                break

            elif opcion == 1:
                nueva_lista_aceptados = clei.seleccion_desempate()
                break
                    
        # Except del try opcion
        except ValueError:
            print 'Opcion invalida'
                 
if __name__ == '__main__':
    main()
