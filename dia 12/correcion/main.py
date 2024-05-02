#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

def abrirArchivo():
    miJSON=[]
    with open('info.json','r') as openfile:
        miJSON= json.load(openfile)
    return miJSON

def guardarArchivo(miData):
    with open("info.json","w") as outfile:
        json.dump(miData,outfile)

def abrirArchivo():
    with open('info.json', 'r') as openfile:
        miJSON = json.load(openfile)
    return miJSON

def guardarArchivo(miData):
    with open("info.json", "w") as outfile:
        json.dump(miData, outfile, indent=4)        


print("################")
print("## PLATAFORMA DE GESTION ##")
print("################")
print("")
print("Hola! Por favor escoge alguna de las opciones:\n1.Revisar estudiantes\n2.Modificar estudiante\n3.Agregar un estudiante\n4.Eliminar estudiante ")
x=int(input("Elige una opcion : "))
miInfo=[]


if(x==1):
    miInfo=abrirArchivo()
    for i in miInfo[0]["estudiantes"]:
        print("################")
        print("GRUPO T2")
        print("")
        print("ID:",i["id"])
        print("Nombre:",i["nombre"])
        print("Apellido:",i["apellido"])
        print("Edad",i["edad"])
        print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
        print("Cédula:",i["cedula"])
        print("E-mail:",i["email"])
        print("GitHub:",i["github"])
        print("################")
        print("")

    for i in miInfo[1]["estudiantes"]:
        print("################")
        print("GRUPO P1")
        print("")
        print("ID:",i["id"])
        print("Nombre:",i["nombre"])
        print("Apellido:",i["apellido"])
        print("Edad",i["edad"])
        print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
        print("Cédula:",i["cedula"])
        print("E-mail:",i["email"])
        print("GitHub:",i["github"])
        print("################")
        print("")
elif(x==2):
    miInfo=abrirArchivo()
    contador = 0
    for i in miInfo[0]["estudiantes"]:
        contador = contador +1
        print("################")
        print(" ESTUDIANTE #",contador)
        print("ID:",i["id"])
        print("Nombre:",i["nombre"])
        print("Apellido:",i["apellido"])
        print("Edad",i["edad"])
        print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
        print("Cédula:",i["cedula"])
        print("E-mail:",i["email"])
        print("GitHub:",i["github"])
        print("################")
        print("")
    contador = 0
    estudiante = int(input("Cual numero de identificacion vas a cambiar?"))
    datoCambiar=print("Que te gustaría cambiar del estudiante:\n1.Nombre\n2.Apellido\n3.Edad\n4.Fecha de nacimiento\n5.Cedula\n6.Email\n7.Github")
    datoCambiar=int(input("Elige una opcion : "))
    if (datoCambiar==1):

        nuevoNombre = input("ingresa el nuevo nombre : ") 
        miInfo[0]["estudiantes"][estudiante-1]["nombre"] = nuevoNombre
        guardarArchivo(miInfo)  
        print("cambio realizado")

    if (datoCambiar==2):
        nuevoApellido = input("ingresa el nuevo apellido : ") 
        miInfo[0]["estudiantes"][estudiante-1]["apellido"] = nuevoApellido
        guardarArchivo(miInfo)  
        print("cambio realizado")

    if (datoCambiar==3):
        nuevaEdad = int(input("ingresa la nueva edad : "))
        miInfo[0]["estudiantes"][estudiante-1]["edad"] = nuevaEdad
        guardarArchivo(miInfo)  
        print("cambio realizado")

    if (datoCambiar==4):
        nuevaFN = int(input("ingresa la nueva fecha de nacimiento D/M/A : "))
        miInfo[0]["estudiantes"][estudiante-1]["fecha de nacimiento"] = nuevaFN
        guardarArchivo(miInfo)  
        print("cambio realizado")

    if (datoCambiar==5):
        nuevaCedula = int(input("ingresa nuevo numero de cedula : "))
        miInfo[0]["estudiantes"][estudiante-1]["cedula"] = nuevaCedula
        guardarArchivo(miInfo)  
        print("cambio realizado")  

    if (datoCambiar==6):
        nuevoEmail = input("ingresa el nuevo email : ")
        miInfo[0]["estudiantes"][estudiante-1]["email"] = nuevoEmail
        guardarArchivo(miInfo)  
        print("cambio realizado") 

    if (datoCambiar==7):
        nuevoGit = input("ingresa el nuevo correo Github : ")
        miInfo[0]["estudiantes"][estudiante-1]["github"] = nuevoGit
        guardarArchivo(miInfo)  
        print("cambio realizado")  

        miInfo=abrirArchivo()
    for i in miInfo[0]["estudiantes"]:
        contador = contador +1
        print("################")
        print(" ESTUDIANTE #",contador)
        print("ID:",i["id"])
        print("Nombre:",i["nombre"])
        print("Apellido:",i["apellido"])
        print("Edad",i["edad"])
        print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
        print("Cédula:",i["cedula"])
        print("E-mail:",i["email"])
        print("GitHub:",i["github"])
        print("################")
        print("")
    contador = 0




elif x == 3:
    nuevo_estudiante = {}
    nuevo_estudiante["id"] = input("ID del nuevo estudiante: ")
    nuevo_estudiante["nombre"] = input("Nombre del nuevo estudiante: ")
    nuevo_estudiante["apellido"] = input("Apellido del nuevo estudiante: ")
    nuevo_estudiante["edad"] = int(input("Edad del nuevo estudiante: "))
    nuevo_estudiante["fechaNacimiento"] = input("Fecha de Nacimiento del nuevo estudiante (DD-MM-AAAA): ")
    nuevo_estudiante["cedula"] = input("Cédula del nuevo estudiante: ")
    nuevo_estudiante["email"] = input("Email del nuevo estudiante: ")
    nuevo_estudiante["github"] = input("GitHub del nuevo estudiante: ")

    miInfo = abrirArchivo()
    miInfo[0]["estudiantes"].append(nuevo_estudiante)
    guardarArchivo(miInfo)
    print("Estudiante agregado correctamente.")

elif x == 4:
    miInfo = abrirArchivo()
    estudiante_a_eliminar = input("Ingrese el ID del estudiante que desea eliminar: ")
    encontrado = False
    for grupo in miInfo:
        for estudiante in grupo["estudiantes"]:
            if estudiante["id"] == estudiante_a_eliminar:
                grupo["estudiantes"].remove(estudiante)
                encontrado = True
                break
        if encontrado:
            break
    if encontrado:
        guardarArchivo(miInfo)
        print("Estudiante eliminado correctamente.")
    else:
        print("Estudiante no encontrado.")

    
    
















        
    

