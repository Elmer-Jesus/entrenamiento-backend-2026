import json # Importamos la librería nativa para manejar JSON
class Usuario:
    def __init__(self, nombre, email, password):
        self.nombre=nombre
        self.email=email
        self.__password=password
        self.seguro=self.validar_email()

    def describir(self):
        print(f"Usuario {self.nombre} | Email: {self.email}")

    def validar_email(self):
        return "@" in self.email and self.email.count("@")==1

    # NUEVO MÉTODO: Convierte el objeto en una respuesta de API
    def to_json(self):
        # Creamos un diccionario (clave-valor) EXCLUYENDO la contraseña por seguridad
        datos_publicos={
            "nombre":self.nombre,
            "email":self.email,
            "estado":"activo",
            "seguro":self.seguro
        }
        # Convertimos el diccionario en un texto formateado tipo JSON
        return json.dumps(datos_publicos, indent=4)
# --- PRUEBA DE API ---
nuevo_usuario=Usuario("Elmer", "elmer@gmail.com", "mi_password_secreto")

print("--- Enviando datos al Frontend (Simulación) ---")
respuesta_servidor=nuevo_usuario.to_json()
print(respuesta_servidor)
print(type(respuesta_servidor)) # Verás que ahora es un 'str' (texto), listo para viajar por red