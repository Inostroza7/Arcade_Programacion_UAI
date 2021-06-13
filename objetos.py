"""""""""
class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print('Hola!, mi nombre es', self.nombre, self.apellido)

class Admin(Usuario):
    def superSaludo(self):
        print('Hola!, me llamo,' ,self.nombre, ' y soy Administrador')

usuario = Usuario('Gustavo','Inostroza')

usuario.saludo()
usuario.nombre = 'Ignacio'
usuario.saludo()
# del usuario.nombre # Eliminamos nombre del usuario
# del usuario
# print(usuario) #Error

admin = Admin('Elon','Musk')
admin.saludo()
admin.superSaludo()
"""""""""


class Animal:
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido

    def saludo(self):
        print('Hola soy un', self.tipo, ', mi nombre es', self.nombre, 'y mi sonido es el', self.sonido)


class Gato(Animal):
    tipo = "gato"


class Perro(Animal):
    tipo = 'perro'


perro = Perro('Firulais', 'Ladrido')
perro.saludo()

gato = Gato('Bola de nieve', 'Maullido')
gato.saludo()
