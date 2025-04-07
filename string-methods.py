texto = "Hola mundo"
texto_con_espacios = "                         texto con espacios"
texto_separado = "Python,JavaScript,Django,React"
lista = ["Hola", "Juan", "Carlos"]
numeros = "123456a"
letras = "abc"
espacio = " "
repeticion = "Manzana, Naranja, Manzana"


print("capitalize", texto.capitalize()) # Convierte la primer lera en mayúscula(el resto en mínusculas)
print("upper", texto.upper()) # Convierte todo el texto en mayúsculas
print("lower", texto.lower()) # Convierte todo el texto en mínusculas
print("strip", texto_con_espacios.strip()) # Elimina los espacios al comienzo y al final
print("replace", texto_con_espacios.replace("espacios", "gracias")) # Remplaza una palabra por otra
print("split", texto_separado.split(",")) # Separa el texto en items de lista
print("join", ",".join(lista)) # Junta los items de una lista en un string
print("find", texto.find("muNdo"))  # Muestra la posición donde aranca el texto ingresado
print("rfind", repeticion.rfind("Manzana")) # Muestra la posición donde aranca el texto ingresado
print("index", texto.index("mundo")) # Muestra la posición donde aranca el texto ingresado
print("startswith", texto.startswith("hoLa")) # Indica si comienza o no con la palabra ingresada
print("endswith", texto.endswith("muNdo")) # Indica si finaliza o no con la palabra ingresada
print("isdigit", numeros.isdigit()) # Indica si todos los caracteres son números o no
print("isalpha", texto.isalpha()) # Indica si todos los caracteres son letras o no
print("isalnum", letras.isalnum()) # Indica si todos los caracteres son alfanuméricos o no
print("count", repeticion.count("Manzana")) # Indica si el string solo está hecho de espacios










