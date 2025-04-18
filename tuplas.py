#----------------------------------
#LISTAS [Colección de elementos inmutables y ordenados]
#----------------------------------
#debe tener al menos un elemento, y una coma al final




"""
frutas = ("Manzana", "Plátano", "Cereza", "Manzana")

numeros = (1,2,4)
print(len(frutas))
"""

# ACTUALIZACIÓN DE UNA TUPLA
"""
frutas = ("Manzana", "Plátano", "Cereza", "Manzana")

frutas2 = list(frutas) #lista

frutas2[1] = "Coco"  #modifico la lista

frutas = tuple(frutas2)  #convierto a tupla la lista y la resigno a la variable original
 
print(frutas)




listas_frutas = list(tuplas_frutas)

listas_frutas.append("Coco")

tuplas_frutas = tuple(listas_frutas)

print(tuplas_frutas)
"""

#CONCATENANDO TUPLAS
"""
tupla_verduleria = ("Manzana", "Plátano", "Cereza", "Manzana")
tuplas_verduras = ("Zanahoria", "Ajo", "Brocoli")

tupla_verduleria += tuplas_verduras

print(tupla_verduleria)
"""

#REMOVIENDO ELEMENTO EN TUPLA
"""
tupla_frutas = ("Manzana", "Plátano", "Cereza", "Manzana")

lista_frutas = list(tupla_frutas)

lista_frutas.remove("Manzana")

tupla_frutas = tuple(lista_frutas)

print(tupla_frutas)
"""
#REMOVIENDO ELEMENTO EN TUPLA
"""
tupla_frutas = ("Manzana", "Plátano", "Cereza", "Manzana")

del tupla_frutas
"""

#DESEMPAQUETANDO TUPLAS
"""
tupla_frutas = ("Manzana", "Plátano", "Cereza", "Manzana","Banana")
(a, b, c, d, e) = tupla_frutas

print(a)
print(b)
print(c)
print(d)
print(e)

print("#######################################")
#desempaquetat solo algunos usando astericos 
(a, b, c, *d) = tupla_frutas
print(a)
print(b)
print(c)
"""

#BUCLES CON TUPLAS
tupla_frutas = ("Manzana", "Plátano", "Cereza", "Manzana","Banana")

#La forma más básica
for fruta in tupla_frutas:
    print(fruta)

#Usando range
print("#######################################")

for i in range(len(tupla_frutas)):
    print(tupla_frutas[i], "con índice", i)

#JUNTAR, CONTAR E INDICE CON TUPLAS
print("#################JUNTAR##################")
tupla_frutas1 = ("Manzana", "Plátano") 
tupla_frutas2 = ("Cereza", "Manzana","Banana")

tupla_frutas = tupla_frutas1 + tupla_frutas2
print(tupla_frutas)

print("#################CONTAR##################")

tupla_frutas = tupla_frutas1*3 + tupla_frutas2
print(tupla_frutas.count("Manzana"))

print("#################CONTAR##################")

tupla_frutas = tupla_frutas1*3 + tupla_frutas2
print(tupla_frutas1.index("Manzana"))