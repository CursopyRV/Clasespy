
# tupla = (1,2,3)
# print(tupla)

""" frutas = ("manzana", "naranja", "uva", "manzana", "uva" )
posicion = frutas.index("uva")

print(f"la primera apricion de 'uva' se da en la posicion : {posicion} ") """

# #conjunto
# frutas = {"manzana", "naranja", "uva", "manzana", "uva" }

# frutas.add = ("coco")
# print(frutas.add)

# # verduras = {"lechuga, tomate, cebolla"}

# """ frutas_y_verduras = frutas | verduras

# print(frutas_y_verduras) """

# print(frutas)

# if"pera" in frutas:
#"""      print("Manzana se encuentra en el conjunto")
# else:
#     print("pera no se encuetra")

# for verdu in frutas :
#      print(verdu)

#DICCIONARIO

""" agenda = {"ana": 12383, "jose": 128383, "juan": 384929}
print(agenda)

lugar = {
    "pais": "argentina",
    "provincia": "Formosa",
    "cp" : 3600

}

print(lugar["pais"]) """ """
""" 
""" Ejercicio: Gestión de un diccionario de contactos
Dado el siguiente diccionario:
● Agrega un nuevo contacto: "Marta" con el correo "marta@example.com".
● Actualiza el correo de "Luis" a "luis2023@example.com".
● Usa un método para eliminar a "Ana" y guarda su correo en una variable.
● Imprime el diccionario final y el correo eliminado.¨
 """ 

contactos = {
    "Ana": "Ana@example.com" , 
"Luis": "luis@example.com" 

}
print(contactos)

contactos["marta"] = "marta@example"
contactos["luis"] = "luiso@example"

print(contactos)

correoeliminado_Ana = contactos.pop("Ana")

print(correoeliminado_Ana)

print(f"Diciconario final")
