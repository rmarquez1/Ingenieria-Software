from CLEI import *
from Inscripcion import *
import sys
import unittest

# Se obtiene un numero y verifica que sea valido
def get_number(msg):
  while 1:
    try:
      num = int(raw_input("%s: " % msg))
    except ValueError:
      sys.stderr.write("El valor no es un numero...\n")
      continue
    return num

# Se obtiene un string y verifica que no sea vacio
def get_string(msg):
  while 1:
    str = raw_input("%s: " % msg)
    str = str.strip()
    if str == "":
      sys.stderr.write("Error: string vacio...\n")
      continue
    else:
      return str
  
# ------------------------------------------------------------------------------
# Pruebas de la clase Comite
# ------------------------------------------------------------------------------
class ComiteTester(unittest.TestCase):

    # Prueba de creacion de un miembro del comite de programa
    def testComite(self):
        comite = Comite('Ramon', 'Marquez', 'usb', 'correo@gmail.com')
        nombre = comite.get_nombre()
        apellido = comite.get_apellido()
        inst_afil = comite.get_inst_afil()
        correo = comite.get_correo()
        self.assertEquals('Ramon', nombre)
        self.assertEquals('Marquez', apellido)
        self.assertEquals('usb', inst_afil)
        self.assertEquals('correo@gmail.com', correo)
        
    # Test de asignacion de presidente al comite
    def testAsignarPresidente(self):
        comite = Comite('Ramon', 'Marquez', 'usb', 'correo@gmail.com')
        comite.set_es_presidente(True)
        res = comite.get_es_presidente()
        self.assertTrue(res, 'Debe ser presidente este miembro de comite')

