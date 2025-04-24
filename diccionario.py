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

