class Usuario:
    def __init__(self, nombre, email, password):
        self.nombre=nombre
        self.email=email
        self.__password=password

    def describir(self):
        print(f"Usuario {self.nombre} | Email: {self.email}")
    
    def actualizar_password(self, vieja_pass, nueva_pass):
        if vieja_pass==self.__password:
            self.__password=nueva_pass
            print("✅ Contraseña actualizada con éxito.")
        else:
            print("❌ Error: La contraseña vieja no coincide. Intento de hackeo detectado.")

    def validar_email(self, email):
        if "@" in email and email.count("@")==1:
            print("✅ Correo valido")
        else:
            print("❌El correo no es valido")
    
# --- PRUEBA DE SEGURIDAD ---
user_test=Usuario("Elmer", "elmer@gmail.com", "Elmer123")
# Verificamos si el correo es valido
user_test.validar_email("elmergmail.com")
# Intento 1: Error (Contraseña vieja mal)
user_test.actualizar_password("12345","elmer1234")
# Intento 2: Éxito
user_test.actualizar_password("Elmer123","elmer1234")
# Intento 3: ¿Podemos ver la contraseña directamente? 
try:
    print(user_test.__password)
except AttributeError:
    print("🛡️ Seguridad activa: No puedes acceder a la contraseña directamente desde afuera.")

