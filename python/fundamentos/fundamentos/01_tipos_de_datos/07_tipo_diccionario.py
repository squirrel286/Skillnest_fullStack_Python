# Diccionarios en Python
estudiante = {"nombre": "Gonzalo", "curso": "Python"} # Notación literal
# Imprimir el nombre del estudiante
print(estudiante["nombre"]) #Imprime: Gonzalo

estudiante["nombre"] = "Vicente"
print(estudiante["nombre"]) #Imprime: Vicente



paises = {} # Diccionario vacío
paises["MEX"] = "México"
paises["COL"] = "Colombia"
paises["CHL"] = "Chile"
paises["PER"] = "Perú"
paises["ARG"] = "Argentina"
print(paises)



if "CRI" in paises: #Preguntamos si existe la clave en el diccionario
    print("¿Deseas reemplazar el valor?")
else: #No existe esa clave
    paises["CRI"] = "Costa Rica"


# Eliminar valores en un diccionario.
    valor_removido = paises.pop("MEX") #Elimina el elemento y devuelve su valor
    print(f"Valor removido: {valor_removido}")
del paises["COL"] #Elimina el elemento
print(paises) #Imprime: {'CHL': 'Chile'}

# Sintaxis multilínea

# pintor = { "nombre": "Frida Kahlo", "pais": "México", "fecha_nacimiento": "6 de julio de 1907"}

# Puede ser escrito de esta manera.
pintor = {
"nombre": "Frida Kahlo",
"pais": "México",
"fecha_nacimiento": "6 de julio de 1907"
}

# Diccionarios anidados
escuela = {
"nombre": "Coding Dojo LATAM",
"profesores": [
    {"nombre": "Alfredo", "apellido": "Salazar", "cursos": ["Python", "Java"]},
    {"nombre": "Valeria", "apellido": "Romero", "cursos": ["Fundamentos", "Java"]},
    {"nombre": "Marcelo", "apellido": "Argotti", "cursos":["MERN", "Python"]}
]
}


