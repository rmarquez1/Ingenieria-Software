#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class Inscritos:
    def __init__(self,persona=None,paquete=None):
        self.persona = persona
        self.paquete = paquete

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

        elif dominio.find('.') == -1:
            print '\nEl formato del dominio no es valido'
            dominio = ''    
    
    return usuario+'@'+dominio