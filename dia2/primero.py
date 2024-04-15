#Al inicio, el programa dará la bienvenida y explicará la naturaleza de la Secuencia de Fibonacci, donde solicitará al usuario ingresar un valor entero "n", 
#representando hasta qué término de la secuencia se generará. Aquí mostrará la secuencia de Fibonacci hasta el enésimo término ingresado por el usuario. 
#Luego, preguntará si el usuario desea continuar o salir, donde si se decide salir, el programa se detendrá; de lo contrario, se repetirá el proceso.
while True:
    print("""Bienvenidos  a mi programa a continuacion veremos describiremos
    la funcion de fibonacci""") 
   
    print("""Se trata de una secuencia infinita de números
    naturales; a partir del 0 y el 1, se van sumando apares,
    de manera que cada número es igual a la suma de sus dos 
    anterior de manera que: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…""")

#Solicita al usuario que ingrese un número entero
    n=int(input("Ingrese un número entero: "))

#Inicializa las variables para generar la secuencia Fibonacci
    a, b = 0, 1
    c = 1

#Mientras no se haya alcanzado el término n de la secuencia
    while c <= n:
    #Si es un índice impar en la secuencia
        if c % 2 == 1:
        #Imprime el número de Fibonacci actual
            print(a, end=", ")
        #Actualiza el valor de "a" sumando "b"
            a += b
        else:
        #Si es un índice par en la secuencia
        #Imprime el número de Fibonacci actual
            print(b, end=", ")
        #Actualizar el valor "b" sumando "a"
            b+= a
    #Incrementar el contador
        c+= 1

#Pregunta al usuario si desea continuar
    continuar = input("\n¿Desea continuar? (s/n): ").lower()
#Si la respuesta no es "s" sale del bucle y finaliza el programa
    if continuar != "s":
        print("¡Hasta luego!")
        break

    #hecho por freiler_ortega cc:1010075774