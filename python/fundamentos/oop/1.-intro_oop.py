# Ésta es la sintaxis para crear una clase llamada "Usuario": 
class Usuario:
    def __init__(self): # Constructor
        self.nombre = "Nariyoshi"
        self.apellido = "Miyagi"
        self.email = "miyagi@codingdojo.la"
        self.limite_credito = 30000
        self.saldo_pagar = 0
        

miyagi = Usuario()

daniel = Usuario()

randy = Usuario()

# Accedemos a los atributos de la instancia
print(miyagi.nombre) # Imprime: Nariyoshi
print(miyagi.apellido)
print(miyagi.email)
print(miyagi.limite_credito)
print(miyagi.saldo_pagar)

# Nuevos valores asignados a atributos de la instancia
daniel.nombre = "Daniel"
daniel.apellido = "Larusso"
daniel.email = "daniel@gmail.com" 
daniel.limite_credito = 100000
daniel.saldo_pagar = 300000

print(daniel.nombre) # Imprime: Daniel

# Valores a nueva instancia
randy.nombre = "Randy" 
randy.apellido = "Cortinez" 
randy.email = "randy@gmail.com"
randy.limite_credito = "INFINITO"
randy.saldo_pagar = 2500

print(randy.limite_credito)


