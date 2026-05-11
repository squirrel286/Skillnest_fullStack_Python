# ➡️ Pasar argumentos 
# Para poder personalizar nuestras instancia vamos a pasar algunos argumentos al método __init__ y que de esta manera podamos asignarle a los atributos los valores correspondientes.

class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0

# Creación de instancias
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la")
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la")

# Imprimimos valores
print(miyagi.nombre) #Imprime: Nariyoshi
print(daniel.nombre) #Imprime: Daniel

'''
Crear una clase Estudiantes, y asignarle los siguientes atributos:
(rut, nombre, apellido, especialidad, fecha_nac)
'''

class Estudiantes:
    def __init__(self, rut, nombre, apellido, especialidad, fecha_nac):
        self.rut = rut 
        self.nombre = nombre
        self.apellido = apellido 
        self.especialidad = especialidad
        self.fecha_nac = fecha_nac

benja = Estudiantes("22926226-2", "Benjamín", "Delgado", "Programación", "07-01-2009")
teté = Estudiantes("22633816-0", "Elizabeth", "Cornejo", "Programación", "30-01-2008")
randy = Estudiantes("22898879-0", "Randy", "Cortinez", "Programación", "28-11-2008")

print(f"El nombre es: {randy.nombre} {randy.apellido} y la especialidad es {randy.especialidad}")
print(f"El nombre es {benja.nombre} {benja.apellido} y la especialidad es {benja.especialidad}")
print(f"El nombre es {teté.nombre} {teté.apellido} y la especialidad es {teté.especialidad}")


def aumentarCredito(self, aumento):
    
    pass