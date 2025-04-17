#----------------------------------
#LISTAS [Colección de elementos inmutables y ordenados]
#----------------------------------
#debe tener al menos un elemento, y una coma al final



frutas = ("Manzana", "Plátano", "Cereza", "Manzana")
numeros = (1,2,4)
print(len(frutas))


# ACTUALIZACIÓN DE UNA TUPLA
frutas2 = list(frutas) #lista

frutas2[1] = "Coco"  #modifico la lista

frutas = tuple(frutas2)  #convierto a tupla la lista y la resigno a la variable original
 
print(frutas)