# ------------------------------------------------------------------------------
# Prueba de la clase CLEI
# ------------------------------------------------------------------------------
class CLEITester(unittest.TestCase):
    
    # Test de asignacion de presidente de comite en la conferencia
    def testAsignarPresidenteComite(self):
        clei = CLEI(2)
        clei.crear_miembros_cp('Ramon', 'Marquez', 'usb', 'correo@gmail.com')
        clei.crear_miembros_cp('Franyelin', 'Colina', 'ucv', 'correo@hotmail.com')
        res = clei.asignar_presidente_comite('correo@gmail.com')
        res1 = clei.asignar_presidente_comite('correo@hotmail.com')
        self.assertTrue(res, 'El miembro de correo correo@gmail.com tiene que ser presidente')
        self.assertFalse(res1, 'El miembro correo@hotmail.com no puede ser presidente')
        
    
    # Test de verificar la existencia de un articulo
    def testVerificarId(self):
        clei = CLEI(3)
        articulo = Articulo(1,'Ingenieria', 'Resumen del articulo', 'Texto del articulo',
                            'software')
        
        articulo.set_autores('Ramon', 'USB', 'Venezuela')
        articulo.set_autores('Jesus', 'USB', 'Colombia')
        
        articulo1 = Articulo(2, 'Sistemas', 'Resumen articulo1', 'Texto articulo1',
                             'informacion', 'tecnologia')

        articulo1.set_autores('Marcos', 'USB', 'USA')
        articulo1.set_autores('Jose', 'USB', 'Mexico')
        articulo1.set_autores('Andreina', 'UCV', 'Venezuela')
        articulo1.set_autores('Sofia', 'UCV', 'Colombia')
        
        clei.articulos[articulo.get_id_articulo()] = articulo
        clei.articulos[articulo1.get_id_articulo()] = articulo1
        res = clei.verificar_id(1)
        res1 = clei.verificar_id(2)
        
        self.assertTrue(res,'Existe articulo 1')
        self.assertTrue(res1,'Existe articulo 2')
        
    # Test que verifica la existencia de un miembro
    def testVerificarCorreo(self):
        clei = CLEI(3)
        comite = Comite('Ramon', 'Marquez', 'usb', 'correo@gmail.com')
        comite1 = Comite('Franyelin', 'Colina', 'ucv', 'correo@hotmail.com')
        
        clei.miembros_cp[comite.get_correo()] = comite
        clei.miembros_cp[comite1.get_correo()] = comite
        
        res = clei.verificar_correo('correo@gmail.com')
        res1 = clei.verificar_correo('correo@hotmail.com')
    
        self.assertTrue(res, 'Debe existir el correo correo@gmail.com')
        self.assertTrue(res1, 'Debe existir el correo correo@hotmail.com')
        
    # Test de listar los paises participantes en la conferencia
    def testPaisConferencia(self):
        clei = CLEI(3)
        articulo = Articulo(1,'Ingenieria', 'Resumen del articulo', 'Texto del articulo',
                            'software')
        
        articulo.set_autores('Ramon', 'USB', 'Venezuela')
        articulo.set_autores('Jesus', 'USB', 'Colombia')
        
        articulo1 = Articulo(2, 'Sistemas', 'Resumen articulo1', 'Texto articulo1',
                             'informacion', 'tecnologia')

        articulo1.set_autores('Marcos', 'USB', 'USA')
        articulo1.set_autores('Jose', 'USB', 'Mexico')
        articulo1.set_autores('Andreina', 'UCV', 'Venezuela')
        articulo1.set_autores('Sofia', 'UCV', 'Colombia')
        
        articulo2 = Articulo(3, 'Traductores', 'Resumen articulo2', 'Texto articulo2',
                             'Automata', 'Lenguaje', 'Deterministico')

        articulo2.set_autores('Maria', 'USB', 'Canada')
        articulo2.set_autores('Carolina', 'USB', 'Mexico')
        articulo2.set_autores('Carla', 'UCV', 'Venezuela')
        articulo2.set_autores('Alejandro', 'UCV', 'Colombia')

        articulo3 = Articulo(4, 'Discretas', 'Resumen articulo3', 'Texto articulo3',
                             'Conjuntos', 'Familia', 'Interseccion', 'Inversa')

        articulo3.set_autores('Andres', 'USB', 'Canada')
        articulo3.set_autores('Marta', 'USB', 'Brazil')
        
        articulo4 = Articulo(5, 'Software', 'Resumen articulo4', 'Texto articulo4',
                             'Clase', 'Diseno', 'Acoplamiento', 'Cohesion', 'Pruebas')

        articulo4.set_autores('Jeremy', 'USB', 'Chile')
        articulo4.set_autores('Johandrick', 'USB', 'Argentina')
        
        clei.articulos[articulo.get_id_articulo()] = articulo
        clei.articulos[articulo1.get_id_articulo()] = articulo1
        clei.articulos[articulo2.get_id_articulo()] = articulo2
        clei.articulos[articulo3.get_id_articulo()] = articulo3
        clei.articulos[articulo4.get_id_articulo()] = articulo4
        
        clei.set_aceptables(1,4.5)
        clei.set_aceptables(2,4)
        clei.set_aceptables(3,3)
        clei.set_aceptables(4,5)
        clei.set_aceptables(5,4.5)
        
        
        lista_paises = clei.paises_conferencia()
        #print 'Lista conferencia: ', lista_paises

    # Test de articulos presentados por un pais y que sean considerados como
    # aceptables
    def testNotasArticulosPais(self):
        clei = CLEI(3)
        articulo = Articulo(1,'Ingenieria', 'Resumen del articulo', 'Texto del articulo',
                            'software')
        
        articulo.set_autores('Ramon', 'USB', 'Venezuela')
        articulo.set_autores('Jesus', 'USB', 'Colombia')
        
        articulo1 = Articulo(2, 'Sistemas', 'Resumen articulo1', 'Texto articulo1',
                             'informacion', 'tecnologia')

        articulo1.set_autores('Marcos', 'USB', 'Venezuela')
        articulo1.set_autores('Jose', 'USB', 'Mexico')
        articulo1.set_autores('Andreina', 'UCV', 'Venezuela')
        articulo1.set_autores('Sofia', 'UCV', 'Colombia')
        
        articulo2 = Articulo(3, 'Traductores', 'Resumen articulo2', 'Texto articulo2',
                             'Automata', 'Lenguaje', 'Deterministico')

        articulo2.set_autores('Maria', 'USB', 'Canada')
        articulo2.set_autores('Carolina', 'USB', 'Mexico')

        articulo3 = Articulo(4, 'Discretas', 'Resumen articulo3', 'Texto articulo3',
                             'Conjuntos', 'Familia', 'Interseccion', 'Inversa')

        articulo3.set_autores('Andres', 'USB', 'Venezuela')
        articulo3.set_autores('Marta', 'USB', 'Brazil')
        
        articulo4 = Articulo(5, 'Software', 'Resumen articulo4', 'Texto articulo4',
                             'Clase', 'Diseno', 'Acoplamiento', 'Cohesion', 'Pruebas')

        articulo4.set_autores('Jeremy', 'USB', 'Chile')
        articulo4.set_autores('Johandrick', 'USB', 'Argentina')
        
        clei.articulos[articulo.get_id_articulo()] = articulo
        clei.articulos[articulo1.get_id_articulo()] = articulo1
        clei.articulos[articulo2.get_id_articulo()] = articulo2
        clei.articulos[articulo3.get_id_articulo()] = articulo3
        clei.articulos[articulo4.get_id_articulo()] = articulo4
        
        clei.set_aceptables(1,4.5)
        clei.set_aceptables(2,4)
        clei.set_aceptables(3,3)
        clei.set_aceptables(4,5)
        
        lista_por_pais = clei.listar_notas_por_pais('Venezuela')
        self.assertEquals(len(lista_por_pais), 3)
        self.assertEquals(5, lista_por_pais[0][1])
        self.assertEquals(4.5, lista_por_pais[1][1])
        self.assertEquals(4, lista_por_pais[2][1])

    # Test de lisar los articulos aceptables por pais
    def testListarPorPais(self):
        clei = CLEI(3)
        articulo = Articulo(1,'Ingenieria', 'Resumen del articulo', 'Texto del articulo',
                            'software')
        
        articulo.set_autores('Ramon', 'USB', 'Venezuela')
        articulo.set_autores('Jesus', 'USB', 'Colombia')
        
        articulo1 = Articulo(2, 'Sistemas', 'Resumen articulo1', 'Texto articulo1',
                             'informacion', 'tecnologia')

        articulo1.set_autores('Marcos', 'USB', 'Venezuela')
        articulo1.set_autores('Jose', 'USB', 'Mexico')
        articulo1.set_autores('Andreina', 'UCV', 'Venezuela')
        articulo1.set_autores('Sofia', 'UCV', 'Colombia')
        
        articulo2 = Articulo(3, 'Traductores', 'Resumen articulo2', 'Texto articulo2',
                             'Automata', 'Lenguaje', 'Deterministico')

        articulo2.set_autores('Maria', 'USB', 'Canada')
        articulo2.set_autores('Carolina', 'USB', 'Mexico')

        articulo3 = Articulo(4, 'Discretas', 'Resumen articulo3', 'Texto articulo3',
                             'Conjuntos', 'Familia', 'Interseccion', 'Inversa')

        articulo3.set_autores('Andres', 'USB', 'Venezuela')
        articulo3.set_autores('Marta', 'USB', 'Brazil')
        
        articulo4 = Articulo(5, 'Software', 'Resumen articulo4', 'Texto articulo4',
                             'Clase', 'Diseno', 'Acoplamiento', 'Cohesion', 'Pruebas')

        articulo4.set_autores('Jeremy', 'USB', 'Chile')
        articulo4.set_autores('Johandrick', 'USB', 'Argentina')
        
        articulo5 = Articulo(6, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo5.set_autores('Jordan', 'USB', 'Chile')
        
        articulo6 = Articulo(7, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo6.set_autores('Julia', 'USB', 'Chile')

        articulo7 = Articulo(8, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo7.set_autores('Francis', 'USB', 'Canada')

        articulo8 = Articulo(9, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo8.set_autores('Francisco', 'USB', 'Venezuela')
        
        clei.crear_articulos(1, articulo)
        clei.crear_articulos(2, articulo1)
        clei.crear_articulos(3, articulo2)
        clei.crear_articulos(4, articulo3)
        clei.crear_articulos(5, articulo4)
        clei.crear_articulos(6, articulo5)
        clei.crear_articulos(7, articulo6)
        clei.crear_articulos(8, articulo7)
        clei.crear_articulos(9, articulo8)

        # ------------------------------------------------------------
        # Se agregan los arbitros puntuaciones y evaluaciones
        cont = clei.asignar_arbitro_puntuacion(1, 'correo', 4)
        clei.agregar_evaluaciones(1, cont)
        cont = clei.asignar_arbitro_puntuacion(2, 'correo', 5)
        clei.agregar_evaluaciones(2, cont)
        cont = clei.asignar_arbitro_puntuacion(3, 'correo', 4)
        clei.agregar_evaluaciones(3, cont)
        cont = clei.asignar_arbitro_puntuacion(4, 'correo', 3)
        clei.agregar_evaluaciones(4, cont)
        cont = clei.asignar_arbitro_puntuacion(5, 'correo', 4)
        clei.agregar_evaluaciones(5, cont)
        cont = clei.asignar_arbitro_puntuacion(6, 'correo', 5)
        clei.agregar_evaluaciones(6, cont)
        cont = clei.asignar_arbitro_puntuacion(7, 'correo', 5)
        clei.agregar_evaluaciones(7, cont)
        cont = clei.asignar_arbitro_puntuacion(8, 'correo', 4)
        clei.agregar_evaluaciones(8, cont)
        cont = clei.asignar_arbitro_puntuacion(9, 'correo', 4)
        clei.agregar_evaluaciones(9, cont)
        
        clei.crear_aceptables()

        lista_paises = clei.listar_articulos_por_pais(2)
        self.assertEquals(len(lista_paises[0][1]), 2)
        self.assertEquals(len(lista_paises[1][1]), 3)
        self.assertEquals(len(lista_paises[2][1]), 4)

    # Test de cantidad minima de articulos
    def testCantidadMinPais(self):
        clei = CLEI(6)
        articulo = Articulo(1,'Ingenieria', 'Resumen del articulo', 'Texto del articulo',
                            'software')
        
        articulo.set_autores('Ramon', 'USB', 'Venezuela')
        articulo.set_autores('Jesus', 'USB', 'Colombia')
        
        articulo1 = Articulo(2, 'Sistemas', 'Resumen articulo1', 'Texto articulo1',
                             'informacion', 'tecnologia')

        articulo1.set_autores('Marcos', 'USB', 'Venezuela')
        articulo1.set_autores('Jose', 'USB', 'Mexico')
        articulo1.set_autores('Andreina', 'UCV', 'Venezuela')
        articulo1.set_autores('Sofia', 'UCV', 'Colombia')
        
        articulo2 = Articulo(3, 'Traductores', 'Resumen articulo2', 'Texto articulo2',
                             'Automata', 'Lenguaje', 'Deterministico')

        articulo2.set_autores('Maria', 'USB', 'Canada')
        articulo2.set_autores('Carolina', 'USB', 'Mexico')

        articulo3 = Articulo(4, 'Discretas', 'Resumen articulo3', 'Texto articulo3',
                             'Conjuntos', 'Familia', 'Interseccion', 'Inversa')

        articulo3.set_autores('Andres', 'USB', 'Venezuela')
        articulo3.set_autores('Marta', 'USB', 'Brazil')
        
        articulo4 = Articulo(5, 'Software', 'Resumen articulo4', 'Texto articulo4',
                             'Clase', 'Diseno', 'Acoplamiento', 'Cohesion', 'Pruebas')

        articulo4.set_autores('Jeremy', 'USB', 'Chile')
        articulo4.set_autores('Johandrick', 'USB', 'Argentina')
        
        articulo5 = Articulo(6, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo5.set_autores('Jordan', 'USB', 'Chile')
        
        articulo6 = Articulo(7, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo6.set_autores('Julia', 'USB', 'Chile')

        articulo7 = Articulo(8, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo7.set_autores('Francis', 'USB', 'Canada')

        articulo8 = Articulo(9, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo8.set_autores('Francisco', 'USB', 'Venezuela')
        
        clei.crear_articulos(1, articulo)
        clei.crear_articulos(2, articulo1)
        clei.crear_articulos(3, articulo2)
        clei.crear_articulos(4, articulo3)
        clei.crear_articulos(5, articulo4)
        clei.crear_articulos(6, articulo5)
        clei.crear_articulos(7, articulo6)
        clei.crear_articulos(8, articulo7)
        clei.crear_articulos(9, articulo8)

        
        
        # ------------------------------------------------------------
        # Se agregan los arbitros puntuaciones y evaluaciones
        cont = clei.asignar_arbitro_puntuacion(1, 'correo', 4)
        clei.agregar_evaluaciones(1, cont)
        cont = clei.asignar_arbitro_puntuacion(2, 'correo', 5)
        clei.agregar_evaluaciones(2, cont)
        cont = clei.asignar_arbitro_puntuacion(3, 'correo', 4)
        clei.agregar_evaluaciones(3, cont)
        cont = clei.asignar_arbitro_puntuacion(4, 'correo', 3)
        clei.agregar_evaluaciones(4, cont)
        cont = clei.asignar_arbitro_puntuacion(5, 'correo', 4)
        clei.agregar_evaluaciones(5, cont)
        cont = clei.asignar_arbitro_puntuacion(6, 'correo', 5)
        clei.agregar_evaluaciones(6, cont)
        cont = clei.asignar_arbitro_puntuacion(7, 'correo', 5)
        clei.agregar_evaluaciones(7, cont)
        cont = clei.asignar_arbitro_puntuacion(8, 'correo', 4)
        clei.agregar_evaluaciones(8, cont)
        cont = clei.asignar_arbitro_puntuacion(9, 'correo', 4)
        clei.agregar_evaluaciones(9, cont)
        
        clei.crear_aceptables()
        # ------------------------------------------------------------
        # Probando seleccion
        lista_min = clei.cantidad_min_articulos(2)
        self.assertEquals(len(lista_min[0][1]), 2)
        self.assertEquals(len(lista_min[1][1]), 2)
        self.assertEquals(len(lista_min[2][1]), 2)

    # Test de agregacion a la lista de aceptados la cantidad minima por pais
    def testAgregarAceptados(self):
        # ---------------------------------------------------------------------
        clei = CLEI(6)
        articulo = Articulo(1,'Ingenieria', 'Resumen del articulo', 'Texto del articulo',
                            'software')
        
        articulo.set_autores('Ramon', 'USB', 'Venezuela')
        articulo.set_autores('Jesus', 'USB', 'Colombia')
        
        articulo1 = Articulo(2, 'Sistemas', 'Resumen articulo1', 'Texto articulo1',
                             'informacion', 'tecnologia')

        articulo1.set_autores('Marcos', 'USB', 'Venezuela')
        articulo1.set_autores('Jose', 'USB', 'Mexico')
        articulo1.set_autores('Andreina', 'UCV', 'Venezuela')
        articulo1.set_autores('Sofia', 'UCV', 'Colombia')
        
        articulo2 = Articulo(3, 'Traductores', 'Resumen articulo2', 'Texto articulo2',
                             'Automata', 'Lenguaje', 'Deterministico')

        articulo2.set_autores('Maria', 'USB', 'Canada')
        articulo2.set_autores('Carolina', 'USB', 'Mexico')

        articulo3 = Articulo(4, 'Discretas', 'Resumen articulo3', 'Texto articulo3',
                             'Conjuntos', 'Familia', 'Interseccion', 'Inversa')

        articulo3.set_autores('Andres', 'USB', 'Venezuela')
        articulo3.set_autores('Marta', 'USB', 'Brazil')
        
        articulo4 = Articulo(5, 'Software', 'Resumen articulo4', 'Texto articulo4',
                             'Clase', 'Diseno', 'Acoplamiento', 'Cohesion', 'Pruebas')

        articulo4.set_autores('Jeremy', 'USB', 'Chile')
        articulo4.set_autores('Johandrick', 'USB', 'Argentina')
        
        articulo5 = Articulo(6, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo5.set_autores('Jordan', 'USB', 'Chile')
        
        articulo6 = Articulo(7, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo6.set_autores('Julia', 'USB', 'Chile')

        articulo7 = Articulo(8, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo7.set_autores('Francis', 'USB', 'Canada')

        articulo8 = Articulo(9, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo8.set_autores('Francisco', 'USB', 'Venezuela')
        
        clei.crear_articulos(1, articulo)
        clei.crear_articulos(2, articulo1)
        clei.crear_articulos(3, articulo2)
        clei.crear_articulos(4, articulo3)
        clei.crear_articulos(5, articulo4)
        clei.crear_articulos(6, articulo5)
        clei.crear_articulos(7, articulo6)
        clei.crear_articulos(8, articulo7)
        clei.crear_articulos(9, articulo8)

        # ------------------------------------------------------------
        # Se agregan los arbitros puntuaciones y evaluaciones
        cont = clei.asignar_arbitro_puntuacion(1, 'correo', 4)
        clei.agregar_evaluaciones(1, cont)
        cont = clei.asignar_arbitro_puntuacion(2, 'correo', 5)
        clei.agregar_evaluaciones(2, cont)
        cont = clei.asignar_arbitro_puntuacion(3, 'correo', 4)
        clei.agregar_evaluaciones(3, cont)
        cont = clei.asignar_arbitro_puntuacion(4, 'correo', 3)
        clei.agregar_evaluaciones(4, cont)
        cont = clei.asignar_arbitro_puntuacion(5, 'correo', 4)
        clei.agregar_evaluaciones(5, cont)
        cont = clei.asignar_arbitro_puntuacion(6, 'correo', 5)
        clei.agregar_evaluaciones(6, cont)
        cont = clei.asignar_arbitro_puntuacion(7, 'correo', 5)
        clei.agregar_evaluaciones(7, cont)
        cont = clei.asignar_arbitro_puntuacion(8, 'correo', 4)
        clei.agregar_evaluaciones(8, cont)
        cont = clei.asignar_arbitro_puntuacion(9, 'correo', 4)
        clei.agregar_evaluaciones(9, cont)
        
        clei.crear_aceptables()
        # ------------------------------------------------------------
        # Probando seleccion
        num_articulos = clei.agregar_aceptados(2)
        self.assertEquals(0, num_articulos)

        # ---------------------------------------------------------------
        # Prueba 2        
        # ---------------------------------------------------------------
        clei = CLEI(7)
        articulo = Articulo(1,'Ingenieria', 'Resumen del articulo', 'Texto del articulo',
                            'software')
        
        articulo.set_autores('Ramon', 'USB', 'Venezuela')
        articulo.set_autores('Jesus', 'USB', 'Colombia')
        
        articulo1 = Articulo(2, 'Sistemas', 'Resumen articulo1', 'Texto articulo1',
                             'informacion', 'tecnologia')

        articulo1.set_autores('Marcos', 'USB', 'Venezuela')
        articulo1.set_autores('Jose', 'USB', 'Mexico')
        articulo1.set_autores('Andreina', 'UCV', 'Venezuela')
        articulo1.set_autores('Sofia', 'UCV', 'Colombia')
        
        articulo2 = Articulo(3, 'Traductores', 'Resumen articulo2', 'Texto articulo2',
                             'Automata', 'Lenguaje', 'Deterministico')

        articulo2.set_autores('Maria', 'USB', 'Canada')
        articulo2.set_autores('Carolina', 'USB', 'Mexico')

        articulo3 = Articulo(4, 'Discretas', 'Resumen articulo3', 'Texto articulo3',
                             'Conjuntos', 'Familia', 'Interseccion', 'Inversa')

        articulo3.set_autores('Andres', 'USB', 'Venezuela')
        articulo3.set_autores('Marta', 'USB', 'Brazil')
        
        articulo4 = Articulo(5, 'Software', 'Resumen articulo4', 'Texto articulo4',
                             'Clase', 'Diseno', 'Acoplamiento', 'Cohesion', 'Pruebas')

        articulo4.set_autores('Jeremy', 'USB', 'Chile')
        articulo4.set_autores('Johandrick', 'USB', 'Argentina')
        
        articulo5 = Articulo(6, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo5.set_autores('Jordan', 'USB', 'Chile')
        
        articulo6 = Articulo(7, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo6.set_autores('Julia', 'USB', 'Chile')

        articulo7 = Articulo(8, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo7.set_autores('Francis', 'USB', 'Canada')

        articulo8 = Articulo(9, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo8.set_autores('Francisco', 'USB', 'Venezuela')
        
        clei.crear_articulos(1, articulo)
        clei.crear_articulos(2, articulo1)
        clei.crear_articulos(3, articulo2)
        clei.crear_articulos(4, articulo3)
        clei.crear_articulos(5, articulo4)
        clei.crear_articulos(6, articulo5)
        clei.crear_articulos(7, articulo6)
        clei.crear_articulos(8, articulo7)
        clei.crear_articulos(9, articulo8)

        # ------------------------------------------------------------
        # Se agregan los arbitros puntuaciones y evaluaciones
        cont = clei.asignar_arbitro_puntuacion(1, 'correo', 4)
        clei.agregar_evaluaciones(1, cont)
        cont = clei.asignar_arbitro_puntuacion(2, 'correo', 5)
        clei.agregar_evaluaciones(2, cont)
        cont = clei.asignar_arbitro_puntuacion(3, 'correo', 4)
        clei.agregar_evaluaciones(3, cont)
        cont = clei.asignar_arbitro_puntuacion(4, 'correo', 3)
        clei.agregar_evaluaciones(4, cont)
        cont = clei.asignar_arbitro_puntuacion(5, 'correo', 4)
        clei.agregar_evaluaciones(5, cont)
        cont = clei.asignar_arbitro_puntuacion(6, 'correo', 5)
        clei.agregar_evaluaciones(6, cont)
        cont = clei.asignar_arbitro_puntuacion(7, 'correo', 5)
        clei.agregar_evaluaciones(7, cont)
        cont = clei.asignar_arbitro_puntuacion(8, 'correo', 4)
        clei.agregar_evaluaciones(8, cont)
        cont = clei.asignar_arbitro_puntuacion(9, 'correo', 4)
        clei.agregar_evaluaciones(9, cont)
        
        clei.crear_aceptables()
        # ------------------------------------------------------------
        # Probando seleccion
        num_articulos = clei.agregar_aceptados(2)
        self.assertEquals(1, num_articulos)

        # ---------------------------------------------------------------
        # Prueba 3        
        # ---------------------------------------------------------------
        clei = CLEI(10)
        articulo = Articulo(1,'Ingenieria', 'Resumen del articulo', 'Texto del articulo',
                            'software')
        
        articulo.set_autores('Ramon', 'USB', 'Venezuela')
        articulo.set_autores('Jesus', 'USB', 'Colombia')
        
        articulo1 = Articulo(2, 'Sistemas', 'Resumen articulo1', 'Texto articulo1',
                             'informacion', 'tecnologia')

        articulo1.set_autores('Marcos', 'USB', 'Venezuela')
        articulo1.set_autores('Jose', 'USB', 'Mexico')
        articulo1.set_autores('Andreina', 'UCV', 'Venezuela')
        articulo1.set_autores('Sofia', 'UCV', 'Colombia')
        
        articulo2 = Articulo(3, 'Traductores', 'Resumen articulo2', 'Texto articulo2',
                             'Automata', 'Lenguaje', 'Deterministico')

        articulo2.set_autores('Maria', 'USB', 'Canada')
        articulo2.set_autores('Carolina', 'USB', 'Mexico')

        articulo3 = Articulo(4, 'Discretas', 'Resumen articulo3', 'Texto articulo3',
                             'Conjuntos', 'Familia', 'Interseccion', 'Inversa')

        articulo3.set_autores('Andres', 'USB', 'Venezuela')
        articulo3.set_autores('Marta', 'USB', 'Brazil')
        
        articulo4 = Articulo(5, 'Software', 'Resumen articulo4', 'Texto articulo4',
                             'Clase', 'Diseno', 'Acoplamiento', 'Cohesion', 'Pruebas')

        articulo4.set_autores('Jeremy', 'USB', 'Chile')
        articulo4.set_autores('Johandrick', 'USB', 'Argentina')
        
        articulo5 = Articulo(6, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo5.set_autores('Jordan', 'USB', 'Chile')
        
        articulo6 = Articulo(7, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo6.set_autores('Julia', 'USB', 'Chile')

        articulo7 = Articulo(8, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo7.set_autores('Francis', 'USB', 'Canada')

        articulo8 = Articulo(9, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo8.set_autores('Francisco', 'USB', 'Venezuela')
        
        clei.crear_articulos(1, articulo)
        clei.crear_articulos(2, articulo1)
        clei.crear_articulos(3, articulo2)
        clei.crear_articulos(4, articulo3)
        clei.crear_articulos(5, articulo4)
        clei.crear_articulos(6, articulo5)
        clei.crear_articulos(7, articulo6)
        clei.crear_articulos(8, articulo7)
        clei.crear_articulos(9, articulo8)

        # ------------------------------------------------------------
        # Se agregan los arbitros puntuaciones y evaluaciones
        cont = clei.asignar_arbitro_puntuacion(1, 'correo', 4)
        clei.agregar_evaluaciones(1, cont)
        cont = clei.asignar_arbitro_puntuacion(2, 'correo', 5)
        clei.agregar_evaluaciones(2, cont)
        cont = clei.asignar_arbitro_puntuacion(3, 'correo', 4)
        clei.agregar_evaluaciones(3, cont)
        cont = clei.asignar_arbitro_puntuacion(4, 'correo', 3)
        clei.agregar_evaluaciones(4, cont)
        cont = clei.asignar_arbitro_puntuacion(5, 'correo', 4)
        clei.agregar_evaluaciones(5, cont)
        cont = clei.asignar_arbitro_puntuacion(6, 'correo', 5)
        clei.agregar_evaluaciones(6, cont)
        cont = clei.asignar_arbitro_puntuacion(7, 'correo', 5)
        clei.agregar_evaluaciones(7, cont)
        cont = clei.asignar_arbitro_puntuacion(8, 'correo', 4)
        clei.agregar_evaluaciones(8, cont)
        cont = clei.asignar_arbitro_puntuacion(9, 'correo', 4)
        clei.agregar_evaluaciones(9, cont)
        
        clei.crear_aceptables()
        # ------------------------------------------------------------
        # Probando seleccion
        num_articulos = clei.agregar_aceptados(2)
        self.assertEquals(4, num_articulos)


    # Test de cantidad minima de articulos
    def testSeleccionPais(self):
        # ---------------------------------------------------------------------
        clei = CLEI(6)
        articulo = Articulo(1,'Ingenieria', 'Resumen del articulo', 'Texto del articulo',
                            'software')
        
        articulo.set_autores('Ramon', 'USB', 'Venezuela')
        articulo.set_autores('Jesus', 'USB', 'Colombia')
        
        articulo1 = Articulo(2, 'Sistemas', 'Resumen articulo1', 'Texto articulo1',
                             'informacion', 'tecnologia')

        articulo1.set_autores('Marcos', 'USB', 'Venezuela')
        articulo1.set_autores('Jose', 'USB', 'Mexico')
        articulo1.set_autores('Andreina', 'UCV', 'Venezuela')
        articulo1.set_autores('Sofia', 'UCV', 'Colombia')
        
        articulo2 = Articulo(3, 'Traductores', 'Resumen articulo2', 'Texto articulo2',
                             'Automata', 'Lenguaje', 'Deterministico')

        articulo2.set_autores('Maria', 'USB', 'Canada')
        articulo2.set_autores('Carolina', 'USB', 'Mexico')

        articulo3 = Articulo(4, 'Discretas', 'Resumen articulo3', 'Texto articulo3',
                             'Conjuntos', 'Familia', 'Interseccion', 'Inversa')

        articulo3.set_autores('Andres', 'USB', 'Venezuela')
        articulo3.set_autores('Marta', 'USB', 'Brazil')
        
        articulo4 = Articulo(5, 'Software', 'Resumen articulo4', 'Texto articulo4',
                             'Clase', 'Diseno', 'Acoplamiento', 'Cohesion', 'Pruebas')

        articulo4.set_autores('Jeremy', 'USB', 'Chile')
        articulo4.set_autores('Johandrick', 'USB', 'Argentina')
        
        articulo5 = Articulo(6, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo5.set_autores('Jordan', 'USB', 'Chile')
        
        articulo6 = Articulo(7, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo6.set_autores('Julia', 'USB', 'Chile')

        articulo7 = Articulo(8, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo7.set_autores('Francis', 'USB', 'Canada')

        articulo8 = Articulo(9, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo8.set_autores('Francisco', 'USB', 'Venezuela')
        
        clei.crear_articulos(1, articulo)
        clei.crear_articulos(2, articulo1)
        clei.crear_articulos(3, articulo2)
        clei.crear_articulos(4, articulo3)
        clei.crear_articulos(5, articulo4)
        clei.crear_articulos(6, articulo5)
        clei.crear_articulos(7, articulo6)
        clei.crear_articulos(8, articulo7)
        clei.crear_articulos(9, articulo8)

        
        
        # ------------------------------------------------------------
        # Se agregan los arbitros puntuaciones y evaluaciones
        cont = clei.asignar_arbitro_puntuacion(1, 'correo', 4)
        clei.agregar_evaluaciones(1, cont)
        cont = clei.asignar_arbitro_puntuacion(2, 'correo', 5)
        clei.agregar_evaluaciones(2, cont)
        cont = clei.asignar_arbitro_puntuacion(3, 'correo', 4)
        clei.agregar_evaluaciones(3, cont)
        cont = clei.asignar_arbitro_puntuacion(4, 'correo', 3)
        clei.agregar_evaluaciones(4, cont)
        cont = clei.asignar_arbitro_puntuacion(5, 'correo', 4)
        clei.agregar_evaluaciones(5, cont)
        cont = clei.asignar_arbitro_puntuacion(6, 'correo', 5)
        clei.agregar_evaluaciones(6, cont)
        cont = clei.asignar_arbitro_puntuacion(7, 'correo', 5)
        clei.agregar_evaluaciones(7, cont)
        cont = clei.asignar_arbitro_puntuacion(8, 'correo', 4)
        clei.agregar_evaluaciones(8, cont)
        cont = clei.asignar_arbitro_puntuacion(9, 'correo', 4)
        clei.agregar_evaluaciones(9, cont)
        
        clei.crear_aceptables()
        # ------------------------------------------------------------
        # Probando seleccion
        num_articulos = clei.agregar_aceptados(2)
        self.assertEquals(0, num_articulos)

        # ---------------------------------------------------------------
        # Prueba 2        
        # ---------------------------------------------------------------
        clei = CLEI(7)
        articulo = Articulo(1,'Ingenieria', 'Resumen del articulo', 'Texto del articulo',
                            'software')
        
        articulo.set_autores('Ramon', 'USB', 'Venezuela')
        articulo.set_autores('Jesus', 'USB', 'Colombia')
        
        articulo1 = Articulo(2, 'Sistemas', 'Resumen articulo1', 'Texto articulo1',
                             'informacion', 'tecnologia')

        articulo1.set_autores('Marcos', 'USB', 'Venezuela')
        articulo1.set_autores('Jose', 'USB', 'Mexico')
        articulo1.set_autores('Andreina', 'UCV', 'Venezuela')
        articulo1.set_autores('Sofia', 'UCV', 'Colombia')
        
        articulo2 = Articulo(3, 'Traductores', 'Resumen articulo2', 'Texto articulo2',
                             'Automata', 'Lenguaje', 'Deterministico')

        articulo2.set_autores('Maria', 'USB', 'Canada')
        articulo2.set_autores('Carolina', 'USB', 'Mexico')

        articulo3 = Articulo(4, 'Discretas', 'Resumen articulo3', 'Texto articulo3',
                             'Conjuntos', 'Familia', 'Interseccion', 'Inversa')

        articulo3.set_autores('Andres', 'USB', 'Venezuela')
        articulo3.set_autores('Marta', 'USB', 'Brazil')
        
        articulo4 = Articulo(5, 'Software', 'Resumen articulo4', 'Texto articulo4',
                             'Clase', 'Diseno', 'Acoplamiento', 'Cohesion', 'Pruebas')

        articulo4.set_autores('Jeremy', 'USB', 'Chile')
        articulo4.set_autores('Johandrick', 'USB', 'Argentina')
        
        articulo5 = Articulo(6, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo5.set_autores('Jordan', 'USB', 'Chile')
        
        articulo6 = Articulo(7, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo6.set_autores('Julia', 'USB', 'Chile')

        articulo7 = Articulo(8, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo7.set_autores('Francis', 'USB', 'Canada')

        articulo8 = Articulo(9, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo8.set_autores('Francisco', 'USB', 'Venezuela')

        articulo9 = Articulo(10, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo9.set_autores('Irene', 'USB', 'Venezuela')
        
        clei.crear_articulos(1, articulo)
        clei.crear_articulos(2, articulo1)
        clei.crear_articulos(3, articulo2)
        clei.crear_articulos(4, articulo3)
        clei.crear_articulos(5, articulo4)
        clei.crear_articulos(6, articulo5)
        clei.crear_articulos(7, articulo6)
        clei.crear_articulos(8, articulo7)
        clei.crear_articulos(9, articulo8)
        clei.crear_articulos(10, articulo9)

        # ------------------------------------------------------------
        # Se agregan los arbitros puntuaciones y evaluaciones
        cont = clei.asignar_arbitro_puntuacion(1, 'correo', 4)
        clei.agregar_evaluaciones(1, cont)
        cont = clei.asignar_arbitro_puntuacion(2, 'correo', 5)
        clei.agregar_evaluaciones(2, cont)
        cont = clei.asignar_arbitro_puntuacion(3, 'correo', 4)
        clei.agregar_evaluaciones(3, cont)
        cont = clei.asignar_arbitro_puntuacion(4, 'correo', 3)
        clei.agregar_evaluaciones(4, cont)
        cont = clei.asignar_arbitro_puntuacion(5, 'correo', 4)
        clei.agregar_evaluaciones(5, cont)
        cont = clei.asignar_arbitro_puntuacion(6, 'correo', 5)
        clei.agregar_evaluaciones(6, cont)
        cont = clei.asignar_arbitro_puntuacion(7, 'correo', 5)
        clei.agregar_evaluaciones(7, cont)
        cont = clei.asignar_arbitro_puntuacion(8, 'correo', 4)
        clei.agregar_evaluaciones(8, cont)
        cont = clei.asignar_arbitro_puntuacion(9, 'correo', 4)
        clei.agregar_evaluaciones(9, cont)
        cont = clei.asignar_arbitro_puntuacion(10, 'correo', 4)
        clei.agregar_evaluaciones(10, cont)
        
        clei.crear_aceptables()
        # ------------------------------------------------------------
        # Probando seleccion
        num_articulos = clei.agregar_aceptados(2)
        clei.seleccionar_por_pais(2)
        self.assertEquals(0, clei.get_num_articulos())


        # ---------------------------------------------------------------
        # Prueba 3        
        # ---------------------------------------------------------------
        clei = CLEI(8)
        articulo = Articulo(1,'Ingenieria', 'Resumen del articulo', 'Texto del articulo',
                            'software')
        
        articulo.set_autores('Ramon', 'USB', 'Venezuela')
        articulo.set_autores('Jesus', 'USB', 'Colombia')
        
        articulo1 = Articulo(2, 'Sistemas', 'Resumen articulo1', 'Texto articulo1',
                             'informacion', 'tecnologia')

        articulo1.set_autores('Marcos', 'USB', 'Venezuela')
        articulo1.set_autores('Jose', 'USB', 'Mexico')
        articulo1.set_autores('Andreina', 'UCV', 'Venezuela')
        articulo1.set_autores('Sofia', 'UCV', 'Colombia')
        
        articulo2 = Articulo(3, 'Traductores', 'Resumen articulo2', 'Texto articulo2',
                             'Automata', 'Lenguaje', 'Deterministico')

        articulo2.set_autores('Maria', 'USB', 'Canada')
        articulo2.set_autores('Carolina', 'USB', 'Mexico')

        articulo3 = Articulo(4, 'Discretas', 'Resumen articulo3', 'Texto articulo3',
                             'Conjuntos', 'Familia', 'Interseccion', 'Inversa')

        articulo3.set_autores('Andres', 'USB', 'Venezuela')
        articulo3.set_autores('Marta', 'USB', 'Brazil')
        
        articulo4 = Articulo(5, 'Software', 'Resumen articulo4', 'Texto articulo4',
                             'Clase', 'Diseno', 'Acoplamiento', 'Cohesion', 'Pruebas')

        articulo4.set_autores('Jeremy', 'USB', 'Chile')
        articulo4.set_autores('Johandrick', 'USB', 'Argentina')
        
        articulo5 = Articulo(6, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo5.set_autores('Jordan', 'USB', 'Chile')
        
        articulo6 = Articulo(7, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo6.set_autores('Julia', 'USB', 'Chile')

        articulo7 = Articulo(8, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo7.set_autores('Francis', 'USB', 'Canada')

        articulo8 = Articulo(9, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo8.set_autores('Francisco', 'USB', 'Venezuela')

        articulo9 = Articulo(10, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo9.set_autores('Irene', 'USB', 'Venezuela')
        
        clei.crear_articulos(1, articulo)
        clei.crear_articulos(2, articulo1)
        clei.crear_articulos(3, articulo2)
        clei.crear_articulos(4, articulo3)
        clei.crear_articulos(5, articulo4)
        clei.crear_articulos(6, articulo5)
        clei.crear_articulos(7, articulo6)
        clei.crear_articulos(8, articulo7)
        clei.crear_articulos(9, articulo8)
        clei.crear_articulos(10, articulo9)

        # ------------------------------------------------------------
        # Se agregan los arbitros puntuaciones y evaluaciones
        cont = clei.asignar_arbitro_puntuacion(1, 'correo', 4)
        clei.agregar_evaluaciones(1, cont)
        cont = clei.asignar_arbitro_puntuacion(2, 'correo', 5)
        clei.agregar_evaluaciones(2, cont)
        cont = clei.asignar_arbitro_puntuacion(3, 'correo', 4)
        clei.agregar_evaluaciones(3, cont)
        cont = clei.asignar_arbitro_puntuacion(4, 'correo', 3)
        clei.agregar_evaluaciones(4, cont)
        cont = clei.asignar_arbitro_puntuacion(5, 'correo', 4)
        clei.agregar_evaluaciones(5, cont)
        cont = clei.asignar_arbitro_puntuacion(6, 'correo', 5)
        clei.agregar_evaluaciones(6, cont)
        cont = clei.asignar_arbitro_puntuacion(7, 'correo', 5)
        clei.agregar_evaluaciones(7, cont)
        cont = clei.asignar_arbitro_puntuacion(8, 'correo', 4)
        clei.agregar_evaluaciones(8, cont)
        cont = clei.asignar_arbitro_puntuacion(9, 'correo', 4)
        clei.agregar_evaluaciones(9, cont)
        cont = clei.asignar_arbitro_puntuacion(10, 'correo', 4)
        clei.agregar_evaluaciones(10, cont)
        
        clei.crear_aceptables()
        # ------------------------------------------------------------
        # Probando seleccion
        num_articulos = clei.agregar_aceptados(2)
        clei.seleccionar_por_pais(2)
        self.assertEquals(1, clei.get_num_articulos())
        
        # ---------------------------------------------------------------
        # Prueba 4        
        # ---------------------------------------------------------------
        clei = CLEI(10)
        articulo = Articulo(1,'Ingenieria', 'Resumen del articulo', 'Texto del articulo',
                            'software')
        
        articulo.set_autores('Ramon', 'USB', 'Venezuela')
        articulo.set_autores('Jesus', 'USB', 'Colombia')
        
        articulo1 = Articulo(2, 'Sistemas', 'Resumen articulo1', 'Texto articulo1',
                             'informacion', 'tecnologia')

        articulo1.set_autores('Marcos', 'USB', 'Venezuela')
        articulo1.set_autores('Jose', 'USB', 'Mexico')
        articulo1.set_autores('Andreina', 'UCV', 'Venezuela')
        articulo1.set_autores('Sofia', 'UCV', 'Colombia')
        
        articulo2 = Articulo(3, 'Traductores', 'Resumen articulo2', 'Texto articulo2',
                             'Automata', 'Lenguaje', 'Deterministico')

        articulo2.set_autores('Maria', 'USB', 'Canada')
        articulo2.set_autores('Carolina', 'USB', 'Mexico')

        articulo3 = Articulo(4, 'Discretas', 'Resumen articulo3', 'Texto articulo3',
                             'Conjuntos', 'Familia', 'Interseccion', 'Inversa')

        articulo3.set_autores('Andres', 'USB', 'Venezuela')
        articulo3.set_autores('Marta', 'USB', 'Brazil')
        
        articulo4 = Articulo(5, 'Software', 'Resumen articulo4', 'Texto articulo4',
                             'Clase', 'Diseno', 'Acoplamiento', 'Cohesion', 'Pruebas')

        articulo4.set_autores('Jeremy', 'USB', 'Chile')
        articulo4.set_autores('Johandrick', 'USB', 'Argentina')
        
        articulo5 = Articulo(6, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo5.set_autores('Jordan', 'USB', 'Chile')
        
        articulo6 = Articulo(7, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo6.set_autores('Julia', 'USB', 'Chile')

        articulo7 = Articulo(8, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo7.set_autores('Francis', 'USB', 'Canada')

        articulo8 = Articulo(9, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo8.set_autores('Francisco', 'USB', 'Venezuela')

        articulo9 = Articulo(10, 'Software1', 'Resumen articulo', 'Texto articulo',
                             'Clase')

        articulo9.set_autores('Irene', 'USB', 'Venezuela')
        
        clei.crear_articulos(1, articulo)
        clei.crear_articulos(2, articulo1)
        clei.crear_articulos(3, articulo2)
        clei.crear_articulos(4, articulo3)
        clei.crear_articulos(5, articulo4)
        clei.crear_articulos(6, articulo5)
        clei.crear_articulos(7, articulo6)
        clei.crear_articulos(8, articulo7)
        clei.crear_articulos(9, articulo8)
        clei.crear_articulos(10, articulo9)

        # ------------------------------------------------------------
        # Se agregan los arbitros puntuaciones y evaluaciones
        cont = clei.asignar_arbitro_puntuacion(1, 'correo', 4)
        clei.agregar_evaluaciones(1, cont)
        cont = clei.asignar_arbitro_puntuacion(2, 'correo', 5)
        clei.agregar_evaluaciones(2, cont)
        cont = clei.asignar_arbitro_puntuacion(3, 'correo', 4)
        clei.agregar_evaluaciones(3, cont)
        cont = clei.asignar_arbitro_puntuacion(4, 'correo', 3)
        clei.agregar_evaluaciones(4, cont)
        cont = clei.asignar_arbitro_puntuacion(5, 'correo', 4)
        clei.agregar_evaluaciones(5, cont)
        cont = clei.asignar_arbitro_puntuacion(6, 'correo', 5)
        clei.agregar_evaluaciones(6, cont)
        cont = clei.asignar_arbitro_puntuacion(7, 'correo', 5)
        clei.agregar_evaluaciones(7, cont)
        cont = clei.asignar_arbitro_puntuacion(8, 'correo', 4)
        clei.agregar_evaluaciones(8, cont)
        cont = clei.asignar_arbitro_puntuacion(9, 'correo', 4)
        clei.agregar_evaluaciones(9, cont)
        cont = clei.asignar_arbitro_puntuacion(10, 'correo', 4)
        clei.agregar_evaluaciones(10, cont)
        
        clei.crear_aceptables()
        # ------------------------------------------------------------
        # Probando seleccion
        num_articulos = clei.agregar_aceptados(2)
        clei.seleccionar_por_pais(2)
        self.assertEquals(0, clei.get_num_articulos())

# -----------------------------------------------------------------------------
#                               MAIN PRINCIPAL
# -----------------------------------------------------------------------------
def main():
    print '\n ----------- BIENVENIDO AL SISTEMA CLEI ----------\n\n'
    print '                       MENU\n'
    
    num = get_number('Indique el numero de articulos que se presentaran en el congreso')   
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

        opcion = get_number(' Indique la operacion que desea realizar')
        if opcion == 0:
            break

        elif opcion == 1:
            while True:
                res = get_string('Crear articulo (s/n)')
                if res == 's' or res == 'S':
                    id_articulo = get_number('ID')
                    existe_id = clei.verificar_id(id_articulo)
                    if existe_id == True:
                        print 'Ya existe articulo con ese id'
                    else:
                        titulo = get_string('Titulo')
                        resumen = get_string('Resumen')
                        texto = get_string('Texto')

                        while True:
                            num_p_claves = get_number('Indique cuantas palabras claves desea asignar al articulo')
                            if num_p_claves < 1 or num_p_claves > 5:
                                print '\nPuede asignar minimo 1 y maximo 5 palabras claves\n'

                            else:
                                if num_p_claves == 1:
                                    p_clave = get_string('Palabra clave')
                                    articulo = Articulo(id_articulo, titulo, resumen, texto, p_clave)

                                elif num_p_claves == 2:
                                    p_clave1 = get_string('Palabra clave')
                                    p_clave2 = get_string('Palabra clave')
                                    articulo = Articulo(id_articulo, titulo, resumen, texto, p_clave1, p_clave2)

                                elif num_p_claves == 3:
                                    p_clave1 = get_string('Palabra clave')
                                    p_clave2 = get_string('Palabra clave')
                                    p_clave3 = get_string('Palabra clave')
                                    articulo = Articulo(id_articulo, titulo, resumen, texto, p_clave1, p_clave2, p_clave3)

                                elif num_p_claves == 4:
                                    p_clave1 = get_string('Palabra clave')
                                    p_clave2 = get_string('Palabra clave')
                                    p_clave3 = get_string('Palabra clave')
                                    p_clave4 = get_string('Palabra clave')
                                    articulo = Articulo(id_articulo, titulo, resumen, texto, p_clave1, p_clave2, p_clave3, p_clave4)

                                elif num_p_claves == 5:
                                    p_clave1 = get_string('Palabra clave')
                                    p_clave2 = get_string('Palabra clave')
                                    p_clave3 = get_string('Palabra clave')
                                    p_clave4 = get_string('Palabra clave')
                                    p_clave5 = get_string('Palabra clave')
                                    articulo = Articulo(id_articulo, titulo, resumen, texto, p_clave1, p_clave2, p_clave3, p_clave4, p_clave5)


                                num_autores = get_number('Indique cantidad de autores')
                                clei.crear_articulos(id_articulo,articulo)
                                # Asignamos los autores al articulo
                                for i in range(num_autores):
                                    nombre_autor = get_string('Indique el nombre del autor')
                                    inst_afil = get_string('Indique la institucion principal')
                                    pais = get_string('Indique el pais proveniente')
                                    clei.asignar_autores(id_articulo,nombre_autor, inst_afil, pais)
                                clei.articulos[id_articulo].imprimir_autores()
                                break
                elif res == 'n' or res == 'N':
                    break
                else:
                    print '\nIndique s/n\n'

        elif opcion == 2:
            while True:
                res = get_string('Crear miembro del CP (s/n)')
                if res == 's' or res == 'S':
                    correo = get_string('Correo')
                    res = clei.verificar_correo(correo)
                    if res == True:
                        print 'Ya existe un miembro con ese correo. Intentelo de nuevo'
                    else:
                        nombre = get_string('Nombre')
                        apellido = get_string('Apellido')
                        inst_afil = get_string('Institucion principal')
                        clei.crear_miembros_cp(nombre, apellido, inst_afil, correo)

                elif res == 'n' or res == 'N':
                    break
                else:
                    print 'Indique s/n'

        elif opcion == 3:
            if len(clei.miembros_cp) != 0:
                while True:
                    presidente = get_string('Indique el presidente del comite de programa')
                    res = clei.verificar_correo(presidente)
                    if res == True:
                        clei.asignar_presidente_comite(presidente)
                        break
                    else:
                        print 'Miembro inexistente. Intente de nuevo'
            else:
                print 'No existe miembros en el comite de programa. Debe crearlos'   

        elif opcion == 4:
            while True:
                if len(clei.miembros_cp)>0 and len(clei.articulos)>0:
                    res = get_string('   Crear arbitros y puntuaciones (s/n)')
                    if res == 's' or res == 'S':   
                        id_articulo = get_number('    ID del articulo a evaluar')
                        existe_id = clei.verificar_id(id_articulo)
                        if existe_id == True:
                            while True:
                                correo = get_string('    Correo del arbitro')
                                existe_correo = clei.verificar_correo(correo)
                                if existe_correo == True:
                                    # Verificamos que ese arbitro no haya evaluado este articulo
                                    ya_evaluo = clei.verificar_arbitro_evaluo(id_articulo, correo)
                                    if  ya_evaluo == False:
                                        while True:
                                            puntaje = get_number('    Ingrese el puntaje')
                                            # Si el puntaje esta en el rango de 1 a 5
                                            if puntaje >= 1 and puntaje <= 5:
                                                cont = clei.asignar_arbitro_puntuacion(id_articulo, correo, puntaje)
                                            else: 
                                                print 'La nota debe ser de 1 a 5. Intentelo de nuevo'
                                            break
                                    else:
                                        print 'Este miembro de comite ya evaluo este articulo'

                                    r = raw_input('    Agregar otro arbitro (s/n):' )
                                    if r == 'N' or r == 'n':
                                        break
                                else:
                                    print 'No existe arbitro con ese correo'

                            clei.agregar_evaluaciones(id_articulo, cont)
                        else:
                            print '\nNo existe articulo con ese id\n'    

                    elif res == 'n' or res == 'N':
                        clei.crear_aceptables()
                        break
                    else:
                        print 'Indique s/n'

                    print clei.evaluaciones
                else:
                    print '''No hay informacion suficiente para realizar esta operacion. Verifique que haya creado articulos
    y miembros de comite de programa''' 
                    break

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
                    res = get_string('\nDesea agregar un nuevo miembro? (s/n)')
                    if res == 's' or res == 'S':

                        nombre = pedir('Nombre')
                        apellido = pedir('Apellido')
                        institucion = pedir_institucion()
                        while True:
                            correo = pedir_correo()
                            if correo in inscritos:
                                res = get_string('Este correo ya esta siendo utilizado, desea introducir otro correo? (s/n): ')
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

        elif opcion == 6:

            for  x in sorted(inscritos):
                print '\n nombre     : ' + inscritos[x].nombre_completo()
                print '   institucion: ' + inscritos[x].get_inst_afil()
                print '   correo     : ' + inscritos[x].get_correo() + '\n'


    while True:
        print '-----  PROCESO DE SELECCION DE ARTICULOS -----'
        print '1. Desempate por presidente de comite\n'
        print '2. Articulos escogidos por pais\n'
        print '0. SALIR'
        
        opcion = get_number('Indique el tipo de seleccion de articulos que desea utilizar')
        if opcion == 0:
            break

        elif opcion == 1:
            correo_presi = get_string('Indique su correo como presidente')
            # si el correo pertenece al correo de los miembros registrados
            existe_correo = clei.verificar_correo(correo_presi)
            if existe_correo == True:
                # Verificamos que el correo ingresado sea el correo del presidente
                if clei.miembros_cp[correo_presi].get_es_presidente() == True:
                    print '-----------------------------------------------'
                    print 'Bienvenido presidente del comite de programa.\n'
                    print '\nElija entre las siguientes opciones:\n'

                    while True:
                        print ' 1. Ver lista de articulos aceptables.\n'
                        print ' 2. Generar articulos a ser aceptados en la conferencia.\n'
                        print ' 0. SALIR'
                        res = get_number('   Indique el tipo de operacion')

                        if res == 0:
                            print 'Finalizo la seleccion de articulos'
                            break

                        elif res == 1:
                            print 'ACEPTABLES: ', clei.get_aceptables()

                        elif res == 2:
                            tam_aceptables = len(clei.get_aceptables())
                            print 'tam aceptables: ', tam_aceptables
                            promedios = clei.listar_promedios(clei.get_aceptables())
                            limite = clei.crear_aceptados_empatados(promedios, clei.get_aceptables())

                            # Caso en que quedan articulos en la lista de empatados.
                            if len(clei.get_empatados()) != 0:
                                # Caso en que queda espacio en la lista de aceptados
                                if limite != 0:
                                    print 'A continuacion se le presentan los articulos pertenecientes a la lista de empatados: \n'
                                    print clei.mostrar_empatados()
                                    print '\nA continuacion se le presentan los articulos que ya pertenecen a la lista de aceptados: \n'
                                    print clei.mostrar_aceptados()
                                    print '\nEspacio restante en la lista de aceptados: ', limite
                                    print '\nEscoja de entre los empatados aquellos que pasaran a los aceptados:\n'

                                    # Mientras haya espacio en la lista de aceptados
                                    while limite>0:
                                        id = get_number(' Indique id del articulo a seleccionar')
                                        clei.seleccionar_desempate(id)
                                        limite -= 1
                                        
                                    print 'Los articulos aceptados son: '
                                    clei.mostrar_aceptados()
                                    break

                                else:
                                    print 'Los articulos aceptados son: '
                                    clei.mostrar_aceptados()
                                    break

                            # Si no hay articulos en la lista de empatados no se realiza
                            # escogencia
                            else:
                                print 'Los articulos aceptados son: '
                                clei.mostrar_aceptados()
                                break

                else:
                    print 'Lo sentimos, ud no esta autorizado para esta operacion...'

            else:
                print 'Lo sentimos, este correo no pertenece a los miembros del comite. Intente de nuevo'

        elif opcion == 2:
            num = get_number('Indique el minimo de articulos por pais')
            # Generamos la lista de los paises participantes en la conferencia
            lista_paises = clei.paises_conferencia()
            valor = num * len(lista_paises)
            # Caso en que el el numero minimo de articulos permitidos por pais
            # por la cantidad de paises participando en la conferencia es menor
            # o igual a la cantidad de articulos maximo que se permiten en la
            # conferencia
            if valor <= clei.get_num_articulos():
                # Obtenemos lo que nos falta para llenar la lista de aceptados
                limite = clei.agregar_aceptados(num)
                # Caso en que halla espacio en la lista de aceptados
                if limite != 0:
                    clei.seleccionar_por_pais(num)
                    # Caso en que haya empates y siga incompleta la lista de 
                    # aceptados
                    if clei.get_num_articulos() != 0:
                        correo_presi = get_string('Indique su correo como presidente')
                        # si el correo pertenece al correo de los miembros registrados
                        existe_correo = clei.verificar_correo(correo_presi)
                        if existe_correo == True:
                            # Verificamos que el correo ingresado sea el correo del presidente
                            if clei.miembros_cp[correo_presi].get_es_presidente() == True:
                                print 'Los empatados se presentan a continuacion: '
                                clei.mostrar_empatados()
                                print '\n Los aceptables por el momento son: '
                                clei.mostrar_aceptados()
                                print '\nEspacio restante en la lista de aceptados: ', limite
                                print '\nEscoja de entre los empatados aquellos que pasaran a los aceptados:\n'
                                # Mientras haya espacio en la lista de aceptados
                                while limite>0:
                                    id = get_number(' Indique id del articulo a seleccionar')
                                    clei.seleccionar_desempate(id)
                                    limite -= 1

                                print 'Los articulos aceptados son: '
                                clei.mostrar_aceptados()
                                break
                            else:
                                print 'Lo sentimos, ud no esta autorizado para esta operacion...'
                        else:
                            print 'Lo sentimos, este correo no pertenece a los miembros del comite. Intente de nuevo'
                    else:
                        print 'Los articulos aceptados son: '
                        clei.mostrar_aceptados()
                        break
                else:
                    print 'Los articulos aceptados son: '
                    clei.mostrar_aceptados()
                    break
            else:
                print 'El numero minimo de articulos por la cantidad de paises debe ser menor o igual que el numero de articulos en la conferencia'
                
                 
if __name__ == '__main__':
   main()