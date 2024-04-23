import json

archivo_json = "large-file.json"

with open(archivo_json, encoding="utf-8") as archivo:
    datos_json = json.load(archivo)


print(datos_json)




print("                  M E N U                  ")
print("""
1.mostrar eventos en la base de datos
2.crear un evento dentro de la base de datos
3.actualizar
4.eliminar evento
""")

opc=int(input("selcciona una opcion por favor :"))

if opc == 1:
    print(datos_json)

