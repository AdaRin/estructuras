# DICCIONARIO
# Un diccionario es una colección de pares clave-valor. 



diccionario = {
    "nombre" : "Juan",
    "apellido" : "Pérez",           
    "edad" : 30,   
    "tecnologias": ["Python", "Java", "C++"]       
}

# Acceder a un valor
claves = diccionario.keys()

# Se puede acceder a los valores de un diccionario utilizando su clave

diccionario["primo"] = "Pedro" 
print(claves)

## Se puede acceder a los valores de un diccionario utilizando su clave
valores = diccionario.values()
print(valores)  

if "nombre" in diccionario:
    print("La clave 'nombre' existe en el diccionario.")
else:   
    print("La clave 'nombre' no existe en el diccionario.")       

#Cambiar, agregar o eliminar elementos
# update
# El método update() se utiliza para agregar o actualizar elementos en un diccionario.
# Si la clave ya existe, se actualiza su valor; si no existe, se agrega un nuevo par clave-valor.
diccionario.update({"nombre": "Pedro", "apellido": "Gómez"})                    

#borrar
# El método pop() se utiliza para eliminar un elemento del diccionario utilizando su clave.
# Devuelve el valor asociado a la clave eliminada.      
diccionario.pop("apellido")
print(diccionario)

# El método del se utiliza para eliminar un elemento del diccionario utilizando su clave.
# No devuelve el valor asociado a la clave eliminada.
del diccionario["nombre"]           
print(diccionario)

# El método clear() se utiliza para eliminar todos los elementos del diccionario.
# Después de llamar a este método, el diccionario estará vacío. 
diccionario.clear()
print(diccionario)

#copiar diccionarios y utlizar bucles
# El método copy() se utiliza para crear una copia superficial de un diccionario.
# Esto significa que se crea un nuevo diccionario con las mismas claves y valores que el original.
# Sin embargo, si los valores son objetos mutables (como listas o diccionarios),
# los cambios en esos objetos afectarán tanto a la copia como al original.
diccionario = {
    "nombre" : "Juan",
    "apellido" : "Pérez",           
    "edad" : 30,   
    "tecnologias": ["Python", "Java", "C++"]       
}       
diccionario_copia = dict(diccionario) # Copia superficial
diccionario["nombre"]  = "Pedro" # Cambia el valor en el diccionario original
print(diccionario_copia) # La copia no se ve afectada
print(diccionario) # El diccionario original se ve afectado

# El método items() se utiliza para obtener una vista de los pares clave-valor del diccionario.
# Devuelve una vista de los elementos del diccionario como una lista de tuplas (clave, valor).
# Esto es útil para iterar sobre los elementos del diccionario.
for clave, valor in diccionario.items():
    print(f"{clave}: {valor}") # Imprime cada clave y su valor asociado
# El método keys() se utiliza para obtener una vista de las claves del diccionario. 
# Devuelve una vista de las claves del diccionario como un objeto dict_keys.
# Esto es útil para iterar sobre las claves del diccionario.
for clave in diccionario.keys():
    print(clave) # Imprime cada clave del diccionario
# El método values() se utiliza para obtener una vista de los valores del diccionario.  
# Devuelve una vista de los valores del diccionario como un objeto dict_values.
# Esto es útil para iterar sobre los valores del diccionario.
for valor in diccionario.values():
    print(valor) # Imprime cada valor del diccionario
# El método get() se utiliza para obtener el valor asociado a una clave en el diccionario.
# Si la clave no existe, devuelve None o un valor predeterminado si se proporciona.
# Esto es útil para evitar errores si la clave no está presente en el diccionario.
valor = diccionario.get("nombre", "No encontrado") # Devuelve "No encontrado" si la clave no existe
print(valor) # Imprime el valor asociado a la clave "nombre" o "No encontrado" si no existe 




