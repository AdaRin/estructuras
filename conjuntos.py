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


#ELIMINAR ELEMENTOS
conjunto_frutas.remove("Banana")
print(conjunto_frutas)

conjunto_frutas.discard("Manzana")
print(conjunto_frutas)

#JUNTAR SET Y BLUCLES EN CONJUNTOS
conjunto_letras = {"a", "b", "c"}
conjunto_numeros = {1, 2, 3}

union = conjunto_letras | conjunto_numeros
print(union)

#JUNTAR SET Y TUPla
conjunto_letras.update(conjunto_numeros)
print(conjunto_letras)

set_tecno_chicago = {"Python", "JavaScript", "AWS"}
set_tecno_ny = {"Python", "Java", "C++"}

set_tecno_chicago.intersection_update(set_tecno_ny)
print(set_tecno_chicago)

set_tecno_chicago.difference_update(set_tecno_ny)
print(set_tecno_chicago)


