#----------------------------------
#LISTAS
#----------------------------------




""""
lista = ["Manzana", "Plátano", "Mandarina","Fresa", "Piña"]
print(lista[-2])
if "Sandia" in lista:
    print("Si, Sandia está en la lista")
else:
   print("No, Sandia no está en la lista")

lista[4:] = ["Frutilla", "Ananá"]
print(lista)

lista.insert(2, "Aguacate")
print(lista)
lista.append("Limón")
print(lista)

#Agregando Listas 

lista2 = ["Lechuga", "Tomate", "Zanahoria"]
lista.extend(lista2)
print(lista)

#Agregando Tuplas
tupla = ("Melón", "Kiwi")
lista.extend(tupla)
print(lista)


#Eliminando elementos
lista.remove("Fresa")
print(lista)

#Eliminando índice
lista.pop(2)
print(lista)

print(lista)
#Usando  pop sin argumento el cual elimina el último elemento
lista.pop()
print(lista)

#Limpiar lista (vacia)
lista.clear()
print(lista)



#BUCLE FOR

frutas = ["Manzana", "Plátano", "Mandarina","Fresa", "Piña"]

for fruta in frutas:
    print(fruta)


#BUCLE FOR CON ÍNDICE DISPONIBLE
frutas = ["Manzana", "Plátano", "Mandarina","Fresa", "Piña"]

for i in range(len(frutas)):
    print(frutas[i])
    
#BUCLE WHILE
frutas = ["Manzana", "Plátano", "Mandarina","Fresa", "Piña"]
i=0
while i<len(frutas):
    print(frutas[i])
    i += 1

    #SHORTHAND (abreviación del ciclo for)
frutas = ["Manzana", "Plátano", "Mandarina","Fresa", "Piña"]
[print(fruta) for fruta in frutas]
"""

import copy


frutas = ["Manzana", "plátano", "Mandarina","Fresa", "Piña", "melón", "Pera"]

                #dato a
                # asignar   bucle           condición
frutas_con_e = [fruta for fruta in frutas if "e" in fruta ]
print(frutas_con_e)

frutas2= [fruta for fruta in frutas if fruta !="Mandarina" ]
print(frutas2)

#Hacer una copia
copia= [fruta for fruta in frutas]
print(copia)

#Hacer una copia
rango= [x for x in range(10) if x<5]
print(rango)

#Poner todo en mayusculas
mayus= [fruta.upper() for fruta in frutas ]
print(mayus)

#Poner todo en mayusculas
min= [fruta.lower() for fruta in frutas ]
print(min)

#Poner todo en minusculas
frutas3= [fruta if fruta != "Pera" else "Aguacate" for fruta in frutas ]
print(frutas3)

#Ordenando listas
numeros = [9,999,820,0,3,1]


frutas.sort(key = str.lower)
numeros.sort()

print(frutas)
print(numeros)

#Ordenando al reves
frutas.reverse()
print(frutas)


#COPIAS DE LISTAS

copia_frutas = frutas.copy()
copia_frutas2 = list(frutas)

print(copia_frutas)
print(copia_frutas2)

#JUNTAR LISTAS

frutasj = frutas + numeros
print(frutasj)

frutas.extend(numeros)
print(frutas)

print(frutas.count("Manzana"))
