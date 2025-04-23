#----------------------------------
#CONJUNTOS [Colección no ordenada de elementos únicos y mutables]
#----------------------------------



conjunto_frutas = {"Manzana", "Plátano", "Cereza", "Manzana","Banana"}

#conjunto_frutas = set("Manzana")
print(conjunto_frutas)


#ACCEDER, AGREGAR Y ELIMINAR

#ACCEDER
for fruta in conjunto_frutas:
    print(fruta)

print("Banana" in conjunto_frutas)

#AGREGAMOS UN ELEMENTO
conjunto_frutas.add("Frutilla")

print(conjunto_frutas)

#AGREGAMOS UN SET

conjunto_frutas2 = {"kIWI", "ARANDANOS", "MANGO"}
conjunto_frutas.update(conjunto_frutas2)
print(conjunto_frutas)
