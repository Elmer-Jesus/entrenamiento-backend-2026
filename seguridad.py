class Usuario:
    def __init__(self, nombre, email):
        self.nombre=nombre
        self.email=email
    def describir(self):
        print(f"Usuario {self.nombre} | Email: {self.email}")

class Admin(Usuario):
    def __init__(self,nombre, email, nivel_acceso):
        super().__init__(nombre, email)
        self.nivel_acceso=nivel_acceso
    def mostrar_privilegios(self):
        print(f"El admin {self.nombre}tiene acceso nivel:{self.nivel_acceso}")

class Invitado(Usuario):
    def __init__(self, nombre, email):
        super().__init__(nombre, email)
    def describir(self):
        print("Soy un invitado,no tengo email regsitrado")

#creamos a nuestro ususario
usuario_comun=Usuario("Elmer", "elmerjesusuquispesulla@gmail.com")
usuario_comun.describir()
#creamos a  nuestro admin
jefe=Admin("Elmer1","elmer@gamil.com","Administrador")
jefe.describir()
jefe.mostrar_privilegios()
#creamos al invitado
invitado=Invitado("Jorge","sin email")
invitado.describir()

