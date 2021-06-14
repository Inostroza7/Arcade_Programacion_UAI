class Usuario:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def saludo(self):
        print('Hola mi nombre es', self.nombre , 'y mi apellido es' , self.apellido ,'tengo', self.edad , 'años')

class Admin(Usuario):
    def saludoAdmin(self):
        print('Hola soy', self.nombre, 'y soy el Admin')

gustavo = Usuario('Gustavo', 'Inostroza','26')

# gustavo.saludo()
elon = Admin('Elon','Musk','40')

#elon.saludoAdmin()
#elon.saludo()
#gustavo.saludo()

class Paralelepipedo:
    def __init__(self,alto,largo,ancho):
        self.alto = alto
        self.largo = largo
        self.ancho = ancho

    def volumen(self):
        print(self.alto * self.largo * self.ancho)

abc = Paralelepipedo(5,2,3)
abc.volumen()