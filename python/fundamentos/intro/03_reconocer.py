"""
Este archivo demuestra varios conceptos básicos en Python.
Completa los comentarios en cada línea para relacionarlos
con los conceptos enumerados en 'reconocer.md'.
"""


import random # Importación de librería para procesos aleatorios.


nombre = "Frida Kahlo" # Declaramos variable llamada nombre tipo string y se le asigna un valor.
print(type(nombre)) # type() = método de python para mostrar el tipo de una variable.
print(len(nombre)) # len() = Devuelve el largo de la variable.


edad = 25 # Declaramos la variable llamada edad con valor numérico (int).



if edad < 18: # Declaramos la primera condición con el if.
   print("Eres menor de edad.") # Si edad es menor (>) a 18, se imprime el texto indicándolo.
elif edad == 18: # Segunda condición con else if (en cambio si...).
   print("Tienes 18 años.") # Si edad es igual (==) a 18, se imprime el texto diciendo que tiene 18 años.
else: # Tercera y última condicion else.
   print("Eres mayor de edad.") # Si no se cumple ninguna de las condiciones anteriores, imprime el mensaje "Eres mayor de edad"


frutas = ["manzana", "pera", "fresa"] # Creamos una variable tipo array (arreglo), con 3 valores empezando desde cero (0, 1, 2).
print(frutas[0]) # Imprime la primera posición (0) del arreglo
frutas[0] = "banana" # A la primera posición del arreglo se le asigna el valor de "banana"
frutas.append("uva") # Se le agrega el valor "uva" al final del arreglo.
frutas.remove("pera") # Se elimina el valor de "pera" en el arreglo.


dimensiones = (200, 50) # Creamos una variable tipo tupla (variable inmutable)
print(dimensiones[0]) # Imprime la posición 0 de la variable creada


persona = { # Variable tipo object (objeto) 
   "nombre": "Carlos", # Se le asigna al ítem "nombre" el valor de "Carlos"
   "edad": 30 # Se le establece al ítem "edad" el valor de "30"
}
print(persona["nombre"]) # Imprime el valor del ítem "nombre"
persona["edad"] = 31 # Se modifica el valor del ítem "edad" a 31
persona["ciudad"] = "Santiago" # Se agrega un ítem llamado "ciudad" con el valor de "Santiago"
del persona["ciudad"] # Borra (delete) el ítem ciudad.


for i in range(5): # for range: Se crea bucle de un rango hasta 5 comenzando desde 0.
   if i == 2: # Condición
       continue # Continue ignora el proceso y continúa.
   if i == 4: # Segunda condición
       break # Si i = 4 se rompe el proceso/bucle.
   print(i) # Imprime el valor de i en cada iteración (hasta el 4).


contador = 0 # Se crea una variable contador de tipo numérica (int).
while contador < 3: # Se crea el bucle while con una condición
   print(f"while contador es: {contador}") # Imprimirá el contador en un mensaje concatenado con f""
   contador += 1 # A contador se le suma uno.


def saludar_usuario(nombre): # def - Palabra reservada para crear función
   return f"Hola, {nombre}" # Devuelve un valor de la función


print(saludar_usuario("Francisca")) # Se imprime "Hola Francisca" - return de la función.