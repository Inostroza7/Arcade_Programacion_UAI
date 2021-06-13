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