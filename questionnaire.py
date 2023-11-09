#!/usr/bin/env/ python3
#By antonioclash819@gmail.com
#GNU/GPL License
#2023/11/08

#Simple questions

print("¿Cual color prefieres? ")
print("[Azul/Rojo/Verde/Otro]")
entrada = input("> ")
if entrada == "Azul" or entrada == "azul":
    print("Se ha guardado el color:", entrada)
elif entrada == "Rojo" or entrada == "rojo":
    print("Se ha guardado el color:", entrada)
elif entrada == "Verde" or entrada == "verde":
    print("Se ha guardado el color:", entrada)
elif entrada == "Otro" or entrada == "otro":
    entr = input("Escribe el color de tu preferencia: ")
    print("Se ha guardado el color:", entr)
else:
    print("Opción no válida")

