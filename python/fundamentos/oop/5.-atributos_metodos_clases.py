# Atributos, métodos de clase, métodos estáticos


# Definición de la clase
class Estudiante:
# Atributo de clase
    colegio = "Liceo Vate Vicente Huidobro"
# Lista en donde estén todos los estudiantes.
estudiantes = []

# Método constructor
def __init__(self, nombre, nota):
    #Atributos de instancia
    self.nombre = nombre
    self.nota = nota
    # Agregar elementos a la lista estudiantes.
    Estudiante.estudiantes.append(self)


    # Método de instancia
def mostrar_info(self):
    print(f"Nombre: {self.nombre}")
    print(f"Nota: {self.nota}")


# Método de CLASE
# Usa "CLS" porque trabaja con la información de la clase.
@classmethod
def cambiar_colegio(cls, nuevo_nombre):
    

    @classmethod # Contar la cantidad de estudiantes existentes
    def cantidad_estudiantes(cls):
        return len(cls.estudiantes)
    
    # Método estático
    print ("=== MÉTODO ESTÁTICO ===")

    print("¿{e1.nombre} aprueba?")
    print(Estudiante.aprobar(e1.nota))

    # Este no usa CLS ni SELF, sólo parámetros.
    @staticmethod
    def aprobar(nota):
        if nota >= 4.0:
            return True
        else:
            return False
    
    
# Creación de objetos (instancias)
e1 = Estudiante("Donovan", 4.0)
e2 = Estudiante("Randy", 6.7)

# Uso de métodos de instancia
print("== MÉTODO DE INSTANCIA ==")
# Mostrar datos de estudiantes.
e1.mostrar_info()
print()
e2.mostrar_info()
print()

# Uso de método de clase
print("=== MÉTODO DE CLASE ===")

Estudiante.cambiar_colegio("Purkuyén")
print(e1.colegio)
print(e2.colegio)
print()

# Contar estudiantes.
print("=== CONTAR ESTUDIANTES ===")


## Función repaso.
## Crear una función que valide usuario y contraseña.

def validador(user, password):
    if user == "matias123" and password == "matias123":
        print(f"Bienvenido, {user}")
        return True
    else:
        print("Acceso denegado.")
        return False    
    

def enviarDatos():
    username = input("Ingrese su usuario: ")
    password = input("Ingrese su contraseña: ")
    validador(username, password)

enviarDatos()
