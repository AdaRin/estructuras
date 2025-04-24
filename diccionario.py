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
