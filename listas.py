#----------------------------------
#LISTAS
#----------------------------------

lista = ["Manzana", "Plátano", "Mandarina","Fresa", "Piña"]
print(lista[-2])

""""
if "Sandia" in lista:
    print("Si, Sandia está en la lista")
else:
   print("No, Sandia no está en la lista")
"""
""""
lista[4:] = ["Frutilla", "Ananá"]
print(lista)
"""

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