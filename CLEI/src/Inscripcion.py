#! /usr/bin/python

# ------------------------------------------------------------------------------
# Clase que implementa a las personas inscritas
# ------------------------------------------------------------------------------
class Inscrito():
    def __init__(self,persona=None, paquete=None):
        self.persona = persona
        
        if paquete == None:
            paquete = pedir_paquete()
        
        if paquete == '1':
            self.paquete = TipoPaqueteCharla()

        elif paquete == '2':
            self.paquete = TipoPaqueteTaller()

        elif paquete == '3':
            self.paquete = TipoPaqueteMixto()

        elif paquete == '4':
            self.paquete = TipoPaqueteAcademico()

        elif paquete == '5':
            self.paquete = TipoPaqueteTemprano()

        else:
            print 'Codigo no valido'
            self.paquete = None

    
    def get_paquete(self):
        if self.paquete != None:
            return str(self.paquete.paquete())
        else:
            return None
    def imprimir_inscrito(self):
        print '\n nombre        : ' + self.persona.nombre_completo()
        print '   institucion : ' + self.persona.get_inst_afil()
        print '   correo      : ' + self.persona.get_correo() 
        print str(self.paquete.paquete())
        
# ------------------------------------------------------------------------------
# Clase que implementa los distintos paquetes de inscripcion
# ------------------------------------------------------------------------------
class TipoPaquete():
    def __init__(self):
        pass
    
class TipoPaqueteCharla(TipoPaquete):
    def paquete(self):
        return "   paquete     : Asistencia exclusiva a charlas"

class TipoPaqueteTaller(TipoPaquete):
    def paquete(self):
        return "   paquete     : Asistencia exclusiva a talleres"
    
class TipoPaqueteMixto(TipoPaquete):
    def paquete(self):
        return"   paquete     : Asistencia a charlas y talleres"
        
class TipoPaqueteAcademico(TipoPaquete):
    def paquete(self):
        return "   paquete     : Descuento por ser academico"
        
class TipoPaqueteTemprano(TipoPaquete):
    def paquete(self):
        return "   paquete     : Descuento por compra temprana"


def pedir_paquete():
    print '\nCon que tipo de paquete desea inscribir al participante?'
    print '1. Asistencia exclusiva a talleres'
    print '2. Asistencia exclusiva a charlas'
    print '3. Asistencia a talleres y charlas'
    print '4. Descuento para academicos'
    print '5. Descuento para compras tempranas'
    return raw_input()

