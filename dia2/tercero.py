
import random

def jugarAdivinaNumero():
    numeroSecreto = random.randint(1, 100)
    intentos = 0

    while intentos < 10:
        intento = int(input("Adivina el número secreto (entre 1 y 100): "))
        intentos += 1

        if intento < numeroSecreto:
            print("El número secreto es mayor. Intenta nuevamente.")
        elif intento > numeroSecreto:
            print("El número secreto es menor. Intenta nuevamente.")
        else:
            print(f"¡Felicidades! Adivinaste el número secreto en {intentos} intentos.")
            return

    print(f"Agotaste tus 10 intentos. El número secreto era {numeroSecreto}.")

jugarAdivinaNumero()

#hecho por freiler_ortega cc=1010075774
