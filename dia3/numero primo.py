#Crear una función que determina si un número dado por el usuario es primo. 
# creamos la funcion que se va a encargar de confrimarnos si nuestro numero es primo o no  
def es_primo(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for m in range(2,n):
            if n % m == 0:
                return False
        return True       

#acontinuacion crearemos el menu para darle una experiencia mas agradable a nuestro usuario

fr=True
while fr:
    print("======MENU PRINCIPAL======")
    print("bienvenido a mi programa ")
    print("1. comprobar si un numero es primo")
    print("2. detener el programa inmediatamente")
    print("3. informacion  sobre los numero primos aqui  ")
    opc=input("ingrese una opcion : ")
    if opc=="1":
        n=int(input("ingrese un numero entero por favor, para verificar si es primo : "))
        if es_primo(n):
            print("")
            print(f"el numero",n, "es un primo.")
        else:
            print("")
            print(f"este numero" ,n,"no es un primo")
            
    elif opc=="2":
        print("gracias por usar mi programa ")
        fr=False
        
    elif opc=="3":
        print("")
        print("LOS NUMEROS PRIMOS ")
        print("")
        print("son aquellos que solo son divisibles entre ellos mismos y el 1")
        print("es decir que si intentamos dividirlos por cualquier otro número")
        print("el resultado no es entero  ")
        print("Dicho de otra forma, si haces la división ")
        print("por cualquier número que no sea 1 o él mismo")
        print("se obtiene un resto distinto de cero.")
        print("autor: freiler_ortega cc: 1010075774")
    
    else:
        print("")
        print("por favor elije una opcion valida (1,2,3): ")


 #===========================================================================================================================================       