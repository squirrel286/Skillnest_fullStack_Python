'''
Actividad: Gestor de inventario
'''


'''
1.- Creación: Crear una lista llamada inventario que contenga los siguientes artículos:
"Laptop", "Ratón", "Monitor", "Cable HDMI"
'''

''' 
2.- Expansión: Utiliza el método correspondiente para agregar "impresora"
y "teclado" al final de la lista. 
'''

'''
3.- Conteo: Utiliza la función integrada para mostrar cuántos elementos hay en total en la lista.
'''

'''
4.- Acceso y modificación: Modifica "Teclado" por "teclado mecánico"
'''

'''
5.- Slicing: Crea una nueva lista llamada "promoción", debe contener sólo los
primeros 3 elementos de la lista "artículos"
'''

'''
6.- Mostrar la lista de inventario ordenado alfabéticamente.
'''

'''
7.- Elimina el último elemento de la lista inventario mostrando el elemento eliminado y la lista final.
'''


inventario = ["laptop", "ratón", "monitor", "cable HDMI"]


inventario.append("impresora")
inventario.append("teclado")

inventario[5] = "teclado mecánico"
print(f"4.- Modificado: {inventario}")

inventario.pop()


promocion = ["laptop", "cable HDMI", "impresora"]

list.sort(promocion)


print(len(inventario))

verUltimo = inventario.pop()
print(verUltimo)

promocion = inventario[0:3]
inventario.sort()
print(inventario)