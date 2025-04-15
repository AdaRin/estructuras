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
"""
    #SHORTHAND
frutas = ["Manzana", "Plátano", "Mandarina","Fresa", "Piña"]
[print(fruta) for fruta in frutas]