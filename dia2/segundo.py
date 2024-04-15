import random

def jugar_adivina_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0
#definimos el while como true para que no tenga limite de intento en adivinar el numero secreto
    while True:
        intento = int(input("Adivina el número secreto (entre 1 y 100): "))
        intentos += 1
        
#si agregamos un numero menor al numero secreto mostramos que el numero debe ser mayor
        if intento < numero_secreto:
            print("El número secreto es mayor. Intenta nuevamente.")
        elif intento > numero_secreto:
#si agregamos un numero mayor al numero secreto mostramos que el numero debe ser menor            
            print("El número secreto es menor. Intenta nuevamente.")
        else:
            print(f"¡Felicidades! Adivinaste el número secreto en {intentos} intentos.")
            break

jugar_adivina_numero()
#hecho por freiler_ortega